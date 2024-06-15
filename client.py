import socket
import sys


# TCP/IPソケットを作成
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# サーバが待ち受けている特定の場所にソケットを接続する。
server_address = '/tmp/socket_file'
print('connecting to {}'.format(server_address))

# サーバーに接続
try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)


flag = True
while flag:

    inputstr = input()

    if(inputstr == 'exit'):
        flag = False
    else:
        # ソケット通信ではデータをバイト形式で送る必要がある
        message = inputstr.encode()
        sock.sendall(message)

        # サーバからの応答を待つ時間を2秒間に設定します。
        # この時間が過ぎても応答がない場合、プログラムは次のステップに進みます。
        sock.settimeout(2)

        # サーバからの応答を待ち、応答があればそれを表示します。
        try:
            while True:
                # サーバからのデータを受け取ります。
                # 受け取るデータの最大量は32バイトとします。
                data = sock.recv(32)

                # データがあればそれを表示し、なければループを終了します。
                if data:
                    print('Server response: ' + data.decode())
                else:
                    break

        # 2秒間サーバからの応答がなければ、タイムアウトエラーとなり、エラーメッセージを表示します。
        except(TimeoutError):
            print('Socket timeout, ending listening for server messages')


print('closing socket')
sock.close()