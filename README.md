**COMPANY**: CODETECH IT SOLUTIONS

**Name**: SHOEB KHAN

**INTERN ID**: CT0806HU

**Domain**: Python Programming

**BATCH Duration**: 12th December to 12th January

**Mentor**: Neela Santhosh Kumar

**PROJECT**: API INTEGRATION AND DATA VISUALIZATION

### Overview of the Code

This Python script is designed to fetch and visualize the current position of the International Space Station (ISS) using the Open Notify API. Here's a breakdown of its functionality:

---

### OUPUT OF THE TASK

![task1](https://github.com/user-attachments/assets/d54f5614-b9fd-4723-8b7e-294472feb706)


### **1. Importing Required Libraries**
- **`requests`**: For making HTTP requests to fetch data from the API.
- **`pandas`**: To structure and handle data in a tabular format for analysis.
- **`matplotlib.pyplot` and `seaborn`**: For data visualization, specifically to create plots.

---

### **2. Fetching Data from the API**
- **API Endpoint**: The script retrieves real-time data from `http://api.open-notify.org/iss-now.json`.
- **Response Handling**:
  - It uses `requests.get()` to fetch the data.
  - The response is converted to JSON format with `.json()`.
  - A status check is implemented to ensure successful retrieval:
    - **Success**: Prints "Data fetched successfully!"
    - **Failure**: Prints "Failed to fetch data."

---

### **3. Extracting and Structuring Data**
- The ISS's **latitude** and **longitude** are extracted from the API response under the `iss_position` key.
- A **Pandas DataFrame** is created to store the latitude and longitude, enabling easy visualization.

---

### **4. Visualizing the Data**
- A scatter plot is generated using **Seaborn**:
  - **Longitude** and **Latitude** are plotted on the x and y axes, respectively.
  - The ISS's position is represented as a blue dot (`scatterplot` with `color='blue'` and `s=100` for size).
- **Additional Plot Features**:
  - Gridlines for better readability.
  - Axes labeled as "Longitude" and "Latitude."
  - Limits set for longitude (-180 to 180) and latitude (-90 to 90) to represent the Earth's coordinate system.
  - Horizontal and vertical lines (`axhline`, `axvline`) added to indicate the equator and prime meridian.

---

### **Key Features**
1. **Real-Time Data**: Fetches live information about the ISS's location.
2. **Error Handling**: Provides feedback if the API request fails.
3. **Visualization**: Clearly displays the ISS's current position on a 2D coordinate plane.
4. **Modular Design**: Uses a combination of libraries for efficient data fetching, handling, and visualization.

---

### **Potential Enhancements**
- **Map Integration**: Overlay the ISS position on a world map for more context.
- **Data Logging**: Store successive positions in a CSV file for tracking and historical analysis.
- **Interactive Plot**: Use tools like `plotly` for an interactive visualization experience.
