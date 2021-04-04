# Stock News Summarizer
Side Project

<h3>How to test on Docker</h3>
<p>
1. Set GOOGLE_APPLICATION_CREDENTIALS in docker-compose.yml to the path to the file contains your service account key
<br>
2. Run <code>docker-compose up</code>


<h3>How to test on CloudRun</h3>
<p>
*Before you run, make sure you have the right service account/permission to deploy to CloudRun
<br>
1. Build your container image 
<br>
<code>
cd backend;
gcloud builds submit --tag gcr.io/stock-news-summarizer/backend</code>
<br>
2. Deploy the container 
<br>
<code>gcloud run deploy --image gcr.io/stock-news-summarizer/backend --memory 4Gi --platform managed</code>
<br>
3. Select northamerica-northeast1 for region
<br>
4. If it fails, go to https://console.cloud.google.com/run?project=stock-news-summarizer
<br>
5. Go to https://console.cloud.google.com/run?project=stock-news-summarizer
<br>
6. Click the service and select 'EDIT AND DEPLOY NEW REVISION'
<br>
6. Add Varialbe <code>HOST={URL}</code> and click Deploy
</p>