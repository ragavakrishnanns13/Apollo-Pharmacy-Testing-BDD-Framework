from utilities.report import BehaveReporter

if __name__ == "__main__":
    reporter = BehaveReporter()
    report_path = reporter.generate_report()
