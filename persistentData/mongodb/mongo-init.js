db = db.getSiblingDB('cct')
db.createCollection('measurements')

db.createUser({
    user: "cctAdmin",
    pwd: "cctAdmin",
    roles: [{ role: "dbOwner", db: "cct" }]
})

db.createUser({
    user: "client-1",
    pwd:  "client-1",
    roles:[{role: "readWrite" , db:"cct"}]
})

print('Collection and users created')