const response = await fetch(
  "https://us-central1-ai-content-generator-481106.cloudfunctions.net",
  {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ prompt })
  }
);
