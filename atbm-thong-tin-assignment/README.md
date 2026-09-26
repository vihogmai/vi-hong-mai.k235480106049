# BÀI TẬP MÔN AN TOÀN VÀ BẢO MẬT THÔNG TIN

## 1. Thuật toán mã hóa hiện đại DES và AES
* **DES (Data Encryption Standard):** Mã hóa khối đối xứng, chia dữ liệu thành khối 64-bit, độ dài khóa 56-bit. Sử dụng cấu trúc mạng Feistel qua 16 vòng lặp. Hiện nay DES không còn an toàn do độ dài khóa ngắn.
* **AES (Advanced Encryption Standard):** Mã hóa khối đối xứng thay thế DES. Khối dữ liệu cố định 128-bit, độ dài khóa linh hoạt 128, 192 hoặc 256 bits tương ứng với 10, 12 hoặc 14 vòng lặp. Các phép biến đổi trong mỗi vòng gồm: SubBytes, ShiftRows, MixColumns và AddRoundKey.

## 2. Thuật toán mã hóa bất đối xứng RSA
Nguyên lý sinh cặp khóa (Public Key & Private Key):
1. Chọn 2 số nguyên tố lớn p và q.
2. Tính n = p * q và hàm Euler phi(n) = (p-1)*(q-1).
3. Chọn số mũ mã hóa e sao cho 1 < e < phi(n) và gcd(e, phi(n)) = 1.
4. Tính số mũ giải mã d sao cho d * e mod phi(n) = 1.
5. Khóa công khai là (e, n), Khóa bí mật là (d, n).

## 3. Các mô hình ứng dụng RSA & So sánh với AES
* **Mô hình ứng dụng RSA:**
  * **Xác thực người nhận:** Người gửi mã hóa bằng Public Key người nhận. Chỉ người nhận giữ Private Key mới giải mã được.
  * **Xác thực người gửi (Chữ ký số):** Người gửi ký bằng Private Key của mình. Người nhận dùng Public Key người gửi để kiểm tra.
  * **Kết hợp cả hai:** Ký bằng Private Key người gửi, sau đó mã hóa gói tin bằng Public Key người nhận.
* **So sánh thời gian Mã hóa/Giải mã:** AES mã hóa/giải mã nhanh hơn RSA từ 100 đến 1000 lần vì AES dựa trên phép toán bảng thế/dịch bit đơn giản, còn RSA phải tính toán lũy thừa số nguyên lớn (2048 - 4096 bits).
* **Mô hình kết hợp sức mạnh (Hybrid Cryptosystem):**
  * Sử dụng **AES Key (Session Key)** ngẫu nhiên để mã hóa toàn bộ dữ liệu lớn (tối ưu tốc độ).
  * Sử dụng **RSA Public Key** để mã hóa chính khóa AES Session Key đó (tối ưu bảo mật trao đổi khóa).
  