import pandas as pd

from dto.computer_dto import computer_dto


class ExcelExtractor(object):
    path_file = ""

    def __init__(self, path: str):
        self.path_file = path

    def get_computer_dto(self) -> list:
        data = pd.read_excel(self.path_file)
        df = pd.DataFrame(data, columns=["client_name",
                                         "hostname",
                                         "ip_address",
                                         "location",
                                         "division",
                                         "merk",
                                         "tipe",
                                         "operation_system",
                                         "processor",
                                         "ram",
                                         "hardisk",
                                         "year",
                                         "seat_management",
                                         "inventory_number",
                                         "note",
                                         ]).fillna('')
        computer_dto_list = []

        for index, row in df.iterrows():
            # year_fixed = row["year"].replace("\xa0", " ")
            seat_management_bool = str(row["seat_management"]).upper() == "TRUE"
            computer_dto_list.append(
                computer_dto(client_name=row["client_name"],
                             hostname=row["hostname"],
                             division=row["division"],
                             ip_address=row["ip_address"],
                             inventory_number=row["inventory_number"],
                             location=row["location"],
                             year=row["year"],
                             seat_management=seat_management_bool,
                             merk=row["merk"],
                             tipe=row["tipe"],
                             note=row["note"],
                             hardisk=row["hardisk"],
                             ram=row["ram"],
                             processor=row["processor"],
                             operation_system=row["operation_system"],
                             deactive=False)
            )
        return computer_dto_list
