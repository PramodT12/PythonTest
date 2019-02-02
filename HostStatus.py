#Read a file and display the status of hosts
#FIle :
#https://www.slb.com/
#https://www.techmahindra.com/
#https://www.adp.com/
#O/P format:
#Host : https://www.slb.com/
#Status : Available

import requests

with open("HostEntries") as fobj:
    for server in fobj:
        server=server.strip()
        r=requests.get(server)
        if r.status_code == 200:
            print("Server    :",server)
            print("Status    :","Success")
