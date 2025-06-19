from celery import Celery
from app.utils import update_status, run_agent, get_output_path

celery_app = Celery("worker", broker="redis://localhost:6379/0")

@celery_app.task
def process_job(job_id, csv_path, jd_path):
    update_status(job_id, "running")
    try:
        out_path = get_output_path(job_id)
        run_agent(csv_path, jd_path, out_path)
        update_status(job_id, "done")
    except Exception:
        update_status(job_id, "failed")