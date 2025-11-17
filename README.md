# CS_HW5 — приложение клинет-сервер с поддержкой TLS

В предыдущую версию [проекта](https://github.com/KuchinaMA/ClientServerApp) добавлена поддержка TLS. В текущей версии всё также реализован простой клиент-сервер, общение осуществляется с помощью протокола TCP.

В данной версии добавлено:
- TLS шифрование всех передаваемых данных;
- Поддержка кастомных сертификатов и приватных ключей;
- Логирование сессионных ключей для анализа трафика.

## Установка и запуск

1. Клонирование репозитория:
```
git clone https://github.com/KuchinaMA/ClientServerApp.git
cd CLientServerApp
```

2. Генерация сертификатов:

```
cd certs
openssl req -x509 -newkey rsa:2048 -keyout certs/server.key.pem -out certs/server.cert.pem -days 365 -nodes -subj "/CN=localhost"
cd ..
```

3. Для логирования ключей
```
export SSLKEYLOGFILE=sslkeylog.txt
```

4. Запуск сервера
```
python3 main.py --role server --certfile certs/server.cert.pem --keyfile certs/server.key.pem
```

5. Запуск клиента (в отдельном окне)
```
export SSLKEYLOGFILE=sslkeylog.txt
python3 main.py --role client --host localhost --port 8888
```