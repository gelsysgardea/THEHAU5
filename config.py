from dataclasses import dataclass
import os
import json
from typing import Union

@dataclass
class Config:
    ...
    # ==================================================
    CHATS = [
           -1002199942999,
           -1002025984391,
           -1001897656640,
    ]

    CLIENT_NAME: str = "ClientName"
    API_ID: int = 25388732
    API_HASH: str = "f9a7ab46494a09f801e3bde68b93f5c1"

    MAX_HOUR_REQUESTS: Union[int, float] = 100


   
    headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36", 
        "bnc-uuid": "43d3e9dd-46ac-4c39-97c4-8b73f4417f5b",  
        "device-info": "TU_DEVICE_INFO",  
        "clienttype": "web",  
        "csrftoken": "c52c55cf31c11f4e9d47b6ee0a895aab",
        "fvideo-id": "3326dd4e9928a34e9c81e0f6de157d52381b4f9e",
        "fvideo-token": "LWLvEfjKgNCvwrnWoeko0eZ9KSCbryEGkgZMlk4jbWslL4J5koS9UG37XROx2uN7YAzPS2wPfqs3ogvGOGYfGBZOp6YfMW8iTpFh79F5AntpLX3pEXyfBJX8Tw0kiRk4WeVJ/Yk681bCR73HQZj0HuBguTrlSfF8XY2POH1NU5Ibne67rCSOLo9JCY+I0y72k=26",
        "x-trace-id": "e2bc9ede-3ed0-4baf-9a47-12a46a5fdf4b",
        "x-ui-request-trace": "e2bc9ede-3ed0-4baf-9a47-12a46a5fdf4b",
        "lang": "es-MX",  
        "Referer": "https://www.binance.com/en/my/wallet/account/payment/cryptobox",
        "Cookie": 'aws-waf-token=b7fa5e66-1bd7-4750-99fd-67319be1e57b:EQoAirIFZjoDAAAA:W5T/w3yQLfE7J3xg7mxCgGJp4VcGFw1vD6lvF46o9bJkPUz/c7QYlxKnzUc08SkohitDgXSRB/t5B1dS3LSDSVNTlGwe7amOOfcdDmyDQVOOqNeZWJbt23c2alAB1BDXs40UkiaM2DkESYISRN7HRS4R3Ch1kATaD5obuTrbFbGaBvioioPp5m5XIUJeq2h6iFg=; bnc-uuid=43d3e9dd-46ac-4c39-97c4-8b73f4417f5b; sajssdk_2015_cross_new_user=1; _gid=GA1.2.335801783.1745628388; BNC_FV_KEY=3326dd4e9928a34e9c81e0f6de157d52381b4f9e; BNC_FV_KEY_T=101-CscATm3aP0YuzrHmw8pewUOp5PE5pyA3RmNtIgZN%2FgcGxTOoYxVd7pUYQMPT9CNpiEcW7YPRIOotYxQBSi%2B2VA%3D%3D-fm9Zw%2F7mmvUSS3%2FzNxm1lw%3D%3D-17; BNC_FV_KEY_EXPIRE=1745649988183; lang=en; language=en; se_gd=lEBEVUBpVFOVAYUELCwkgZZCgVFAABXWlMe9bW0VlRSUQElNWVNd1; se_gsd=dy4gLCtiIi03IxI1JzI2DiYnDVFWAwZaWFxAUVxRV1RUElNT1; r20t=web.3D133A9BFBDF0AB8ED636B13E26C0C46; r30t=1; cr00=9068381BA3A23DBC135533E228C16324; d1og=web.1096314291.D79DD0EF878DE6E918B1EAF1B4C71F70; r2o1=web.1096314291.5BD8B6CEB26EE9E30F4194D9B50D4687; f30l=web.1096314291.073538CDBCBE184BB9A916C22B9B1571; currentAccount=; logined=y; isAccountsLoggedIn=y; BNC-Location=MX; OptanonAlertBoxClosed=2025-04-26T01:03:28.569Z; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221096314291%22%2C%22first_id%22%3A%221966f8f597f91f-028852982006be-26011c51-2073600-1966f8f5980172b%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk2NmY4ZjU5N2Y5MWYtMDI4ODUyOTgyMDA2YmUtMjYwMTFjNTEtMjA3MzYwMC0xOTY2ZjhmNTk4MDE3MmIiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIxMDk2MzE0MjkxIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%221096314291%22%7D%2C%22%24device_id%22%3A%221966f8f597f91f-028852982006be-26011c51-2073600-1966f8f5980172b%22%7D; theme=dark; p20t=web.1096314291.C06D7EB43575A919A30628A9803059A5; se_sd=QULAlB1FXDWVQxUVQEgAgZZCxFBIBESVVQS5fVENlRSUQD1NWVwQ1; _gcl_au=1.1.114092956.1745629765; _uetsid=18181230223b11f0a0e0f9e65d23e8b1; _uetvid=18184580223b11f09a31d50655d2604d; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Apr+25+2025+19%3A22%3A17+GMT-0600+(hora+est%C3%A1ndar+central)&version=202411.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=ced02f57-31fd-4ca9-8772-baf8bc3fd1ff&interactionCount=2&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&AwaitingReconsent=false&intType=1&geolocation=MX%3BCHH; _ga=GA1.1.1965283554.1745628388; _ga_3WP50LGEEC=GS1.1.1745629409.1.1.1745630539.60.0.0',
    }

    def __getelement__(self, element: str) -> Union[int, float, bool, str]:
        return getattr(self, element, None)

