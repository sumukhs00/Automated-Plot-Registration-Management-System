/*jslint browser:true */
"use strict"

window.erd = window.erd || {}

;(function() {
  erd.ConnectHelper = function(stage) {
    this.stage = stage
  }

  erd.ConnectHelper.prototype.items = function(source, destination, details) {
    if (typeof details !== "object") {
      details = {}
    }
    if (source && destination) {
      var s = source.getType()
      var d = destination.getType()
      if (s === "Attribute" && d === "Entity") {
        return this.attributeToEntity(source, destination)
      } else if (s === "Entity" && d === "Attribute") {
        return this.attributeToEntity(destination, source)
      } else if (s === "Attribute" && d === "Attribute") {
        if (source.details.isComposite) {
          return this.attributeToAttribute(destination, source)
        } else if (destination.details.isComposite) {
          return this.attributeToAttribute(source, destination)
        }
      } else if (s === "Entity" && d === "Relationship") {
        return this.entityToRelationship(source, destination, details)
      } else if (s === "Relationship" && d === "Entity") {
        return this.entityToRelationship(destination, source, details)
      } else if (s === "Attribute" && d === "Relationship") {
        return this.attributeToRelationship(source, destination)
      } else if (s === "Relationship" && d === "Attribute") {
        return this.attributeToRelationship(destination, source)
      } else if (s === "Table" && d === "Table") {
        if (source.hasPk()) {
          return this.tableToTable(source, destination, details)
        } else if (destination.hasPk()) {
          return this.tableToTable(destination, source, details)
        }
      } else if (s === "Dimension" && d === "Dimension") {
        if (source.hasPk()) {
          return this.tableToTable(source, destination, details)
        } else if (destination.hasPk()) {
          return this.tableToTable(destination, source, details)
        }
      } else if (s === "Dimension" && d === "Fact") {
        if (source.hasPk()) {
          return this.tableToTable(source, destination, details)
        }
      }
    }
  }

  // Assign the attribute to the entity, removing the attribute from the previous owner if necessary.
  erd.ConnectHelper.prototype.attributeToEntity = function(attribute, entity) {
    this.disconnectAttribute(attribute)
    var connector = this.stage.factory.createConnector(attribute, entity)
    entity.addAttribute(attribute)
    this.stage.addItem(connector)
  }

  // Assign the attribute to the relationship, removing the attribute from the previous owner if necessary.
  erd.ConnectHelper.prototype.attributeToRelationship = function(attribute, relationship) {
    this.disconnectAttribute(attribute)
    var connector = this.stage.factory.createConnector(attribute, relationship)
    relationship.addAttribute(attribute)
    this.stage.addItem(connector)
  }

  // Assign the attribute to the composite-attribute, removing the attribute from the previous owner if necessary.
  erd.ConnectHelper.prototype.attributeToAttribute = function(attribute, compositeAttribute) {
    this.disconnectAttribute(attribute)
    var connector = this.stage.factory.createConnector(attribute, compositeAttribute)
    compositeAttribute.addAttribute(attribute)
    this.stage.addItem(connector)
  }

  // Connect a relationship to an entity, claiming a details slot on the relationship
  // if one does not already exist for the entity and one is available.
  erd.ConnectHelper.prototype.entityToRelationship = function(entity, relationship, details) {
    var slot = relationship.getSlot(details.slotIndex)
    if (slot === null) {
      slot = relationship.getAvailableSlot()
      details.slotIndex = slot.slotIndex
    }
    slot.entityId = entity.details.id

    var connector = this.stage.factory.createRelationshipConnector(entity, relationship, details)
    this.stage.addItem(connector)
    relationship.updateConnectors()
  }

  erd.ConnectHelper.prototype.tableToTable = function(pkTable, fkTable, details) {
    // The fk attribute will already exist if we are deserializing.
    if (typeof details.fkAttributeId === "number" && fkTable.getAttributeById(details.fkAttributeId) !== null) {
      var connector = this.stage.factory.createTableConnector(pkTable, fkTable, details)
      this.stage.addItem(connector)
    } else {
      var fk = pkTable.createFk(pkTable)
      fkTable.addAttribute(fk)
      var connector = this.stage.factory.createTableConnector(pkTable, fkTable, {
        fkAttributeId: fk.id
      })
      this.stage.addItem(connector)
      return fk
    }
  }

  erd.ConnectHelper.prototype.disconnectAttribute = function(attribute) {
    if (attribute.getOwner() !== null) {
      var connector = this.stage.findConnectorByIds(attribute.details.id, attribute.getOwner().details.id)
      if (connector !== null) {
        this.stage.removeItem(connector)
      }
      attribute.getOwner().removeAttribute(attribute)
      attribute.setOwner(null)
    }
  }
})()
