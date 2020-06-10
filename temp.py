from sum import extra
from rouge import Rouge

#extra(text,n,op)
# if op == 1:
#         return(bow(text,n)) 49,18,42
#     elif op == 2:
#         return(lexs(parser,n))
#     elif op == 3:
#         return(luhn(parser,n))
#     elif op == 4:
#         return(lsa(parser,n))
#     elif op == 5:
#         return(textrank(parser,n))
#     elif op == 6:
#         return(sumbasic(parser,n))
#     elif op == 7:
#         return(klsum(parser,n))
#     elif op == 8:
#         return(reduction(parser,n))
#     elif op ==9:
#         return(tfidf(text,n))



rouge = Rouge()

text = '''The Company hereby agrees to employ Employee, and Employee hereby agrees to render his 
exclusive service to the Company, in his current capacity of Senior Vice 
President and Chief Financial Officer of the Company, with such duties as may be assigned to him from time to time by the 
Board of Directors.\nThis Agreement shall be effective commencing on June
1, 2002 (the effective date of this Agreement). This Agreement shall, as of its
first anniversary, and on each annual anniversary thereof, be extended
automatically, without further action by the Employee or the Company, for an
additional one (1) year, so that there shall, as of June 1 of each year, be
three (3) years remaining in the term of this Agreement (the "Employment
Period"), subject to earlier termination as hereinafter provided.\n
Unless otherwise agreed by the Company and
Employee, throughout the term of this Agreement, Employee's business office
shall be located in Frisco, Texas.\n
Employee shall be compensated by the Company at a
minimum base rate of $15,833.33 per month, payable semimonthly on the fifteenth
and final days of each month during the period of Employee's employment under
this Agreement, subject to such increases and additional payments as may be
determined from time to time by the Board of Directors of the Company in its
sole discretion. Employee shall also be entitled to participate in any Company
discretionary bonus plan. Such compensation shall be in addition to any group
insurance, pension, profit sharing, and other employee benefits, which are
extended from time to time to Employee in the discretion of the Board of
Directors of the Company and for which Employee is eligible. Subject to such
rules and procedures as are from time to time specified by the Company, the
Company shall also reimburse Employee for all reasonable expenses incurred by
him on behalf of the Company.\n
Employee shall devote his full working time to
the business of the Company; provided, however, Employee shall be excused from
performing any services for the Company hereunder during periods of temporary
incapacity and during vacations conforming to the Company's standard vacation
policy, without thereby in any way affecting the compensation to which he is
entitled hereunder.'''

reference = '''The company agrees to employ the Employee for his services as Senior Vice president and Chief Financial Officer.
The agreement shall be effective from June 1,2002 and shall be extended by one year at every anniversary that is subject to earlier termination.
Employee's business office is located in Frisco, Texas unless altered by the company
Employee shall be compensated with $15,833.33 per month which is payable semimonthy on the fifteenth and final days of each month. 
The additional payments will be subject to the Board of Directors. The employee can apply for comapny's bonus plans. Compensations and other benefits is also subject to the discretion of the Board of Directors. 
Reasonable expenses on behalf of the company will be reimbursed.
Employee shall devote exclusive service to company and will be excused in cases of incapacity or vacations while entitled to compensation.'''


for i in range(1,10):
    hypothesis = extra(text,4,i)
    scores = rouge.get_scores(str(hypothesis), str(reference))
    print(f"Model {i}..............................................")
    print(hypothesis)
    print("\n")

    print(scores)





