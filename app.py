from flask import Flask,render_template,request
import pickle



app=Flask(__name__)


with open('rfc_model.pkl','rb')as f:
    model=pickle.load(f)

# by default method get
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')



@app.route('/result',methods=['POST','GET'])
def result():
    tenure=float(request.form.get('tenure'))
    monthly_charges=float(request.form.get('monthly_charges'))
    total_charges=float(request.form.get('total_charges'))
    multiple_lines=int(request.form.get('multiple_lines'))
    internet_service=int(request.form.get('internet_service'))
    online_backups=int(request.form.get('online_backups'))
    device_protection=int(request.form.get('device_protection'))
    tech_support=int(request.form.get('tech_support'))
    contract_encoder=int(request.form.get('contract_encoder'))
    payment_method=int(request.form.get('payment_method'))
    input=[tenure,monthly_charges,total_charges,multiple_lines,internet_service,online_backups,device_protection,tech_support,contract_encoder,payment_method]
    
    predict=model.predict([input])
    print(predict)
    if predict==[0]:
        result="No Churn"
    else:
        result="Churn"
 
    
    
    
    return render_template('result.html',res=result)
    




if __name__=='__main__':
    app.run(debug=True)