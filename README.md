# LocalChatMessenger

## 概要

Pythonのソケット通信とfakerパッケージを使用して、クライアントサーバ間で情報をやりとりするシンプルなアプリケーションです。このプロジェクトはコンピュータサイエンス学習サービス[Recursion](https://recursion.example.com)の課題で取り組みました。

## インストール

- スクリプトを実行するにはPythonの[faker](https://pypi.org/project/Faker/0.7.4/)パッケージをインストールする必要があります。

```sh
pip install faker
```
- もしくはrequirements.txtを使用してインストール
```sh
pip install -r requirements.txt
```

## 実行方法

- 以下のコマンドを使用して、実行する。

```sh
python3 server.py
```
```sh
python3 client.py
```
クライアント側のターミナルで任意の値を入力

### 注意
- 名前付きパイプ（UNIXソケット）を使用しているため、Windowsの標準的なコマンドプロンプトやPowerShellでは動作しません。
- このアプリケーションはLinuxまたはWSL（Windows Subsystem for Linux）環境で動作します。
