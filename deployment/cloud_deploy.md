<!-- # 🛠 Cloud Deployment (Backend API)

## 📍 Using Render (Free Tier)
1. Push backend folder to GitHub.
2. Go to [https://render.com](https://render.com)
3. Create a new Web Service → Connect your repo
4. Set Build Command: `pip install -r requirements.txt`
5. Set Start Command: `uvicorn app.main:app --host 0.0.0.0 --port 8000`
6. Add Redis as a service (Render supports it)
7. Add environment variable:
   - `CELERY_BROKER_URL=redis://<your-redis-host>:6379/0`

---

## 🚀 Using GCP Cloud Run
1. Enable Cloud Run & Artifact Registry on GCP.
2. Build Docker image:
   ```bash
   docker build -t gcr.io/<project-id>/resume-backend backend/ -->

   # ☁️ Cloud Deployment Instructions

## 📦 Backend Deployment (GCP Cloud Run)

1. Build Docker Image:
   ```bash
   docker build -t gcr.io/<your-project-id>/resume-backend ../backend