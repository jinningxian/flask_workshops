import requests
from flask import render_template, url_for, redirect, Flask, request
import flask

print("Import success!")


app = flask.Flask('__name__')  # create flask object and assign to variable
app.config["DEBUG"] = True  # enables hot-reload feature theat reloads the page everytime there is a change

# @app.route('/', methods=['GET'])
# def homepage():
#     return "<p>Hello World!</p>"
@app.route('/search', methods=['POST'])
def  form_submit():
	user_query = request.form['search_query']
	print(user_query)
	direct_url = url_for('.search_imdb',query_string=user_query)
	print(direct_url)
	return redirect(direct_url)

@app.route('/search/<query_string>', methods=['GET'])
def search_imdb(query_string):
    url = "https://imdb8.p.rapidapi.com/title/auto-complete"

    querystring = {"q":query_string}

    headers = {
        'x-rapidapi-key': "ba41f17946msh7f87a4076bc2fc6p1a2cefjsn388c3bd05daf",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()
    return render_template('search-result.html', data=data)


# @app.route('/search/<video_title>')
# def dynamic_function(video_title):
#     return "Video title: " + video_title

# rendering html
@app.route("/")
def landing_page():
    try:
        return render_template('landing-page.html', user_name='Charlie')
    except NameError:
        return "An error occurred"

@app.route("/error")
def error_page():
    return render_template('error404.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")