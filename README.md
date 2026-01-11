<h1 align="center">SmartBus Ticketing System</h1>
<p align="center">
  A data-driven public transport ticketing platform built in Python
</p>

<hr>

<h2>Overview</h2>
<p>
SmartBus Ticketing is a Python-based ticket management system that simulates a real-world public transport booking platform. 
It allows customers to browse ticket categories, view detailed ticket information, and purchase tickets, while administrators can manage ticket prices through a secure admin panel.
</p>

<hr>

<h2>Customer Features</h2>
<ul>
  <li>Browse ticket categories such as Student, Adult, Network, and Season tickets</li>
  <li>View ticket details including price, duration, entitlements, and number of passengers</li>
  <li>Purchase tickets with automatic timestamping</li>
  <li>View full purchase history</li>
  <li>Tickets displayed in tabular format using pandas</li>
</ul>

<hr>

<h2>Admin Features</h2>
<ul>
  <li>Password-protected administrator access</li>
  <li>View all available tickets</li>
  <li>Modify ticket prices</li>
  <li>Save updated ticket data back to the CSV database</li>
  <li>View ticket data in tabular format</li>
</ul>

<hr>

<h2>Data Architecture</h2>
<p>
The system uses a CSV file as a data source. Each row in the CSV is read into a dictionary and tickets are grouped into categories using a dictionary-based indexing system. 
This allows efficient filtering and fast access when users select a category.
</p>

<hr>

<h2>Technologies Used</h2>
<ul>
  <li>Python</li>
  <li>pandas for data analysis and tabular display</li>
  <li>CSV for file-based data storage</li>
  <li>Object-Oriented Programming</li>
  <li>Terminal User Interface</li>
</ul>

<hr>



<hr>

<h2>Purpose</h2>
<p>
This project was developed as part of a university software development module to demonstrate the use of data structures, object-oriented programming, file handling, and real-world datasets in a working application.
</p>

<hr>

<h2>Author</h2>
<p>
Developed by Saif.
</p>