import datetime
from time import sleep

from config import TIME_ZONE
from main import bot
from models import Student
from utils import get_schedule


def notify(group, user_id, flag):
    bot.send_message(user_id, text=get_schedule('Сьогодні', group, bot, user_id, flag))


def main():
    current_time = TIME_ZONE.localize(datetime.datetime.now()).time().replace(second=0, microsecond=0)
    target_users = Student.at_time(current_time)
    for user in target_users:
        notify(user.group.group_code, user.student_id, user.extend)
        sleep(0.05)


if __name__ == '__main__':
    Student.set_notify_time(282213187, '8:43')
    main()