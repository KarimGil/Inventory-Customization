odoo.define('inventory_customization.Session', function (require) {
    'use strict';

    var Session = require('web.Session');
    var ajax = require('web.ajax');
    var concurrency = require('web.concurrency');
    var core = require('web.core');
    var local_storage = require('web.local_storage');
    var mixins = require('web.mixins');
    var utils = require('web.utils');

    var _t = core._t;
    var qweb = core.qweb;

    Session.include({
        setCompanies: function (main_company_id, company_ids) {
            var hash = $.bbq.getState()
            hash.cids = company_ids.sort(function(a, b) {
                if (a === main_company_id) {
                    return -1;
                } else if (b === main_company_id) {
                    return 1;
                } else {
                    return a - b;
                }
            }).join(',');
            utils.set_cookie('cids', hash.cids || String(main_company_id));
            $.bbq.pushState({'cids': hash.cids}, 0);
            $.ajax({
                url: '/translate_lang',
                type: 'POST',
                data: {'main_company_id': main_company_id},
                success: function(response) {
                    console.log('Python function called successfully');
                    location.reload();
                },
                error: function(xhr, status, error) {
                    console.error('Error calling Python function:', error);
                    location.reload();
                }
            });
        }
    });
});
