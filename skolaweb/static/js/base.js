/*
 * Copyright (c) 2013, Divio AG
 * Licensed under BSD
 * http://github.com/aldryn/aldryn-boilerplate-bootstrap3
 */

// #############################################################################
// NAMESPACES
/**
 * @module Cl
 */
// istanbul ignore next
var Cl = window.Cl || {};
/* global outdatedBrowser */


function getStyleObject(stobj){
        var dom = stobj.get(0);
        var style;
        var returns = {};
        if(window.getComputedStyle){
            var camelize = function(a,b){
                return b.toUpperCase();
            };
            style = window.getComputedStyle(dom, null);
            for(var i = 0, l = style.length; i < l; i++){
                var prop = style[i];
                var camel = prop.replace(/\-([a-z])/g, camelize);
                var val = style.getPropertyValue(prop);
                returns[camel] = val;
            };
            return returns;
        };
        if(style = dom.currentStyle){
            for(var prop in style){
                returns[prop] = style[prop];
            };
            return returns;
        };
        return stobj.css();
}

// #############################################################################
// BASE
// istanbul ignore next
(function ($) {
    'use strict';

    // shorthand for invoking jQuery(document).ready
    $(function () {
        // removes noscript form body and adds print-js
        if (window.Cl && window.Cl.Utils) {
            Cl.Utils._document();
        }

        // DOCS: https://github.com/burocratik/outdated-browser
        if (window.outdatedBrowser) {
            outdatedBrowser({
                'languagePath': '',
                'lowerThan': 'boxShadow'
            });
        }


        $("#search-result").bind("DOMSubtreeModified",function(){
            $(this).hide();
            $("#search-dialog-body").html($("#search-result").html());
        });

        $("#obory-btn").click(function(){
            $("#obory-menu").toggle(500);
 		});

        var categoryarticles = $(".category-article");
        console.log(categoryarticles[2]);
        if (categoryarticles.length > 0) {
            for (var i=2; i<categoryarticles.length; i++) {
                categoryarticles[i].hidden=true;
            }
        }

         $('.vertical').find('.slider').bxSlider({
             mode: 'vertical',
             slideWidth: 800,
             minSlides: 2,
             slideMargin: 20,
             speed: 1000,
             pagerType: 'short'
            // auto:true
        });

         $('.horizontal').find('.slider').bxSlider({
             mode: 'horizontal',
             slideWidth: 800,
             minSlides: 1,
             slideMargin: 100,
             speed: 1000,
             pagerType: 'short'
            // auto:true
        });

    })
})(jQuery);
