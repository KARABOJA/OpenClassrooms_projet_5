db = connect( 'mongodb://' + process.env.MONGO_INITDB_ROOT_USERNAME + ':' + process.env.MONGO_INITDB_ROOT_PASSWORD + '@localhost/admin' );
db.createUser({user: process.env.TECHNIQUEMIGRATIONLOGIN, pwd: process.env.TECHNIQUEMIGRATIONPASSWORD, roles: [ { role: "readWrite", db: "test" },{ role: "readWrite", db: "prod" } ]});
db.createUser({user: process.env.TECHNIQUETESTLOGIN, pwd: process.env.TECHNIQUETESTPASSWORD, roles: [ { role: "read", db: "test" },{ role: "read", db: "prod" } ]});
db.createUser({user: process.env.DEVLOGIN, pwd: process.env.DEVPASSWORD, roles: [ { role: "read", db: "test" },{ role: "read", db: "prod" } ]});
db.createUser({user: process.env.USERLOGIN, pwd: process.env.USERPASSWORD, roles: [ { role: "read", db: "prod" } ]});
