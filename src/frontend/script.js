async function generate() {
  const prompt = document.getElementById("prompt").value;
  const resultEl = document.getElementById("result");

  resultEl.textContent = "Generating...";

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

  const data = await response.json();

  if (data.result) {
    resultEl.textContent = data.result;
  } else {
    resultEl.textContent = "Error generating text";
  }
}
