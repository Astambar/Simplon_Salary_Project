def get_filiales(employe_data):
    """
    Récupère la liste des filiales d'une entreprise.

    Args:
        employe_data (dict): Dictionnaire contenant les données des employés, 
                             incluant les informations sur les entreprises.

    Returns:
        list: Liste des filiales de l'entreprise, ou None si aucune filiale n'est trouvée.
    """
    for enterprise in employe_data['Enterprise']:
        if enterprise['Filial']:
            return enterprise['Filial']


def get_filiale(employe_data, name_filiale):
    """
    Récupère une filiale spécifique par son nom.

    Args:
        employe_data (dict): Dictionnaire contenant les données des employés.
        name_filiale (str): Le nom de la filiale à récupérer.

    Returns:
        dict: Dictionnaire contenant les informations de la filiale, ou None si la filiale n'est pas trouvée.
    """
    filiales = get_filiales(employe_data)
    for filial in filiales:
        if filial == name_filiale:
            return filiales[filial]


def get_filiale_employe(employe_data:dict, name_filiale:str) -> list[dict]:
    """
    Récupère la liste des employés d'une filiale.

    Args:
        employe_data (dict): Dictionnaire contenant les données des employés.
        name (str): Le nom de la filiale dont on veut récupérer les employés.

    Returns:
        list: Liste des employés de la filiale, ou None si la filiale n'est pas trouvée.
    """
    filiale = get_filiale(employe_data, name_filiale)
    return filiale['Employes']


def get_filiale_employe_info(employe_data:dict, name_filiale:str, name_employe:str)-> dict:
    """
    Récupère les informations d'un employé spécifique dans une filiale donnée.

    Args:
        employe_data (dict): Dictionnaire contenant les données des employés.
        filiale (str): Le nom de la filiale.
        name_employe (str): Le nom de l'employé dont on veut récupérer les informations.

    Returns:
        dict: Dictionnaire contenant les informations de l'employé, ou None si l'employé n'est pas trouvé.
    """
    employees = get_filiale_employe(employe_data, name_filiale)
    for employee in employees:
        if employee['name'] == name_employe:
            return employee


def get_month_salary_employee(employe_data:dict, name_filiale:str, name_employe:str)->float|int|None:
    """
    Récupère le salaire mensuel d'un employé spécifique dans une filiale donnée.

    Args:
        employe_data (dict): Dictionnaire contenant les données des employés.
        filiale (str): Le nom de la filiale.
        name_employe (str): Le nom de l'employé.

    Returns:
        float: Le salaire mensuel de l'employé, ou None si l'employé ou son salaire n'est pas trouvé.
    """
    infos_employe = get_filiale_employe_info(employe_data, name_filiale, name_employe)
    return infos_employe.get('monthly_salary') if infos_employe else None


def get_statistic_filiale(employe_data:dict, name_filiale:str)-> list[dict]:
    """
    Récupère les statistiques d'une filiale spécifique.

    Args:
        employe_data (dict): Dictionnaire contenant les données des employés.
        name_filiale (str): Le nom de la filiale.

    Returns:
        list: Liste des statistiques de la filiale, ou None si la filiale n'est pas trouvée.
    """
    filiale = get_filiale(employe_data, name_filiale)
    return filiale['StatisticFilial'] if filiale else None


def get_average_filiale(employe_data:dict, name_filiale:str)->float|int:
    """
    Récupère le salaire moyen d'une filiale spécifique.

    Args:
        employe_data (dict): Dictionnaire contenant les données des employés.
        name_filiale (str): Le nom de la filiale.

    Returns:
        float: Le salaire moyen de la filiale, ou None si la filiale n'est pas trouvée.
    """
    return get_focus_info_filiale(employe_data, name_filiale, 'average_salary')


def get_focus_info_filiale(employe_data:dict, name_filiale:str, name_data_stat:str) -> float|int:
    """
    Récupère une information spécifique d'une filiale, comme le salaire moyen, minimum ou maximum.

    Args:
        employe_data (dict): Dictionnaire contenant les données des employés.
        name_filiale (str): Le nom de la filiale.
        name_data_stat (str): Le nom de la statistique à récupérer (e.g., 'average_salary').

    Returns:
        float: La valeur de la statistique demandée, ou None si la filiale ou la statistique n'est pas trouvée.
    """
    infos_filiale = get_statistic_filiale(employe_data, name_filiale)
    for info in infos_filiale:
        if name_data_stat in info:
            return info[name_data_stat]
    return None


def get_minimum_filiale(employe_data:dict, name_filiale:str)->int|float:
    """
    Récupère le salaire minimum d'une filiale spécifique.

    Args:
        employe_data (dict): Dictionnaire contenant les données des employés.
        name_filiale (str): Le nom de la filiale.

    Returns:
        float: Le salaire minimum de la filiale, ou None si la filiale n'est pas trouvée.
    """
    return get_focus_info_filiale(employe_data, name_filiale, 'salary_minimum')


def get_maximum_filiale(employe_data, name_filiale):
    """
    Récupère le salaire maximum d'une filiale spécifique.

    Args:
        employe_data (dict): Dictionnaire contenant les données des employés.
        name_filiale (str): Le nom de la filiale.

    Returns:
        float: Le salaire maximum de la filiale, ou None si la filiale n'est pas trouvée.
    """
    return get_focus_info_filiale(employe_data, name_filiale, 'maximum_salary')


def get_all_filiale(enterprise_data_static):
    """
    Récupère toutes les filiales d'une entreprise.

    Args:
        enterprise_data_static (dict): Dictionnaire contenant les données statiques des entreprises.

    Returns:
        list: Liste de toutes les filiales, ou None si aucune filiale n'est trouvée.
    """
    all_filiale = None  # Cette fonction n'est pas encore implémentée.
    return all_filiale
