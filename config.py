from os import getenv
from dotenv import load_dotenv

load_dotenv()


### ❖ ➥
API_ID = (getenv("API_ID", None))

### ❖ ➥
API_HASH = getenv("API_HASH", None)

### ❖ ➥
STRING_SESSION = getenv("STRING_SESSION", None)

### ❖ ➥
OWNER_ID = int(getenv("OWNER_ID", "6927241780"))

### ❖ ➥
MONGO_URL = getenv("MONGO_URL", None)

### ❖ ➥
SUPPORT_GRP = getenv("SUPPORT_GRP", "Ravan_Lankaa")

### ❖ ➥
UPDATE_CHNL = getenv("UPDATE_CHNL", "God_Ravana")

### ❖ ➥
OWNER_USERNAME = getenv("OWNER_USERNAME", "GOD_R4V4N")


