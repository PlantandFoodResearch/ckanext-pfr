// Enable JavaScript's strict mode. Strict mode catches some common
// programming errors and throws exceptions, prevents some unsafe actions from
// being taken, and disables some confusing and bad JavaScript features.
"use strict";

console.log('loading pfr_popover.js', this.ckan.module)
this.ckan.module('pfr_popover', function (jQuery) {
  return {
    initialize: function () {
      console.log("PFR_popover initialized for element: ", this.el);
    }
  };
});