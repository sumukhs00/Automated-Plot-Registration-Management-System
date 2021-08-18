/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  erd.TableConnector = function(pkTable, fkTable, details) {
    erd.Connector.call(this, pkTable, fkTable, details);
    this.pkTable = pkTable;
    this.fkTable = fkTable;
  };

  _.assign(erd.TableConnector.prototype, erd.Connector.prototype);

  erd.TableConnector.prototype.getType = function() {
    return 'TableConnector';
  };

  erd.TableConnector.prototype.updateAnchors = function() {
    if (this.sourceAnchor !== null) {
      this.sourceAnchor.removeConnector(this);
      this.sourceAnchor = null;
    }
    if (this.destinationAnchor !== null) {
      this.destinationAnchor.removeConnector(this);
      this.destinationAnchor = null;
    }

    var pkAnchors = this.pkTable.getAnchorsByAttributeId(0); // Pass 0 for the PK anchors
    var fkAnchors = this.fkTable.getAnchorsByAttributeId(this.details.fkAttributeId);

    // Find the closest pair of anchors
    var foundDistance = Number.MAX_VALUE;
    for (var i = 0; i < pkAnchors.length; ++i) {
      var a = pkAnchors[i];
      for (var j = 0; j < fkAnchors.length; ++j) {
        var b = fkAnchors[j];
        var distance = erd.utils.distance(a.getPoint(), b.getPoint());
        if (distance < foundDistance) {
          this.sourceAnchor = a;
          this.destinationAnchor = b;
          foundDistance = distance;
        }
      }
    }

    // Finish connecting anchors
    this.sourceAnchor.addConnector(this);
    this.destinationAnchor.addConnector(this);
  };

  erd.TableConnector.prototype.removeFromStage = function(stage) {
    erd.Connector.prototype.removeFromStage.call(this, stage);
    var attr = this.fkTable.getAttributeById(this.details.fkAttributeId);
    if (attr !== null) {
      this.fkTable.removeAttribute(attr, stage);
    }
  };

})();
