import os
import subprocess
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(filename='backup.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Configuration
SOURCE_DIR = '/path/to/source/directory'
REMOTE_USER = 'remote_user'
REMOTE_HOST = '14.194.125.46'
REMOTE_DIR = '/path/to/remote/directory'

def backup_to_remote():
    try:
        result = subprocess.run(
            ['rsync', '-avz', SOURCE_DIR, f'{REMOTE_USER}@{REMOTE_HOST}:{REMOTE_DIR}'],
            check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        logging.info('Backup to remote server succeeded.')
        logging.info(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        logging.error('Backup to remote server failed.')
        logging.error(e.stderr.decode())

if __name__ == '__main__':
    backup_to_remote()
