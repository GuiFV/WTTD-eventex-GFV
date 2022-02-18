from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    # def setUp(self):
    #     self.form = SubscriptionForm()

    def test_form_has_fields(self):
        """Form must have 4 fields"""
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        #self.assertSequenceEqual(expected, list(self.form.fields))
        self.assertSequenceEqual(expected, list(form.fields))

    # def test_cpf_is_digit(self):
    #     """CPF must only accept digits"""
    #     #12345678910 ABDC5678910
    #     data = dict(name='Guilherme Viotti', cpf='ABCD5678910',
    #                 email='guilherme@viotti.com', phone='21-99999-4444')
    #     form = SubscriptionForm(data)
    #     form.is_valid()
    #
    #     self.assertListEqual(['cpf'], list(form.errors))
    #
    #
    # def test_cpf_has_11_digits(self):
    #     """CPF must have 11 digits"""
    #     # 12345678910 1234
    #     data = dict(name='Guilherme Viotti', cpf='1234',
    #                 email='guilherme@viotti.com', phone='21-99999-4444')
    #     form = SubscriptionForm(data)
    #
    #     form.is_valid()
    #     self.assertListEqual(['cpf'], list(form.errors))


    def test_cpf_is_digit(self):
        """CPF must only accept digits"""
        #12345678910 ABDC5678910
        form = self.make_validated_form(cpf='ABCD5678910')
        #self.assertListEqual(['cpf'], list(form.errors))
        self.assertFormErrorMessage(form, 'cpf', 'CPF deve conter apenas números')


    def test_cpf_has_11_digits(self):
        """CPF must have 11 digits"""
        # 12345678910 1234
        form = self.make_validated_form(cpf='1234')
        #self.assertListEqual(['cpf'], list(form.errors))

            # errors = form.errors
            # errors_list = errors['cpf']
            # msg = 'CPF deve ter 11 números'
            # self.assertListEqual([msg], errors_list)

        self.assertFormErrorMessage(form, 'cpf', 'CPF deve ter 11 números')

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors['cpf']
        self.assertListEqual([msg], errors_list)

    def make_validated_form(self, **kwargs):
        valid = dict(name='Guilherme Viotti', cpf='12345678910',
                    email='guilherme@viotti.com', phone='21-99999-4444')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form

