from datetime import date


def get_auto_status(start_date, end_date):
    if not start_date and not end_date:
        return 'Статус неизвестен'

    today = date.today()
    if (end_date and end_date < today) or (not end_date and start_date and start_date < today):
        return 'Завершено'
    if (start_date and end_date > today) or (not start_date and end_date and end_date > today):
        return 'Запланировано'
    if (start_date and end_date and start_date <= today <= end_date) or \
            (start_date and not end_date and start_date == today) or \
            (end_date and not start_date and end_date == today):
        return 'Проводится'
    return 'Статус неизвестен'
