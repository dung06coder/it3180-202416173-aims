# BÀI THẢO LUẬN LAB 03 – IT3180

## Câu 1 (Slide 43): Merge base là gì?

- **Merge base** là "tổ tiên chung gần nhất" (common ancestor) của hai nhánh mà bạn đang muốn gộp (merge) lại với nhau.
- Git sử dụng trạng thái tại merge base làm điểm mốc chuẩn để đối chiếu với nhánh hiện tại và nhánh mục tiêu, từ đó thuật toán Git tự động tính toán ra những thay đổi cần gộp hoặc phát hiện chính xác vị trí bị xung đột (conflict).

## Câu 2 (Slide 43): Vì sao `master` và `release/*` phải dùng `revert` thay vì `reset`?

- `master` và `release/*` là các nhánh chia sẻ (dùng chung) và đã được công khai (public). Việc sử dụng `reset` sẽ xóa sạch lịch sử các commit cũ, gây ra lỗi mất đồng bộ nghiêm trọng cho kho chứa cục bộ của các thành viên khác.
- Lệnh `revert` an toàn tuyệt đối vì nó giữ nguyên toàn bộ lịch sử cũ. Khi chạy, nó tạo ra một commit mới tinh chứa nội dung đảo ngược lại những thay đổi của commit bị sai, giúp tiến trình lịch sử luôn tiến về phía trước một cách minh bạch.
