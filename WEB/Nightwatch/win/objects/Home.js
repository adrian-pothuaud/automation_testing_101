module.exports = {

    elements : {
        appointment_button : {
          selector: "#btn-make-appointment"
        },
        title : {
            selector : "h1",
            text : "CURA Healthcare Service"
        },
        menu : {
          selector: "#menu-toggle"
        }
    },

    sections : {
        menu: {
            selector: '#menu-toggle',
            elements: {
              history: {
                selector: 'a[href*:"history.php#history"]'
              },
              login: {
                selector: 'a[href*:"profile.php#login"]'
              },
              logout: {
                selector: 'a[href*:"authenticate.php?logout"]'
              }
            }
          }
    },

    url : "http://demoaut.katalon.com/"
}