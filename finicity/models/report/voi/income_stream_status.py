import enum


# https://community.finicity.com/s/article/Credit-Decisioning#generate_voi_report
class IncomeStreamStatus(enum.Enum):
    active = "active"
    inactive = "inactive"

    @staticmethod
    def from_description(description):
        return IncomeStreamStatus(description)
