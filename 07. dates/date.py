from datetime import datetime

date1 = datetime.now()  # Actually Date and hour
print(date1.isoformat())  # Format ISO: 2023-08-25T15:20:30.123456

date2 = datetime.strptime("2023/01/01 22:00:00", "%Y/%m/%d %H:%M:%S")
print(date2.isoformat())  # 2023-01-01T22:00:00

date3 = datetime.fromtimestamp(1678720536.905)
print(date3.isoformat())  # 2023-03-13T15:15:36.905000

date4 = datetime(2023, 4, 3, 17, 30)
print(date4.isoformat())  # 2023-04-03T17:30:00