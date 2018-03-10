// Handle arrow key control of slides
var Key = {
  LEFT:   37,
  UP:     38,
  RIGHT:  39,
  DOWN:   40
};

/**
 * old IE: attachEvent
 * Firefox, Chrome, or modern browsers: addEventListener
 */
function _addEventListener(evt, element, fn) {
  if (window.addEventListener) {
    element.addEventListener(evt, fn, false);
  }
  else {
    element.attachEvent('on'+evt, fn);
  }
}

function handleKeyboardEvent(evt) {
  if (!evt) {evt = window.event;} // for old IE compatible
  var keycode = evt.keyCode || evt.which; // also for cross-browser compatible

  var info = document.getElementById("arrowkeys");
  switch (keycode) {
    case Key.LEFT:
      plusSlides(-1);
      window.alert('left')
      break;
    case Key.RIGHT:
      plusSlides(1);
      console.log('right')
      break;
  }
}

_addEventListener('keydown', document, handleKeyboardEvent);