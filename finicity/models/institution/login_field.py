from dataclasses import dataclass
from typing import Optional


# https://community.finicity.com/s/article/202460265-Institutions#loginfield_record
@dataclass
class LoginField(object):
    unused_fields: dict  # this is for forward compatibility and should be empty
    id: str  # The ID of this field
    name:  str  # The system name for this field
    value: str  # A default value for this field, if found (always blank for masked fields)
    displayOrder: Optional[int]  # An ordinal number to facilitate sorting fields for display
    mask: Optional[bool]  # true if the contents of this field should NOT be displayed on the screen (for password-style fields)
    description: Optional[str]  # The displayable name for this field
    instructions: Optional[str]  # Additional instructions from the institution (should be displayed if present)
    valueLengthMin: Optional[int]  # The minimum length for this field's value, or "0" if not known
    valueLengthMax: Optional[int]  # The maximum length for this field's value, or "0" if not known

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        id = data.pop('id')
        name = data.pop('name')
        value = data.pop('value')
        displayOrder = data.pop('displayOrder', None)
        mask_str = data.pop('mask', None)
        mask = bool(mask_str) if mask_str else None
        description = data.pop('description', None)
        instructions = data.pop('instructions', None)
        valueLengthMin_str = data.pop('valueLengthMin', None)
        valueLengthMin = int(valueLengthMin_str) if valueLengthMin_str else None
        valueLengthMax_str = data.pop('valueLengthMax', None)
        valueLengthMax = int(valueLengthMax_str) if valueLengthMax_str else None
        return LoginField(
            id=id,
            name=name,
            value=value,
            displayOrder=displayOrder,
            mask=mask,
            description=description,
            instructions=instructions,
            valueLengthMin=valueLengthMin,
            valueLengthMax=valueLengthMax,
            unused_fields=data,
        )
