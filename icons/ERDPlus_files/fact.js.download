/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  erd.Fact = function(details) {
    erd.BaseTable.call(this, details);
  };

  _.assign(erd.Fact.prototype, erd.BaseTable.prototype);

  erd.Fact.prototype.getType = function() {
    return 'Fact';
  };

  erd.Fact.prototype.getTableTitle = function() {
    return this.details.name + ' fact table';
  };

  erd.Fact.prototype.getTableLineWidth = function() {
    return 2;
  };

  erd.Fact.prototype.getBounds = function(forMouseMove) {
    // Add extra size for thick line strokes
    var bounds = erd.BaseTable.prototype.getBounds.call(this, forMouseMove);
    bounds.left -= 1;
    bounds.bottom += 1;
    bounds.right += 1;
    return bounds;
  };

  erd.Fact.prototype._getAutomaticSortOrder = function(pkAttributes, regAttributes, fkAttributes) {
    return fkAttributes.concat(pkAttributes).concat(regAttributes);
  };

})();
