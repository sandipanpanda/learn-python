from dotenv import load_dotenv
load_dotenv()
import os
password = os.getenv('PASSWORD')
print(password)
