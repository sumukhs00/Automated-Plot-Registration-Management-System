/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  erd.AttributeOwner = function() {
    this.childAttributes = [];
  };

  erd.AttributeOwner.prototype.addAttribute = function(attribute) {
    if (!this.containsAttribute(attribute)) {
      this.childAttributes.push(attribute);
      attribute.setOwner(this);
    }
  };

  erd.AttributeOwner.prototype.removeAttribute = function(attribute) {
    this.childAttributes = _.reject(this.childAttributes, function(attr) {
      return attr.details.id === attribute.details.id;
    });
  };

  erd.AttributeOwner.prototype.containsAttribute = function(attribute) {
    var found = _.find(this.childAttributes, function(attr) {
      return attr.details.id === attribute.details.id;
    });
    return found !== undefined;
  };

  erd.AttributeOwner.prototype.moveChildAttributes = function(dx, dy) {
    for (var i = 0; i < this.childAttributes.length; ++i) {
      this.childAttributes[i].move(dx, dy);
    }
  };

  erd.AttributeOwner.prototype.removeAllChildAttributes = function(stage) {
    for (var i = this.childAttributes.length - 1; i >= 0; --i) {
      this.childAttributes[i].removeFromStage(stage);
    }
    this.childAttributes = [];
  };

  // Gets combined bounds of all child attributes
  erd.AttributeOwner.prototype.getChildAttributeBounds = function() {
    var bounds = {
      left: Number.MAX_VALUE,
      top: Number.MAX_VALUE,
      right: Number.MIN_VALUE,
      bottom: Number.MIN_VALUE
    };
    for (var i = 0; i < this.childAttributes.length; ++i) {
      var other = this.childAttributes[i].getBounds(true);
      bounds = erd.utils.combineBounds(bounds, other);
    }
    return bounds;
  };

  // Define rotations to be used before giving up trying to position a new attribute
  var autoRotations = [0, Math.PI / 16, Math.PI / -16];

  // Defines 22 attribute offset positions without overlap
  var autoOffsets = [
    {x: 0,    y: -84},
    {x: 72,   y: -48},
    {x: 100,  y: 0},
    {x: 72,   y: 48},
    {x: 0,    y: 84},
    {x: -72,  y: 48},
    {x: -100, y: 0},
    {x: -72,  y: -48},
    {x: 0,    y: -140},  // start of outer circle
    {x: 86,   y: -112},
    {x: 165,  y: -76},
    {x: 188,  y: -25},
    {x: 188,  y: 25},
    {x: 165,  y: 76},
    {x: 86,   y: 112},
    {x: 0,    y: 140},
    {x: -86,  y: 112},
    {x: -165, y: 76},
    {x: -188, y: 25},
    {x: -188, y: -25},
    {x: -165, y: -76},
    {x: -86,  y: -112}
  ];

  // Returns the first available "fan" position for a new attribute.
  erd.AttributeOwner.prototype.getNextAutomaticPosition = function() {
    var center = this.getCenterPoint();

    for (var i = 0; i < autoRotations.length; ++i) {
      var angle = autoRotations[i];
      for (var j = 0; j < autoOffsets.length; ++j) {
        var offset = autoOffsets[j];
        var pt = {
          x: center.x + offset.x,
          y: center.y + offset.y
        };
        pt = erd.utils.rotate(pt, center, angle);
        if (this.findAttributeAtPosition(pt) === null) {
          return pt;
        }
      }
    }

    // If we make it this far the user has created a lot of attributes all at once!
    return {
      x: center.x,
      y: center.y + 50
    };
  };

  erd.AttributeOwner.prototype.findAttributeAtPosition = function(pt) {
    for (var i = 0; i < this.childAttributes.length; ++i) {
      var attr = this.childAttributes[i];
      if (attr.details.x === pt.x && attr.details.y === pt.y) {
        return attr;
      }
    }
    return null;
  };

})();
