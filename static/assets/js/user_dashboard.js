document.getElementById("book-spot-btn").addEventListener("click", bookSpot);

// Function to handle booking
function bookSpot() {
    let parkingId = Math.floor(Math.random() * 10000); // Generate random parking ID
    document.getElementById("parking-id").textContent = parkingId;

    // Update spaces (just for demo purposes)
    let bookedSpaces = document.getElementById("booked-spaces").textContent;
    let emptySpaces = document.getElementById("empty-spaces").textContent;

    document.getElementById("booked-spaces").textContent = parseInt(bookedSpaces) + 1;
    document.getElementById("empty-spaces").textContent = parseInt(emptySpaces) - 1;
}

// You can set the username dynamically based on user data
document.getElementById("username").textContent = "Welcome, Jane Smith!";
