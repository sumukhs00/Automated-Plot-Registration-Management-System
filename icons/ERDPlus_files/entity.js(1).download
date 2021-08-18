/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  erd.EntityMouseHandler = function(stage) {
    erd.BaseMouseHandler.call(this, stage);
  };

  _.assign(erd.EntityMouseHandler.prototype, erd.BaseMouseHandler.prototype);

  erd.EntityMouseHandler.prototype.onMouseDown = function(evt, x, y) {
    var entity = this.stage.factory.entity({
      x: x,
      y: y
    });
    this.stage.handleMouseDropItem(entity);
  };

})();
