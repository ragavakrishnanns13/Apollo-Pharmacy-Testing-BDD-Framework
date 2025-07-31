import os
import datetime
from selenium import webdriver
from utilities.report import BehaveReporter

# Setup log directory
base_dir = r'C:/Users/10835482/Desktop/CodingChallenges/GladiatorBDD/'
log_dir = os.path.join(base_dir, 'logs')
os.makedirs(log_dir, exist_ok=True)

scenario_log_file = os.path.join(log_dir, 'scenario_log.txt')
step_log_file = os.path.join(log_dir, 'step_log.txt')

def before_all(context):
    options = webdriver.ChromeOptions()
    print("Instance created")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(options=options)

def after_step(context, step):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "PASSED" if step.status == "passed" else "FAILED"
    log_entry = f"[{timestamp}] Step: {step.name} - {status}\n"

    with open(step_log_file, "a") as log:
        log.write(log_entry)

def after_scenario(context, scenario):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "PASSED" if scenario.status == "passed" else "FAILED"
    log_entry = f"[{timestamp}] Scenario: {scenario.name} - {status}\n"

    with open(scenario_log_file, "a") as log:
        log.write(log_entry)

def after_all(context):
    print("Instance destroyed")
    context.driver.quit()

    # Generate HTML report
    reporter = BehaveReporter()
    reporter.generate_report()
