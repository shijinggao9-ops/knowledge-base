---
tags: [Python, 自动化, Excel自动化, 邮件自动化, 爬虫, 定时任务, 商科知识库]
date: 2026-08-05
---

# 20-4-4 Python自动化与爬虫基础

**定位**：如果说Pandas解决的是“怎么分析数据”，那么Python自动化解决的是“怎么让重复的工作自己跑起来”。在商业场景中，大量的时间被消耗在重复性事务上：每月生成同样的报表、每天发送同样的邮件、从网页复制粘贴数据。Python可以把这些重复劳动变成“一键运行的脚本”，把人力解放出来做真正有价值的事。这个文件覆盖Excel自动化、邮件自动发送、基础网页数据获取和定时任务调度——帮你把“重复的工作”交给代码，把“思考的工作”留给自己。

**适用场景**：批量处理多个Excel文件、自动生成并发送日报/周报、从网页获取公开数据（如价格、政策、竞品动态）、定时运行数据清洗和报告生成任务。


## 一、核心概念词典

### 1.1 Excel自动化：openpyxl

`openpyxl`是Python中最常用的Excel读写库——它可以读取和写入`.xlsx`格式的Excel文件，支持修改单元格、样式、图表等功能。

**安装**：

```bash
pip install openpyxl
```

#### 读取Excel文件

```python

from openpyxl import load_workbook
# 打开工作簿
wb = load_workbook('sales_data.xlsx')
# 查看所有工作表名称
print(wb.sheetnames)
# 选择工作表
ws = wb['Sheet1']
# 读取单元格值
cell_value = ws['A1'].value
# 或使用行列索引（从1开始）
cell_value = ws.cell(row=1, column=1).value
# 遍历行
for row in ws.iter_rows(min_row=2, values_only=True):
    print(row)  # row是一个元组，包含该行所有单元格的值
# 保存修改（如果只是读取，不需要保存）
# wb.save('sales_data.xlsx')
```

#### 写入Excel文件

```python

from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill
# 创建新工作簿
wb = Workbook()
ws = wb.active
ws.title = '销售报表'
# 写入标题行
headers = ['客户', '城市', '销售额', '订单数']
ws.append(headers)
# 写入数据
data = [
    ['张三', '北京', 25000, 15],
    ['李四', '上海', 18000, 12],
    ['王五', '北京', 32000, 20],
]
for row in data:
    ws.append(row)
# 设置样式：标题加粗居中
for cell in ws[1]:
    cell.font = Font(bold=True)
    cell.alignment = Alignment(horizontal='center')
# 设置列宽
ws.column_dimensions['A'].width = 12
ws.column_dimensions['B'].width = 12
ws.column_dimensions['C'].width = 15
ws.column_dimensions['D'].width = 12
# 保存
wb.save('sales_report.xlsx')
```

#### 修改已有Excel文件

```python

# 打开已有文件，追加数据
wb = load_workbook('sales_report.xlsx')
ws = wb.active
# 追加一行新数据
ws.append(['赵六', '深圳', 15000, 8])
# 插入公式（计算总销售额）
ws['E1'] = '合计'
ws['E2'] = '=SUM(C2:C5)'
wb.save('sales_report_updated.xlsx')
```

### 1.2 邮件自动化：smtplib与email

`smtplib`负责发送邮件，`email`库负责构建邮件内容。常用于自动发送日报、周报、数据异常告警等。

**安装**：smtplib和email是Python内置库，无需额外安装。

```python

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
# 邮件配置（使用示例邮箱）
SMTP_SERVER = 'smtp.qq.com'      # QQ邮箱的SMTP服务器
SMTP_PORT = 465                  # SSL端口
SENDER_EMAIL = 'your_email@qq.com'
SENDER_PASSWORD = 'your_auth_code'  # 邮箱授权码，不是登录密码
RECEIVER_EMAIL = 'receiver@company.com'
```

#### 发送纯文本邮件


