import pandas as pd

# 가상의 예상 온도 데이터
dates = pd.date_range(start='2022-01-01', end='2022-12-31', freq='M')
temperatures = [5, 6, 7, 8, 9, 10, 11, 12, 11, 10, 9, 8] * int(len(dates) / 12)
data = {'Date': dates, 'Temperature (C)': temperatures}

# DataFrame 생성
df = pd.DataFrame(data)

# CSV 파일로 저장
df.to_csv('seoul_temperature_2022.csv', index=False)
