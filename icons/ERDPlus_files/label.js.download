/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  erd.LabelMouseHandler = function(stage) {
    erd.BaseMouseHandler.call(this, stage);
  };

  _.assign(erd.LabelMouseHandler.prototype, erd.BaseMouseHandler.prototype);

  erd.LabelMouseHandler.prototype.onMouseDown = function(evt, x, y) {
    var label = this.stage.factory.label({
      x: x - 50,
      y: y - 25
    });
    this.stage.handleMouseDropItem(label);
  };

})();
