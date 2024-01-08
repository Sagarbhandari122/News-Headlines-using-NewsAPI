from flask import Flask, render_template, request
import requests

app = Flask(__name__, template_folder='c:\\Users\\Asus\\Documents\\Networking Python')


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		country = request.form['country']
		from_date = request.form['from_date']

		url = ('https://newsapi.org/v2/top-headlines?'
		       f'country={country}&'
		       f'from={from_date}&'
		       'sortBy=popularity&'
		       'apiKey=b4d393080c0f4c518e8f62ed504d8417')

		response = requests.get(url)

		if response.status_code == 200:
			data = response.json()
			articles = data['articles']
			print(f"Number of articles retrieved: {len(articles)}")
			return render_template('/templete/index.html', articles=articles)
		else:
			return f'Request failed with status code {response.status_code}'
	else:
		return render_template('/templete/index.html', articles=[])

if __name__ == '__main__':
	app.run(debug=True)