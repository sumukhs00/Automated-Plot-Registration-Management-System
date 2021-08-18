/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  erd.AttributeMouseHandler = function(stage) {
    erd.BaseMouseHandler.call(this, stage);
  };

  _.assign(erd.AttributeMouseHandler.prototype, erd.BaseMouseHandler.prototype);

  erd.AttributeMouseHandler.prototype.onMouseDown = function(evt, x, y) {
    var attribute = this.stage.factory.attribute({
      x: x,
      y: y
    });
    this.stage.handleMouseDropItem(attribute);
  };

})();
