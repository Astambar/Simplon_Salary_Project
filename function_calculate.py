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
