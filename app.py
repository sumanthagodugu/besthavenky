from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>CI/CD Demo</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 40px;
                background: #f5f5f5;
            }
 
            .marquee-box {
                width: 100%;
                overflow: hidden;
                white-space: nowrap;
                box-sizing: border-box;
                border: 2px solid black;
                background: white;
                padding: 20px 0;
            }
 
            .marquee-text {
                display: inline-block;
                padding-left: 100%;
                animation: scroll-left 12s linear infinite;
                font-size: 36px;
                font-weight: bold;
                color: black;
            }
 
            @keyframes scroll-left {
                0% {
                    transform: translateX(0%);
                }
                100% {
                    transform: translateX(-100%);
                }
            }
        </style>
    </head>
    <body>
        <div class="marquee-box">
            <div class="marquee-text">
                Hi Vijya this website is using CI/CD pipeline in backend
            </div>
        </div>
    </body>
    </html>
    """
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
