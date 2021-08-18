/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  erd.Dimension = function(details) {
    erd.BaseTable.call(this, details);
  };

  _.assign(erd.Dimension.prototype, erd.BaseTable.prototype);

  erd.Dimension.prototype.getType = function() {
    return 'Dimension';
  };

  erd.Dimension.prototype._getAutomaticSortOrder = function(pkAttributes, regAttributes, fkAttributes) {
    return fkAttributes.concat(pkAttributes).concat(regAttributes);
  };

})();
