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

        var screen = $(window);
        $(".menu-obory > .strojirenstvi").click(function () {
            if (screen.width() > 1000) {
                $(".info").hide();
                $(".menu-obory > div").css({"background-color":"#e3e3e3"});
                $(".menu-obory > .search").css({"background-color":"#fff"});
                $(".menu-obory > div a").css({"color":"#333"});
                $(".info.strojirenstvi").show(500);
                $(this).css({"background-color":"#003052"});
                $(this).children("a").css({"color":"white"});
            }
        });

        $(".menu-obory > .informatika").click(function () {
            if (screen.width() > 1000) {
                $(".info").hide();
                $(".menu-obory > div").css({"background-color":"#e3e3e3"});
                $(".menu-obory > .search").css({"background-color":"#fff"});
                $(".menu-obory > div a").css({"color":"#333"});
                $(".info.informatika").show(500);
                $(this).css({"background-color":"#45c9e1"});
                $(this).children("a").css({"color":"white"});
            }
        });

        $(".info").click(function () {
             $(".info").hide();
             $(".menu-obory > div").css({"background-color":"#e3e3e3"});
             $(".menu-obory > .search").css({"background-color":"#fff"});
             $(".menu-obory > div a").css({"color":"#333"});
        });

        var increase = true;
        $(".frontpage-aktuality").click(function () {
             if (increase) {
                 $(".main-block").animate({width: "100%"}, 500);
                 $(".frontpage-sidebar").hide();
                 increase=false;
             } else {
                 $(".main-block").animate({width: "83.33333%"}, 500);
                 $(".frontpage-sidebar").show();
                 increase=true;
             }
        });

        $(".panel-search").hide();
        $(".search").click(function () {
            $(".panel-search").toggle(500);
        });

        $(".obor-informatika").prevAll(".informatika").css({"background-color":"#45c9e1"});

    });

})(jQuery);
