import json
import statistics
from function_get import *
from function_calculate import *
def read_file_json(filename:str):
    with open(filename) as f:
        return json.load(f)
def extract_primary_key(dictionary:dict) -> list:
    keys_primary = []
    for key in dictionary:
        keys_primary.append(key)

        

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
def generate_json_enterprise(employes_data):
    employes_data = calcul_salaire(employes_data)
    employes_data_static = calcul_stat_salariales(employes_data)
    print()
    enterprise_data_static = calcul_stats_Enterprise(employes_data_static)
    return enterprise_data_static
def table_info_filiale_employe_statistic(employe_data_statistic):
    #Nom Filial
    # Name employe  

    return None
def main():
    employes_data = read_file_json('employes-data.json')
    employe_data_static = generate_json_enterprise(employes_data)
    



main()