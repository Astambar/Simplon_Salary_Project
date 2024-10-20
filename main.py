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
    enterprise_data_static = calcul_stats_Enterprise(employes_data_static)
    return enterprise_data_static
def generate_json_enterprise_bis(enterprise_data_static):
      for name_enterprise in enterprise_data_static:
           if isinstance(name_enterprise, str):
                return enterprise_data_static[name_enterprise]
      return None
def generate_json_Filiales(enterprise_data_static):
    enterprise = generate_json_enterprise_bis(enterprise_data_static)
    for enterprise_data in enterprise:
         for internal in enterprise_data:
              if internal == "Filial":
                   return enterprise_data[internal]
    return None
def generate_json_employes_simplify(enterprise_data_static):
     filiales = generate_json_Filiales(enterprise_data_static)
     new_dict_simplify = {}
     for filial in filiales:
          datas_filial = filiales[filial]
          for data_filial in datas_filial:
               if data_filial == "Employes":
                    employes_filial = datas_filial[data_filial]
                    new_dict_simplify[filial] = []
                    for employ in employes_filial:
                         new_dict_simplify[filial].append(
                              {
                                   'name': employ["name"],
                                   'job': employ["job"],
                                   'monthly_salary': employ["monthly_salary"],
                                   })
                    
     return new_dict_simplify
def generate_json_statistic_enterprise(enterprise_data_static):
    enterprise = generate_json_enterprise_bis(enterprise_data_static)
    for enterprise_data in enterprise:
        for internal in enterprise_data:
            if internal == "EnterpriseStatistic":
                return enterprise_data[internal]
    return None

def generate_json_essential_data(enterprise_data_static):
     return None
def len_perfect(string, len_default = 24):
     len_string = len(string)
     if len_string != len_default:
        if len_string < len_default:
            string += " "*(len_default-len_string)
     return string
def table_info_filiale_employe_statistic(employe_data_statistic):
    employe_data_simplify = generate_json_employes_simplify(employe_data_statistic)
    filiale_data= generate_json_Filiales(employe_data_statistic)
    # Nom Filial
    # Name employe  | rôle | Salary_month
    string_prepare_table =  ""
    for filiale in employe_data_simplify:
         string_prepare_table += f"Entreprise: {filiale}:\n\n"
         filiale_employes = employe_data_simplify[filiale]
         average_salary = get_average_filiale(employe_data_statistic, filiale)
         minimum_salary = get_minimum_filiale(employe_data_statistic, filiale)
         maximum_salary = get_maximum_filiale(employe_data_statistic, filiale)
         for employ in filiale_employes:
              name = len_perfect(employ['name'])
              job = len_perfect(employ['job'])
              string_prepare_table += f"{name}| {job}| Salaire mensuel: {employ['monthly_salary']}€\n"
         string_prepare_table += f"\n"
         string_prepare_table += f"{"=" * 80} \n"
         string_prepare_table += f"Statistiques des salaires pour l'entreprise {filiale}:\n"
         string_prepare_table += f"Salaire moyen: {average_salary}\n"
         string_prepare_table += f"Salaire le plus élevé: {maximum_salary}\n"
         string_prepare_table += f"Salaire le plus bas:{minimum_salary}\n"
         string_prepare_table += f"{"=" * 80} \n"
    print(string_prepare_table)

    return None
def main():
    employes_data = read_file_json('employes-data.json')
    employe_data_static = generate_json_enterprise(employes_data)
    table_info_filiale_employe_statistic(employe_data_static)
main()