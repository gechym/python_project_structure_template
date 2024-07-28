import uvicorn
import sys

from utils.get_config import get_config
config = get_config()


def main():
    if len(sys.argv) > 1:
        # command
        command = sys.argv[1]
        match command:
            case "server":
                host = config['server']['host']
                port = config['server']['port']
                uvicorn.run("server:app", host=host, port=port, reload=True)
            case _:  # default case
                print("Usage: python main.py server")
    else:
        print("Usage: python main.py server")


if __name__ == "__main__":
    main()
