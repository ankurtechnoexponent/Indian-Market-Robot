import http.client
import mimetypes

conn = http.client.HTTPConnection("api.connect.angelone.in")

payload = """{
    "clientcode": "CLIENT_ID",
    "password": "CLIENT_PIN",
    "totp": "TOTP_CODE",
    "state": "STATE_VARIABLE"
}"""

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-UserType': 'USER',
    'X-SourceID': 'WEB',
    'X-ClientLocalIP': 'CLIENT_LOCAL_IP',
    'X-ClientPublicIP': 'CLIENT_PUBLIC_IP',
    'X-MACAddress': 'MAC_ADDRESS',
    'X-PrivateKey': 'API_KEY'
  }
conn.request(
    "POST",    "/rest/auth/angelbroking/user/v1/loginByPassword",payload,headers)

res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
