# TPOS_MIPT


### Ansible

---
**Алгоритм тестирования:**

1. Запустить виртуальную машину с Vagrant и выполнить Ansible-скрипт.
2. Проверить, что при запросе `GET /service_data` получены начальные данные.
3. Подождать более 1 минуты и проверить обновление `uptime`.
4. Повторно выполнить Ansible-скрипт и убедиться, что `uptime` не сброшен и Nginx не перезапущен.
5. Изменить первую строку в `service_state`, повторно выполнить Ansible и проверить обновление файла и рестарт Nginx.
6. Подождать более 1 минуты и проверить, что `uptime` обновлен.

---

