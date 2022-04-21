#import modules
from flask import Flask , jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests
from datetime import datetime

#flask app instance
app = Flask(__name__)
CORS(app)

DAY_INDEX = [0,1,2,3,4]
student_list_ids = ['19-7-14-0','19-7-14-1','19-7-14-2','19-7-14-3','19-7-14-4']
professor_list_ids = ['20-6-12-0','20-6-12-1','20-6-12-2','20-6-12-3','20-6-12-4']
#api routes
@app.route('/api/restaurant')
def get_data():
    student_result , professor_result = [], []
    TODAY_INDEX = datetime.today().weekday()-6
    URL = 'https://www.cbnucoop.com/service/restaurant/'
    soup = BeautifulSoup(requests.get(URL).content, "html.parser")

    #for student data
    data = soup.find('div', {'data-table':student_list_ids[TODAY_INDEX]})
    main_dish = data.find('h6').text
    food_names = [ele.text for ele in data.find_all('li')]
    food_names.append(main_dish)
    food_names = [foodname.replace('/', '-') for foodname in food_names]
    student_result = list(reversed(food_names))

    #for professor data
    data = soup.find('div', {'data-table':professor_list_ids[TODAY_INDEX]})
    main_dish = data.find('h6').text
    food_names = [ele.text for ele in data.find_all('li')]
    food_names.append(main_dish)
    food_names = [foodname.replace('/', '-') for foodname in food_names]
    professor_result = list(reversed(food_names))


    return jsonify({'student':student_result , 'professor': professor_result})
    #for getting one week data
    # URL = 'https://www.cbnucoop.com/service/restaurant/'
    # soup = BeautifulSoup(requests.get(URL).content, "html.parser")
    # student_result , professor_result = [], []

    # for day_index, student_list_id in enumerate(student_list_ids):
    #     data = soup.find('div', {'data-table':student_list_id})
    #     main_dish = data.find('h6').text
    #     food_names = [ele.text for ele in data.find_all('li')]
    #     food_names.append(main_dish)
    #     student_result.append(list(reversed(food_names)))
    # for day_index, professor_list_id in enumerate(professor_list_ids):
    #     data = soup.find('div', {'data-table':professor_list_id})
    #     main_dish = data.find('h6').text
    #     food_names = [ele.text for ele in data.find_all('li')]
    #     food_names.append(main_dish)
    #     professor_result.append(list(reversed(food_names)))
    # return jsonify({'student':student_result , 'professor': professor_result})

#start flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 9001, debug=True)