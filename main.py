import sys
import io
from datetime import datetime

# Đảm bảo in tiếng Việt chuẩn UTF-8 trên Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

print("Xin chào! Môi trường của tôi đã sẵn sàng cho khóa học AI Agent 101!")
print("Thời gian hiện tại:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
