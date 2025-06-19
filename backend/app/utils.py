import os, json
from ml_agent.agent import run_agent

def status_path(job_id): return f"uploaded_jobs/{job_id}/status.json"
def get_output_path(job_id): return f"uploaded_jobs/{job_id}/output.csv"

def update_status(job_id, status):
    with open(status_path(job_id), "w") as f:
        json.dump({"status": status}, f)

def get_job_status(job_id):
    try:
        with open(status_path(job_id)) as f:
            return json.load(f)
    except:
        return {"status": "unknown"}

def get_job_result(job_id):
    out_path = get_output_path(job_id)
    if os.path.exists(out_path):
        return {"download_url": f"/static/{job_id}/output.csv"}
    return {"error": "Not ready"}