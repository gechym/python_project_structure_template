import uvicorn
import sys

from utils.get_config import get_config

CONFIG = get_config()

def run_server():
    uvicorn.run("server:app", host=f"{CONFIG['server']['host']}", port=CONFIG['server']['port'], reload=True)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "server":
        run_server()
    else:
        print("Sử dụng: python main.py server")