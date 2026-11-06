# BÀI THẢO LUẬN LAB 02 – IT3180

## Câu 1 (Slide 35): Vì sao phải đồng bộ `master` trước khi PR?

- Để đảm bảo code trên nhánh tính năng của bạn có thể tích hợp trơn tru với những thay đổi mới nhất mà người khác (hoặc chính bạn) vừa gộp vào nhánh `master`.
- Nếu có xung đột (conflict) mã nguồn, bạn sẽ chủ động phát hiện và xử lý ngay tại máy cá nhân trên nhánh của mình trước khi gửi Pull Request. Việc này giúp quá trình review dễ dàng và an toàn hơn.

## Câu 2 (Slide 35): Khi nào không được dùng `rebase`?

- Tuyệt đối **không được dùng** `rebase` cho các commit đã được push/chia sẻ lên remote repository (ví dụ như các nhánh dùng chung `master` hoặc `release/*`).
- Bản chất `rebase` là viết lại lịch sử (tạo ra các mã commit SHA mới). Nếu rebase trên nhánh chung, nó sẽ phá vỡ lịch sử đồng bộ của các thành viên khác đang làm việc trên cùng nhánh đó. Chỉ dùng `rebase` để dọn dẹp lịch sử trên nhánh cá nhân chưa push.

## Câu 3 (Slide 35): Nhánh `feature/*` khác nhánh `topic/*` ra sao?

- `feature/*`: Dành cho việc phát triển các tính năng phần mềm thực sự (ví dụ: giỏ hàng, module tìm kiếm). Những thay đổi ở đây trực tiếp tác động đến logic hoạt động của ứng dụng.
- `topic/*`: Dành cho các chủ đề công việc không làm thay đổi logic ứng dụng, chẳng hạn như cập nhật tài liệu (docs), tạo template Pull Request, vẽ biểu đồ Use Case, hay thiết lập cấu hình.
