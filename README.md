<h1 align="center">SmartBus Ticketing System</h1>
<p align="center">
  A scalable, data-driven public transport ticketing platform implemented in Python
</p>

<hr>

<h2>Overview</h2>
<p>
SmartBus Ticketing is a modular, data-driven ticket management system designed to simulate a real-world public transport booking platform. 
The application provides both customer-facing and administrative functionality, enabling efficient ticket browsing, purchasing, and pricing management through a unified CSV-based data layer.
</p>

<hr>

<h2>Customer Capabilities</h2>
<ul>
  <li>Browse dynamically generated ticket categories derived directly from live CSV data</li>
  <li>Inspect detailed ticket attributes including price, duration, entitlements, and passenger limits</li>
  <li>Execute ticket purchases with automatic timestamping and persistent storage</li>
  <li>Retrieve and analyse historical purchase data</li>
  <li>Interact with ticket data displayed using structured pandas DataFrames</li>
</ul>

<hr>

<h2>Administrator Capabilities</h2>
<ul>
  <li>Secure, password-protected access to administrative controls</li>
  <li>View, audit, and manage the full ticket catalogue</li>
  <li>Dynamically modify ticket pricing in real time</li>
  <li>Persist updates back to the central CSV data source</li>
  <li>Visualise ticket data in a tabular format for validation and verification</li>
</ul>

<hr>

<h2>Data Architecture</h2>
<p>
The system utilises a CSV-driven data architecture where each ticket record is mapped into a dictionary-based data model. 
Ticket records are grouped into categories using a dictionary-of-objects pattern, allowing efficient lookup, filtering, and traversal without repeatedly scanning the entire dataset.
</p>

<hr>

<h2>Technology Stack</h2>
<ul>
  <li>Python for application logic</li>
  <li>pandas for data analysis, transformation, and tabular visualisation</li>
  <li>CSV for persistent, structured data storage</li>
  <li>Object-Oriented Programming for encapsulation and modularity</li>
  <li>Terminal-based user interface with role-based access control</li>
</ul>

<hr>



<hr>

<h2>Purpose</h2>
<p>
This project was developed as part of a university software engineering module to demonstrate the practical application of data structures, object-oriented design, file-based persistence, and data analysis in a production-style ticketing system.
</p>

<hr>

<h2>Author</h2>
<p>
Developed by Saif.
</p>