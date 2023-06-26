document.getElementById("loginForm").addEventListener("submit", function (event){
    event.preventDefault(); // Prevent the form from submitting normally

    // Get the values entered by the user
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Create an object with the user credentials
    var credentials = {
        username: username,
        password: password
    };

    // Send a POST request to the backend login route
    fetch("http://localhost:8000/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(credentials)
    })
    .then(response => response.json())
    .then(data => {
        // Jandle the response from the backend
        if (data.success) {
            // Display success message
            document.getElementById("message").textContent = "Login successful!";
        } else {
            // Display error message
            document.getElementById("message").textContent = "Invalid username or password.";
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
});