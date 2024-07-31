import cv2
import numpy as np
import os

def rotate_image(image, angle):
    # Tính kích thước của ảnh
    height, width = image.shape[:2]
    # Tính tâm của ảnh
    center = (width / 2, height / 2)
    # Tạo ma trận xoay
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    # Áp dụng phép biến đổi
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    return rotated_image

# Tạo thư mục lưu trữ ảnh đã xoay (nếu thư mục chưa tồn tại)
output_dir = 'D:/Images'
os.makedirs(output_dir, exist_ok=True)

# Tạo danh sách các đường dẫn ảnh từ 'D:/Black_rot (1).JPG' đến 'D:/Black_rot (170).JPG'
image_paths = [f'D:/Black_rot ({i}).JPG' for i in range(1, 171)]

for image_path in image_paths:
    # Load ảnh từ đường dẫn
    image = cv2.imread(image_path)

    # Kiểm tra xem ảnh đã được load thành công chưa
    if image is None:
        print(f"Không thể đọc được ảnh: {image_path}")
    else:
        # Chuyển đổi ảnh thành các góc độ khác nhau và lưu vào thư mục
        angles = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180]  # Các góc độ bạn muốn chuyển đổi

        for angle in angles:
            rotated_image = rotate_image(image, angle)
            filename = os.path.splitext(os.path.basename(image_path))[0]  # Lấy tên tệp mà không có phần mở rộng
            output_path = os.path.join(output_dir, f'{filename}_rotated_{angle}.JPG')
            cv2.imwrite(output_path, rotated_image)

print(f"Các ảnh đã được lưu vào thư mục {output_dir}.")
