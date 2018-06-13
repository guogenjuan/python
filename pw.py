#python3
#pw.py -An insecure password locker program.
PASSWORD={'eamil':'guogenjuan@126.com','blog':'guogenjuan','luggage':'12345'}

import sys,pyperclip
if len(sys.argv)<2:
    print('Usage： python pw.py [account]-copy account password')
    sys.exit()
account = sys.argv[1] 

if account in PASSWORD:
    pyperclip.copy(PASSWORD[account])
    print('Password for'+account+'copied to clipboard')
else:
    print('There id  no account named'+account)
