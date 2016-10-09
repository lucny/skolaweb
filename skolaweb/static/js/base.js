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

        $("#search-close").hide();
        $(".aldryn-newsblog-article-search").hide();

        $("#search-open").click(function () {
           $(".aldryn-newsblog-article-search").show();
           $("#main").attr("class","col-xs-8");
           $("#sidebar").attr("class","col-xs-4");
           $(".menu-obory").hide();
           $(this).hide();
            $("#search-close").show();
        });

/*        $("#main").click(function () {
           $("#main").attr("class","col-sm-10 col-xs-11");
           $("#sidebar").attr("class","col-sm-2 col-xs-1");
           $(".menu-obory").show();
        });*/

        $(".aldryn-newsblog-article-search .form-inline").submit(function(e){
            $("#search-close").show();
        });

        $("#search-close").click(function () {
           $("#main").attr("class","col-sm-10 col-xs-10");
           $("#sidebar").attr("class","col-sm-2 col-xs-2");
           $(".menu-obory").show();
           $(".search-results").html("");
           $(this).hide();
           $("#search-open").show();
           $(".aldryn-newsblog-article-search").hide();
        });

    })
})(jQuery);
