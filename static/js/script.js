console.log("Hello, World!");

function updateMaxNumber() {
            const productInput = document.getElementById('productSelect').value;
            const numberInput = document.getElementById('number');

            if (productInput === "Scooter") {
                numberInput.max = 4;
            } else if (productInput === "BMW G 310 GS") {
                numberInput.max = 2;
            } else {
                numberInput.max = 1; // Default max value
            }

            numberInput.value = 1; // Reset the value if it exceeds the new max
            updateMaxNumberChosen();

            // Reset the value if it exceeds the new max
            if (numberInput.value > numberInput.max) {
                numberInput.value = numberInput.max; // Set to max if current value exceeds
            } else if (numberInput.value < 1) {
                numberInput.value = 1; // Ensure minimum value is 1
            }
        }

function updateMaxNumberChosen() {
            let deposit = document.getElementById('deposit').value;
            console.log(deposit);
            const productInput = document.getElementById('productSelect').value;
            const numberInput = document.getElementById('number');
            let deposit_value = 0

            if (productInput === "Scooter") {
                deposit_value = 5000 * numberInput.value;

                deposit = deposit_value;
                console.log(deposit);
                document.getElementById('deposit').value = `R ${deposit}`;
            } else if (productInput === "BMW G 310 GS") {
                deposit_value = 8000 * numberInput.value;
                deposit = deposit_value;
                console.log(deposit);
                document.getElementById('deposit').value = `R ${deposit}`;
            } else {
                deposit_value = 8000;
                deposit = deposit_value;
                document.getElementById('deposit').value = `R ${deposit}`;
            }
        }



function onDateStartChange() {
            const startDate = document.getElementById('date-start').value;
            let endDate = document.getElementById('date-end').value;
            document.getElementById('date-end').value = startDate;
            endDate = document.getElementById('date-end').value
            console.log(startDate, endDate);
            onDateEndChange();

//            if (startDate > endDate) {
//                document.getElementById('endDate').value = startDate;
//            }
        }

function onDateEndChange() {
            let startDate = document.getElementById('date-start').value;
            let endDate = document.getElementById('date-end').value;

            const productInput = document.getElementById('productSelect').value;
            const numberInput = document.getElementById('number');

            if (productInput === "Scooter") {
                numberInput.max = 4;
            } else if (productInput === "BMW G 310 GS") {
                numberInput.max = 2;
            } else {
                numberInput.max = 4; // Default max value
            }

            let startDateValue = new Date(startDate);
            let endDateValue = new Date(endDate);
//            document.getElementById('date-start').value = endDate;
            let duration = endDateValue - startDateValue;
            let durationInDays = Math.ceil((duration) / (1000 * 60 * 60 * 24)) + 1;
            console.log(durationInDays)
            console.log(startDate, endDate);
            let cost = 0;
            if (productInput === "Scooter") {
                if (durationInDays === 1) {
                    cost = 600 * numberInput.value;
                } else if (durationInDays > 1 && durationInDays < 7) {
                cost = 700 * durationInDays * numberInput.value;
                } else if (durationInDays >= 7 && durationInDays < 30) {
                    let costA = durationInDays % 7;
                    let costB = durationInDays / 7;
                    console.log("Cost A",costA);
                    console.log("Cost B",costB);
                    cost = 600 * durationInDays * numberInput.value;
                }
            } else if (productInput === "BMW G 310 GS") {
                numberInput.max = 2;
            } else {
                numberInput.max = 4; // Default max value
            }
            }