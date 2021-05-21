const {app, BrowserWindow} = require('electron')
const path = require('path')

function createWindow(){
    const win = new BrowserWindow({
        width:800,
        height:600,
        webPreferences:{
            preload:path.join(__dirname,'js/preload.js')
        }
    })

    win.loadFile('pages/index.html')
}

app.whenReady().then(()=>{
    createWindow()

    app.on('activate',()=>{
        if(BrowserWindow.getAllWindows().length==0){
            createWindow()
        }
    })
})

app.on('window-all-closed',()=>{
    if(process.platform!='darwin'){
        app.quit()
    }
})