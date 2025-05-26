from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd
from datetime import datetime


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


df = pd.DataFrame(columns=['Date', 'Open', 'High', 'Low', 'Close', 'Adj_Close', 'Volume'])
driver.get("https://finance.yahoo.com/quote/PLTR/history/?period1=1736553600&period2=1739318400#eyJsYXlvdXQiOnsiaW50ZXJ2YWwiOiJkYXkiLCJwZXJpb2RpY2l0eSI6MSwidGltZVVuaXQiOm51bGwsImNhbmRsZVdpZHRoIjoxLCJmbGlwcGVkIjpmYWxzZSwidm9sdW1lVW5kZXJsYXkiOnRydWUsImFkaiI6dHJ1ZSwiY3Jvc3NoYWlyIjp0cnVlLCJjaGFydFR5cGUiOiJjYW5kbGUiLCJleHRlbmRlZCI6ZmFsc2UsIm1hcmtldFNlc3Npb25zIjp7fSwiYWdncmVnYXRpb25UeXBlIjoib2hsYyIsImNoYXJ0U2NhbGUiOiJsaW5lYXIiLCJzdHVkaWVzIjp7InZvbCB1bmRyIjp7InR5cGUiOiJ2b2wgdW5kciIsImlucHV0cyI6eyJTZXJpZXMiOiJzZXJpZXMiLCJpZCI6InZvbCB1bmRyIiwiZGlzcGxheSI6InZvbCB1bmRyIn0sIm91dHB1dHMiOnsiVXAgVm9sdW1lIjoiIzBkYmQ2ZWVlIiwiRG93biBWb2x1bWUiOiIjZmY1NTQ3ZWUifSwicGFuZWwiOiJjaGFydCIsInBhcmFtZXRlcnMiOnsiY2hhcnROYW1lIjoiY2hhcnQiLCJlZGl0TW9kZSI6dHJ1ZX0sImRpc2FibGVkIjpmYWxzZX19LCJwYW5lbHMiOnsiY2hhcnQiOnsicGVyY2VudCI6MSwiZGlzcGxheSI6IlBMVFIiLCJjaGFydE5hbWUiOiJjaGFydCIsImluZGV4IjowLCJ5QXhpcyI6eyJuYW1lIjoiY2hhcnQiLCJwb3NpdGlvbiI6bnVsbH0sInlheGlzTEhTIjpbXSwieWF4aXNSSFMiOlsiY2hhcnQiLCJ2b2wgdW5kciJdfX0sInNldFNwYW4iOnsibXVsdGlwbGllciI6MSwiYmFzZSI6InllYXIiLCJwZXJpb2RpY2l0eSI6eyJwZXJpb2QiOjEsInRpbWVVbml0IjoiZGF5In0sInNob3dFdmVudHNRdW90ZSI6dHJ1ZSwiZm9yY2VMb2FkIjpmYWxzZSwidXNlRXhpc3RpbmdEYXRhIjp0cnVlfSwib3V0bGllcnMiOmZhbHNlLCJhbmltYXRpb24iOnRydWUsImhlYWRzVXAiOnsic3RhdGljIjp0cnVlLCJkeW5hbWljIjpmYWxzZSwiZmxvYXRpbmciOmZhbHNlfSwibGluZVdpZHRoIjoyLCJmdWxsU2NyZWVuIjp0cnVlLCJzdHJpcGVkQmFja2dyb3VuZCI6dHJ1ZSwiY29sb3IiOiIjMDA4MWYyIiwiY3Jvc3NoYWlyU3RpY2t5IjpmYWxzZSwic3ltYm9scyI6W3sic3ltYm9sIjoiUExUUiIsInN5bWJvbE9iamVjdCI6eyJzeW1ib2wiOiJQTFRSIiwicXVvdGVUeXBlIjoiRVFVSVRZIiwiZXhjaGFuZ2VUaW1lWm9uZSI6IkFtZXJpY2EvTmV3X1lvcmsiLCJwZXJpb2QxIjoxNzM5MTE2ODAwLCJwZXJpb2QyIjoxNzM5MjY4MDAwfSwicGVyaW9kaWNpdHkiOjEsImludGVydmFsIjoiZGF5IiwidGltZVVuaXQiOm51bGwsInNldFNwYW4iOnsibXVsdGlwbGllciI6MSwiYmFzZSI6InllYXIiLCJwZXJpb2RpY2l0eSI6eyJwZXJpb2QiOjEsInRpbWVVbml0IjoiZGF5In0sInNob3dFdmVudHNRdW90ZSI6dHJ1ZSwiZm9yY2VMb2FkIjpmYWxzZSwidXNlRXhpc3RpbmdEYXRhIjp0cnVlfX1dfSwiZXZlbnRzIjp7ImRpdnMiOnRydWUsInNwbGl0cyI6dHJ1ZSwidHJhZGluZ0hvcml6b24iOiJub25lIiwic2lnRGV2RXZlbnRzIjpbXX0sInByZWZlcmVuY2VzIjp7ImN1cnJlbnRQcmljZUxpbmUiOnRydWUsImRpc3BsYXlDcm9zc2hhaXJzV2l0aERyYXdpbmdUb29sIjpmYWxzZSwiZHJhZ2dpbmciOnsic2VyaWVzIjp0cnVlLCJzdHVkeSI6ZmFsc2UsInlheGlzIjp0cnVlfSwiZHJhd2luZ3MiOm51bGwsImhpZ2hsaWdodHNSYWRpdXMiOjEwLCJoaWdobGlnaHRzVGFwUmFkaXVzIjozMCwibWFnbmV0IjpmYWxzZSwiaG9yaXpvbnRhbENyb3NzaGFpckZpZWxkIjpudWxsLCJsYWJlbHMiOnRydWUsImxhbmd1YWdlIjpudWxsLCJ0aW1lWm9uZSI6IkFtZXJpY2EvTmV3X1lvcmsiLCJ3aGl0ZXNwYWNlIjo1MCwiem9vbUluU3BlZWQiOm51bGwsInpvb21PdXRTcGVlZCI6bnVsbCwiem9vbUF0Q3VycmVudE1vdXNlUG9zaXRpb24iOmZhbHNlfX0-")

navi= driver.find_element(By.TAG_NAME, 'tbody')

rows = navi.find_elements(By.TAG_NAME, 'tr')

data_list = []

for row in rows:
    elements = row.find_elements(By.TAG_NAME, 'td')
    date = elements[0].text.replace(',', '')
    # Convert to datetime object
    date_obj = datetime.strptime(date, "%b %d %Y")

    # Format to DDMMYYYY
    formatted_date = date_obj.strftime("%d%m%Y")

    # Convert to integer
    date_int = int(formatted_date)
    data = {'Date': date_int,
            'Open': elements[1].text, 
            'High': elements[2].text, 
            'Low': elements[3].text, 
            'Close': elements[4].text, 
            'Adj_Close': elements[5].text, 
            'Volume': elements[6].text.replace(',', '')}
    print(data)
    data_list.append(data)

df = pd.DataFrame(data_list)
print(df)
df.to_csv('PLTR_latest.csv', index=False)