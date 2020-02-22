import enum


# https://community.finicity.com/s/article/201750879-Error-and-Aggregation-Status-Codes
class AggregationStatusCode(enum.Enum):
    code_103 = "103"  # Invalid Credentials
    code_108 = "108"  # User Action Required
    code_109 = "109"  # User Action Required
    code_169 = "169"  # Duplicate Account
    code_185 = "185"  # Missing or Incorrect MFA Answer
    code_187 = "187"  # Missing or Incorrect MFA Answer
    code_913 = "913"  # Account Has Been Closed
    code_914 = "914"  # Account No Longer Available
    code_931 = "931"  # Bank security requires a one time passcode for every connection.
    code_936 = "936"  # Customer's language preference is not supported for aggregation.
    code_900 = "900"  # New Institution being created
    code_901 = "901"  # New Institution being created
    code_903 = "903"  # New Institution being created
    code_904 = "904"  # New Institution being created
    code_905 = "905"  # Institution down for maintenance
    code_906 = "906"  # Institution down for maintenance
    code_907 = "907"  # Institution down for maintenance
    code_910 = "910"  # Institution connection is currently down and is being worked on.
    code_915 = "915"  # Institution not working for a specific user or group of users.
    code_916 = "916"  # Institution not working for a specific user or group of users.
    code_920 = "920"  # This institution does not currently support aggregation.
    code_921 = "921"  # This institution does not currently support aggregation.
    code_922 = "922"  # This institution does not currently support aggregation.
    code_923 = "923"  # This institution does not currently support aggregation.
    code_924 = "924"  # This institution does not currently support aggregation.
    code_925 = "925"  # This institution does not currently support aggregation.
    code_926 = "926"  # This institution does not currently support aggregation.
    code_927 = "927"  # This institution does not currently support aggregation.
    code_928 = "928"  # This institution does not currently support aggregation.
    code_929 = "929"  # This institution does not currently support aggregation.
