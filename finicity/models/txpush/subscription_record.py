from dataclasses import dataclass

from finicity.models.txpush.subscription_type import SubscriptionType


# https://community.finicity.com/s/article/205139316-TxPUSH-Services?ui-force-components-controllers-recordGlobalValueProvider.RecordGvp.getRecord=1&r=5#subscription_record
@dataclass
class SubscriptionRecord(object):
    id: int  # The subscription ID
    accountId: int  # The account being monitored by this subscription
    type: SubscriptionType
    callbackUrl: str  # The TxPUSH Listener URL where event notifications will be sent
    signingKey: str  # A signing key that will be used to validate the signature of events received for this subscription
