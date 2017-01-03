#run PowerUp and report results

import os
import getpass
import subprocess
import logging

from lib.cuckoo.common.abstracts import Auxiliary
from lib.cuckoo.common.constants import CUCKOO_ROOT, CUCKOO_GUEST_PORT
from lib.cuckoo.common.exceptions import CuckooOperationalError
from lib.common.results import upload_to_host

log = logging.getLogger(__name__)

class PowerUp(Auxiliary):
    def __init(self):
        Auxiliary.__init__(self)
        self.proc = None
    
    def start(self):
        """
        Runs the powerup privesc module on the system and returns the result
        :return the text result of the powerup module
        """
        #self.key = "powerup_info"
        #after determining module works as desired, will process data into a dict to store. Until then, leave commented
        #data = {}
        
        #open the process and capture STDOUT 
        process = subprocess.Popen(["C:\Program Files\WindowsPowerShell\Modules\PowerSploit\Privesc\PowerUp.ps1 > C:\powerupOutput.txt"], stdout=subprocess.PIPE)
        #try:
            #try to get output from program
        #    (output, err) = process.communicate(timeout=60)
        #except TimeoutExpired:
            #if program takes longer than 60s to run, kill the program
        #    proc.kill()

        #data = output
        #data = "This is a test"
        return log.info("Started PowerUp")


    def stop(self):
        upload_to_host("C:\powerupOutput.txt", os.path.join("logs", "powerUpOutput.txt"))
