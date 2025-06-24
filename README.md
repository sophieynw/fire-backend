
# Fire Model API

Lightweight Flask back-end REST API that serves a Random Forest Classifier model for predicting forest fires based on a simulated dataset.
## Run Locally

Clone the project

```bash
git clone git@github.com:sophieynw/fire-backend.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Start development server

```bash
python app.py
```
## Environment Variables

To run this project, you may need to add the following environment variables to your .env file if you wish to pull my pkl file from my S3 bucket.

`MODEL_URL` - please DM me if you wish to test my API locally


## Appendix

Repo for frontend React app can be found [here](https://github.com/sophieynw/fire-frontend)
