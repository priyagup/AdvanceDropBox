# AdvanceDropBox
This project functioning is similar to Google Docs. It supports real time editing and viewing files/folders/database by clients. It is a distributed system where multiple client can simultaneously edit and view. Every write done by any client will be reflected in all the locations the file is open. To maintain the fault/crash tolerance, the project implements the concept of replication of servers with specific design.
1) Connecting with MongoDB for storage
2) using Flask framework for UI 
3) Activating Restful API's
