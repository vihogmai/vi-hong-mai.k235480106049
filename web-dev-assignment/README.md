# Web Development Assignment

Bài tập môn Lập trình Web sử dụng Docker, Nginx, Node-RED và MariaDB.

## Cấu trúc dịch vụ
- **Nginx**: Web server & Reverse proxy (Cổng 80)
- **Node-RED**: Xử lý API `/api/tacke` (Cổng 1880)
- **MariaDB**: Cơ sở dữ liệu Relational DB
- **phpMyAdmin**: Giao diện quản trị CSDL (Cổng 8080)

## Hướng dẫn chạy dự án
1. Khởi chạy hệ thống bằng Docker:
   ```bash
   docker compose up -d