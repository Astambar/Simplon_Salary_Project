import json
import statistics
def read_file_json(filename:str):
    with open(filename) as f:
        return json.load(f)
def extract_primary_key(dictionary:dict) -> list:
    keys_primary = []
    for key in dictionary:
        keys_primary.append(key)
def calcul_salaire(employes_data:dict):
    for enterprise in employes_data:
        for employee in employes_data[enterprise]:
            contract_hours = employee['contract_hours']
            difference = employee['weekly_hours_worked'] - employee['contract_hours']
            hourly_rate = employee['hourly_rate']
            if difference > 0:
                employee['monthly_salary'] = ((1.5 * (hourly_rate * difference)) + (hourly_rate * contract_hours)) * 4
            else:
                employee['monthly_salary'] = (hourly_rate * contract_hours) * 4
    return (employes_data)

def calcul_stat_salariales(employes_data: dict):
    new_employee_data = {}

    for filiale in employes_data:
        count = 0
        sal_min = float('inf')  # Initialiser à l'infini
        sal_max = float('-inf')  # Initialiser à -infini
        total = 0
        
        # Initialiser les données de l'entreprise
        new_employee_data[filiale] = {
            "Employes": employes_data[filiale],
            "StatisticFilial": {}
        }
        
        for employee in employes_data[filiale]:
            if 'monthly_salary' in employee:
                if sal_max < employee['monthly_salary']:
                    sal_max = employee['monthly_salary']
                elif sal_min > employee['monthly_salary']:
                    sal_min = employee['monthly_salary']
                total += employee['monthly_salary']
                count += 1

        if count > 0:  # Éviter la division par zéro
            sal_moyen = total / count
            new_employee_data[filiale]["StatisticFilial"] = [
                {"average_salary": sal_moyen},
                {"salary_minimum": sal_min},
                {"maximum_salary": sal_max}
            ]
        else:
            new_employee_data[filiale]["StatisticFilial"] = [
                {"average_salary": 0},
                {"salary_minimum": 0},
                {"maximum_salary": 0}
            ]
    
    return new_employee_data
def calcul_stats_Enterprise(employes_data:dict):
    count = 0
    total = 0
    moyen_filial_salariale = 0
    minimum_filial_salariale = float('inf')  # Initialiser à l'infini
    maximum_filial_salariale = float('-inf')  # Initialiser à -infini
    for filiale in employes_data:
        
        max_base = employes_data[filiale]['StatisticFilial'][2]['maximum_salary']
        min_base = employes_data[filiale]['StatisticFilial'][1]['salary_minimum']
        if maximum_filial_salariale < max_base: # max < max_base
            maximum_filial_salariale = max_base
        elif minimum_filial_salariale > min_base:
            minimum_filial_salariale = min_base
        count += 1
        total += employes_data[filiale]['StatisticFilial'][0]['average_salary']
    if count > 0:
        moyen_filial_salariale = total / count
        employes_data = {"Enterprise":[
            {"Filial":employes_data},
            {"EnterpriseStatistic":[
                {"average_salary":moyen_filial_salariale},
                {"salary_minimum":minimum_filial_salariale},
                {"maximum_salary":maximum_filial_salariale}
            ]}
        ]}
    else:
        employes_data = {"Enterprise":[
            {"Filial":employes_data},
            {"EnterpriseStatistic":[
            {"average_salary":moyen_filial_salariale},
            {"salary_minimum":minimum_filial_salariale},
            {"maximum_salary":maximum_filial_salariale}
            ]}
        ]}
    return employes_data
        
def get_filiales(employe_data):
    for enterprise in employe_data['Enterprise']:
        if enterprise['Filial']:
            return enterprise['Filial']
def get_filiale(employe_data, name):
    filiales = get_filiales(employe_data)
    for filial in filiales:
        if filiales[filial]:
            return filiales[filial]

def get_filiale_employe(employe_data, name):
    filiale = get_filiale(employe_data, name)
    return filiale['Employes']
def get_filiale_employe_info(employe_data, filiale, name_employe):
    employees = get_filiale_employe(employe_data,filiale)
    for employee in employees:
        if employee['name'] == name_employe:
            return employee
def get_month_salary_employee(employe_data, filiale, name_employe):
    infos_employe = get_filiale_employe_info(employe_data, filiale, name_employe)
    for info in infos_employe:
        if info == 'monthly_salary':
            return infos_employe[info]       
def get_statistic_filiale(employe_data, name_filiale):
    filiale = get_filiale(employe_data, name_filiale)
    return filiale['StatisticFilial']
def get_average_filiale(employe_data, name_filiale):
    return get_focus_info_filiale(employe_data, name_filiale, 'average_salary')
def get_focus_info_filiale(employe_data, name_filiale, name_data_stat):
    infos_filiale = get_statistic_filiale(employe_data, name_filiale)
    for info in infos_filiale:
        for key in info:
            if key == name_data_stat:
                return info[key]
def get_minimum_filiale(employe_data, name_filiale):
    return get_focus_info_filiale(employe_data, name_filiale, 'salary_minimum')
def get_maximum_filiale(employe_data, name_filiale):
    return get_focus_info_filiale(employe_data, name_filiale, 'maximum_salary')
def get_all_filiale(enterprise_data_static):
    all_filiale = None
    return all_filiale
def print_all_get(enterprise_data_static):
        print(
        f"{get_filiale_employe(enterprise_data_static, 'TechCorp')=}\n\
        {get_filiale(enterprise_data_static, 'TechCorp')=}\n\
        \n{get_filiale_employe_info(enterprise_data_static, 'TechCorp','Helen')=}\n\
        \n{get_month_salary_employee(enterprise_data_static, 'TechCorp','Helen')=}\
        \n{get_statistic_filiale(enterprise_data_static, 'TechCorp')=}\
        \n{get_average_filiale(enterprise_data_static, 'TechCorp')=}\
        \n{get_minimum_filiale(enterprise_data_static, 'TechCorp')=}\
        \n{get_maximum_filiale(enterprise_data_static, 'TechCorp')=}")
def generate_json_enterprise(employe_data):
    employes_data = calcul_salaire(employes_data)
    employes_data_static = calcul_stat_salariales(employes_data)
    print()
    enterprise_data_static = calcul_stats_Enterprise(employes_data_static)
    return enterprise_data_static
def table_info_filiale_employe_statistic(employe_data_statistic):

    return None
def main():
    employes_data = read_file_json('employes-data.json')
    employe_data_static = generate_json_enterprise(employes_data)
    



main()