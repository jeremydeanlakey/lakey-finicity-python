import enum


# https://community.finicity.com/s/article/Credit-Decisioning#generate_voi_report
class IncomeStreamStatus(enum.Enum):
    active = "ACTIVE"
    inactive = "INACTIVE"

    @staticmethod
    def from_description(description):
        return IncomeStreamStatus(description)
