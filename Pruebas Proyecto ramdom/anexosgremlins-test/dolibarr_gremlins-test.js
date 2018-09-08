function loadScript(callback) {
  var s = document.createElement('script');
  s.src = 'https://rawgithub.com/marmelab/gremlins.js/master/gremlins.min.js';
  if (s.addEventListener) {
    s.addEventListener('load', callback, false);
  } else if (s.readyState) {
    s.onreadystatechange = callback;
  }
  document.body.appendChild(s);
}

//
function testDolibarr(ttl, callback) {
  function stop() {
    horde.stop();
    callback();
  }

//Puede llenar campos, dar clic, y manejar scroller despues de ingresar
gremlins.createHorde()
  	  .gremlin(gremlins.species.formFiller())
	  .gremlin(gremlins.species.clicker().clickTypes(['click']))
	  .gremlin(gremlins.species.scroller())
	  .gremlin(function() {
	    window.$ = function() {};
	  })
	  .unleash();

  var horde = window.gremlins.createHorde();

  horde.seed(1234);

  horde.after(callback);
  window.onbeforeunload = stop;
  setTimeout(stop, ttl);
  horde.unleash();
}

describe('Monkey dolibarr ', function() {



  it('Test dolibarr', function() {
  
	browser.url('http://dolibarr-pruebas.herokuapp.com/index.php');        			
        browser.waitForVisible('#login_line2', 10000);	
	browser.element('input[id="username"]').click().keys('admin');		
	browser.element('input[id="password"]').click().keys('123456');
        browser.click('input[type="submit"]')

    	browser.timeoutsAsyncScript(60000);
    	browser.executeAsync(loadScript);

	browser.timeoutsAsyncScript(60000);
    	browser.executeAsync(testDolibarr, 50000);

  });


  afterAll(function() {
    browser.log('browser').value.forEach(function(log) {
      browser.logger.info(log.message.split(' ')[2]);
    });
  });

});
