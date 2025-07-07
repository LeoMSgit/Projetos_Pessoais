SELECT 
    m.iban AS sender,
    COUNT(t.sender) AS transactions,
    GROUP_CONCAT(DISTINCT c.name ORDER BY c.name ASC) AS currencies
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
