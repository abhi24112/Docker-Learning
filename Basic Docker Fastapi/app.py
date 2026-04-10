from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

class reviews(BaseModel):
    movie_name: str
    star: int
    description: str

class NumberSum(BaseModel):
    num1: float
    num2: float

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Number Summation App</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }
            
            .container {
                background: white;
                border-radius: 15px;
                box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
                padding: 40px;
                max-width: 500px;
                width: 100%;
            }
            
            h1 {
                color: #333;
                margin-bottom: 10px;
                text-align: center;
                font-size: 2em;
            }
            
            .subtitle {
                color: #666;
                text-align: center;
                margin-bottom: 30px;
                font-size: 0.95em;
            }
            
            .form-group {
                margin-bottom: 20px;
            }
            
            label {
                display: block;
                margin-bottom: 8px;
                color: #333;
                font-weight: 600;
                font-size: 0.95em;
            }
            
            input[type="number"] {
                width: 100%;
                padding: 12px 15px;
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                font-size: 1em;
                transition: border-color 0.3s;
            }
            
            input[type="number"]:focus {
                outline: none;
                border-color: #667eea;
                box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
            }
            
            button {
                width: 100%;
                padding: 12px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 1em;
                font-weight: 600;
                cursor: pointer;
                transition: transform 0.2s, box-shadow 0.2s;
                margin-top: 10px;
            }
            
            button:hover {
                transform: translateY(-2px);
                box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
            }
            
            button:active {
                transform: translateY(0);
            }
            
            .result-container {
                margin-top: 30px;
                padding: 20px;
                background: #f8f9fa;
                border-radius: 8px;
                border-left: 4px solid #667eea;
                display: none;
            }
            
            .result-container.show {
                display: block;
                animation: slideIn 0.3s ease;
            }
            
            @keyframes slideIn {
                from {
                    opacity: 0;
                    transform: translateY(-10px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            
            .result-label {
                color: #666;
                font-size: 0.9em;
                margin-bottom: 8px;
            }
            
            .result-value {
                font-size: 2em;
                color: #667eea;
                font-weight: bold;
            }
            
            .error {
                color: #e74c3c;
                background: #fadbd8;
                padding: 12px;
                border-radius: 8px;
                margin-top: 15px;
                display: none;
                border-left: 4px solid #e74c3c;
            }
            
            .error.show {
                display: block;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🧮 Sum Calculator</h1>
            <p class="subtitle">Add two numbers together</p>
            
            <form id="sumForm">
                <div class="form-group">
                    <label for="num1">First Number</label>
                    <input 
                        type="number" 
                        id="num1" 
                        placeholder="Enter first number"
                        step="0.01"
                        required
                    >
                </div>
                
                <div class="form-group">
                    <label for="num2">Second Number</label>
                    <input 
                        type="number" 
                        id="num2" 
                        placeholder="Enter second number"
                        step="0.01"
                        required
                    >
                </div>
                
                <button type="submit">Calculate Sum</button>
            </form>
            
            <div class="error" id="errorMsg"></div>
            
            <div class="result-container" id="resultContainer">
                <div class="result-label">Result:</div>
                <div class="result-value" id="resultValue">0</div>
            </div>
        </div>
        
        <script>
            document.getElementById('sumForm').addEventListener('submit', async (e) => {
                e.preventDefault();
                
                const num1 = parseFloat(document.getElementById('num1').value);
                const num2 = parseFloat(document.getElementById('num2').value);
                const errorMsg = document.getElementById('errorMsg');
                const resultContainer = document.getElementById('resultContainer');
                
                errorMsg.classList.remove('show');
                
                try {
                    const response = await fetch('/sum', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({num1, num2})
                    });
                    
                    if (!response.ok) throw new Error('Calculation failed');
                    
                    const data = await response.json();
                    document.getElementById('resultValue').textContent = data.result;
                    resultContainer.classList.add('show');
                } catch (error) {
                    errorMsg.textContent = '❌ Error: ' + error.message;
                    errorMsg.classList.add('show');
                    resultContainer.classList.remove('show');
                }
            });
        </script>
    </body>
    </html>
    """

@app.post("/sum")
async def sum_numbers(data: NumberSum):
    """Sum two numbers and return the result"""
    return {"result": data.num1 + data.num2}

# If you want to run at the specific port.
# uvicorn app:app --reload --port 8080