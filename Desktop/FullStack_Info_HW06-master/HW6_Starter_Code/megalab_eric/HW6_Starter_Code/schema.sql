drop table if exists trips;
create table trips (
	customer_id integer primary key,
	trip_name text not null,
	destination text not null,
	friend text not null
);

drop table if exists orders;
create table orders (
	order_id integer primary key,
	name_of_part text not null,
	manufacturer_of_part text not null,
	customer_ordered numeric,
	FOREIGN KEY (customer_ordered) REFERENCES trips(customer_id)
);

drop table if exists address;
create table address (
	address_id integer primary key,
	street_address text not null,
	city text not null,
	state text not null,
	country text not null,
	zip_code numeric not null
);



