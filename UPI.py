#!/usr/bin/env python
# coding: utf-8

# # About UPI Dataset -
# 
# 
# *  The data for UPI transactions and it's performance relating to Banks for the month of February 2023 is pulled from National Payment Corporation of India's Website
# 
# 
# * Webise consist of tables - 
# 1. UPI Top 50 Banks Performance
# 2. UPI Apps
# 3. UPI P2P and P2M Transactions
# 4. Top 15 PSPs
# 5. UPI Merchant Category Classification
# 
# * These Tables are further classified for interpretability

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline ')
import warnings
from warnings import filterwarnings
warnings.filterwarnings('ignore')


# In[2]:


import io
get_ipython().run_line_magic('cd', '"C:\\Users\\leand\\OneDrive\\Desktop\\Data Set\\\\Gov\\UPI"')


# In[3]:


upi_remitter_banks = pd.read_excel('UPI Remitter Banks.xlsx')


# In[4]:


upi_beneficiary_banks = pd.read_excel('UPI Beneficiary Banks.xlsx')


# In[5]:


upi_payer_PSP_performance = pd.read_excel('UPI Payer PSP Performance.xlsx')


# In[6]:


upi_payee_PSP_performance = pd.read_excel('UPI Payee PSP Performer.xlsx')


# In[7]:


UPI_P2P_and_P2M_transactions = pd.read_excel('UPI P2P and P2M Transactions.xlsx')


# In[8]:


UPI_Apps_Customer_Initiated_Transactions = pd.read_excel('UPI Apps Customer Initiated Transactions.xlsx')


# In[9]:


High_Transacting_Categories = pd.read_excel('High Transacting Categories.xlsx')


# In[10]:


Medium_Transacting_Categories = pd.read_excel('Medium Transacting Categories.xlsx')


# In[11]:


All_Other_Transacting_Categories = pd.read_excel('All Other Categories.xlsx')


# # All Data tables imported with further classification
# 
# * After Classifying we have - 
# 
# 1. UPI Remitter Banks
# 2. UPI Beneficiary Banks
# 3. UPI Payer PSP Performance
# 4. UPI Payee PSP Performance
# 5. UPI P2P and P2M Transactions
# 6. UPI Apps Customer Initiated Transactions
# 7. High Transacting Categories
# 8. Medium Transacting Categories
# 9. All Other Transacting Categories
# 
# 
# # Glossary for UPI Remitter Banks - 
# 
# 
# * Remitter - The account holder who is sending the money
#        
#        
# * Beneficiary - The account holder who is receiving money
#       
#       
# * Remitter Bank - The bank of the account holder who is sending the money
#      
#      
# * Beneficiary Bank - The bank of the account holder who is receiving money
# 
# 
# * Business Decline (BD) - Transaction decline due to a customer entering an invalid pin, incorrect beneficiary account etc. Or     due to other business reasons such as exceeding per transaction limit, exceeding permitted count of transactions per day,       exceeding amount limit for the day etc. Such declined transactions are termed as Business Decline. Any decline which is not     because of a technical reason of the bank or NPCI is termed as business Decline.
# 
# 
# * Technical Decline (TD) - Transaction decline due to technical reasons, such as unavailability of systems and network issues on   bank or NPCI side.
#     
#     
# * The Debit Reversal Success percentage indicates the % of total cases, where a customer account may be debited and their bank     is unable to confirm instantly about the status of reversal of such a debit. When reversal/credit is not processed instantly,   it is processed manually by the bank as per the extant RBI guidelines.
#      
#      
# * Deemed Approved (Pending Credit Confirmation for UPI remittance transactions) - Deemed Approved percentage indicates the total   percentage of cases of the total transactions, where credit confirmations are not received online from the beneficiary banks     for the credit. If the beneficiary account is not credited online, transaction would be manually processed by the beneficiary   bank as per the extant RBI guidelines.
# 
# 

# In[12]:


upi_remitter_banks.info()


# In[13]:


upi_remitter_banks.shape


# In[14]:


upi_remitter_banks.describe()


# In[15]:


upi_remitter_banks.columns


# In[16]:


upi_remitter_banks['UPI Remitter Banks'] 


# In[17]:


import matplotlib.pyplot as plt
import seaborn as sns

# Sort the data by the total volume in descending order
upi_remitter_banks = upi_remitter_banks.sort_values('Total Volume (In Mn)', ascending=False)

# Set the figure size
plt.figure(figsize=(12, 14))

# Create the horizontal bar plot with a color gradient
colors = sns.color_palette('Greens', len(upi_remitter_banks), desat=0.8)
plt.barh(upi_remitter_banks['UPI Remitter Banks'], upi_remitter_banks['Total Volume (In Mn)'], color=colors)

# Add data labels to each bar
for i, v in enumerate(upi_remitter_banks['Total Volume (In Mn)']):
    plt.text(v, i, str(v), color='white', fontweight='bold', fontsize=12, va='center')

# Set the title and subtitle for the plot
plt.title('Total UPI Transaction Volume by Remitter Bank', fontsize=20)
plt.suptitle('February 2023', fontsize=14, y=0.94)