```python

def send_text_email(subject, body, to_email):
    # 构建邮件
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email
    # 发送邮件
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
# 使用
send_text_email(
    '每日销售日报',
    f'今日销售额：1,250,000元\n订单数：128单\n平均客单价：9,765元',
    RECEIVER_EMAIL
)
```

#### 发送带附件的邮件（附Excel报表）

```python

def send_email_with_attachment(subject, body, to_email, attachment_path):
    # 构建邮件容器
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email
    # 添加正文
    body_part = MIMEText(body, 'plain', 'utf-8')
    msg.attach(body_part)
    # 添加附件
    with open(attachment_path, 'rb') as f:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(f.read())
        encoders.encode_base64(part)
        filename = attachment_path.split('/')[-1]
        part.add_header(
            'Content-Disposition',
            f'attachment; filename="{filename}"'
        )
        msg.attach(part)
    # 发送
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
# 使用（假设已生成报表文件）
send_email_with_attachment(
    '月度销售报告',
    '请查收本月销售报告，数据截止2026年7月。',
    RECEIVER_EMAIL,
    'monthly_report.xlsx'
)
```

> **重要提醒**：不要将邮箱密码或授权码直接写在代码中。生产环境中应使用环境变量（`os.getenv()`）或配置文件存储敏感信息，避免代码泄露导致账号被盗。


### 1.3 爬虫基础：requests与BeautifulSoup

爬虫是“用代码自动从网页获取信息”的技术。在商业场景中，可用于监控竞品价格、收集行业政策、获取公开市场数据等。**使用爬虫时务必遵守网站的`robots.txt`，尊重版权和法律法规。**

#### 安装


```bash

pip install requests beautifulsoup4
```

#### 获取网页内容（requests）

python

import requests
# 发送GET请求获取网页内容
url = 'https://example.com/data'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
response = requests.get(url, headers=headers)
# 检查请求是否成功
if response.status_code == 200:
    html_content = response.text
    print('获取成功')
else:
    print(f'获取失败，状态码：{response.status_code}')

#### 解析HTML提取数据（BeautifulSoup）

python

from bs4 import BeautifulSoup
# 解析HTML
soup = BeautifulSoup(html_content, 'html.parser')
# 查找标签
title = soup.title.text  # 获取页面标题
# 查找特定元素：find()返回第一个匹配，find_all()返回所有匹配
first_heading = soup.find('h1').text
# 通过class查找
items = soup.find_all('div', class_='product-item')
for item in items:
    name = item.find('span', class_='product-name').text
    price = item.find('span', class_='product-price').text
    print(f'{name}: {price}')
# 获取属性（如链接）
links = soup.find_all('a')
for link in links:
    href = link.get('href')
    text = link.text
    print(f'{text}: {href}')

#### 从API获取数据（最常用的数据采集方式）

很多网站提供公开API（Application Programming Interface），返回结构化数据（通常是JSON格式），比解析HTML更方便、更稳定。

python

import requests
import json
# 调用公开API（示例：jsonplaceholder）
api_url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(api_url)
if response.status_code == 200:
    data = response.json()  # 自动解析为Python列表/字典
    print(f'获取到 {len(data)} 条数据')
    print(data[0])  # 查看第一条

#### 处理动态网页：Selenium入门

当网页内容由JavaScript动态加载时，`requests`无法获取完整数据，这时需要使用`Selenium`模拟浏览器操作。

**安装**：

bash

pip install selenium

**示例（使用Chrome浏览器）** ：

python

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# 无头模式（不显示浏览器窗口）
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get('https://example.com')
# 等待页面加载（实际中常用WebDriverWait）
# 获取渲染后的页面内容
html = driver.page_source
# 查找元素
title = driver.find_element('tag name', 'h1').text
driver.quit()

### 1.4 定时任务：schedule与系统任务调度

#### schedule库（Python内部调度）

python

import schedule
import time
def daily_report_job():
    print('生成日报并发送...')
    # 这里调用实际的报表生成函数
# 每天早上9:00执行
schedule.every().day.at('09:00').do(daily_report_job)
# 每隔10分钟执行
# schedule.every(10).minutes.do(daily_report_job)
print('调度器已启动，按Ctrl+C停止...')
while True:
    schedule.run_pending()
    time.sleep(60)  # 每分钟检查一次

