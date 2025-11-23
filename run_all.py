import subprocess
import sys
import os
import time

def run_process(cmd, cwd=None):
    return subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def run_backend():
    backend_path = os.path.join(os.getcwd(), "backend/app")
    cmd = ["uvicorn", "main:app", "--reload"]
    return run_process(cmd, backend_path)

def run_frontend():
    frontend_path = os.path.join(os.getcwd(), "frontend")
    cmd = ["npm", "run", "dev"]
    return run_process(cmd, frontend_path)


if __name__ == "__main__":
    root = os.getcwd()

    # Start Backend
    backend_proc = run_backend()

    # Wait for backend to start
    time.sleep(2)

    # Start Frontend
    frontend_proc = run_frontend()

    print("\n🔥 Both backend and frontend are running!")
    print("⚠️ Press CTRL + C to stop everything.\n")

    try:
        backend_proc.wait()
        frontend_proc.wait()
    except KeyboardInterrupt:
        print("\n⛔ Stopping both services...")
        backend_proc.terminate()
        frontend_proc.terminate()
        backend_proc.wait()
        frontend_proc.wait()
        print("✔️ Shutdown complete.")
