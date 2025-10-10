from dateutil.relativedelta import relativedelta
from django.utils import timezone
from decimal import Decimal, ROUND_HALF_UP, getcontext
from datetime import date
from emi.models import EMI


# import LoanSettings
try:
    from loan_ticket.models import LoanSettings
except Exception:
    LoanSettings = None

# make decimal math safer
getcontext().prec = 28


def calculate_emi(principal, annual_rate, tenure_months):
    """
    Returns monthly EMI (Decimal) rounded to 2 dp.
    principal: numeric
    annual_rate: numeric (e.g. 12.5 for 12.5%)
    tenure_months: int
    """
    P = Decimal(str(principal))
    N = int(tenure_months)
    if N <= 0:
        raise ValueError("tenure_months must be > 0")

    # monthly rate as a decimal fraction
    R = (Decimal(str(annual_rate)) / Decimal('100')) / Decimal('12')

    if R == 0:
        emi = P / Decimal(N)
    else:
        one_plus_r_pow_n = (Decimal(1) + R) ** N
        emi = (P * R * one_plus_r_pow_n) / (one_plus_r_pow_n - Decimal(1))

    return emi.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


def create_emis_for_loan(loan_ticket):
    """
    Given a loan_ticket instance (with .loan_amount, .loan_tenure, optionally .interest_rate,
    and optionally .start_date), create EMI rows and update loan_ticket.end_date.

    This function:
    - pulls interest from LoanSettings if loan_ticket.interest_rate is falsy
    - calculates per-period interest/principal and remaining balance
    - creates EMI objects with emi_amount and outstanding_amount set to remaining balance after payment
    - updates loan_ticket.end_date and saves the model
    - returns the final end_date (datetime.date)
    """
    # ensure loan_ticket has start_date and interest_rate
    if not getattr(loan_ticket, 'start_date', None):
        loan_ticket.start_date = date.today()
        # If other fields need to be saved at loan creation time, do it in your view.
        loan_ticket.save(update_fields=['start_date'] if hasattr(loan_ticket, 'start_date') else None)

    if not getattr(loan_ticket, 'interest_rate', None) and LoanSettings:
        latest = LoanSettings.objects.order_by('-created_at').first() or LoanSettings.objects.last()
        if latest:
            loan_ticket.interest_rate = latest.interest_rate
            # persist interest_rate onto the loan_ticket so future logic reads it
            loan_ticket.save(update_fields=['interest_rate'])

    total_amount = Decimal(str(loan_ticket.loan_amount))
    duration = int(loan_ticket.loan_tenure)
    interest_rate = Decimal(str(loan_ticket.interest_rate or 0))
    start_date = loan_ticket.start_date or date.today()

    if duration <= 0:
        raise ValueError("loan_tenure must be a positive integer")

    emi_amount = calculate_emi(total_amount, interest_rate, duration)
    remaining_balance = total_amount

    last_end = start_date
    for i in range(1, duration + 1):
        emi_start = timezone.make_aware(start_date + relativedelta(months=i - 1))
        emi_end = timezone.make_aware(start_date + relativedelta(months=i))
        # interest component for this period
        monthly_interest = (remaining_balance * (interest_rate / Decimal('100')) / Decimal('12')).quantize(
            Decimal('0.01'), rounding=ROUND_HALF_UP
        )

        # principal component is EMI - interest
        principal_component = (emi_amount - monthly_interest).quantize(
            Decimal('0.01'), rounding=ROUND_HALF_UP
        )

        # On the last installment, absorb any rounding residuals into principal
        if i == duration:
            principal_component = remaining_balance
            emi_amount = (monthly_interest + principal_component).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

        remaining_balance = (remaining_balance - principal_component).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        if remaining_balance < Decimal('0.00'):
            remaining_balance = Decimal('0.00')

        EMI.objects.create(
            loan_ticket=loan_ticket,
            emi_no=i,
            emi_amount=emi_amount,
            outstanding_amount=remaining_balance,
            start_date=emi_start,
            end_date=emi_end,
            status='Pending'
        )

        current_start = emi_end
            # ✅ After loop, set final end date on loan ticket
        loan_ticket.end_date = emi_end
        loan_ticket.save(update_fields=['end_date'])

        last_end = emi_end

    # Update loan_ticket end_date (and optionally totals if those fields exist)
    fields_to_update = []
    if hasattr(loan_ticket, 'end_date'):
        loan_ticket.end_date = last_end
        fields_to_update.append('end_date')

    # optional: set totals if those fields are present on the model
    total_payable = (emi_amount * Decimal(duration)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    total_interest = (total_payable - Decimal(str(loan_ticket.loan_amount))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    if hasattr(loan_ticket, 'total_payable'):
        loan_ticket.total_payable = total_payable
        fields_to_update.append('total_payable')
    if hasattr(loan_ticket, 'total_interest'):
        loan_ticket.total_interest = total_interest
        fields_to_update.append('total_interest')

    if fields_to_update:
        loan_ticket.save(update_fields=fields_to_update)
    else:
        # ensure at least end_date is persisted elsewhere if needed in your view
        loan_ticket.save()

    return last_end



# def calculate_emi(principal, annual_rate, tenure_months):
#     """
#     Returns monthly EMI based on principal, annual interest rate, and tenure.
#     """
#     P = Decimal(principal)
#     R = Decimal(annual_rate) / (12 * 100)
#     N = int(tenure_months)

#     if R == 0:
#         emi = P / N
#     else:
#         emi = (P * R * (1 + R) ** N) / ((1 + R) ** N - 1)

#     return emi.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


# def create_emis_for_loan(loan_ticket):
#     """
#     Creates EMI records for the given loan_ticket.
#     Each EMI has unique start and end dates spaced one month apart.
#     """
#     total_amount = loan_ticket.loan_amount
#     duration = loan_ticket.loan_tenure
#     interest_rate = loan_ticket.interest_rate
#     start_date = loan_ticket.start_date

#     emi_amount = calculate_emi(total_amount, interest_rate, duration)

#     for i in range(1, duration + 1):
#         emi_start = start_date + relativedelta(months=i - 1)
#         emi_end = start_date + relativedelta(months=i)

#         EMI.objects.create(
#             loan_ticket=loan_ticket,
#             emi_no=i,
#             emi_amount=emi_amount,
#             outstanding_amount=emi_amount,
#             start_date=emi_start,
#             end_date=emi_end,
#             status='Pending'
#         )

#     # return the final EMI's end date for updating the loan_ticket
#     return emi_end