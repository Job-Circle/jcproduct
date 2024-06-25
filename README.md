# Job-Circle Product

# MongoDB Tutorial

## Installation

For installation view the script folder with instructions available.

## Getting Started

1. **Start MongoDB:**
   - Open a new terminal and run MongoDB by executing:
     ```bash
     mongod
     ```
   - This command starts the MongoDB server locally.

2. **Connect to MongoDB:**
   - Open another terminal and connect to MongoDB using:
     ```bash
     mongo
     ```
   - This opens the MongoDB shell where you can execute commands.

## Basic Commands

### Show Databases

```bash
show dbs
```

### Switch Database

```bash
use <database_name>
```

### Show Collections

```bash
show collections
```

### Create Collections

```bash
db.createCollection("<collection_name>")
```

### Insert into Collection

```bash
db.<collection_name>.insertOne({ key: value })
```

### Find Documents

```bash
db.<collection_name>.find()
```

### Update Documents

```bash
db.<collection_name>.updateOne({ filter }, { update })
```

### Delete Documents

```bash
db.<collection_name>.deleteOne({ filter })
```

### Drop Collection

```bash
db.<collection_name>.drop()
```

### Drop Database

```bash
db.dropDatabase()
```

## Querying and Aggregation

### Query with Conditions

```bash
db.<collection_name>.find({ key: value })
```

### Aggregation Pipeline

```bash
db.<collection_name>.aggregate([{ $match: { key: value }}, { $group: { _id: "$key", total: { $sum: 1 }}}])
```

## Index Operations

### Create Index

```bash
db.<collection_name>.createIndex({ key: 1 })
```

### List Indexes

```bash
db.<collection_name>.getIndexes()
```

### Drop Index

```bash
db.<collection_name>.dropIndex({ key: 1 })
```


#### Example MongoDB Operations


1. **Creating a Database and Collection:**
   Connect to MongoDB and create a database named `webstore` with a collection named `products`.

   ```javascript
   // MongoDB shell commands
   use webstore
   db.createCollection("products")
   ```

2. **Adding a New Product:**
   Insert a new product item into the `products` collection.

   ```javascript
   // Inserting a new product
   db.products.insertOne({
     name: "Laptop",
     price: 1200.00,
     description: "High-performance laptop with SSD storage.",
     inventory: 50
   })
   ```

3. **Querying Products:**
   Query products to retrieve information based on specific criteria.

   ```javascript
   // Querying products
   db.products.find({ name: "Laptop" })
   ```

4. **Updating Product Inventory:**
   Update the inventory of a product when new stock arrives.

   ```javascript
   // Updating product inventory
   db.products.updateOne(
     { name: "Laptop" },
     { $set: { inventory: 60 } }
   )
   ```



