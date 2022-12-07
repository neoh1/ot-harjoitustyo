# Architechture

## UI

Currently login screen
Main GUI with button functionality and animations

## Application logic
```mermaid
 classDiagram
      ModelTraining "*" --> "1" User
      class User{
          username
          password
      }
      class ModelTraining{
          id
          Models
          Logs
          Parameters
      }
```

## Data saving
Username and password are saved into an encrypted table in a SQLite-database.
Training results and parameters are also saved encrypted to the same database in another table.
