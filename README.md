# MLOps HW2 ШАД 

## Описание

Этот сервис выполняет автоматический inference модели CatBoost на данных первого соревнования

сервис читает из Kafka сообщения формата test.csv

применяет к ним предобработку (как в соревновании)

делает предсказания с использованием уже готовой модели (из соревнования)

сервис пишет в Kafka сообщения со скором и флагом фрода

## Команды:

git clone https://github.com/Angelina814/mlops-hw2.git

cd mlops-hw2

docker-compose up --build

Streamlit UI: http://localhost:8501 Kafka UI: http://localhost:8080

Логи: docker-compose logs <service_name> # Например: fraud_detector, kafka, interface

## Использование:

Загрузите CSV через интерфейс Streamlit. Для тестирования работы проекта используется файл формата test.csv из соревнования https://www.kaggle.com/competitions/teta-ml-1-2025

Kafka UI: Просматривайте сообщения в топиках transactions и scoring Логи обработки: /app/logs/service.log внутри контейнера fraud_detector

Результаты- скоринговые оценки пишутся в топик scoring
