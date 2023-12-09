#! /usr/bin/env python3

from crontab import CronTab

CUSTOM_JOB_COMMENT = 'Custom Update Service State'

if __name__ == '__main__':
    custom_cron = CronTab(user='root')
    # Удаляем все предыдущие задания cron, лучше использовать cron.remove(comment=CUSTOM_JOB_COMMENT), но это не сработало :(
    custom_cron.remove_all()
    custom_job = custom_cron.new(command='sed -i "s/is .*$/is $(($(ps -o etimes= -p $(cat /var/run/nginx.pid)) / 60)) minutes/" /opt/custom_service_state', comment=CUSTOM_JOB_COMMENT)
    custom_job.minute.every(1)
    custom_cron.write()
    print('Custom cron is running')