#### 系统级调度（更稳定）

|系统|工具|说明|
|---|---|---|
|Windows|任务计划程序|图形界面，可设置触发条件和执行脚本|
|macOS/Linux|crontab|命令行配置，灵活且稳定|

**crontab示例（每天9:00执行）** ：

bash

0 9 * * * /usr/bin/python3 /path/to/your_script.py

## 二、商业场景还原

> 本节将自动化与爬虫还原到真实的商业情境中。

### 场景1：批量合并多个Excel文件

**情境**：每月收到各区域的销售报表（`区域_202601.xlsx`、`区域_202602.xlsx`……），需要合并为一张总表并生成汇总。

python

import pandas as pd
import glob
from openpyxl import Workbook
def merge_excel_files(pattern, output_file):
    """
    合并所有匹配pattern的Excel文件
    pattern示例: 'sales_*.xlsx'
    """
    all_files = glob.glob(pattern)
    df_list = []
    for file in all_files:
        df = pd.read_excel(file)
        df['来源文件'] = file  # 增加一列标记来源
        df_list.append(df)
    # 合并所有数据
    df_merged = pd.concat(df_list, ignore_index=True)
    # 保存合并结果
    df_merged.to_excel(output_file, index=False)
    print(f'合并完成，共{len(df_merged)}行，保存至{output_file}')
    return df_merged
# 使用
merged = merge_excel_files('区域_*.xlsx', '2026年_汇总销售表.xlsx')

### 场景2：自动发送每日销售日报

**情境**：每天早晨9:00，从数据库/Excel读取昨日销售数据，自动生成日报并发送给管理层。

python

import pandas as pd
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def get_yesterday_sales():
    """获取昨日销售数据（模拟）"""
    # 实际场景中，这里可能是从数据库查询或Excel读取
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    return {
        'date': yesterday,
        'sales': 1250000,
        'orders': 128,
        'avg_order': 9765.63,
        'top_product': 'A系列'
    }
def send_daily_report():
    data = get_yesterday_sales()
    # 生成邮件正文
    body = f"""
    各位领导好，
    以下是昨日（{data['date']}）销售数据简报：
    📊 销售额：{data['sales']:,.0f} 元
    📦 订单数：{data['orders']} 单
    💰 平均客单价：{data['avg_order']:,.2f} 元
    🏆 热销产品：{data['top_product']}
    更多详情请查看BI仪表板。
    -- 系统自动发送，请勿回复
    """
    # 发送邮件（使用之前的send_text_email函数）
    send_text_email(f'销售日报_{data["date"]}', body, 'management@company.com')
# 配合schedule使用
schedule.every().day.at('09:00').do(send_daily_report)

### 场景3：监控竞品价格变化

**情境**：需要定期获取竞品在电商平台上的价格，监控价格变化趋势（仅限公开数据，遵守网站规则）。

python

