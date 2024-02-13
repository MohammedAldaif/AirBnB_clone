#!/usr/bin/python3


class city(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ''
        self.state_id = ''
