/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  erd.Selectable = function() {};

  erd.Selectable.prototype._isSelected = false;

  erd.Selectable.prototype.clearSelection = function() {
    this._isSelected = false;
  };

  erd.Selectable.prototype.getIsSelected = function() {
    return this._isSelected;
  };

  erd.Selectable.prototype.setIsSelected = function(selected) {
    this._isSelected = selected;
  };

  erd.Selectable.prototype.toggleSelected = function() {
    this._isSelected = !this._isSelected;
  };

  erd.Selectable.prototype.postLoad = function() {
  };

})();
