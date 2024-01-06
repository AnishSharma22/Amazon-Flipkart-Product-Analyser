# Product Recommendation Engine

This web application and soon-to-be browser extension empower users to make informed decisions about purchasing products. By simply providing a product link from Amazon or Flipkart, users gain insights and recommendations tailored to their needs.

LINK : https://amazon-flipkart-product-analyser-2z8l.vercel.app/

## Features

- **Product Analysis:** Input a product link to receive detailed analysis and recommendations.
- **Informative Insights:** Gain access to insightful information aiding purchase decisions.
- **Local Deployment:** Easily run the project locally to explore and contribute.
- **Contribution Opportunities:** Open to contributions; top contributors will receive bounty rewards.

## Local Setup

### Frontend

1. **Installation:** Navigate to the frontend directory and install dependencies.
    ```bash
    npm install
    ```

2. **Run Development Server:** Execute the following command to start the frontend server.
    ```bash
    npm run dev
    ```

### Backend (FastAPI)

1. **Installation:** Move to the server directory and install the required dependencies.
    ```bash
    cd server
    pip install -r requirements.txt
    ```

2. **Run Backend Server:** Launch the backend FastAPI server using Uvicorn.
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

### Running Backend via Docker

1. **Navigate:** Move to the server directory.
    ```bash
    cd server
    ```

2. **Docker Compose:** Use the following command to set up and run the backend server using Docker.
    ```bash
    docker-compose up
    ```

## Contributions

Contributions to enhance this project are encouraged and appreciated! The project welcomes contributors, and the top contributors will be rewarded with bounty rewards.

### How to Contribute

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push the branch to your fork.
4. Open a pull request detailing your changes.

### Contributor Rewards

- Top contributors will receive bounty rewards.
- Contributions improving functionality, adding new features, or enhancing user experience are highly valued.

## License

This project is licensed under [TAGDA FOUNDATIONS](LICENSE).
