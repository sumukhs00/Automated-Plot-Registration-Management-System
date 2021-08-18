/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  erd.SelectMouseHandler = function(stage) {
    erd.BaseMouseHandler.call(this, stage);
    this.mouseInteraction = null;
  };

  _.assign(erd.SelectMouseHandler.prototype, erd.BaseMouseHandler.prototype);

  erd.SelectMouseHandler.prototype.onMouseMove = function(evt, x, y) {
    if (this.mouseInteraction !== null) {
      if (this.mouseInteraction.hasItem) {
        // Limit x,y within the bounds
        x = Math.max(x, this.mouseInteraction.bounds.left);
        x = Math.min(x, this.mouseInteraction.bounds.right);
        y = Math.max(y, this.mouseInteraction.bounds.top);
        y = Math.min(y, this.mouseInteraction.bounds.bottom);
        var dx = x - this.mouseInteraction.lastMouseX;
        var dy = y - this.mouseInteraction.lastMouseY;
        this.mouseInteraction.lastMouseX = x;
        this.mouseInteraction.lastMouseY = y;
        if (!this.mouseInteraction.isMovingShape) {
          this.stage.invokeStartMoveCallback();
          this.mouseInteraction.isMovingShape = true;
        }
        if (this.mouseInteraction.labelResize) {
          this.mouseInteraction.item.resizeLabel(dx, dy);
        } else {
          this.stage.moveSelectedShapes(dx, dy);
        }
      } else if (this.mouseInteraction.multiSelectPoints !== null) {
        this.mouseInteraction.multiSelectPoints.x2 = x;
        this.mouseInteraction.multiSelectPoints.y2 = y;
      } else {
        this.mouseInteraction.multiSelectPoints = {
          x1: this.mouseInteraction.lastMouseX,
          y1: this.mouseInteraction.lastMouseY,
          x2: x,
          y2: y
        };
      }
      this.stage.draw();
    }
  };

  erd.SelectMouseHandler.prototype.onMouseDown = function(evt, x, y) {
    var item = this.stage.hitTest(x, y);
    this.stage.invokeActiveItemChangedCallback(item);
    var labelResize = false;
    if (item !== null) {
      if (item.getType() === 'Label' && item.hitTestResize(x, y)) {
        this.stage.clearSelection();
        item.toggleSelected();
        labelResize = true;
      } else if (evt.ctrlKey) {
        item.toggleSelected();
      } else if (!item.getIsSelected()) {
        this.stage.clearSelection();
        item.setIsSelected(true);
      }
    } else {
      this.stage.clearSelection();
    }

    this.mouseInteraction = {
      lastMouseX: x,
      lastMouseY: y,
      hasItem: (item !== null),
      item: item,
      multiSelectPoints: null,
      isMovingShape: false,
      labelResize: labelResize
    };

    // Calculate the allowed x,y bounds of the mouse so that the selected items stay within the canvas.
    // This should be done after update the selection state above.
    var bounds = this.stage.getBounds(true);
    this.mouseInteraction.bounds = {
      left: x - bounds.left,
      top: y - bounds.top,
      right: x + this.stage.canvas.width - bounds.right,
      bottom: y + this.stage.canvas.height - bounds.bottom
    };

    this.stage.draw();
  };

  erd.SelectMouseHandler.prototype.onMouseUp = function(evt, x, y) {
    if (this.mouseInteraction !== null) {

      if (this.mouseInteraction.multiSelectPoints !== null) {
        var rect = normalizeRect(this.mouseInteraction.multiSelectPoints);
        if (!evt.ctrlKey) {
          this.stage.clearSelection();
        }
        this.stage.selectByRect(rect);
      }

      if (this.mouseInteraction.isMovingShape) {
        this.stage.invokeEndMoveCallback();
      }

      this.mouseInteraction = null;
      this.stage.draw();
    }
  };

  erd.SelectMouseHandler.prototype.drawSpecial = function(context) {
    if (this.mouseInteraction !== null && this.mouseInteraction.multiSelectPoints !== null) {
      context.beginPath();
      context.lineWidth = erd.settings.strokeWidth;
      context.strokeStyle = erd.settings.stroke;
      context.fillStyle = erd.settings.selectRectFill;
      var rect = normalizeRect(this.mouseInteraction.multiSelectPoints);
      context.rect(rect.x, rect.y, rect.w, rect.h);
      context.fill();
      context.stroke();
    }
  };

  // Normalize the multiselect points into a rectangle of (x,y,w,h)
  var normalizeRect = function(multiSelectPoints) {
    var rect = {};
    rect.x = Math.min(multiSelectPoints.x1, multiSelectPoints.x2);
    rect.y = Math.min(multiSelectPoints.y1, multiSelectPoints.y2);
    rect.w = Math.abs(multiSelectPoints.x1 - multiSelectPoints.x2);
    rect.h = Math.abs(multiSelectPoints.y1 - multiSelectPoints.y2);
    return rect;
  };

})();
