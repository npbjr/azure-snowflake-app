# Azure Snowflake Python Integration App ❄️🌐

## Goals 🚀
- **Integrate Azure function and snowflake**  
- **Ingest sample feed to snowflake from azure**  
- **Expose Azure API to be consumed by client apps**

## Prerequisites ✅

- **Docker** installed on your machine

## Getting Started 🌟

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/npbjr/azure-snowflake-app.git
   cd azure-snowflake-app
   ```

2. **run docker compose**:
   ```bash
   docker-compose up
   ```

3. **run Browser or Curl**:
   ```bash
   http://localhost:7071/api/http_snowflake_analytics?name=123
   ```
   or curl
   ```bash
    curl -X GET http://localhost:7071/api/http_snowflake_analytics?name=triximylove
    ```
