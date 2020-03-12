import enum


# https://community.finicity.com/s/article/Credit-Decisioning#generate_voi_report
class ReportStatus(enum.Enum):
    inProgress = "inProgress"
    success = "success"
    failure = "failure"
