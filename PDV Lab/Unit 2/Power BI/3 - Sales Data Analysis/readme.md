# Power BI Use Cases Documentation

This document provides a detailed guide for various use cases in a Power BI project. Please follow the instructions as they are presented.

## Use Case 1: Identifying the Trend of Sales to Each Geography

**Objective:** Analyze sales trends in different geographical locations.

1. Connect the `Locations` and `Sales` tables in the data model using the connection string (geo:locations and geography:sales).
2. Create a column chart with the X-axis set to "GEO" and the Y-axis set to "Amount."
3. Observe potential blank entries in the chart due to inconsistencies in the "Geography" column.
4. Apply data transformation using Power Query Editor to clean and format the "Geography" column, including trimming.
5. Save your changes.
6. In the report view, examine the visualization. You may want to aggregate data by sum, mean, max, or min of "Amount" by geography. For Y-axis, select "Average" to see the results.

## Use Case 2: Amounts by Individual Sales People

**Objective:** Analyze sales amounts by individual salespeople.

1. Create a stacked bar chart with the X-axis set to "Amount" and the Y-axis set to "Sales Person" (as there are numerous salespeople).
2. Identify and address any blanks in the "Teams" column.
3. Use the Power BI interactive mode to locate and understand the blank entries.
4. Select a table visual to list the salespeople with blank entries for further investigation.
5. In the table view, select the "Sales Person" table and perform data transformation. Identify and handle null entries by adding them to a special team.
6. Select the "Team" column, right-click, and choose the "Replace Values" rule, with "Find" set to "null" and "Replace" set to "Special." Close and apply.
7. In the report view, the issue with null entries should be resolved, with all null entries now categorized under the "Special" team.

This completes the data clean-up process.

## Use Case 3: Analyzing Sales Person Performance

**Objective:** Analyze the performance of salespeople.

1. Create a new page by clicking on the "+" at the bottom of the page and rename it.
2. Since there are a large number of salespeople, select a table visual. Include columns "Sales Person Name" and "Amount."
3. Delete the "Amount" column, and right-click the "Sales" table to create a new measure. This opens the formula bar for Data Analysis Expressions (DAX).
4. Enter the following DAX expression: "Total Amount = SUM(sales[Amount])" and commit it. This custom measure logic is applied to the data and appears in the Sales data pane with a calculator symbol indicating it's a custom measure.
5. A measure has both logical (the formula you added) and visual definitions. It acts like a tiny calculator attached to the data for dynamic calculations.
6. To add visual definition, click on the "Total Amount" field. In the format ribbon, set the currency type to INDIAN Rupee and commit the changes.
7. The table now displays information about all salespeople. If you want to analyze sales from a team perspective, add slicer visualizations to the report.

## Use Case 4: Formatting Our Visualization

**Objective:** Format the report for a professional appearance.

1. In the format pane, select "Visuals" and format headings by giving the title "Sales Team and Their Performance." You can use the search feature or select options from the pane.
2. Use DAX to create measures for performance metrics. For example, if you want to show "Total Boxes (Sales)," create a new measure on the "Sales" table: "Total Boxes = SUM(sales[Boxes])." Format it as a whole number with zero decimal places.
3. As this is a performance report, sort it by "Total Amount." Click on "Total Amount" to access a list of sorting options in ascending or descending order.
4. Calculate "Amount per Box" using a DAX measure (Composite DAX measure). Since you have "Total Amount" and "Total Boxes" columns, create a new column: "Amount per Box" using the DAX measure on the "Sales" table: "Amount per Box = [Total Amount] / [Total Boxes]" (no parentheses within the workbook). Format it to display the INDIAN Rupee symbol and two decimal places.
5. Since "Amount per Box" is an important performance indicator, use Conditional Formatting visuals (data bars) in Power BI. First, select the table, then access the format options. In the "Cell Element" section, apply settings to the "Amount per Box" column and enable data bars. You can select the logic and color.
6. If the colors are overlapping the price values, adjust the data bar settings. In the "fx" section, set the maximum custom value to 20, 25, or 30 to prevent color overlap.

## Use Case 5: Adding Category and Geo Splits

**Objective:** Visualize salespeople's performance by category and geography.

1. Create a stacked column chart with the X-axis set to "Category" and the Y-axis set to "Total Amount."
2. Configure interactions to display data for selected salespeople.
3. Duplicate the chart and change the X-axis to "Geo" for geography-based analysis.

## Use Case 6: Adding Titles, Logos to Your Reports

**Objective:** Enhance the report's presentation with titles and logos.

1. In the "Insert" tab, select "Insert Text" and add a title, then resize it.
2. In the "Insert" tab, select "Insert Image" and add a logo.

## Use Case 7: Sales Trend Analysis and Forecasting

**Objective:** Perform sales trend analysis and forecasting.

1. To conduct trend analysis and forecasting, you need time-series data.
2. In the table view, select the sales data table, which contains data, amounts, customers, and boxes. These can be modeled as time-series data.
3. Sub-Use Case: Customer trend analysis
   - Analyze how many customers are served on a daily basis in the year 2023 and forecast for 2024.
   - Create a new page, name it "Sales Trend Analysis and Forecasting."
   - Select a line chart with X-axis set to "Date" and Y-axis set to a measure for customers, such as "Total Customers = SUM(sales[Customers])."
   - Note that the date field has a hierarchy of year, quarter, month, and day, so use the arrow option at the top of the visual.
   - Add a category to the legend to partition the data by products.
4. Sub-Use Case: Forecasting for 3 Months
   - In the visual icon of the chart, enable the checkbox for forecasting and trend lines for future analysis.

## Publishing Your Report

**Objective:** Publish your Power BI report online.

1. Click on the "Publish" button to upload your report to the Power BI service.
2. Copy the published link to share your report with others. You can open the link in a browser without login credentials to view the report in read-only mode.