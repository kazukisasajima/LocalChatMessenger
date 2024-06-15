# socketとosモジュールをインポートします
import socket
import os
from faker import Faker


# UNIXソケットをストリームモードで作成します
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# このサーバが接続を待つUNIXソケットのパスを設定します
server_address = '/tmp/socket_file'

# 以前の接続が残っていた場合に備えて、サーバアドレスをアンリンク（削除）します
try:
    os.unlink(server_address)
# サーバアドレスが存在しない場合、例外を無視します
except FileNotFoundError:
    pass

print('Starting up on {}'.format(server_address))

# サーバアドレスにソケットをバインド（接続）します
sock.bind(server_address)

# ソケットが接続要求を待機するようにします
sock.listen(1)

# Fakerインスタンスを作成
faker = Faker()

# 無限ループでクライアントからの接続を待ち続けます
while True:
    # クライアントからの接続を受け入れます
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # ループが始まります。これは、サーバが新しいデータを待ち続けるためのものです。
        while True:
            # ここでサーバは接続からデータを読み込みます。
            # 16という数字は、一度に読み込むデータの最大バイト数です。
            data = connection.recv(16)

            if data:
                # 受け取ったデータはバイナリ形式なので、それを文字列に変換。
                data_str =  data.decode('utf-8')
                print('Received ' + data_str)

                # Fakerを使用してランダムな応答を生成
                response = faker.text() 

                # ここでメッセージをバイナリ形式（エンコード）に戻してから送信します。
                connection.sendall(response.encode())

            # クライアントからデータが送られてこなければ、ループを終了します。
            else:
                print('no data from', client_address)
                break

    finally:
        print("Closing current connection")
        connection.close()