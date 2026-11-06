# BÀI THẢO LUẬN LAB 01 – IT3180

## Câu 1 (Slide 19): Cấu hình `--global` được lưu ở đâu? Khác gì so với `--local`?

- **Vị trí lưu:**
  - Cấu hình `--global` được lưu tại file `~/.gitconfig` trong thư mục gốc của người dùng (trên Windows thường là `C:\Users\<Tên_User>\.gitconfig`).
  - Cấu hình `--local` được lưu tại file `.git/config` nằm ngay bên trong thư mục ẩn của repository hiện tại.
- **Khác biệt:**
  - `--global`: Áp dụng chung cho tất cả các repository của user trên máy tính đó.
  - `--local`: Chỉ áp dụng riêng cho repository hiện tại. Nếu cả hai cùng định nghĩa một thông số, cấu hình `--local` sẽ có độ ưu tiên cao hơn và ghi đè lên `--global`.

## Câu 2 (Slide 26): Vì sao dùng `git mv`?

- `git mv <cũ> <mới>` tương đương với chuỗi lệnh: di chuyển file bằng hệ điều hành + `git rm` file cũ + `git add` file mới vào Staging area.
- Lệnh này giúp Git ghi nhận ngay hành động đổi tên/di chuyển (rename) với độ tin cậy 100%, bảo toàn trọn vẹn metadata và lịch sử commit của tệp. Lịch sử này có thể truy vết dễ dàng bằng `git log --follow`. Nếu di chuyển bằng chuột thông thường rồi mới `git add .`, Git có nguy cơ hiểu lầm là bạn vừa xóa file cũ và tạo một file mới tinh.

## Câu 3 (Slide 26): `release/lab01` có phải baseline không?

- **Có.** Theo lý thuyết SCM, Baseline là một trạng thái cấu hình phần mềm đã được kiểm tra, thống nhất và chính thức "đóng băng" tại một thời điểm cụ thể.
- Nhánh `release/lab01` đóng vai trò là phiên bản nộp bài chính thức, mọi thay đổi mới phát triển trên `master` sau này sẽ không làm ảnh hưởng đến baseline này.

## Câu 4 (Slide 26): Vì sao không commit thẳng `master` dù làm một mình?

- Để tuân thủ đúng **Quy trình kiểm soát thay đổi (Change Control)** và tạo thói quen làm việc nhóm chuyên nghiệp.
- Mọi thay đổi cần đi qua nhánh riêng và tạo Pull Request (PR). Điều này kết hợp với Branch Protection trên `master` giúp bảo vệ code khỏi thao tác sai lầm, dễ dàng review lại chính mình và tạo tiền đề để dùng AI hoặc CI/CD duyệt code tự động sau này.
