# Power BI Use Case Documentation

This document outlines the various use cases for a Power BI project, providing step-by-step instructions and explanations for each use case.

## Table of Contents
1. [Identifying the Trend of Sales to Each Geography](#use-case-1-identifying-the-trend-of-sales-to-each-geography)
2. [Amounts by Individual Sales People](#use-case-2-amounts-by-individual-sales-people)
3. [Analyzing Sales Person Performance](#use-case-3-analyzing-sales-person-performance)
4. [Formatting Our Visualization](#use-case-4-formatting-our-visualization)
5. [Adding Category and Geo Splits](#use-case-5-adding-category-and-geo-splits)
6. [Adding Titles, Logos to Your Reports](#use-case-6-adding-titles-logos-to-your-reports)
7. [Sales Trend Analysis and Forecasting](#use-case-7-sales-trend-analysis-and-forecasting)
8. [Publishing Your Report](#publishing-your-report)

---

### Use Case 1: Identifying the Trend of Sales to Each Geography
**Objective:** Analyze the trend of sales to different geographies.

1. Connect the `Locations` and `Sales` tables in the data model using the connection string (geo:locations and geography:sales).
2. Create a column chart with the X-axis as "GEO" and the Y-axis as "Amount."
3. Observe blank entries in the chart due to inconsistencies in the "Geography" column.
4. Apply a data transformation using Power Query Editor to clean and format the "Geography" column by trimming.
5. Save the changes.

### Use Case 2: Amounts by Individual Sales People
**Objective:** Analyze sales amounts by individual salespeople.

1. Create a stacked bar chart with the X-axis as "Amount" and the Y-axis as "Sales Person."
2. Identify and fix blank entries in the "Teams" column.
3. Use the Power BI interactive mode to locate blank entries and select a table visual to list the blank salespeople.
4. In the table view, select the "Sales Person" table and transform null entries by adding them to a special team.
5. Apply changes in the report view to fix the issue.

### Use Case 3: Analyzing Sales Person Performance
**Objective:** Analyze the performance of salespeople.

1. Create a table visual with columns "Sales Person Name" and "Amount."
2. Delete the "Amount" column and create a new measure using DAX to calculate the total amount: "Total Amount = sum(sales[Amount])."
3. Format the "Total Amount" with the appropriate currency type.
4. Enhance the report by adding slicer visualizations for team analysis.

### Use Case 4: Formatting Our Visualization
**Objective:** Format the report for a professional look.

1. Format headings by giving the title "Sales Team and Their Performance."
2. Create custom measures, e.g., "Total Boxes = sum(sales[Boxes])," and format them.
3. Sort the "Total Amount" column.
4. Calculate "Amount per Box" using a DAX measure and format it.
5. Use Conditional Formatting visuals (data bars) to highlight the "Amount per Box."
6. Add images to the visualization to enhance its appeal.

### Use Case 5: Adding Category and Geo Splits
**Objective:** Show salespeople's performance by category and geography.

1. Create a stacked column chart with X-axis as "Category" and Y-axis as "Total Amount."
2. Configure interactions to show data for selected salespeople.
3. Duplicate the chart and change the X-axis to "Geo" for geography analysis.

### Use Case 6: Adding Titles, Logos to Your Reports
**Objective:** Add titles and logos to improve report presentation.

1. Insert text for the title and resize it.
2. Insert an image to the report.

### Use Case 7: Sales Trend Analysis and Forecasting
**Objective:** Analyze sales trends and perform forecasting.

1. Create a line chart with X-axis as "Date" and Y-axis as "Total Customers."
2. Create a measure for "Total Customers" using DAX.
3. Add a category to the legend.
4. Enable forecasting for future analysis.

### Publishing Your Report
**Objective:** Publish your Power BI report online.

1. Click on the "Publish" button to publish the report.
2. Copy the published link for sharing with others in read-only mode.

---

These are the step-by-step instructions for various use cases in your Power BI project. Follow these guidelines to create, analyze, and share your reports effectively.