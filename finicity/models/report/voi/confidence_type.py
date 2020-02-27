import enum


# https://community.finicity.com/s/article/Credit-Decisioning#generate_voi_report
class ConfidenceType(enum.Enum):
    low = "LOW"
    moderate = "MODERATE"
    high = "HIGH"

    @staticmethod
    def from_description(description):
        return ConfidenceType(description)
