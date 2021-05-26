const {Menu} = require('electron')
const electron = require('electron')
const app = electron.app
const shell = require('electron').shell

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
      submenu: [
        {
          label: i18n.__('Documentation'),
          click() {
            
          }
        },
        {
          label: i18n.__('Contact us'),
          click() {
            shell.openExternal("mailto:rafa10031999@gmail.com?subject=&body=");
          }
        }
      ]
    }
]

const menu = Menu.buildFromTemplate(template)
Menu.setApplicationMenu(menu)