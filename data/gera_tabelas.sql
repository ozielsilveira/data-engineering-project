-- ************************************** [departments]
CREATE TABLE [departments]
(
 [departmentId] uuid IDENTITY ,
 [name]         varchar(100) NOT NULL ,
 [location]     varchar(64) NOT NULL ,


 CONSTRAINT [pk_departments] PRIMARY KEY CLUSTERED ([departmentId] ASC)
);
GO


-- ************************************** [employees]
CREATE TABLE [employees]
(
 [employeeId]   uuid IDENTITY ,
 [departmentId] uuid NOT NULL ,
 [name]         varchar(100) NOT NULL ,
 [position]     varchar(100) NOT NULL ,
 [createdAt]    datetime NOT NULL ,
 [salary]       numeric(7,2) NOT NULL ,


 CONSTRAINT [pk_employees] PRIMARY KEY CLUSTERED ([employeeId] ASC)
);
GO


CREATE NONCLUSTERED INDEX [fk_employees__departments] ON [employees] 
 (
  [departmentId] ASC
 )

GO


-- ************************************** [products]
CREATE TABLE [products]
(
 [productId]     uuid IDENTITY ,
 [name]          varchar(100) NOT NULL ,
 [description]   varchar(300) NOT NULL ,
 [costPrice]     numeric(7,2) NOT NULL ,
 [sellingPrice]  numeric(7,2) NOT NULL ,
 [stockQuantity] numeric(5,2) NOT NULL ,


 CONSTRAINT [pk_products] PRIMARY KEY CLUSTERED ([productId] ASC)
);
GO


-- ************************************** [customers]
CREATE TABLE [customers]
(
 [customerId] uuid IDENTITY ,
 [name]       varchar(100) NOT NULL ,
 [address]    varchar(300) NOT NULL ,
 [email]      varchar(64) NOT NULL ,


 CONSTRAINT [PK_1] PRIMARY KEY CLUSTERED ([customerId] ASC)
);
GO


-- ************************************** [orders]
CREATE TABLE [orders]
(
 [orderId]    uuid IDENTITY ,
 [customerId] uuid NOT NULL ,
 [createdAt]  datetime NOT NULL ,
 [total]      numeric(7,2) NOT NULL ,


 CONSTRAINT [pk_orders] PRIMARY KEY CLUSTERED ([orderId] ASC)
);
GO


CREATE NONCLUSTERED INDEX [fk_orders__customers] ON [orders] 
 (
  [customerId] ASC
 )

GO


-- ************************************** [orderItems]
CREATE TABLE [orderItems]
(
 [itemId]      uuid IDENTITY ,
 [orderId]     uuid NOT NULL ,
 [productId]   uuid NOT NULL ,
 [productName] varchar(100) NOT NULL ,
 [quantity]    numeric(5,2) NOT NULL ,
 [unitPrice]   numeric(7,2) NOT NULL ,
 [totalPrice]  numeric(7,2) NOT NULL ,


 CONSTRAINT [pk_orderItems] PRIMARY KEY CLUSTERED ([itemId] ASC)
);
GO


CREATE NONCLUSTERED INDEX [fk_orderItems__orders] ON [orderItems] 
 (
  [orderId] ASC
 )

GO

CREATE NONCLUSTERED INDEX [fk_orderItems__products] ON [orderItems] 
 (
  [productId] ASC
 )

GO
