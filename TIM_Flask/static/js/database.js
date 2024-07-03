$(document).ready(function() {
    // Function to handle database switching
    function switchDatabase(databaseName) {
        // Send a POST request to switch to the selected database
        $.ajax({
            url: "{{ url_for('db.switch_db', db='_db_name_') }}".replace('_db_name_', databaseName),
            method: 'POST',
            success: function(data) {
                // If the database is switched successfully, reload the page
                location.reload();

            },
            error: function(xhr, status, error) {
                // If there's an error switching the database, show an error message
                alert('Error switching database: ' + error);
            }
        });
    }

    $('#createDatabase').click(function() {
        // Send a POST request to your Flask backend to create a new database
        $.ajax({
            url: "{{ url_for('db.create_db') }}",  // Use url_for to generate the URL
            method: 'POST',
            success: function(data) {
                // If the database is created successfully, notify the user
                alert(data.message); // Display the success message returned from the server
                // Optionally, you can update the UI to reflect the new database
                // For example, add the new database name to a list or reload the page
            },
            error: function(xhr, status, error) {
                // If there's an error creating the database, show an error message
                alert('Error creating database: ' + error);
            }
        });
    });

    // Function to retrieve the list of databases and display them to the user
    function getAndDisplayDatabases() {
        // Send a GET request to your Flask backend to retrieve the list of databases
        $.ajax({
            url: "{{ url_for('db.list_databases') }}",
            method: 'GET',
            success: function(data) {
                // If the list of databases is retrieved successfully, display it to the user
                var databaseList = $('#databaseList');
                databaseList.empty(); // Clear previous database entries

                // Append each database name to the databaseList div
                data.databases.forEach(function(database, index) {
                    // Generate the database name dynamically as V0, V1, V2, ...
                    var dbName = 'TIM V' + index;

                    // Create a clickable element for each database name
                    var databaseElement = $('<p style="padding-left: 50px; margin-top: 8px; margin-bottom: 10px; cursor: pointer;">' + dbName + '</p>');
                    databaseElement.css('cursor', 'pointer'); // Set cursor to pointer
                    databaseElement.click(function() {
                        // When a database name is clicked, switch to that database
                        switchDatabase(database);
                    });
                    // Append the clickable database element to the databaseList div
                    databaseList.append(databaseElement);
                });
            },
            error: function(xhr, status, error) {
                // If there's an error retrieving the list of databases, show an error message
                alert('Error retrieving databases: ' + error);
            }
        });
    }

    // Call the function to retrieve and display databases when the document is ready
    getAndDisplayDatabases();
});