# Set the labels for the x and y axis
plt.xlabel('Total Volume (In Mn)', fontsize=16)
plt.ylabel('UPI Remitter Banks', fontsize=16)

# Add a legend to explain the color coding
plt.legend(['Total Volume'], fontsize=16)

# Use a modern font and increase the font size
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 14

# Add a grid to make it easier to read and compare values across the horizontal axis
plt.grid(axis='x', linestyle='--')

# Adjust spacing between the bars to prevent overlapping labels
plt.subplots_adjust(left=0.3)

# Display the plot
plt.show()


# # Taking top 10 banks based on Total Volume

# In[18]:


top_10_UPI_remitter_banks = upi_remitter_banks.nlargest(10, 'Total Volume (In Mn)')
top_10_UPI_remitter_banks


# In[19]:


top_10_UPI_remitter_banks.columns


# In[20]:


top_10_UPI_remitter_banks = top_10_UPI_remitter_banks.sort_values('Total Volume (In Mn)', ascending=False)
plt.figure(figsize=(10, 6))
plt.barh(top_10_UPI_remitter_banks['UPI Remitter Banks'], top_10_UPI_remitter_banks['Total Volume (In Mn)'], color='#7CB5EC')
plt.title('Total UPI Transaction Volume by Remitter Bank top 10', fontsize=16)
plt.xlabel('Total Volume (In Mn)', fontsize=12)
plt.ylabel('UPI Remitter Banks', fontsize=12)
plt.legend(['Total Volume'], fontsize=12)
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10
plt.show()


# # Let's go over bank with highest technical declines and lowest Approval

# In[21]:


top_10_UPI_remitter_banks_with_highest_technical_declines = upi_remitter_banks.nlargest(10, 'Technical Decline')
top_10_UPI_remitter_banks_with_highest_technical_declines


# In[22]:


top_10_UPI_remitter_banks_with_lowest_approved_trans = upi_remitter_banks.nsmallest(10, 'Approved')
top_10_UPI_remitter_banks_with_lowest_approved_trans


# # oops  -

# * Business Decline (BD) - Transaction decline due to a customer entering an invalid pin, incorrect beneficiary account etc. Or     due to other business reasons such as exceeding per transaction limit, exceeding permitted count of transactions per day,       exceeding amount limit for the day etc. Such declined transactions are termed as Business Decline. Any decline which is not     because of a technical reason of the bank or NPCI is termed as business Decline.

# In[23]:


oops = upi_remitter_banks.nlargest(10, 'Business Decline')
oops


# # Remitter Banks with lowest DRS - 

# In[24]:


banks_w_least_DRS = upi_remitter_banks.nsmallest(10, 'Debit Reversal Success')
banks_w_least_DRS


# # We have explored the data for Remitter Banks , now let's dig Beneficiary Banks

# In[25]:


upi_beneficiary_banks.info()


# # Glossary
# 
# * Business Decline (BD) - Transaction decline due to a customer entering an invalid pin, incorrect beneficiary account etc. Or due to other business reasons such as exceeding per transaction limit, exceeding permitted count of transactions per day, exceeding amount limit for the day etc. Such declined transactions are termed as Business Decline. Any decline which is not because of a technical reason of the bank or NPCI is termed as business Decline.
# 
# 
# * Technical Decline (TD) - Transaction decline due to technical reasons, such as unavailability of systems and network issues on bank or NPCI side.
# 
# 
# * The Debit Reversal Success percentage indicates the % of total cases, where a customer account may be debited and their bank is unable to confirm instantly about the status of reversal of such a debit. When reversal/credit is not processed instantly, it is processed manually by the bank as per the extant RBI guidelines.
# 
# 
# * Deemed Approved (Pending Credit Confirmation for UPI remittance transactions) - Deemed Approved percentage indicates the total percentage of cases of the total transactions, where credit confirmations are not received online from the beneficiary banks for the credit. If the beneficiary account is not credited online, transaction would be manually processed by the beneficiary bank as per the extant RBI guidelines.
# 
# 
# * Remitter - The account holder who is sending the money
# * Beneficiary - The account holder who is receiving money
# * Remitter Bank - The bank of the account holder who is sending the money
# * Beneficiary Bank - The bank of the account holder who is receiving money

# In[26]:


upi_beneficiary_banks.describe()


# In[27]:


upi_beneficiary_banks = upi_beneficiary_banks.sort_values('Total Volume (In Mn)', ascending=False)

plt.figure(figsize=(12, 14))

colors = sns.color_palette('Greens', len(upi_remitter_banks), desat=0.8)
plt.barh(upi_beneficiary_banks['UPI Beneficiary Banks'], upi_beneficiary_banks['Total Volume (In Mn)'], color=colors)

for i, v in enumerate(upi_beneficiary_banks['Total Volume (In Mn)']):
    plt.text(v, i, str(v), color='white', fontweight='bold', fontsize=12, va='center')

plt.title('Total UPI Transaction Volume by Beneficiary Bank', fontsize=20)
plt.suptitle('February 2023', fontsize=14, y=0.94)

plt.xlabel('Total Volume (In Mn)', fontsize=16)
plt.ylabel('UPI Beneficiary Banks', fontsize=16)

