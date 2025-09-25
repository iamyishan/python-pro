import argparse

# 创建解析器
# parser = argparse.ArgumentParser(description='这是一个命令行参数解析示例')
#
# # 添加参数
# parser.add_argument('filename', help='要处理的文件名')
# parser.add_argument('-v', '--verbose', action='store_true', help='显示详细信息')
# parser.add_argument('-n', '--number', type=int, default=10, help='处理数量')
#
# # 解析参数
# args = parser.parse_args()
#
# # 使用参数
# print(f"处理文件: {args.filename}")
# if args.verbose:
#     print("启用详细模式")
# print(f"处理数量: {args.number}")

# 运行程序
#python script.py data.txt -v -n 20


# 这是llamafactory内部实现的简化示例

def main():
    # 创建命令解析器
    parser = argparse.ArgumentParser(prog='llamafactory-cli')
    subparsers = parser.add_subparsers(dest='command')

    # 启动服务的子命令
    server_parser = subparsers.add_parser('serve', help='启动模型服务')
    server_parser.add_argument('--model', required=True, help='模型路径')
    server_parser.add_argument('--port', type=int, default=8000, help='服务端口')

    # 训练模型的子命令
    train_parser = subparsers.add_parser('train', help='训练模型')
    train_parser.add_argument('--data', required=True, help='训练数据路径')
    train_parser.add_argument('--epochs', type=int, default=3, help='训练轮次')

    # 解析命令行参数
    args = parser.parse_args()

    # 根据命令执行对应逻辑
    if args.command == 'serve':
        print(args.model,">>>>",args.port)
    elif args.command == 'train':
        print(args.data, "=======", args.epochs)


if __name__ == '__main__':
    main()