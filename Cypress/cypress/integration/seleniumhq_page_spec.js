describe('Home Page Test', function() {

    it('Visits the SeleniumHQ', function() {
      cy.visit('https://www.seleniumhq.org/')
    })

    it("Verifies SeleniumHQ link in Header", function() {
        expect(cy.get("#header > h1 > a").location("href")).to.be.equal("/")
    })
  })