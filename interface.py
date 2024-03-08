from flask import Flask, jsonify, render_template, request
from utils import SalaryPrediction
import config

app = Flask(__name__)


@app.route('/')
def salary_model():
    print('Welcome to the salary prediction Model')
    return render_template('page12.html')

@app.route('/predict_salary', methods = ['POST','GET'])
def get_insurance_charges():
    if request.method == 'POST':
        print('We are in POST Method')
        data = request.form
        Total_Experience = eval(data['Total_Experience'])  
        Team_Lead_Experience = eval(data['Team_Lead_Experience'])
        Project_Manager_Experience = eval(data['Project_Manager_Experience'])
        Certifications = eval(data['Certifications'])
     
        # print(f'age ={age}, sex = {sex}, bmi = {bmi}, children = {children}, smoker = {smoker}, region = {region}')  
        
        s_salary = SalaryPrediction(Total_Experience,Team_Lead_Experience,Project_Manager_Experience,Certifications)
        Salary1 = s_salary.get_predicted_salary()
        output=round(Salary1[0][0],2)
        # return jsonify({'Result': f'Total Salary is: RS. {round(Salary1[0][0],2)}'})
        return render_template('page12.html',prediction_text='Predicted Salary is Rs:{}'.format(output))
        
    else:
        print('We are in GET Method')
        data1 = request.args
        Total_Experience = eval(data['Total_Experience'])   
        Team_Lead_Experience = eval(data['Team_Lead_Experience'])
        Project_Manager_Experience = eval(data['Project_Manager_Experience'])
        Certifications = eval(data['Certifications'])
        

        s_salary1 = SalaryPrediction(Total_Experience,Team_Lead_Experience,Project_Manager_Experience,Certifications)
        Salary2 = s_salary1.get_predicted_salary()
        output1=round(Salary2[0][0],2)
        # return jsonify({'Result': f'Total Salary is : RS. {round(Salary2[0][0],2)}'})
        return render_template('page12.html',prediction_text='Predicted Salary is Rs:{}'.format(output1))
        
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = config.PORT_NUMBER, debug =True)