const express = require('express')
const router = express.Router()
const { spawn } = require('child_process')


router.get('/', function(req, res) {

    const pythonProcess = spawn("python3", ["./public/converter/main.py", "./002.pd"])
        //const pythonProcess = spawn("ls", ["-la"])
    pythonProcess.stdout.on('data', function(data) {

        //console.log(typeof data)
        console.log(data)
        let obj = JSON.parse(data.toString())
        res.render('index', { 'graph': obj })
    })

    pythonProcess.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });
})

module.exports = router;