plt.legend(['Total Volume'], fontsize=16)

plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 14

plt.grid(axis='x', linestyle='--')

plt.subplots_adjust(left=0.3)

plt.show()


# # Taking top 10 banks based on Total Volume

# In[28]:


upi_beneficiary_banks.columns


# In[29]:


top_10_UPI_beneficiary_banks = upi_beneficiary_banks.nlargest(10, 'Total Volume (In Mn)')
top_10_UPI_beneficiary_banks


# In[30]:


top_10_UPI_beneficiary_banks = top_10_UPI_beneficiary_banks.sort_values('Total Volume (In Mn)', ascending=False)

plt.figure(figsize=(10, 6))

plt.barh(top_10_UPI_beneficiary_banks['UPI Beneficiary Banks'], top_10_UPI_beneficiary_banks['Total Volume (In Mn)'], color='#7CB5EC')

plt.title('Total UPI Transaction Volume by Remitter Bank top 10', fontsize=16)

plt.xlabel('Total Volume (In Mn)', fontsize=12)
plt.ylabel('UPI Beneficiary Banks', fontsize=12)

plt.legend(['Total Volume'], fontsize=12)

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10
plt.show()


# # Now let's look at bank with highest technical declines and lowest Approval in Beneficiary Banks

# In[31]:


top_10_UPI_beneficiary_banks_with_highest_technical_declines = upi_beneficiary_banks.nlargest(10, 'Technical Decline')
top_10_UPI_beneficiary_banks_with_highest_technical_declines


# In[32]:


top_10_UPI_beneficiary_banks_with_lowest_approval = upi_beneficiary_banks.nsmallest(10, 'Approved')
top_10_UPI_beneficiary_banks_with_lowest_approval


# # Banks with lowest Deemed Approved
# 
# * Deemed Approved (Pending Credit Confirmation for UPI remittance transactions) - Deemed Approved percentage indicates the total percentage of cases of the total transactions, where credit confirmations are not received online from the beneficiary banks for the credit. If the beneficiary account is not credited online, transaction would be manually processed by the beneficiary bank as per the extant RBI guidelines. (Bhaiya mai bhej diya hu)

# In[33]:


banks_w_least_DA = upi_beneficiary_banks.nlargest(10, 'Deemed Approved')
banks_w_least_DA


# # We have explored the data for Beneficiary Banks , now let's dig upi apps

# In[34]:


UPI_Apps_Customer_Initiated_Transactions


# In[35]:


UPI_Apps_Customer_Initiated_Transactions.columns


# In[36]:


top_10_UPI_apps = UPI_Apps_Customer_Initiated_Transactions.nlargest(10, 'Value (Cr)')
top_10_UPI_apps


# In[37]:


UPI_Apps_Customer_Initiated_Transactions['App Name']


# In[38]:


whatsapp_data = UPI_Apps_Customer_Initiated_Transactions[UPI_Apps_Customer_Initiated_Transactions['App Name'] == 'WhatsApp']
print(whatsapp_data)


# # Highest Transactions using UPI

# In[39]:


High_Transacting_Categories


# In[40]:


High_Transacting_Categories_sorted = High_Transacting_Categories.sort_values(by = 'MCC',ascending=False)


# In[41]:


High_Transacting_Categories_sorted


# In[42]:


Medium_Transacting_Categories


# In[43]:


Medium_Transacting_Categories.sort_values(by = 'MCC', ascending=False)


# In[44]:


All_Other_Transacting_Categories


# In[45]:


All_Other_Transacting_Categories.sort_values(by = 'MCC', ascending=False)


# # Now let's see P2P and P2M UPI transaction

# In[46]:


UPI_P2P_and_P2M_transactions


# In[47]:


# Let's take important dataframes and put them in excel file then Power Bi


# In[48]:


# top_10_UPI_remitter_banks
# top_10_UPI_remitter_banks_with_highest_technical_declines
# top_10_UPI_remitter_banks_with_lowest_approved_trans
# oops
# banks_w_least_DRS
# top_10_UPI_beneficiary_banks
# top_10_UPI_beneficiary_banks_with_highest_technical_declines
# banks_w_least_DA
# top_10_UPI_apps
# High_Transacting_Categories
# Medium_Transacting_Categories
# All_Other_Transacting_Categories
# UPI_P2P_and_P2M_transactions


# In[49]:


top_10_UPI_remitter_banks


# In[50]:


top_10_UPI_remitter_banks_with_highest_technical_declines


# In[51]:


top_10_UPI_remitter_banks_with_lowest_approved_trans


# In[52]:


oops


# In[53]:


banks_w_least_DRS


# In[54]:


top_10_UPI_beneficiary_banks


# In[55]:


top_10_UPI_beneficiary_banks_with_highest_technical_declines


# In[56]:


banks_w_least_DA


# In[57]:


top_10_UPI_apps


# In[58]:


High_Transacting_Categories


# In[59]:


Medium_Transacting_Categories


# In[60]:


All_Other_Transacting_Categories


# In[61]:


UPI_P2P_and_P2M_transactions


# In[ ]:




