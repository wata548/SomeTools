import yt_dlp
import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



def Download(urls):
    path = os.path.join('./downloads', '%(playlist_title)s', '%(playlist_index)s. %(title)s.%(ext)s')
    
    setting = {  
        'outtmpl':path,
        'format': 'bestaudio/best',  
        'postprocessors': [
            { 
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3', 
                'preferredquality': '320',
            }
        ],
    }

    with yt_dlp.YoutubeDL(setting) as ydl :
        ydl.download([urls])
        #for url in urls :
            #ydl.download([url])


@app.route('/execute', methods=['POST'])
def execute():
    data = request.json
    inputValue = data.get("input_value")
    
    if not inputValue:
        return jsonify({"error": "No URL provided"}), 400
    
    try:
        Download(inputValue)
        return jsonify({"message": "Download started!"})  # ✅ 응답 반환 추가
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    
    
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000,debug=True)