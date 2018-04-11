module.exports = {
    'Demot test Google' : function (browser) {
      browser
        .url('http://www.google.com')
        .waitForElementVisible('body', 1000)
        .setValue('input[type=text]', 'nightwatch')
        .waitForElementVisible('input[name=btnK]', 1000)
        .click('input[class=lsb]')
        .pause(1000)
        .assert.containsText('#main', 'Night Watch')
        .end();
    }
  };