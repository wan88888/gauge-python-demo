# Gauge Python Demo

这是一个使用Gauge和Python进行自动化测试的示例项目。项目展示了如何使用Gauge框架进行Web UI测试和API测试。

## 项目结构

```
├── specs/                 # 测试规范文件目录
│   ├── login_test.spec    # 登录测试规范
│   └── api_test.spec      # API测试规范
├── step_impl/             # 步骤实现目录
│   ├── pages/             # 页面对象模型
│   ├── login_test_impl.py # 登录测试实现
│   └── api_test_impl.py   # API测试实现
└── env/                   # 环境配置目录
```

## 环境要求

- Python 3.11+
- Gauge
- Chrome浏览器（用于UI测试）

## 安装步骤

1. 安装Gauge
   ```bash
   # macOS
   brew install gauge
   
   # Windows
   choco install gauge
   ```

2. 安装Python依赖
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows使用: .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

## 运行测试

运行所有测试：
```bash
gauge run specs/
```

运行特定测试：
```bash
gauge run specs/login_test.spec
```

## 测试报告

测试执行后，HTML报告将生成在 `reports/html-report` 目录下。

## 持续集成

项目已配置GitHub Actions用于自动化测试。每次推送到主分支时都会自动运行测试。

## 贡献指南

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个Pull Request

## 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件