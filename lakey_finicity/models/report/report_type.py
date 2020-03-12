import enum


# https://community.finicity.com/s/article/Credit-Decisioning#generate_voi_report
class ReportType(enum.Enum):
    voa = "voa"  # Verification of Assets
    voi = "voi"  # Verification of Income
