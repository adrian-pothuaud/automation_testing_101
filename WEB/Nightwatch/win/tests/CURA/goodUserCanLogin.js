module.exports = {
    'CURA Test : User Can Login' : function (client) {
        var myLoginPage = client.page.Login();
        var myHomePage = client.page.Home();

        myLoginPage
            .navigate()
            .waitForElementVisible('@username', 1000)
            .setValue('@username', 'John Doe')
            .setValue('@password', 'ThisIsNotAPassword')
            .click('@submit');

        myHomePage
            .waitForElementVisible('@title', 3000);

        client.end();
    }
  };