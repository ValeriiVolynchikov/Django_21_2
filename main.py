# Импорт встроенной библиотеки для работы веб-сервера
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        try:
            with open("./html/contacts.html", "rb") as file:
                html_content = file.read()
            self.wfile.write(html_content)  # Отправка HTML-контента
        except FileNotFoundError:
            self.send_response(404)
            self.wfile.write(bytes("Page not found", "utf-8"))

    def do_POST(self):
        """ Метод для обработки входящих POST-запросов """
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        print(body)
        print(body.decode("utf-8"))  # Декодируем данные в строку

        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes("<html><body><h1>Form submitted successfully!</h1></body></html>", "utf-8"))



if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрах в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")
