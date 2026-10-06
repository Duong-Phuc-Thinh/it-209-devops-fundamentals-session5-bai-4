import subprocess
import os

def run_command(command):
    print(f"Executing: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result.returncode

def simulate_gitflow_hotfix():
    print("=== BẮT ĐẦU MÔ PHỎNG QUY TRÌNH HOTFIX GITFLOW ===")
    
    # Khởi tạo git repo tạm thời để minh họa
    run_command("git init test_repo")
    os.chdir("test_repo")
    
    # Thiết lập cấu hình git cơ bản cho test
    run_command("git config user.name 'Gitflow Bot'")
    run_command("git config user.email 'bot@gitflow.local'")
    
    # Tạo commit ban đầu trên main (v1.0.0)
    with open("app.py", "w") as f:
        f.write("# Stable v1.0.0\nprint('App running')\n")
    run_command("git add app.py")
    run_command("git commit -m 'Initial commit v1.0.0'")
    run_command("git tag -a v1.0.0 -m 'Stable v1.0.0'")
    
    # Tạo nhánh develop
    run_command("git checkout -b develop")
    with open("feature.py", "w") as f:
        f.write("# New feature in progress\n")
    run_command("git add feature.py")
    run_command("git commit -m 'Develop new feature'")
    
    # Phát sinh lỗi trên main, tạo nhánh hotfix từ main
    run_command("git checkout main")
    run_command("git checkout -b hotfix/v1.0.1")
    
    # Sửa lỗi lộ dữ liệu trên hotfix
    with open("app.py", "w") as f:
        f.write("# Stable v1.0.0 - Hotfixed\nprint('App running securely')\n")
    run_command("git add app.py")
    run_command("git commit -m 'Fix critical data leak vulnerability'")
    
    # Merge hotfix vào main và tạo tag v1.0.1
    run_command("git checkout main")
    run_command("git merge hotfix/v1.0.1 --no-ff -m 'Merge hotfix/v1.0.1 into main'")
    run_command("git tag -a v1.0.1 -m 'Release Hotfix 1.0.1'")
    
    # Merge hotfix ngược lại vào develop để đồng bộ
    run_command("git checkout develop")
    run_command("git merge hotfix/v1.0.1 --no-ff -m 'Merge hotfix/v1.0.1 into develop'")
    
    # Xóa nhánh hotfix
    run_command("git branch -d hotfix/v1.0.1")
    
    # Kiểm tra kết quả
    print("=== KIỂM TRA LỊCH SỬ GIT ===")
    run_command("git branch -a")
    run_command("git tag")
    run_command("git log --graph --oneline --all")
    
    os.chdir("..")
    print("=== HOÀN TẤT MÔ PHỎNG ===")

if __name__ == "__main__":
    simulate_gitflow_hotfix()
