## INNER JOIN (SELF JOIN is a special case of inner join where it looks at a pair)
SELECT 
    COUNT(DISTINCT u.user_id)
FROM 
    users u JOIN posts p ON u.user_id = p.user_id

## OUTER JOIN # Preserves all rows
SELECT 
    *
FROM 
    users u OUTER JOIN posts p ON u.user_id = p.user_id
WHERE 
    u.active_status = False OR p.active_status = False 

## Left JOIN # Preserves the left table rows 
SELECT
    COUNT(
        DISTINCT CASE 
            WHEN p.post_id IS NOT NULL THEN u.user_id 
        END
    )
FROM 
    users u LEFT JOIN posts p ON u.user_id = p.user_id

## Right JOIN # Preserves the right table rows
SELECT 
    COUNT(
        DISTINCT CASE 
            WHEN u.country = "US" THEN p.post_id
        END
    )
FROM
    user u RIGHT JOIN posts p ON u.user_id = p.user_id

