from django.shortcuts import render
from .models import BankDetail
# Create your views here.
# import pandas as pd
# tmp_data=pd.read_csv('bank_branches.csv',sep=';')
# #ensure fields are named~ID,Product_ID,Name,Ratio,Description
# #concatenate name and Product_id to make a new field a la Dr.Dee's answer
# details = [
#     BankDetail(
#         ifsc = tmp_data.ix[row]['ifsc'],
#         bank_id = tmp_data.ix[row]['bank_id'],
#         branch = tmp_data.ix[row]['branch'],
#         address = tmp_data.ix[row]['address'],
#         city = tmp_data.ix[row]['city'],
#         district = tmp_data.ix[row]['district'],
#         state = tmp_data.ix[row]['state'],
#         bank_name= tmp_data.ix[row]['bank_name'],
#     )
#     for row in tmp_data['ID']
# ]
# BankDetail.objects.bulk_create(details)

# path='bank_branches.csv'
# with open(path) as f:
#         reader = csv.reader(f)
#         for row in reader:
#             created = BankDetail.objects.get_or_create(
#                 ifsc=row[0],
#                 bank_id=row[1],
#                 branch=row[2],
#                 address=row[3],
#                 city=row[4],
#                 district=row[5],
#                 state=row[6],
#                 bank_name=row[7],
#                 )