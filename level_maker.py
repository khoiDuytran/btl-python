import os
import json
# Tạo level với số lượng mục tiêu và chướng ngại vật
def create_level(targets, obstacles, filename):
    # Kiểm tra nếu thư mục 'levels' không tồn tại và tạo mới
    if not os.path.exists('levels'):
        os.makedirs('levels')
    
    # Kiểm tra xem đường dẫn có phải là tệp không
    file_path = os.path.join('levels', filename)
    
    # Tạo tệp JSON và ghi dữ liệu vào đó
    level_data = {
        'targets': targets,
        'obstacles': obstacles
    }
    with open(file_path, 'w') as f:
        json.dump(level_data, f)
    print(f'Level {filename} created!')

# Ví dụ tạo level với 3 mục tiêu và 2 chướng ngại vật
if __name__ == '__main__':
    targets = [(100, 150, 'd'), (200, 250, 's'), (300, 650, 'p')]
    obstacles = [(700, 200)]
    create_level(targets, obstacles, 'level1.json')
