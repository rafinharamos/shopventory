import unittest
from datetime import datetime
from time import sleep
from typing import List
from freezegun import freeze_time


def get_account_ids_to_run(account_ids_list: List, range_time: str = None):
    interval = 15
    if range_time == "day":
        time_average = datetime.now().day
    if range_time == "hour":
        time_average = datetime.now().hour
    else:
        range_time = "minute"
        time_average = datetime.now().minute
    index_mod = time_average % interval
    print(f"{range_time}: {time_average}")
    account_ids_to_return = [
        account_id
        for i, account_id in enumerate(account_ids_list)
        if i % interval == index_mod
    ]
    return account_ids_to_return


class TestAccountId(unittest.TestCase):
    def setUp(self):
        self.id_list = [number for number in range(1000, 1200, 1)]

    @freeze_time("2012-01-14 12:00:00")
    def test_get_account_ids_minute_15(self):
        resp = get_account_ids_to_run(self.id_list)
        self.assertEqual(
            resp,
            [
                1000,
                1015,
                1030,
                1045,
                1060,
                1075,
                1090,
                1105,
                1120,
                1135,
                1150,
                1165,
                1180,
                1195,
            ],
        )

    @freeze_time("2012-01-14 12:01:00")
    def test_get_account_ids_minute_16(self):
        resp = get_account_ids_to_run(self.id_list)
        self.assertEqual(
            resp,
            [
                1001,
                1016,
                1031,
                1046,
                1061,
                1076,
                1091,
                1106,
                1121,
                1136,
                1151,
                1166,
                1181,
                1196,
            ],
        )

    @freeze_time("2012-01-15 13:15:00")
    def test_get_account_ids_hour(self):
        resp = get_account_ids_to_run(self.id_list, "hour")
        self.assertEqual(
            resp,
            [
                1013,
                1028,
                1043,
                1058,
                1073,
                1088,
                1103,
                1118,
                1133,
                1148,
                1163,
                1178,
                1193,
            ],
        )

    @freeze_time("2012-01-15 13:16:00")
    def test_get_account_ids_same_hour(self):
        resp = get_account_ids_to_run(self.id_list, "hour")
        self.assertEqual(
            resp,
            [
                1013,
                1028,
                1043,
                1058,
                1073,
                1088,
                1103,
                1118,
                1133,
                1148,
                1163,
                1178,
                1193,
            ],
        )

    @freeze_time("2012-01-16 13:16:00")
    def test_get_account_ids_day(self):
        resp = get_account_ids_to_run(self.id_list, "day")
        self.assertEqual(
            resp,
            [
                1001,
                1016,
                1031,
                1046,
                1061,
                1076,
                1091,
                1106,
                1121,
                1136,
                1151,
                1166,
                1181,
                1196,
            ],
        )

    @freeze_time("2012-01-17 13:16:00")
    def test_get_account_ids_next_day(self):
        resp = get_account_ids_to_run(self.id_list, "day")
        self.assertEqual(
            resp,
            [
                1001,
                1016,
                1031,
                1046,
                1061,
                1076,
                1091,
                1106,
                1121,
                1136,
                1151,
                1166,
                1181,
                1196,
            ],
        )


if __name__ == "__main__":
    id_list = [number for number in range(1000, 1200, 1)]
    for i in range(60):
        print(i, get_account_ids_to_run(id_list, "hour"))
        sleep(60)
