SELECT address_id,
    address,
    district,
    city_id,
    postal_code,
    phone
FROM address
WHERE address_id IN (1, 23, 4, 5, 33, 666)
ORDER BY address_id;