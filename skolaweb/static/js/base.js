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


        $(".ucitel-detail").hide();
        $(".ucitel-jmeno").click(function(){
            var bgcolor = $(this).css("background-color");
            var color = $(this).css("color");
            $(this).css({"background-color": color});
            $(this).css({"color": bgcolor});
            $(this).siblings(".ucitel-detail").toggle(500);
        });

        $(".info").hide();
        $(".menu-obory-down").hide();

        $(".menu-obory").mouseenter(function(){
            var screen = $(window);
            if (screen.width() > 1000) {
                $(".menu-obory-down").show(200);
            }
        });

        $(".menu-obory-down > div").mouseenter(function(){
            $(this).css({"opacity":0.5});
        });

        $(".menu-obory-down > div").mouseleave(function(){
            $(this).css({"opacity":1});
        });

        $(".menu-obory-down > .strojirenstvi").click(function(){
            $(".info").hide();
			$(".info.strojirenstvi").show(500);
        });

        $(".menu-obory-down > .informatika").click(function(){
            $(".info").hide();
			$(".info.informatika").show(500);
        });

        $(".info").click(function(){
            $(".info").hide();
            $(".menu-obory-down").hide();
        });

    });

})(jQuery);
