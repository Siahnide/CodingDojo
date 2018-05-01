SELECT * FROM billing;

# 1
SELECT MONTHNAME(charged_datetime) AS month, SUM(amount) AS revenue
FROM billing 
WHERE MONTHNAME(charged_datetime) = 'March' AND YEAR(charged_datetime) = 2012
GROUP BY month;

# 2
SELECT clients.client_id, SUM(amount)
FROM billing
LEFT JOIN clients ON clients.client_id = billing.client_id
WHERE clients.client_id = 2
GROUP BY clients.client_id;

# 3
SELECT sites.domain_name,clients.client_id
FROM sites
JOIN clients ON sites.client_id = clients.client_id
WHERE clients.client_id = 10;

# 4
SELECT clients.client_id, COUNT(sites.domain_name) AS number_of_websites,MONTHNAME(sites.created_datetime) AS month_created,YEAR(sites.created_datetime) AS year_created
FROM clients
JOIN sites ON clients.client_id =sites.client_id
WHERE clients.client_id = 1
GROUP BY sites.site_id;

SELECT clients.client_id, COUNT(sites.domain_name) AS number_of_websites,MONTHNAME(sites.created_datetime) AS month_created,YEAR(sites.created_datetime) AS year_created
FROM clients
JOIN sites ON clients.client_id =sites.client_id
WHERE clients.client_id = 20
GROUP BY sites.site_id;

# 5
SELECT sites.domain_name,COUNT(leads.leads_id),CONCAT(MONTHNAME(leads.registered_datetime),' ',DAY(leads.registered_datetime),' ',YEAR(leads.registered_datetime)) AS date_generated
FROM sites
LEFT JOIN leads ON leads.site_id = sites.site_id
WHERE ((MONTHNAME(leads.registered_datetime) = 'January') OR  (MONTHNAME(leads.registered_datetime) = 'February')) AND ((DAY(leads.registered_datetime) > 1) OR (DAY(leads.registered_datetime) < 15) ) AND YEAR(leads.registered_datetime) = 2011
GROUP BY leads.leads_id;

# 6
SELECT CONCAT(clients.first_name,clients.last_name) AS client_name, COUNT(leads.leads_id) AS number_of_leads
FROM clients
JOIN sites ON sites.client_id = clients.client_id
LEFT JOIN leads ON leads.site_id = sites.site_id
WHERE YEAR(leads.registered_datetime) = 2011
GROUP BY clients.client_id;

# 7
SELECT CONCAT(clients.first_name,clients.last_name) AS client_name,COUNT(leads.leads_id) AS number_of_leads,MONTHNAME(leads.registered_datetime) AS date_generated
FROM clients 
JOIN sites ON sites.client_id = clients.client_id
LEFT JOIN leads ON leads.site_id = sites.site_id
WHERE YEAR(leads.registered_datetime) = 2011 AND MONTH(leads.registered_datetime) < 7
GROUP BY leads.leads_id;

#8
SELECT CONCAT(clients.first_name,clients.last_name) AS client_name,sites.domain_name AS website,COUNT(leads.leads_id) AS number_of_leads,CONCAT(MONTHNAME(leads.registered_datetime),' ',DAY(leads.registered_datetime),',',' ',YEAR(leads.registered_datetime)) AS date_generated
FROM clients
JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON leads.site_id = sites.site_id
WHERE YEAR(leads.registered_datetime) = 2011
GROUP BY sites.site_id
ORDER BY clients.client_id;

SELECT CONCAT(clients.first_name,clients.last_name) AS client_name,sites.domain_name AS website,COUNT(leads.leads_id) AS number_of_leads
FROM clients
JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON leads.site_id = sites.site_id

GROUP BY sites.site_id
ORDER BY clients.client_id;

# 9
SELECT CONCAT(clients.first_name,clients.last_name) AS client_name, SUM(billing.amount) AS Total_Revenue,MONTHNAME(billing.charged_datetime) AS month_charge,YEAR(billing.charged_datetime) AS year_charge
FROM clients
JOIN billing ON billing.client_id = clients.client_id


GROUP BY clients.client_id, MONTH(billing.charged_datetime)
ORDER BY clients.client_id, YEAR(billing.charged_datetime),MONTH(billing.charged_datetime);

# 10
SELECT CONCAT(clients.first_name,clients.last_name) AS client_name,GROUP_CONCAT(sites.domain_name,' / ')
FROM clients
JOIN sites ON sites.client_id = sites.client_id
GROUP BY clients.client_id







