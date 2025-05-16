gRPC_server
このプロジェクトは、Python を使用して構築された基本的な gRPC サーバーの実装例です。
別リポジトリのswiftクライアントとの通信を想定しています。

📁 プロジェクト構成
gRPC_server/
├── hello.proto
├── hello_pb2.py
├── hello_pb2_grpc.py
├── server.py
└── __pycache__/

hello.proto: gRPC サービスとメッセージの定義を記述した Protocol Buffers ファイルです。

hello_pb2.py & hello_pb2_grpc.py: hello.proto から自動生成された Python コードです。

server.py: gRPC サーバーのメインスクリプトで、サービスの実装とサーバーの起動処理が含まれています。

🚀 動作環境
Python 3.x

grpcio および grpcio-tools パッケージ

⚙️ セットアップ手順
依存パッケージのインストール

pip install grpcio grpcio-tools
Protocol Buffers ファイルから Python コードの生成

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. hello.proto
gRPC サーバーの起動

python server.py
🧪 クライアント
gRPC_testリポジトリを参照してください
