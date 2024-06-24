# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Profit & Loss (US) / Balance sheet (US) MIS templates",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "author": "Binhex,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/account-financial-reporting",
    "category": "Localization",
    "depends": ["mis_template_financial_report"],
    "data": [
        "data/mis_report_style.xml",
        "data/mis_report.xml",
        "data/mis_report_kpi.xml",
        "data/mis_report_subreport.xml",
        "views/mis_report_instance_views.xml",
        "views/mis_report_kpi_views.xml",
        "views/templates.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "mis_template_financial_report/static/src/components/mis_report_widget.xml",
            "mis_template_financial_report/static/src/components/mis_report_widget.css",
        ],
        "web.report_assets_common": [
            "mis_template_financial_report/static/src/css/report.css"
        ],
    },
    "maintainers": ["Christian-RB"],
}
