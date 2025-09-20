from emi.models import EMI
from dateutil.relativedelta import relativedelta

def create_emis_for_loan(loan_ticket):
    total_amount = loan_ticket.loan_amount      
    duration = loan_ticket.loan_tenure     
    emi_amount = total_amount / duration
    start_date = loan_ticket.start_date

    for i in range(1, duration + 1):
        EMI.objects.create(
            loan_ticket=loan_ticket,
            emi_no=i,
            emi_amount=emi_amount,
            outstanding_amount=emi_amount,
            start_date=start_date,
            end_date=start_date + relativedelta(months=+1),
            status='Pending'
        )
        start_date += relativedelta(months=+1)
