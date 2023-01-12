import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def get_shows():

    showstories_url = 'https://hacker-news.firebaseio.com/v0/showstories.json'
    show_ids = requests.get(showstories_url).json()[:5]

 
    shows = []
    for show_id in show_ids:
        show_url = f'https://hacker-news.firebaseio.com/v0/item/{show_id}.json'
        show = requests.get(show_url).json()
        shows.append(show)
    
    return render_template("latest_shows.html", shows=shows)

if __name__ == '__main__':
    app.run()