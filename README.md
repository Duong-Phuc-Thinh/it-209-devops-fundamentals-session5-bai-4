# Bài 4: Mô phỏng quy trình Hotfix & Gitflow thực tế

## Giới thiệu
Bài tập này hướng dẫn quy trình thực hiện Hotfix theo mô hình Gitflow chuẩn trong trường hợp hệ thống production (nhánh main) gặp lỗi nghiêm trọng cần sửa gấp mà không thể chờ đợi các tính năng chưa hoàn thiện ở nhánh develop.

## Sơ đồ Gitflow Hotfix
```text
*   (main) Tag v1.0.1: Fix critical security vulnerability
|\
| *   (hotfix/v1.0.1) Sửa lỗi lộ dữ liệu người dùng
|/
*   (develop) Đang phát triển tính năng mới
|
*   (main) Tag v1.0.0: Stable release
```

## Hướng dẫn chạy chương trình mô phỏng
Chạy file script Python để tự động hóa hoặc kiểm tra quy trình Git commands:
```bash
python main.py
```