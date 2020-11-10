from app.bot import launch_bot
from dotenv import load_dotenv
from pathlib import Path

import os


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

if __name__ == "__main__":
    launch_bot(os.getenv("TOKEN"))
