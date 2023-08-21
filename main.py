from nslookup import Nslookup
import time
import logging
import os

domain = os.environ['DOMAIN']

while(True) : 
    dns_query = Nslookup()
    try :
        ips_record = dns_query.dns_lookup(domain)
        if ips_record.answer == [] :
            logging.error('DNS Error')
        else :
            logging.info(ips_record.response_full, ips_record.answer)
            print(ips_record.response_full, ips_record.answer)

    except Exception as e: 
        logging.warning(e)

    time.sleep(5)



