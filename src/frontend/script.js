const response = await fetch(
  "https://us-central1-ai-content-generator-481106.cloudfunctions.net/generate_ai",
  {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ prompt })
  }
);
