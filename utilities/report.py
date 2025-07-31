import os
import datetime
import time
import shutil

class BehaveReporter:
    """
    Class Name: Behave Reporter
    Author: Moksha Tej
    Description: Reporter utility, that uses behave-html-formatter reporter with customisation
    Return Type: report.html
    Parameters: None
    """
    BASE_DIRECTORY = 'C:/Users/10835482/Desktop/CodingChallenges/GladiatorBDD/Reports'
    REPORT_DIRECTORY = os.path.join(BASE_DIRECTORY, "BehaveReport")

    def __init__(self):
        time.sleep(2)
        # Remove all contents of the REPORT_DIRECTORY if it exists
        if os.path.exists(self.REPORT_DIRECTORY):
            shutil.rmtree(self.REPORT_DIRECTORY)
        os.makedirs(self.REPORT_DIRECTORY, exist_ok=True)

    def generate_report(self):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
        timestamped_folder = os.path.join(self.REPORT_DIRECTORY, f"BehaveReport_{timestamp}")
        os.makedirs(timestamped_folder, exist_ok=True)

        behave_command = (
            f"behave -f behave_html_formatter:HTMLFormatter -o {timestamped_folder}/report.html"
        )
        os.system(behave_command)

        report_path = os.path.join(timestamped_folder, "report.html")
        if os.path.exists(report_path):
            os.startfile(report_path)

        return report_path

