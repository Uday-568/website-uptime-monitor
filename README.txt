Website Uptime Monitor – Project Explanation

## Project Overview

The Website Uptime Monitor is a simple web application developed using Python and the Flask framework. The purpose of this project is to check whether a given website is available (online) or not and display its status to the user. The application also keeps a record of all checked websites and visualizes the results using a chart.

This project demonstrates the basic concepts of web development, API requests, backend logic, and data visualization.

## Technologies Used

1. Python – Used as the main programming language.
2. Flask – A lightweight web framework used to build the backend web application.
3. Requests Library – Used to send HTTP requests to websites and retrieve their status codes.
4. HTML – Used to design the structure of the web interface.
5. Chart.js – Used to display the status results in a graphical pie chart.
6. JSON – Used to store and manage website monitoring data.

## Project Objective

The main objective of this project is to monitor website availability by checking HTTP response codes and categorizing them into different statuses such as Online, Client Error, Server Error, or Offline.

## How the Project Works

1. The user enters a website URL in the input field on the web interface.
2. The Flask backend receives the request.
3. The application sends an HTTP request to the entered website using the Python Requests library.
4. The server response is analyzed using the HTTP status code.
5. Based on the response code, the website is categorized as:

   * Online (status code 200–399)
   * Client Error (status code 400–499)
   * Server Error (status code 500–599)
   * Offline (no response or connection failure)
6. The result is displayed on the webpage.
7. The result is stored in a JSON file for tracking purposes.
8. Chart.js updates the pie chart showing the number of Online, Offline, and Error results.

## Project Features

• Checks the availability of any website in real time.
• Classifies responses into Online, Client Error, Server Error, and Offline categories.
• Stores monitoring results in a JSON file.
• Displays results using a dynamic pie chart visualization.
• Provides a simple and user-friendly web interface.

## Project File Structure

app.py
The main backend file that runs the Flask application and handles website status checking.

templates/
Contains HTML templates used to display the webpage.

index.html
The frontend interface where users enter URLs and view results.

uptime_data.json
Stores monitoring results such as URL, status, and timestamp.

requirements.txt
Lists the Python libraries required to run the project.

## Key Learning Outcomes

• Understanding how web applications work using Flask.
• Learning how HTTP requests and response status codes function.
• Implementing backend logic using Python.
• Working with JSON for data storage.
• Creating simple data visualizations using Chart.js.
• Integrating frontend and backend components.

## Possible Future Improvements

• Monitoring multiple websites simultaneously.
• Adding automatic periodic checks for uptime monitoring.
• Calculating uptime percentage over time.
• Adding email or notification alerts when a website goes offline.
• Creating a dashboard with historical analytics.

## Conclusion

The Website Uptime Monitor is a practical beginner-friendly project that demonstrates the integration of backend programming, web development, and data visualization. It provides a basic foundation for understanding how monitoring tools used in real-world DevOps environments operate.