import requests
from bs4 import BeautifulSoup
import time
import json
def get_product_price(product_url):
    """模拟从电商详情页获取价格（实际需适配具体网站结构）"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    try:
        response = requests.get(product_url, headers=headers, timeout=10)
        if response.status_code != 200:
            return None
        soup = BeautifulSoup(response.text, 'html.parser')
        # 假设价格在class="price"的span中
        price_elem = soup.find('span', class_='price')
        if price_elem:
            price_text = price_elem.text.strip()
            # 提取数字
            price = float(''.join(filter(lambda x: x.isdigit() or x == '.', price_text)))
            return price
    except Exception as e:
        print(f'获取价格失败：{e}')
    return None
def monitor_prices(product_urls):
    """批量监控多个产品价格"""
    results = {}
    for name, url in product_urls.items():
        price = get_product_price(url)
        results[name] = {
            'price': price,
            'time': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        print(f'{name}: {price}元')
        time.sleep(2)  # 控制请求频率，避免被反爬
    return results
# 使用
urls = {
    '产品A': 'https://example.com/product_a',
    '产品B': 'https://example.com/product_b',
}
monitor_prices(urls)

## 三、常见错误与陷阱

|错误|后果|正确做法|
|---|---|---|
|将邮箱密码/授权码硬编码在代码中|代码泄露导致账号被盗|用环境变量存储敏感信息：`os.getenv('EMAIL_PASSWORD')`|
|爬虫请求频率过高|IP被封禁|设置请求间隔（`time.sleep(2)`），使用代理IP池|
|不处理HTTP异常状态码|程序因`4xx`/`5xx`错误崩溃|检查`response.status_code`，用`try/except`捕获异常|
|编码问题导致中文乱码|写入Excel/邮件的内容无法阅读|指定`encoding='utf-8'`；Excel写入时用`openpyxl`原生方法|
|`openpyxl`无法读取`.xls`文件|报错|先用`pandas`的`pd.read_excel()`读取，或使用`xlrd`库|
|自动化脚本依赖本地文件路径|换电脑后路径失效|使用相对路径，或用`os.path.join()`构建路径|

## 四、面试高频题

### 4.1 概念题

**题目1：如何用Python实现Excel报表的自动生成？**

回答要点：用`pandas`处理数据 → 用`openpyxl`或`xlsxwriter`写入Excel并设置样式 → 用`smtplib`发送邮件 → 用`schedule`或系统定时任务设置自动运行。

**题目2：爬虫被反爬了怎么办？**

回答要点：

- 添加`User-Agent`头（模拟浏览器）
    
- 降低请求频率，增加`time.sleep()`
    
- 使用代理IP轮换
    
- 使用`Selenium`模拟真实浏览器（对付JavaScript渲染）
    
- 使用`requests.Session()`保持会话
    

**题目3：如何处理网页内容是动态加载的？**

回答要点：检查页面是否通过AJAX/JavaScript加载数据。如果是，可以尝试找到数据接口（API）直接请求JSON数据；如果找不到，使用`Selenium`或`Playwright`模拟浏览器渲染。

### 4.2 代码题

**题目：写一个Python脚本，读取一个Excel文件（`input.xlsx`）中的销售数据，按“产品”分组汇总销售额，生成一个新的Excel文件（`output.xlsx`）。**

python

import pandas as pd
# 读取数据
df = pd.read_excel('input.xlsx')
# 分组汇总
result = df.groupby('产品')['销售额'].sum().reset_index()
result.columns = ['产品', '总销售额']
# 导出
result.to_excel('output.xlsx', index=False)
print('汇总完成！')

## 五、实战自测题

- □ 
    
    **Excel自动化**：写一个脚本，读取一个Excel文件中的所有工作表（Sheet），将每个工作表的数据分别保存为独立的CSV文件。
    
- □ 
    
    **邮件发送**：写一个脚本，自动发送一封带附件（一个Excel文件）的邮件，正文中注明“请查收附件”。
    
- □ 
    
    **爬虫练习**：从公开API（如`https://jsonplaceholder.typicode.com/posts`）获取数据，提取标题和内容，保存为CSV文件。
    
- □ 
    
    **定时任务**：写一个Python脚本，每天下午5:00自动执行一个数据备份任务（将指定文件夹下的文件压缩为ZIP并存入备份目录）。
    
- □ 
    
    **综合题**：设计一个完整的自动化方案：每天早上8:00从数据库读取昨日销售数据 → 生成Excel报表 → 发送邮件给管理层。请写出核心代码并说明各步骤使用的库。
    

## 六、关联笔记

- [[20-1 Excel]]（自动化处理的目标之一是批量操作Excel文件）
    
- [[20-4-1 Python基础语法与数据环境搭建]]（自动化脚本的编程基础）
    
- [[20-4-2 Python数据分析核心库（Pandas、NumPy）]]（自动化中处理数据的主要工具）
    
- [[20-4-3 Python数据可视化（Matplotlib、Seaborn）]]（自动化生成报表图表）
    
- [[20-4-5 R语言入门与统计分析]]（R中的自动化与Python互为补充）
    
- [[85-7 数据分析]]（自动化能力在数据分析岗位中的价值）