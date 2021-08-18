/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  var WIDTH = 150;
  var HALF_WIDTH = WIDTH / 2;
  var LINE_HEIGHT = 15;
  var LINE_MARGIN = 2;
  var SUFFIX_MARGIN = 10;
  var BRACKET_SIZE = 5;

  var attributeDefaults = {
    // "names" is an array to support composite foreign keys. All other attributes
    // have an array of size one.
    names: ['Attribute'],
    order: 0,
    pkMember: false,
    optional: false,
    soloUnique: false,
    fk: false,
    dataType: 'int',
    dataTypeSize: null  // More accurately, this is the size or custom data type
  };

  erd.BaseTable = function(details) {
    erd.Selectable.call(this);
    this.details = {
      name: 'Table',
      x: 0,
      y: 0,
      sort: "automatic",
      attributes: [],
      uniqueGroups: [] // Array of array's of attribute IDs.
    };
    _.assign(this.details, details);

    this.moved = false;
    this.anchors = [];

    // Add the two PK anchors
    this.anchors.push(new erd.TableAnchor(this, 0, LINE_HEIGHT, 'left', 0));
    this.anchors.push(new erd.TableAnchor(this, WIDTH, LINE_HEIGHT, 'right', 0));

    for (var i = 0; i < this.details.attributes.length; ++i) {
      this.createAnchors(this.details.attributes[i]);
    }
    this.updateHeight();
    this.updateAllAnchors();
  };

  _.assign(erd.BaseTable.prototype, erd.Selectable.prototype);

  erd.BaseTable.prototype.hitTest = function(x, y) {
    // (x,y) is the top left
    return (this.details.x < x &&
            this.details.y < y &&
            this.details.x + WIDTH > x &&
            this.details.y + this._attributesHeight + LINE_HEIGHT > y);
  };

  erd.BaseTable.prototype.getCenterPoint = function() {
    return {
      x: this.details.x + HALF_WIDTH,
      y: this.details.y + (this._attributesHeight + LINE_HEIGHT) / 2
    };
  };

  erd.BaseTable.prototype.containedBy = function(rect) {
    var x = this.details.x + HALF_WIDTH;
    var y = this.details.y + (this._attributesHeight + LINE_HEIGHT) / 2;
    return erd.utils.rectContainsPoint(rect, x, y);
  };

  erd.BaseTable.prototype.move = function(dx, dy) {
    if (!this.moved) {
      this.moved = true;
      this.details.x += dx;
      this.details.y += dy;
      this.updateConnectors();
    }
  };

  erd.BaseTable.prototype.updateConnectors = function() {
    for (var i = 0; i < this.anchors.length; ++i) {
      var anchor = this.anchors[i];
      anchor.updateAllConnectors();
    }
  };

  /**
   * Add the given attribute or composite-attribute. See attributeDefaults.
   */
  erd.BaseTable.prototype.addAttribute = function(attribute) {
    _.defaults(attribute, attributeDefaults);
    
    var max = _.reduce(this.details.attributes, function(max, attr) {
      return Math.max(max, attr.id);
    }, 0);
    attribute.id = max + 1;

    var orderMax = _.reduce(this.details.attributes, function(max, attr) {
      return Math.max(max, attr.order);
    }, 0);
    attribute.order = orderMax + 1;

    this.details.attributes.push(attribute);
    this.updateHeight();
    this.createAnchors(attribute);
    this.updateAllAnchors();
    return attribute;
  };

  erd.BaseTable.prototype.removeAttribute = function(attribute, stage) {
    if (attribute.pkMember) {
      this.removePkConnectors(stage);
    }
    if (attribute.fk) {
      var anchors = this.getAnchorsByAttributeId(attribute.id);
      for (var i = 0; i < anchors.length; ++i) {
        anchors[i].removeAllConnectorsFromStage(stage);
      }
      this.anchors = _.reject(this.anchors, function(a) {
        return a.attributeId === attribute.id;
      });
    }
    this.details.attributes = _.reject(this.details.attributes, function(attr) {
      return attr.id === attribute.id;
    });
    this.updateHeight();
    this.updateAllAnchors();
  };

  erd.BaseTable.prototype.removePkConnectors = function(stage) {
    var anchors = this.getAnchorsByAttributeId(0);
    for (var i = 0; i < anchors.length; ++i) {
      anchors[i].removeAllConnectorsFromStage(stage);
    }
  };

  erd.BaseTable.prototype.createAnchors = function(attribute) {
    if (attribute.fk) {
      this.anchors.push(new erd.TableAnchor(this, 0, LINE_HEIGHT, 'left', attribute.id));
      this.anchors.push(new erd.TableAnchor(this, WIDTH, LINE_HEIGHT, 'right', attribute.id));
    }
  };

  // Update offsets for anchors of one attribute
  erd.BaseTable.prototype._updateAnchorOffsets = function(attributeId, y) {
    for (var i = 0; i < this.anchors.length; ++i) {
      if (this.anchors[i].attributeId === attributeId) {
        this.anchors[i].setOffsetY(y);
      }
    }
  };

  erd.BaseTable.prototype.updateHeight = function() {
    var countNames = _.reduce(this.details.attributes, function(count, attr) {
      return count + attr.names.length;
    }, 0);
    this._attributesHeight = Math.max(
      countNames * LINE_HEIGHT,
      LINE_HEIGHT);
  };

  erd.BaseTable.prototype.getTableTitle = function() {
    return this.details.name;
  };

  erd.BaseTable.prototype.getTableLineWidth = function() {
    return 1;
  };

  erd.BaseTable.prototype.draw = function(context) {
    context.save();
    context.translate(this.details.x + 0.5, this.details.y + 0.5);
    erd.utils.fillText(context, this.getTableTitle(), {
      x: HALF_WIDTH,
      y: LINE_HEIGHT,
      maxWidth: WIDTH,
      textAlign: 'center',
      textBaseline: 'bottom'
    });

    context.save();
    context.beginPath();
    if (this.getIsSelected()) {
      context.fillStyle = erd.settings.selectedShapeFill;
    } else {
      context.fillStyle = erd.settings.shapeFill;
    }
    context.lineWidth = erd.settings.strokeWidth;
    context.strokeStyle = erd.settings.stroke;
    context.lineWidth = this.getTableLineWidth();
    context.rect(0, LINE_HEIGHT, WIDTH, this._attributesHeight);
    context.fill();
    context.stroke();
    context.restore();

    var y = LINE_HEIGHT;
    var attributesInOrder = this.getAttributesByOrder();
    for (var i = 0; i < attributesInOrder.length; ++i) {
      var attr = attributesInOrder[i];
      var height = this.drawAttribute(context, attr, y + LINE_HEIGHT / 2);
      y += height;
    }
    context.restore();

    for (var i = 0; i < this.anchors.length; ++i) {
      this.anchors[i].draw(context);
    }
  };

  erd.BaseTable.prototype.drawAsConnectTarget = function(context, strokeStyle) {
    this.draw(context);
    context.save();
    context.beginPath();
    context.translate(this.details.x, this.details.y);
    context.rect(0, 0, WIDTH, LINE_HEIGHT + this._attributesHeight);
    context.strokeStyle = strokeStyle;
    context.lineWidth = erd.settings.connectStrokeWidth * 2;
    context.stroke();
    context.restore();
  };

  erd.BaseTable.prototype.drawAttribute = function(context, attr, y) {
    var h = LINE_HEIGHT * attr.names.length;
    var maxWidth = 0;
    for (var i = 0; i < attr.names.length; ++i) {
      var textMetrics = erd.utils.fillText(context, attr.names[i], {
        x: LINE_MARGIN,
        y: y + LINE_HEIGHT * i,
        maxWidth: WIDTH - 2 * LINE_MARGIN,
        underline: attr.pkMember,
        font: attr.pkMember ? erd.settings.boldFont : erd.settings.font
      });
      maxWidth = Math.max(maxWidth, textMetrics.width);
    }

    // Draw composite bracket
    var bracketX = 0;
    var bracketY = 0;
    if (attr.names.length > 1) {
      context.beginPath();
      var bracketX = maxWidth + SUFFIX_MARGIN;
      var bracketY = y - LINE_HEIGHT / 2 + 2;
      context.moveTo(bracketX, bracketY);
      context.lineTo(bracketX + BRACKET_SIZE, bracketY);
      context.lineTo(bracketX + BRACKET_SIZE, bracketY + h - 4);
      context.lineTo(bracketX, bracketY + h - 4);
      context.stroke();
    } else {
      bracketX = maxWidth + SUFFIX_MARGIN;
      bracketY = y - LINE_HEIGHT / 2;
    }

    // Draw suffix
    var suffix = '';
    if (attr.optional) {
      suffix += '(O)';
    }
    if (attr.fk) {
      suffix += '(FK)';
    }
    suffix += this._getUniqueSuffix(attr);
    if (suffix.length > 0) {
      erd.utils.fillText(context, suffix, {
        font: erd.settings.smallFont,
        x: bracketX + SUFFIX_MARGIN,
        y: bracketY + h / 2,
        maxWidth: WIDTH,
      });
    }

    return h;
  };

  /**
   * Returns a temporary array of attributes in the order they should be drawn
   */
  erd.BaseTable.prototype.getAttributesByOrder = function() {
    var pkAttributes = [];
    var fkAttributes = [];
    var regAttributes = [];
    for (var i = 0; i < this.details.attributes.length; ++i) {
      var attr = this.details.attributes[i];
      if (attr.pkMember) {
        pkAttributes.push(attr);
      } else if (attr.fk) {
        fkAttributes.push(attr);
      } else {
        regAttributes.push(attr);
      }
    }

    if (this.details.sort === 'automatic') {
      return this._getAutomaticSortOrder(pkAttributes, regAttributes, fkAttributes);
    } else {
      pkAttributes = _.sortBy(pkAttributes, function(attr) {
        return attr.order;
      });
      var otherAttributes = regAttributes.concat(fkAttributes);
      otherAttributes = _.sortBy(otherAttributes, function(attr) {
        return attr.order;
      });

      // sort attriubtes by order however keep all PK attributes together.
      if (pkAttributes.length === 0) {
        return otherAttributes;
      } else if (otherAttributes.length === 0) {
        return pkAttributes;
      } else {
        var attributes = [];
        while (otherAttributes.length > 0 && otherAttributes[0].order < pkAttributes[0].order) {
          attributes = attributes.concat(otherAttributes.splice(0, 1));
        }
        attributes = attributes.concat(pkAttributes);
        attributes = attributes.concat(otherAttributes);
        return attributes;
      }
    }
  };

  erd.BaseTable.prototype._getAutomaticSortOrder = function(pkAttributes, regAttributes, fkAttributes) {
    return pkAttributes.concat(regAttributes).concat(fkAttributes);
  };

  erd.BaseTable.prototype._getUniqueSuffix = function(attribute) {
    var suffixes = [];
    if (attribute.soloUnique && !attribute.pkMember) {
      suffixes.push('(U)');
    }
    for (var i = 0; i < this.details.uniqueGroups.length; ++i) {
      if (this.details.uniqueGroups[i].indexOf(attribute.id) !== -1) {
        suffixes.push('(Ugroup' + (i + 1) + ')');
      }
    }
    if (suffixes.length > 0) {
      return suffixes.join('');
    } else {
      return '';
    }
  };

  erd.BaseTable.prototype.getBounds = function(forMouseMove) {
    var bounds = {
      left: this.details.x,
      top: this.details.y,
      right: this.details.x + WIDTH + 1,
      bottom: this.details.y + this._attributesHeight + LINE_HEIGHT + 1
    };
    for (var i = 0; i < this.anchors.length; ++i) {
      var a = this.anchors[i];
      if (a.countConnectors() > 0) {
        if (a.side === 'left') {
          bounds.left -= a.getAnchorWidth();
        } else {
          bounds.right += a.getAnchorWidth();
        }
      }
    }
    return bounds;
  };

  erd.BaseTable.prototype.hasPk = function() {
    for (var i = 0; i < this.details.attributes.length; ++i) {
      if (this.details.attributes[i].pkMember) {
        return true;
      }
    }
    return false;
  };

  erd.BaseTable.prototype.getAnchorsByAttributeId = function(attributeId) {
    var anchors = [];
    for (var i = 0; i < this.anchors.length; ++i) {
      if (this.anchors[i].attributeId === attributeId) {
        anchors.push(this.anchors[i]);
      }
    }
    return anchors;
  };

  erd.BaseTable.prototype.getAttributeById = function(attributeId) {
    for (var i = 0; i < this.details.attributes.length; ++i) {
      if (this.details.attributes[i].id === attributeId) {
        return this.details.attributes[i];
      }
    }
    return null;
  };

  erd.BaseTable.prototype.createFk = function() {
    var fk = _.cloneDeep(attributeDefaults);
    fk.names = [];
    fk.references = [];

    /*
      references is an array of objects like below.

        {
          "tableId": <id>,
          "attributeId": <id>,
          "fkSubIndex": <index>
        }

      This reference refers to the related primary key table.
      fkSubIndex is defined if the referenced primary key attribute
      is itself a FK to some other table.
    */

    fk.fk = true;
    for (var i = 0; i < this.details.attributes.length; ++i) {
      var attr = this.details.attributes[i];
      if (attr.pkMember) {

        if (attr.fk) {
          for (var j = 0; j < attr.names.length; ++j) {
            fk.names.push(attr.names[j]);
            fk.references.push({
              tableId: this.details.id,
              attributeId: attr.id,
              fkSubIndex: j
            });
          }
        } else {
          fk.names.push(attr.names[0]);
          fk.references.push({
            tableId: this.details.id,
            attributeId: attr.id
          });
        }

      }
    }
    return fk;
  };

  erd.BaseTable.prototype.removeFromStage = function(stage) {
    // Remove all attributes first to properly remove connectors and FK fields in other tables
    while (this.details.attributes.length > 0) {
      this.removeAttribute(this.details.attributes[0], stage);
    }
    for (var i = 0; i < this.anchors[i]; ++i) {
      this.anchors[i].removeAllConnectorsFromStage(stage);
    }
    stage.removeItem(this);
  };

  erd.BaseTable.prototype.postLoad = function() {
    this.updateAllAnchors();
  };

  erd.BaseTable.prototype.updateAllAnchors = function() {
    // Update anchor positions - similar to drawing the attributes
    var y = LINE_HEIGHT;

    var attributesInOrder = this.getAttributesByOrder();
    var totalPkHeight = 0;
    var endPkY = y;
    for (var i = 0; i < attributesInOrder.length; ++i) {
      var attr = attributesInOrder[i];
      var height = LINE_HEIGHT * attr.names.length
      y += height;
      if (attr.fk) {
        this._updateAnchorOffsets(attr.id, y - height / 2);
      }
      if (attr.pkMember) {
        totalPkHeight += height;
        endPkY = y;
      }
    }
    this._updateAnchorOffsets(0, endPkY - totalPkHeight / 2);
  };

})();
