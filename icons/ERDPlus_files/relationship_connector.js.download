/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  erd.ParticipationType = {
    mandatory: 'mandatory',
    optional: 'optional',
    unspecified: 'unspecified'
  };

  erd.CardinalityType = {
    many: 'many',
    one: 'one',
    unspecified: 'unspecified'
  };

  erd.RelationshipConnector = function(entity, relationship, details) {
    erd.Connector.call(this, entity, relationship, details);
    this.entity = entity;
    this.relationship = relationship;
  };

  _.assign(erd.RelationshipConnector.prototype, erd.Connector.prototype);

  erd.RelationshipConnector.prototype.getType = function() {
    return 'RelationshipConnector';
  };

  erd.RelationshipConnector.prototype.removeFromStage = function(stage) {
    var slot = this.getRelationshipSlot();
    if (slot !== null) {
      slot.entityId = 0;
    }
    erd.Connector.prototype.removeFromStage.call(this, stage);
  };

  erd.RelationshipConnector.prototype.getRelationshipSlot = function() {
    return this.relationship.getSlot(this.details.slotIndex);
  };

  /**
   * Returns the opposite slot details or null if no entity has been assigned yet.
   * See entity_anchor.js calling this method.
   */
  erd.RelationshipConnector.prototype.getOppositeRelationshipSlot = function() {
    // Only two slots are supported
    var index = (this.details.slotIndex + 1) % 2;
    var details = this.relationship.getSlot(index);
    if (details.entityId !== 0) {
      return details;
    } else {
      return null;
    }
  };

  erd.RelationshipConnector.prototype.updateAnchors = function() {
    if (this.sourceAnchor !== null) {
      this.sourceAnchor.removeConnector(this);
      this.sourceAnchor = null;
    }
    if (this.destinationAnchor !== null) {
      this.destinationAnchor.removeConnector(this);
      this.destinationAnchor = null;
    }

    /////////////

    // Determine which connector case we are dealing with
    var otherConnector = this.getOtherConnector();
    if (otherConnector === null) {
      // This is the only connector attached to the relationship
      this.updateAnchorsSingleConnector();
    } else if (this.isUnary()) {
      this.updateAnchorsUnaryConnector(otherConnector);
    } else {
      this.updateAnchorsDoubleConnector(otherConnector);
    }
  };

  // Update anchors for only this connector
  erd.RelationshipConnector.prototype.updateAnchorsSingleConnector = function() {
    var distances = this.computeDistances();
    var closestPair = this.getClosestPair(distances);

    this.sourceAnchor = closestPair.eAnchor;
    this.destinationAnchor = closestPair.rAnchor;

    this.sourceAnchor.addConnector(this);
    this.destinationAnchor.addConnector(this);
  };

  // Update anchors for both this and the other entity
  erd.RelationshipConnector.prototype.updateAnchorsDoubleConnector_old = function(otherConnector) {
    var thisDistances = this.computeDistances();
    var thisClosestPair = this.getClosestPair(thisDistances);

    var otherDistances = otherConnector.computeDistances();
    otherConnector.replaceAnchors(null, null);
    var otherClosestPair = this.getClosestPair(otherDistances);

    if (thisClosestPair.distance < otherClosestPair.distance) {
      this.sourceAnchor = thisClosestPair.eAnchor;
      this.destinationAnchor = thisClosestPair.rAnchor;
      var oppositeAnchor = this.relationship.getOppositeAnchor(thisClosestPair.rAnchor);
      var eAnchor = this.getClosestPairByAnchor(otherDistances, oppositeAnchor).eAnchor;
      otherConnector.replaceAnchors(eAnchor, oppositeAnchor);
    } else {
      otherConnector.replaceAnchors(otherClosestPair.eAnchor, otherClosestPair.rAnchor);
      var oppositeAnchor = this.relationship.getOppositeAnchor(otherClosestPair.rAnchor);
      var eAnchor = this.getClosestPairByAnchor(thisDistances, oppositeAnchor).eAnchor;
      this.sourceAnchor = eAnchor;
      this.destinationAnchor = oppositeAnchor;
    }

    this.sourceAnchor.addConnector(this);
    this.destinationAnchor.addConnector(this);
  };

  // Update anchors for both this and the other entity
  erd.RelationshipConnector.prototype.updateAnchorsDoubleConnector = function(otherConnector) {
    var thisDistances = this.computeDistances();
    var otherDistances = otherConnector.computeDistances();
    otherConnector.replaceAnchors(null, null);

    //
    var minDistance = Number.MAX_VALUE;
    var bestConfig = null;
    for (var i = 0; i < this.relationship.outerAnchors.length; ++i) {
      var config = {};

      config.rAnchor1 = this.relationship.outerAnchors[i];
      var pair = this.getClosestPairByAnchor(thisDistances, config.rAnchor1);
      config.eAnchor1 = pair.eAnchor;
      config.distance = pair.distance;

      config.rAnchor2 = this.relationship.getOppositeAnchor(config.rAnchor1);
      pair = this.getClosestPairByAnchor(otherDistances, config.rAnchor2);
      config.eAnchor2 = pair.eAnchor;
      config.distance += pair.distance;

      if (config.distance < minDistance) {
        bestConfig = config;
        minDistance = config.distance;
      }
    }

    this.sourceAnchor = bestConfig.eAnchor1;
    this.destinationAnchor = bestConfig.rAnchor1;
    this.sourceAnchor.addConnector(this);
    this.destinationAnchor.addConnector(this);

    otherConnector.replaceAnchors(bestConfig.eAnchor2, bestConfig.rAnchor2);
  };

  erd.RelationshipConnector.prototype.updateAnchorsUnaryConnector = function() {
    var thisDistances = this.computeDistances();

    // Remove left and right entity anchors from thisDistances
    var arr = [];
    for (var i = 0; i < thisDistances.length; ++i) {
      if (thisDistances[i].eAnchor.side === 'top' || thisDistances[i].eAnchor.side === 'bottom') {
        arr.push(thisDistances[i]);
      }
    }
    thisDistances = arr;

    var otherConnector = this.getOtherConnector();
    var pt1 = this.relationship.getCenterPoint();
    var pt2 = this.entity.getCenterPoint();

    var thisRelationshipAnchor;
    var otherRelationshipAnchor;
    if (Math.abs(pt1.x - pt2.x) < Math.abs(pt1.y - pt2.y)) {
      // Use left and right relationship anchors
      if (this.details.id < otherConnector.details.id) {
        thisRelationshipAnchor = this.relationship.outerAnchors[0];
        otherRelationshipAnchor = this.relationship.outerAnchors[2];
      } else {
        thisRelationshipAnchor = this.relationship.outerAnchors[2];
        otherRelationshipAnchor = this.relationship.outerAnchors[0];
      }
    } else {
      // Use top and bottom relationship anchors
      if (this.details.id < otherConnector.details.id) {
        thisRelationshipAnchor = this.relationship.outerAnchors[1];
        otherRelationshipAnchor = this.relationship.outerAnchors[3];
      } else {
        thisRelationshipAnchor = this.relationship.outerAnchors[3];
        otherRelationshipAnchor = this.relationship.outerAnchors[1];
      }
    }

    otherConnector.replaceAnchors(null, null);
    this.sourceAnchor = this.getClosestPairByAnchor(thisDistances, thisRelationshipAnchor).eAnchor;
    this.destinationAnchor = thisRelationshipAnchor;
    this.sourceAnchor.addConnector(this);
    this.destinationAnchor.addConnector(this);

    var otherEntityAnchor = this.getClosestPairByAnchor(thisDistances, otherRelationshipAnchor).eAnchor;
    otherConnector.replaceAnchors(otherEntityAnchor, otherRelationshipAnchor);
 };

  erd.RelationshipConnector.prototype.replaceAnchors = function(eAnchor, rAnchor) {
    if (this.sourceAnchor !== null) {
      this.sourceAnchor.removeConnector(this);
      this.sourceAnchor = null;
    }
    if (this.destinationAnchor !== null) {
      this.destinationAnchor.removeConnector(this);
      this.destinationAnchor = null;
    }

    if (eAnchor !== null) {
      this.sourceAnchor = eAnchor;
      this.sourceAnchor.addConnector(this);
    }
    if (rAnchor !== null) {
      this.destinationAnchor = rAnchor;
      this.destinationAnchor.addConnector(this);
    }
  };

  erd.RelationshipConnector.prototype.getOtherConnector = function() {
    // Get other connector of the unary relationship
    var otherConnector = null;
    for (var i = 0; i < this.relationship.outerAnchors.length; ++i) {
      var anchor = this.relationship.outerAnchors[i];
      if (anchor.firstConnector() !== null && anchor.firstConnector().details.id !== this.details.id) {
        otherConnector = anchor.firstConnector();
      }
    }
    return otherConnector;
  };

  // Returns true if this connector is part of a unary relationship
  erd.RelationshipConnector.prototype.isUnary = function() {
    return (this.relationship.details.slots[0].entityId === this.relationship.details.slots[1].entityId);
  };

  // Compute and return all anchor distances between the relationship and the entity
  erd.RelationshipConnector.prototype.computeDistances = function() {
    var distances = [];
    for (var i = 0; i < this.relationship.outerAnchors.length; ++i) {
      for (var j = 0; j < this.entity.entityAnchors.length; ++j) {
        var pair = {
          rAnchor: this.relationship.outerAnchors[i],
          eAnchor: this.entity.entityAnchors[j]
        };
        pair.distance = erd.utils.distance(pair.rAnchor.getPoint(), pair.eAnchor.getPoint());
        distances.push(pair);
      }
    }
    return distances;
  };

  // Get closest pair of anchors from a distances array returned by computeDistances
  erd.RelationshipConnector.prototype.getClosestPair = function(distances) {
    var index = 0;
    for (var i = 1; i < distances.length; ++i) {
      if (distances[i].distance < distances[index].distance && distances[i].eAnchor.countConnectors() === 0) {
        index = i;
      }
    }
    return distances[index];
  };

  erd.RelationshipConnector.prototype.getClosestPairByAnchor = function(distances, relationshipAnchor) {
    var d = Number.MAX_VALUE;
    var index = -1;
    for (var i = 0; i < distances.length; ++i) {
      if (relationshipAnchor === distances[i].rAnchor) {
        if (distances[i].distance < d && distances[i].eAnchor.countConnectors() === 0) {
          d = distances[i].distance;
          index = i;
        }
      }
    }
    return distances[index];
  };

})();
