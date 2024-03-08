import pickle
import json
import numpy as np
# import config

class SalaryPrediction():

    def __init__(self,Total_Experience,Team_Lead_Experience,Project_Manager_Experience,Certifications):
        self.Total_Experience = Total_Experience
        self.Team_Lead_Experience = Team_Lead_Experience
        self.Project_Manager_Experience = Project_Manager_Experience
        self.Certifications = Certifications
    def load_model(self):
        with open('Linear_Model.pkl', 'rb') as f:
            self.model = pickle.load(f)

        with open('project_data.json', 'r') as f:
            self.project_data = json.load(f)

    def get_predicted_salary(self):
        self.load_model()

        test_array = np.zeros(len(self.project_data['columns']))
        test_array[0] = self.Total_Experience
        test_array[1] = self.Team_Lead_Experience
        test_array[2] = self.Project_Manager_Experience
        test_array[3] = self.Certifications
        print('Test Array :', test_array)

        predicted_salary = self.model.predict([test_array])
        print(f'Salary is : RS. {predicted_salary}')
        return predicted_salary
    if __name__ == '__main__':
        Total_Experience = 7
        Team_Lead_Experience =2 
        Project_Manager_Experience =4
        Certifications = 1
        salary = SalaryPrediction(Total_Experience,Team_Lead_Experience,Project_Manager_Experience,Certifications)
        salary.get_predicted_salary()