import subprocess
import os

print("=" * 60)
print("GitHub 推送脚本")
print("=" * 60)
print()

# apps 仓库
print("[1/2] 处理 apps 仓库")
print("-" * 60)
os.chdir(r'd:\临时\代码重构工程\apps')

# 检查 git 状态
result = subprocess.run('git status', shell=True, capture_output=True, text=True)
print("Git 状态:")
print(result.stdout if result.stdout else result.stderr)
print()

# 检查远程仓库
result = subprocess.run('git remote -v', shell=True, capture_output=True, text=True)
print("远程仓库:")
print(result.stdout if result.stdout else "无")
print()

# 检查提交历史
result = subprocess.run('git log --oneline -3', shell=True, capture_output=True, text=True)
print("最近提交:")
print(result.stdout if result.stdout else "无")
print()

# 提交并推送
print("提交代码...")
result = subprocess.run('git add .', shell=True, capture_output=True, text=True)
result = subprocess.run('git commit -m "Fix API parameters - class to class_name"', shell=True, capture_output=True, text=True)
if result.returncode == 0:
    print("✓ 提交成功")
else:
    print(f"提交信息: {result.stderr if result.stderr else result.stdout}")

print()
print("推送到 GitHub...")
print("-" * 60)
result = subprocess.run('git push -u origin master --force', shell=True, capture_output=True, text=True)
if result.returncode == 0:
    print("✓ apps 仓库推送成功")
else:
    print("✗ apps 仓库推送失败")
    print(f"错误: {result.stderr if result.stderr else result.stdout}")

print()
print("=" * 60)

input("按 Enter 键退出...")