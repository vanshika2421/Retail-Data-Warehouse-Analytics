import pandas as pd


def validate_customer_data(df):

    required_columns = [
        "CustomerID",
        "FirstName",
        "LastName",
        "Email"
    ]

    return all(
        column in df.columns
        for column in required_columns
    )


def validate_sales_data(df):

    required_columns = [
        "CustomerID",
        "ProductID",
        "Quantity",
        "LineTotal"
    ]

    return all(
        column in df.columns
        for column in required_columns
    )


def test_customer_schema_validation():

    data = {

        "CustomerID":[1,2],
        "FirstName":["John","Alex"],
        "LastName":["Smith","Brown"],
        "Email":["a@test.com","b@test.com"]

    }


    df = pd.DataFrame(data)


    assert validate_customer_data(df) == True



def test_sales_schema_validation():

    data = {

        "CustomerID":[1],
        "ProductID":[10],
        "Quantity":[2],
        "LineTotal":[500]

    }


    df = pd.DataFrame(data)


    assert validate_sales_data(df) == True



def test_empty_dataframe():

    df = pd.DataFrame()


    assert df.empty == True