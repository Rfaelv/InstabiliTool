const {Menu} = require('electron')
const electron = require('electron')
const app = electron.app
// var i18n = new(require(__dirname + '\\translations\\i18n'))

var i18n = new(require('../translations/i18n'))


const template = [
    {
      label: i18n.__('File'),
      submenu: [
        {
          label: i18n.__('About'),
          click() {
            return
          },
        },
        {type: 'separator'},
        {
          label: i18n.__('New'),
          click() {
            return
          },
          accelerator: 'Ctrl+N'
        },
        {
          label: i18n.__('Open'),
          click() {
            return
          },
          accelerator: 'Ctrl+O'
        },
        {
          label: i18n.__('Save'),
          click() {
            return
          },
          accelerator: 'Ctrl+S'
        },
        {
          label: i18n.__('Save as...'),
          click() {
            return
          },
        },
        {type: 'separator'},
        {
            label: i18n.__('Quit'),
            click() {
              app.quit()
            },
          }
      ]
    },
    {
        label: i18n.__('Options'),
        submenu: [

        ]
    },
    {
        label: i18n.__('Definitions'),
        submenu: [
            {
                label: i18n.__('Units')
            },
            {
                label: i18n.__('Axes')
            }
        ]
    },
    {
      label: i18n.__('Help'),
      click() {
        // shell.openExternal('https://gitlab.com/programa-o-em-python-javascript-p-blico/analise-dinamica-de-passarelas/-/blob/master/README.md')
      }
    }
]

const menu = Menu.buildFromTemplate(template)
Menu.setApplicationMenu(menu)