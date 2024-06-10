import requests
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='app_health_checker.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Define the URL to check
URL = 'http://your_application_url'

def check_application_status(url):
    try:
        response = requests.get(url)
        status_code = response.status_code

        if status_code == 200:
            logging.info(f'Application is UP. Status Code: {status_code}')
            return 'UP'
        else:
            logging.warning(f'Application is DOWN. Status Code: {status_code}')
            return 'DOWN'

    except requests.RequestException as e:
        logging.error(f'Application is DOWN. Error: {str(e)}')
        return 'DOWN'

if __name__ == '__main__':
    status = check_application_status(URL)
    print(f'The application status is: {status}')
