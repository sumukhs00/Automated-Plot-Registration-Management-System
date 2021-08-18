/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  erd.UndoManager = function(stage) {
    this.undoStack = [];
    this.redoStack = [];
    this.stage = stage;
    this.archiver = new erd.DiagramArchive(this.stage);
    this.currentAction = null;
  };

  erd.UndoManager.prototype.clear = function() {
    this.undoStack = [];
    this.redoStack = [];
  };

  erd.UndoManager.prototype.hasCurrentAction = function() {
    return this.currentAction !== null;
  };

  erd.UndoManager.prototype.startAction = function() {
    this.stage.invokeDirtyCallback();
    if (this.currentAction === null) {
      this.currentAction = {
        undoContent: this.archiver.toJson(),
        redoContent: null
      };
    }
  };

  erd.UndoManager.prototype.endAction = function() {

    if (this.currentAction !== null) {
      this.undoStack.push(this.currentAction);
      this.currentAction = null;
      this.redoStack = [];
    }
    this.stage.invokeDirtyCallback();
  };

  erd.UndoManager.prototype.canUndo = function() {
    return this.undoStack.length > 0;
  };

  erd.UndoManager.prototype.canRedo = function() {
    return this.redoStack.length > 0;
  };

  erd.UndoManager.prototype.undo = function() {
    if (this.canUndo()) {
      var action = this.undoStack.pop();
      if (action.redoContent === null) {
        action.redoContent = this.archiver.toJson();
      }
      this.archiver.fromJson(action.undoContent);
      this.stage.draw();
      this.redoStack.push(action);
      this.stage.invokeDirtyCallback();
    }
  };

  erd.UndoManager.prototype.redo = function() {
    if (this.canRedo()) {
      var action = this.redoStack.pop();
      this.archiver.fromJson(action.redoContent);
      this.stage.draw();
      this.undoStack.push(action);
      this.stage.invokeDirtyCallback();
    }
  };

})();
