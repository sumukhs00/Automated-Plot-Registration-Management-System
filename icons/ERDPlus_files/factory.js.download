/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  erd.Factory = function(stage) {
    this.stage = stage;
    this.nextId = 1;
  };

  erd.Factory.prototype.entity = function(details) {
    return this.initItem(new erd.Entity(details));
  };

  erd.Factory.prototype.attribute = function(details) {
    return this.initItem(new erd.Attribute(details));
  };

  erd.Factory.prototype.relationship = function(details) {
    return this.initItem(new erd.Relationship(details));
  };

  erd.Factory.prototype.table = function(details) {
    return this.initItem(new erd.Table(details));
  };

  erd.Factory.prototype.fact = function(details) {
    return this.initItem(new erd.Fact(details));
  };

  erd.Factory.prototype.dimension = function(details) {
    return this.initItem(new erd.Dimension(details));
  };

  erd.Factory.prototype.label = function(details) {
    return this.initItem(new erd.Label(details));
  };

  erd.Factory.prototype.initItem = function(item) {
    if (typeof item.details.id === 'number') {
      if (this.nextId <= item.details.id) {
        this.nextId = item.details.id + 1;
      }
    } else {
      item.details.id = this.nextId;
      this.nextId += 1;
    }
    return item;
  };

  erd.Factory.prototype.createConnector = function(sourceItem, destinationItem, details) {
    return this.initItem(new erd.Connector(sourceItem, destinationItem, details));
  };

  erd.Factory.prototype.createRelationshipConnector = function(sourceItem, destinationItem, details) {
    return this.initItem(new erd.RelationshipConnector(sourceItem, destinationItem, details));
  };

  erd.Factory.prototype.createTableConnector = function(pkTable, fkTable, details) {
    return this.initItem(new erd.TableConnector(pkTable, fkTable, details));
  };

})();
