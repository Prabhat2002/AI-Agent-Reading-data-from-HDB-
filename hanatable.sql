CREATE COLUMN TABLE INVOICES (
    InvoiceId NVARCHAR(36) NOT NULL,
    CustomerId NVARCHAR(20) NOT NULL,
    InvoiceDate DATE NOT NULL,
    Country NVARCHAR(50) NOT NULL,
    City NVARCHAR(50) NOT NULL,
    State NVARCHAR(50),
    Address NVARCHAR(200) NOT NULL,
    TotalAmount DECIMAL(15,2) NOT NULL,
    Currency NVARCHAR(3) NOT NULL,
    Region NVARCHAR(50) NOT NULL,
    IsPartialDelivery BOOLEAN NOT NULL,
    RefOrderNo NVARCHAR(20) NOT NULL,
    PRIMARY KEY (InvoiceId)
);




