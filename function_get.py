def get_filiales(employe_data):
    for enterprise in employe_data['Enterprise']:
        if enterprise['Filial']:
            return enterprise['Filial']
def get_filiale(employe_data, name_filiale):
    filiales = get_filiales(employe_data)
    for filial in filiales:
        if filial == name_filiale:
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