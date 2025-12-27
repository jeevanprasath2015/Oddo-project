fetch("/api/requests")
  .then(res => res.json())
  .then(data => {
    data.filter(r => r.type === "Preventive")
        .forEach(r => {
          document.getElementById("calendar")
            .innerHTML += `<li>${r.scheduled_date} - ${r.subject}</li>`;
        });
  });