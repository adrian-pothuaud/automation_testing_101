module.exports = {
    'CURA Test : User Cannot Login' : function (client) {
        var myLoginPage = client.page.Login();

        myLoginPage
            .navigate()
            .waitForElementVisible('@username', 1000)
            .setValue('@username', 'Jane Doe')
            .setValue('@password', 'ThisIsAPassword')
            .click('@submit')
            .waitForElementVisible('@failed', 3000);

        client.end();
    }
  };