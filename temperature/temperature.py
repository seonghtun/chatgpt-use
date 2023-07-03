from fastapi import FastAPI, Request
import uvicorn
from fastapi.responses import HTMLResponse
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

app = FastAPI()

# CSV 파일 경로
csv_file = 'seoul_temperature_2022.csv'

@app.get("/", response_class=HTMLResponse)
async def get_index():
    html_content = """
    <html>
    <head>
        <title>Seoul Temperature</title>
    </head>
    <body>
        <h1>Seoul Temperature</h1>
        <img src="/plot" alt="Temperature Plot">
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/plot")
async def plot_temperature():
    # CSV 파일 읽기
    df = pd.read_csv(csv_file)

    # 그래프 그리기
    plt.plot(df['Date'], df['Temperature (C)'])
    plt.xlabel('Date')
    plt.ylabel('Temperature (C)')
    plt.title('Seoul Temperature')
    plt.xticks(rotation=45)
    
    # 그래프 이미지를 메모리에 저장
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    
    # 이미지를 응답으로 반환
    return bytes(buffer.getvalue())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

