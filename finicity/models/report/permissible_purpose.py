

# https://community.finicity.com/s/article/Permissible-Purpose-Codes
import enum


class PermissiblePurpose(enum.Enum):
    CODE_0A = "0A"  # Time share loan
    CODE_0B = "0B"  # Consumer  Written Consent
    CODE_0F = "0F"  # Construction Loan
    CODE_0G = "0G"  # Flexible Spending Credit Card
    CODE_00 = "00"  # Auto Loan
    CODE_01 = "01"  # Unsecured Loan
    CODE_02 = "02"  # Secured Loan
    CODE_03 = "03"  # Partially secured Loan
    CODE_04 = "04"  # Home improvement Loan
    CODE_05 = "05"  # FHA home improvement Loan
    CODE_06 = "06"  # Installment sales contract
    CODE_07 = "07"  # Revolving charge account
    CODE_08 = "08"  # Real estate, unk type, term in yrs
    CODE_09 = "09"  # Loan secured by co-signer
    CODE_1C = "1C"  # Purchase of Household Goods
    CODE_10 = "10"  # Commercial transaction with personal liability, guarantee or written instruction
    CODE_11 = "11"  # Recreational merchandise loan
    CODE_12 = "12"  # Education
    CODE_13 = "13"  # Lease
    CODE_15 = "15"  # Check credit or line of credit
    CODE_17 = "17"  # Manufactured home
    CODE_18 = "18"  # Credit Card
    CODE_19 = "19"  # FHA mortgage (terms in years)
    CODE_2A = "2A"  # Secured credit card  (rev terms)
    CODE_2C = "2C"  # Real estate mortgage, Farmers Home Administration (FMHA) (terms in years)
    CODE_2K = "2K"  # Government Sponsored Travel Card
    CODE_20 = "20"  # Note loan
    CODE_22 = "22"  # Secured by household goods
    CODE_23 = "23"  # Secured by household goods / other collateral
    CODE_25 = "25"  # VA real estate mortgage (terms in years)
    CODE_26 = "26"  # Conventional real estate mortgage  including purchase money and first mortgage (terms in years)
    CODE_27 = "27"  # Real estate mortgage, (term in months) with or without collateral  (usually second mortgage)
    CODE_3A = "3A"  # Auto lease
    CODE_3F = "3F"  # Pre-qualification Consent
    CODE_31 = "31"  # Unknown – Extension of credit, review, or collection
    CODE_4D = "4D"  # Cellular phone
    CODE_47 = "47"  # Credit line secured, revolving
    CODE_48 = "48"  # Collection dept/attorney/agency
    CODE_49 = "49"  # Insurance underwriting
    CODE_5A = "5A"  # R.E. – jr liens and non-purchase money first  (terms in years)
    CODE_5B = "5B"  # Second Mortgage – terms in months
    CODE_5C = "5C"  # Checking or Savings – possible additional offers
    CODE_5J = "5J"  # Business Credit Loan
    CODE_6A = "6A"  # Commercial installment loan
    CODE_6B = "6B"  # Commercial Mortgage – terms in years
    CODE_6C = "6C"  # Credit Granting – possible additional offers
    CODE_6D = "6D"  # Home Equity
    CODE_65 = "65"  # Government guaranteed unsecured loan
    CODE_66 = "66"  # Government guaranteed secured loan
    CODE_67 = "67"  # Government direct unsecured loan
    CODE_68 = "68"  # Government direct secured loan
    CODE_7A = "7A"  # Commercial line of credit (rev terms)
    CODE_7B = "7B"  # Agriculture
    CODE_78 = "78"  # Installment loan
    CODE_8A = "8A"  # Business credit card (rev terms)
    CODE_85 = "85"  # Bi-monthly mortgage payment (terms in years)
    CODE_87 = "87"  # Semi-monthly mortgage payment (terms in years)
    CODE_89 = "89"  # Home equity line of credit (revolving terms)
    CODE_9A = "9A"  # Secured home improvement
    CODE_9B = "9B"  # Business Line personally guaranteed
    CODE_90 = "90"  # Medical debt
    CODE_91 = "91"  # Debt consolidation
    CODE_92 = "92"  # Utility company
    CODE_98 = "98"  # Credit granting
