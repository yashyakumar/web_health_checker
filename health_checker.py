import requests
import os
import datetime
http_codes={
    200: 'OK',
    301: 'Moved Permanently',
    302: 'Found',
    400: 'Bad Request',
    401: 'Unauthorized',
    403: 'Forbidden',
    404: 'Not Found',
    500: 'Internal Server Error',
    502: 'Bad Gateway',
    503: 'Service Unavailable'
}
now=datetime.datetime.now()
log_time=now.strftime('%Y-%m-%d %H:%M:%S')

with open('websites.txt', 'r') as file:
    urls = [line.strip() for line in file if line.strip()]

for url in urls:
    try:
        response=requests.get(f'https://{url}', timeout=5)  # Set a timeout for the request
      # Raise an error for bad responses
        if response.status_code == 200:
            
           print("URL is valid and reachable.")
        else:
           with open('error_log.txt', 'a') as log_file:
              
               log_file.write(f"{log_time}: {url} is not reachable  with http error code {response.status_code} ({http_codes.get(response.status_code, 'Unknown Status')})\n")


    except requests.exceptions.RequestException as e:  # Catch any request-related errors
      
        with open('error_log.txt', 'a') as log_file:
              
               log_file.write(f"{log_time}: {url} is invalid or unreachable\n")

