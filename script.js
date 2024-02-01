function drag(ev, vehicleType) {
    ev.dataTransfer.setData("text", vehicleType);
}

function drop(ev) {
    ev.preventDefault();
    var vehicleType = ev.dataTransfer.getData("text");

    // Create a new instance based on the dragged vehicle type
    var newVehicle = createVehicle(vehicleType);

    // Set common attributes for the new vehicle
    newVehicle.querySelector(".brand").innerText = prompt("Enter Sample Brand Name:") || 'Default Brand';
    newVehicle.querySelector(".model").innerText = prompt("Enter Sample Model Name:") || 'Default Model';
    newVehicle.querySelector(".year").innerText = prompt("Enter Sample Year:") || 'Default Year';

    // Set additional attributes for subclasses
    if (vehicleType !== 'Vehicle') {
        setAdditionalAttributes(newVehicle, vehicleType);
    }

    // Add the new instance to the drop container
    document.getElementById("vehicleContainer").appendChild(newVehicle);

    // Add event listener to handle removal of the new instance
    newVehicle.addEventListener("click", function () {
        this.parentNode.removeChild(this);
    });
}

function allowDrop(ev) {
    ev.preventDefault();
}

function createVehicle(vehicleType) {
    switch (vehicleType) {
        case 'Vehicle':
            return createVehicleElement("Vehicle object is created");
        case 'Car':
            return createVehicleElement("Car object is created");
        case 'Bike':
            return createVehicleElement("Bike object is created");
        case 'Cycle':
            return createVehicleElement("Cycle object is created");
        case 'Tractor':
            return createVehicleElement("Tractor object is created ");
        default:
            return null;
    }
}

function createVehicleElement(type) {
    var vehicle = document.createElement("div");
    vehicle.classList.add("vehicle");
    vehicle.innerHTML = `<h4>${type}</h4><p>Brand: <span class="brand"></span>, Model: <span class="model"></span>, Year: <span class="year"></span></p>`;
    return vehicle;
}

function setAdditionalAttributes(vehicle, vehicleType) {
    switch (vehicleType) {
        case 'Car':
            vehicle.innerHTML += "<p>Fuel Type: <span class='fuel-type'>Petrol</span>, Doors: <span class='num-doors'>4</span></p>";
            break;
        case 'Bike':
            vehicle.innerHTML += "<p>Bike Type: <span class='bike-type'>Cruiser</span>, Color: <span class='color'>Black</span></p>";
            break;
        case 'Cycle':
            vehicle.innerHTML += "<p>Wheels: <span class='num-wheels'>2</span>, Has Basket: <span class='has-basket'>Yes</span></p>";
            break;
        case 'Tractor':
            vehicle.innerHTML += "<p>Hitch Type: <span class='hitch-type'>Three-Point Hitch</span>, Plows: <span class='num-plows'>5</span></p>";
            break;
        default:
            break;
    }
}
