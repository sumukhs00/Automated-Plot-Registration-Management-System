/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  erd.TableMouseHandler = function(stage) {
    erd.BaseMouseHandler.call(this, stage);
  };

  _.assign(erd.TableMouseHandler.prototype, erd.BaseMouseHandler.prototype);

  erd.TableMouseHandler.prototype.onMouseDown = function(evt, x, y) {
    var table = this.stage.factory.table({
      x: x,
      y: y
    });
    this.stage.handleMouseDropItem(table);
  };

})();
