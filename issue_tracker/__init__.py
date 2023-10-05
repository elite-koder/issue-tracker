import os
from issue_tracker.settings import *

PROD = "PROD"
DEV = "DEV"
FABRIC = DEV
if os.getenv("FABRIC") == PROD:
    FABRIC = PROD
    from issue_tracker.prod_settings import *
