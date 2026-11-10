const fareForm = document.querySelector("form");
const result = document.getElementById("result");

fareForm.addEventListener("submit", async function(event) {
    event.preventDefault();

    const origin = document.getElementById("origin").value.trim();
    const destination = document.getElementById("destination").value.trim();
    const travelTime = document.getElementById("travel-time").value;

    if (!origin || !destination) {
        result.innerHTML = "<p>Please enter both locations.</p>";
        return;
    }

    if (origin.toLowerCase() === destination.toLowerCase()) {
        result.innerHTML = "<p>Starting point and destination cannot be the same.</p>";
        return;
    }

    result.innerHTML = "<p>Calculating your estimated fare...</p>";

    try {
        const response = await fetch("/calculate-fare", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                origin: origin,
                destination: destination,
                travel_time: travelTime
            })
        });

        const data = await response.json();

        if (!response.ok) {
            result.innerHTML = `<p>${data.error}</p>`;
            return;
        }

        result.innerHTML = `
            <h3>Fare Estimate</h3>
            <p><strong>From:</strong> ${data.origin}</p>
            <p><strong>To:</strong> ${data.destination}</p>
            <h2>KES ${data.minimum_fare} - ${data.maximum_fare}</h2>
            <p>${data.message}</p>
        `;

    } catch (error) {
        result.innerHTML = "<p>Unable to calculate fare. Please try again.</p>";
        console.error(error);
    }
});