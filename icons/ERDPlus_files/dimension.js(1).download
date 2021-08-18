/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  erd.DimensionMouseHandler = function(stage) {
    erd.BaseMouseHandler.call(this, stage);
  };

  _.assign(erd.DimensionMouseHandler.prototype, erd.BaseMouseHandler.prototype);

  erd.DimensionMouseHandler.prototype.onMouseDown = function(evt, x, y) {
    var dimension = this.stage.factory.dimension({
      x: x,
      y: y,
      name: 'Dimension'
    });
    this.stage.handleMouseDropItem(dimension);
  };

})();
