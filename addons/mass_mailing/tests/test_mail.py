# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp.addons.mail.tests.common import TestMail


class test_message_compose(TestMail):

    def test_OO_mail_mail_tracking(self):
        """ Tests designed for mail_mail tracking (opened, replied, bounced) """
        mail = self.env['mail.mail'].create({
            'subject': 'Test Tracking',
            'body_html': '<p>Hello <a href="http://www.example.com">Link</a></p>',
            'email_to': 'user@example.com',
        })
        self.assertTrue(mail)
        self.assertEqual(mail.state, 'outgoing')
        
        # Test tracking URL generation
        tracking_url = mail._get_tracking_url(self.cr, self.uid, mail)
        self.assertIn('mail/track/', tracking_url)
        
        # Test body with tracking & base tag
        body = mail.send_get_mail_body(self.cr, self.uid, [mail.id])
        self.assertIn('base href', body)
