import os
from datetime import datetime

# Please customize the following variables 
USER_NAME = "ydong"
VERSION = "1.0.0"

def say_hi(msg: str = "Hi!", file_directory: str = "/app/data/") -> None:
    timestamp = datetime.now().strftime("%Y%m%d%H%M")
    file_name = f"outputfile_{USER_NAME}_{VERSION}_timestamp_{timestamp}.txt"
    file_path = os.path.join(file_directory, file_name)


    with open(file_path, "w") as file:
        file.write(msg)

    print(f"File '{file_path}' created successfully.")

def add_numbers(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    say_hi()
