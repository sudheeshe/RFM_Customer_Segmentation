from flask import Flask, request, render_template
import pandas as pd


app = Flask(__name__)


@app.route('/', methods=['GET', "POST"])
def home():
    return render_template('home_page.html')

@app.route('/submit', methods=['POST'])
def result():

    csv = 'Data/Deployment_data/dataset_for_prediction.csv'
    customer_id = int(request.form.get('customer_id'))
    data = pd.read_csv(csv, dtype={'CustomerID':int, 'Type_of_customers': str})
    index_list = list(data['CustomerID'])

    output = ""

    if customer_id in index_list:

        filtered_df = data[data['CustomerID']== customer_id ]

        output =  filtered_df.Type_of_customers.values[0]

    else:
        output = 'Customer_ID not found in database, Maybe a New Customer or Please check Customer_ID'

    return render_template('result.html',result=output)

if __name__ == "__main__":
    app.run(debug=True)