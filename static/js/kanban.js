fetch("/api/requests")
  .then(res => res.json())
  .then(data => {
    data.forEach(r => {
      const card = document.createElement("div");
      card.className = "card";
      card.innerText = r.subject;
      document.getElementById(r.status).appendChild(card);
    });
  });