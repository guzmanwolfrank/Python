TRADING ACCOUNT TRACKER
======================

Files included:
1. Dashboard.csv - Overview of all accounts
2. Account_1.csv - Detailed daily tracking for Account 1
3. Account_2.csv - Detailed daily tracking for Account 2
4. Account_3.csv - Detailed daily tracking for Account 3
5. Account_4.csv - Detailed daily tracking for Account 4
6. Account_5.csv - Detailed daily tracking for Account 5
7. Account_6.csv - Detailed daily tracking for Account 6
8. Account_7.csv - Detailed daily tracking for Account 7
9. Account_8.csv - Detailed daily tracking for Account 8
10. Account_9.csv - Detailed daily tracking for Account 9
11. Account_10.csv - Detailed daily tracking for Account 10
12. Account_11.csv - Detailed daily tracking for Account 11
13. Account_12.csv - Detailed daily tracking for Account 12
14. Account_13.csv - Detailed daily tracking for Account 13
15. Account_14.csv - Detailed daily tracking for Account 14
16. Account_15.csv - Detailed daily tracking for Account 15
17. Account_16.csv - Detailed daily tracking for Account 16
18. Account_17.csv - Detailed daily tracking for Account 17
19. Account_18.csv - Detailed daily tracking for Account 18
20. Account_19.csv - Detailed daily tracking for Account 19
21. Account_20.csv - Detailed daily tracking for Account 20

GOOGLE SHEETS IMPORT INSTRUCTIONS:
--------------------------------
1. Create a new Google Sheet
2. Create a separate sheet for each account plus the dashboard
3. For each sheet, go to File > Import > Upload and select the corresponding CSV
4. Choose 'Replace data at selected cell' and make sure cell A1 is selected
5. Set up formulas in the Dashboard to pull data from individual account sheets

SUGGESTED FORMULAS FOR DASHBOARD:
--------------------------------
To pull latest balance: =QUERY('Account X'!A:L,"SELECT L WHERE A = date '"&TEXT(TODAY(),"yyyy-mm-dd")&"'",0)
To calculate days since payout: =DATEDIF([Last Payout Date Cell], TODAY(), "D")
To find highest profit day: =QUERY('Account X'!A:H,"SELECT A WHERE H = "&MAX('Account X'!H:H)&"",0)
