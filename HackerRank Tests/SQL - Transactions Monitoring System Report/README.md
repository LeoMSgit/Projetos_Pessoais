Transactions Monitoring System Report
As part of HackerPay's billing analytics, a team needs a list of monitored transactions. The report should include three columns:

Column	Description
Sender	This is monitor.iban.
Transactions	Count the number of transactions associated with the sender where transactions.completed = 'yes'.
Currencies	Create a comma-delimited list of currencies.name associated with the transactions, sorted ascending.
The report should sort the rows by sender in ascending order.

Database Schema
The report utilizes three tables:

1. Currencies
Name	Type	Description
code	VARCHAR(64)	Currency code
name	VARCHAR(64)	Currency name
2. Transactions
Name	Type	Description
currency_code	VARCHAR(64)	Currency code
sender	VARCHAR(64)	Sender IBAN
completed	VARCHAR(64)	Completion status
3. Monitor
Name	Type	Description
iban	VARCHAR(64)	Sender IBAN
SQL Query Example
Here’s an example of an SQL query that generates the report:

sql
Copiar código
SELECT 
    m.iban AS sender,
    COUNT(t.sender) AS transactions,
    STRING_AGG(DISTINCT c.name, ', ' ORDER BY c.name) AS currencies
FROM 
    monitor m
LEFT JOIN 
    transactions t ON m.iban = t.sender AND t.completed = 'yes'
LEFT JOIN 
    currencies c ON t.currency_code = c.code
GROUP BY 
    m.iban
ORDER BY 
    m.iban ASC;
This query retrieves the sender's IBAN, counts the completed transactions, and creates a sorted list of associated currencies.
