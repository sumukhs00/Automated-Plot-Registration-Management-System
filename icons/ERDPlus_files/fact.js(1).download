/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  erd.FactMouseHandler = function(stage) {
    erd.BaseMouseHandler.call(this, stage);
  };

  _.assign(erd.FactMouseHandler.prototype, erd.BaseMouseHandler.prototype);

  erd.FactMouseHandler.prototype.onMouseDown = function(evt, x, y) {
    var fact = this.stage.factory.fact({
      x: x,
      y: y,
      name: 'Fact'
    });
    this.stage.handleMouseDropItem(fact);
  };

})();
