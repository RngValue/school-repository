select manufacturer.ManufacturerID, manufacturer.manufacturer, count(product.ProductID) as "Number of products" from product
inner join manufacturer on product.ManufacturerID = manufacturer.ManufacturerID
group by manufacturer.ManufacturerID order by count(product.ProductID) desc;