/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  var printShape

  erd.debug = {};
  erd.debug.enable = window.localStorage.getItem('debug') === 'true';

  // A debugging function. Tries to find a diagram and print it.
  erd.debug._activeStage = null;
  erd.debug.printStage = function() {
    if (erd.debug._activeStage !== null) {
      var stage = erd.debug._activeStage;
      for (var i = 0; i < stage.shapes.length; ++i) {
        var s = stage.shapes[i];
        erd.debug.printShape(s);
      }
      for (var j = 0; j < stage.connectors.length; ++j) {
        var c = stage.connectors[j];
        erd.debug.printConnector(c);
      }
    }
  };

  erd.debug.printShape = function(shape) {
    var str = shape.getType() + ' ' + shape.details.name + ' (' + shape.details.id + ')';
    if (shape.getType() === 'Relationship') {
      str = str + ' slot entities ' + shape.details.slots[0].entityId + ', ' + shape.details.slots[1].entityId;
    }
    console.log(str);
  };

  erd.debug.printConnector = function(conn) {
    var src = conn.sourceItem;
    var dest = conn.destinationItem;
    var str = conn.getType() + ' (' + conn.details.id + ') ' + src.details.id + ' -> ' + dest.details.id;
    if (conn.getType() === 'RelationshipConnector') {
      str = str + ' slot index ' + conn.details.slotIndex;
    }
    console.log(str);
  };

})();
