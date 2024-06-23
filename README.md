# OLS for 4 Years

## Overview

This project conducts a simple regression analysis using Densely Inhabited District (DID) population density as the explanatory variable and Relative Total Factor Productivity (TFP) as the dependent variable. The analysis focuses on four specific years, providing a detailed view of the relationship between DID population density and relative TFP in Japan.

## Key Features

- **Regression Analysis**: Utilizes Ordinary Least Squares (OLS) regression to understand the impact of DID population density on relative TFP.
- **Visualization**: Includes a scatter plot of relative TFP versus DID population density, complemented by a regression line to illustrate the relationship.

## Running the Analysis

To run this analysis, follow these steps:

1. **Build the Docker Image**:
   
   First, build the Docker image for the project using the following command:

   ```bash
   docker build -t main .
    ```

2. **Run the Docker Container**:

    After building the image, execute the container with this command:

    ```bash
    docker run -it -v $(pwd):/app main
    ```

## Important Notes

- Ensure that Docker is installed on your system and is running before executing these commands.
- The analysis is interactive and requires user input to proceed.
