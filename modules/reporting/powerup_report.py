#a simple reporting module for powerup

import os

from lib.cuckoo.common.abstracts import Report
from lib.cuckoo.common.exceptions import CuckooReportError

class PowerUpReport(Report):
    def run(self, results):
        """
        Collects the results of powerup returned by the PowerUp Module (/cuckoo/modules/processing/powerup.py)
        and writes to a report found at /cuckoo/storage/analyses/<task_id>/reports
        """
            try:
                report = open(os.path.join(self.reports_path, "powerUp_report.txt"), "w")
                report.write(results["powerup_info"])

                report.close()
            except (TypeError, IOError) as e:
                raise CuckooReportError("Could not write PowerUp Report, :(")
