# Day 32: Excel Manipulations
**Instructions:** 
1. Open a new python file.
2. The most widely used tool in analytics and business is actually Excel, so it's extremely common to automate regular reports. While Excel is a powerful tool that accomplishes most business needs, there are two major issues: a lack of transparency and a lack of version control. Often, business reports are created in Excel and contain embedded formulas to transform the data. However, while the cell contains the formula, the user only sees the output. This causes problems if the developer didn't password protect the cells and the formula is overwritten or changed at a later date. Since there is no version control functionality, the business may not even know this change occurred and decisions could be made on incorrect information. Pro tip, do not price financial market funds using an Excel spreadsheet, especially when the formulas are not protected. Python provides the ability to harden the transformation process to protect the business from these types of mistakes. [Practical Business Python](https://www.pbpython.com/) is a phenomenal resource for converting existing Excel reports into hardened python processes. 
3. Even though Excel is not a database tool, multiple sheets or workbooks are often used in this fashion. Additionally, many data entry tasks entail copying data from one spreadsheet and pasting it in another. Both of these functions are prone to errors. The `openpyxl` package provides enhanced functionality with interfacing with Excel workbooks. Load the workbook into a variable. This stores the workbook as a workbook object.
    ```
    import openpyxl
    
    sales_wb = openpyxl.load_workbook('Sales.xlsx')
    customers_wb = openpyxl.load_workbook('CustomerDIM.xlsx')
    products_wb = openpyxl.load_workbook('ProductDIM.xlsx')
    ```
4. Load the applicable sheet from each workbook into a variable. This stores the worksheet as a worksheet object.
    ```
    sales = sales_wb["sales"]
    customers = customers_wb["customer_dim"]
    products = products_wb["product_dim"]
    ```
5. The variables act as a named matrix where calling a specific cell with the `.value` method will return a data point.
    ```
    print(customers["C5"].value)
    ```
6. Writing to the excel spreadsheet is as easy as calling the cell and setting it equal to the desired value. Additionally, the `.value` method can be used for this same functionality.
    ```
    sales["E1"] = "first_name"
    sales["F1"].value = "last_name"
    sales["G1"] = "product_name"
    sales["H1"] = "product_price"
    sales["I1"] = "subtotal"
    sales["J1"] = "tax"
    sales["K1"] = "total"
    ```
7. In order to use the customer and product IDs to expand on the data, `for` loops are leveraged to iterate through the two sudo-dimension tables to match the identifiers. By enumerating over the contents of the worksheet, each row is turned into a tuple. Additionally, starting at `2` ensures the header is skipped in the transformation. The sales tax and the final cost can be added once a match is found. This information can easily be obtained through using python formulas. Additionally, displaying monies without the proper formatting is not ideal. The `.number_format` method can be applied to the `.cell` method. This allows the user to customize the cell formatting. After all of the transformations are applied, the workbook is saved to finalize the results.
    ```
    for i, sr in enumerate(sales.rows, start=2):
        for j, cr in enumerate(customers.rows, start=2):
            if sales[f"B{i}"].value == cr[0].value:
                sales[f"E{i}"] = cr[1].value
                sales[f"F{i}"] = cr[2].value

        for k, pr in enumerate(products.rows, start=2):
            if sales[f"C{i}"].value == pr[0].value:
                sales[f"G{i}"] = pr[1].value
                sales[f"H{i}"] = pr[2].value

        try:
            sales[f"I{i}"] = sales[f"H{i}"].value * sales[f"D{i}"].value
            sales.cell(row=i, column=9).number_format = "$#,##0.00"

            sales[f"J{i}"] = sales[f"I{i}"].value * 0.06
            sales.cell(row=i, column=10).number_format = "$#,##0.00"

            sales[f"K{i}"] = sales[f"I{i}"].value + sales[f"J{i}"].value
            sales.cell(row=i, column=11).number_format = "$#,##0.00"
        except TypeError:
            pass

    sales_wb.save("Sales.xlsx")
    ```
8. Update the [log file](../../log.md) with what you have learned today.
