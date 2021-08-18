/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  erd.utils = {};

  var defaultFillTextOptions = {
    x: 0,
    y: 0,
    maxWidth: undefined,
    underline: false,
    dottedUnderline: false,
    textAlign: 'left',
    textBaseline: 'middle',
    font: erd.settings.font,
    fillStyle: erd.settings.fontColor
  };

  var defaultWrapTextOptions = {
    x: 0,
    y: 0,
    width: 100,
    height: 100,
    font: erd.settings.font,
    fillStyle: erd.settings.fontColor
  };

  /**
   * see defaultFillTextOptions.
   */
  erd.utils.fillText = function(context, text, options) {
    if (options === undefined) {
      options = {};
    }
    _.defaults(options, defaultFillTextOptions);

    context.save();
    context.font = options.font;
    context.fillStyle = options.fillStyle;
    context.textAlign = options.textAlign;
    context.textBaseline = options.textBaseline;
    if (typeof options.maxWidth === 'number') {
      context.fillText(text, options.x, options.y, options.maxWidth);
    } else {
      context.fillText(text, options.x, options.y);
    }
    var textMetrics = context.measureText(text);
    if (options.underline) {
      var width = Math.min(textMetrics.width, options.maxWidth);
      var ux, uy;
      if (options.textAlign === 'center') {
        ux = options.x - width / 2;
        uy = options.y + 5.5;
      } else if (options.textAlign === 'left') {
        ux = options.x;
        uy = options.y + 5.5;
      }

      context.beginPath();
      if (options.dottedUnderline) {
        context.setLineDash(erd.settings.dashArray);
      } else {
        context.setLineDash([]);
      }
      context.lineWidth = erd.settings.strokeWidth;
      context.strokeStyle = erd.settings.stroke;
      context.moveTo(ux, uy);
      context.lineTo(ux + width, uy);
      context.stroke();
    }
    context.restore();

    return textMetrics;
  };

  /**
   * see defaultWrapTextOptions
   */
  erd.utils.wrapText = function(context, text, options) {
    if (options === undefined) {
      options = {};
    }
    _.defaults(options, defaultWrapTextOptions);

    context.save();
    context.font = options.font;
    context.fillStyle = options.fillStyle;
    context.textAlign = options.textAlign;
    context.textBaseline = options.textBaseline;

    var lineHeight = parseInt(options.font) + 2;
    var lines = erd.utils._fragmentText(context, text, options.width);
    var y = options.y;

    if (options.textAlign === 'center' && options.textBaseline === 'middle') {
      if (lines.length > 0) {
        // Adjust y
        var extraHeight = lineHeight * (lines.length - 1);
        y -= extraHeight / 2;
      }
    }

    for (var i = 0; i < lines.length; ++i) {
      var line = lines[i];
      var lineOptions = {
        x: options.x,
        y: y,
        dottedUnderline: options.dottedUnderline,
        underline: options.underline,
        textAlign: options.textAlign,
        textBaseline: options.textBaseline,
        maxWidth: options.maxWidth
      };
      erd.utils.fillText(context, line, lineOptions);
      y += lineHeight;
      if (options.height - y < lineHeight) {
        break;
      }
    }

    context.restore();
  };

  /**
   * Fragment the text for multiline display.
   */
  erd.utils._fragmentText = function(context, text, maxWidth) {
    var words = text.split(' ');
    var lines = [];
    var line = '';
    if (context.measureText(text).width < maxWidth) {
      return [text];
    }
    while (words.length > 0) {
      while (context.measureText(words[0]).width >= maxWidth) {
        var tmp = words[0];
        words[0] = tmp.slice(0, -1);
        if (words.length > 1) {
            words[1] = tmp.slice(-1) + words[1];
        } else {
            words.push(tmp.slice(-1));
        }
      }
      if (context.measureText(line + words[0]).width < maxWidth) {
        line += words.shift() + ' ';
      } else {
        lines.push(line);
        line = '';
      }
      if (words.length === 0) {
        lines.push(line);
      }
    }
    return lines;
  };

  erd.utils.distance = function(pt1, pt2) {
    var dx = (pt2.x - pt1.x) * (pt2.x - pt1.x);
    var dy = (pt2.y - pt1.y) * (pt2.y - pt1.y);
    return Math.sqrt(dx + dy);
  };

  erd.utils.rectContainsPoint = function(rect, x, y) {
    return (rect.x < x &&
            rect.y < y &&
            rect.x + rect.w > x &&
            rect.y + rect.h > y);
  };

  erd.utils.combineBounds = function(bounds1, bounds2) {
    return {
      left: Math.min(bounds1.left, bounds2.left),
      top: Math.min(bounds1.top, bounds2.top),
      right: Math.max(bounds1.right, bounds2.right),
      bottom: Math.max(bounds1.bottom, bounds2.bottom)
    };
  };

  // Rotates pt angle radians around another point given by origin
  erd.utils.rotate = function(pt, origin, angle) {
    var newX = origin.x + (pt.x-origin.x)*Math.cos(angle) - (pt.y-origin.y)*Math.sin(angle);
    var newY = origin.y + (pt.x-origin.x)*Math.sin(angle) + (pt.y-origin.y)*Math.cos(angle);
    return {
      x: newX,
      y: newY
    };
  };

})();
