# BÀI THẢO LUẬN LAB 05 – IT3180

## Câu 1: Ưu, nhược điểm của Upstream first so với Release first?

- **Upstream first (sửa trên master trước rồi cherry-pick sang release):**
  - _Ưu điểm:_ Đảm bảo mã nguồn gốc (`master`) luôn sạch và được sửa trước, tránh lỗi tái phát ở tương lai.
  - _Nhược điểm:_ Khi nhánh `master` đã phát triển quá xa, việc `cherry-pick` ngược lại nhánh release cũ rất dễ xảy ra xung đột phức tạp.
- **Release first (sửa trên release trước rồi cherry-pick về master - giống Lab 05):**
  - _Ưu điểm:_ Phản ứng nhanh, tạo bản vá chính xác và tương thích tuyệt đối ngay trên phiên bản người dùng đang gặp sự cố.
  - _Nhược điểm:_ Đòi hỏi kỷ luật cao; lập trình viên dễ quên lan truyền bản sửa lỗi về `master`, khiến lỗi lặp lại ở bản phát hành sau.

## Câu 2: Nếu quên lan truyền bản sửa sang release/lab05, lệnh nào ở Phần F sẽ phát hiện?

- **Lệnh 1:** `git cherry -v origin/master origin/release/lab05` (phát hiện commit sót).
- **Lệnh 2:** `git tag --contains <FIX_SHA>` (sẽ không thấy tag v1.1.0).
- **Lệnh 3:** Chạy vòng lặp test Python trên cả 3 nhánh. Bản nào quên lan truyền sẽ in ra kết quả rỗng `0` thay vì `1`.
