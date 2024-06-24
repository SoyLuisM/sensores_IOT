const express = require('express')
const app = express()

const port = 8080

let temperatura = 0;
let humedad =0;

app.use(express.json())
app.use(express.urlencoded({ extended: true }))

app.get('/', (req, res) => {
    res.send(`temperatura= ${temperatura}°C Humadad= ${humedad}`)
    console.log('Valotemperatura= ${temperatura}°C Humadad= ${humedad}rew')
})

app.post('/', (req, res) => {
    temperatura = req.body.temperatura
    humedad = req.body.humedad
    res.send('ok')
})
app.listen(port, ()=> {
    console.log(`escuchando en el puerto ${port}`)
})



