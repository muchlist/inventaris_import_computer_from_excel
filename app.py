import os
import time

import setting
from utils.excel_reader import ExcelExtractor
from utils.postman import Postman


def main_program():
    path_file = os.path.join('static', setting.file_name)

    reader = ExcelExtractor(path_file)
    computer_list = reader.get_computer_dto()

    postman = Postman()
    postman.set_base_url(setting.base_url)
    token_response = postman.get_token(setting.user_name, setting.password)
    postman.set_token(token_response)

    list_response = []

    for computer in computer_list:
        response = postman.post_cctv(computer)
        list_response.append(response)
        time.sleep(0.3)

    file_response_path = os.path.join("static", "response.txt")
    file_response_text = open(file_response_path, "w")
    for response in list_response:
        file_response_text.writelines(f"{response}\n")
        print(response)
    file_response_text.close()


if __name__ == '__main__':
    main_program()
