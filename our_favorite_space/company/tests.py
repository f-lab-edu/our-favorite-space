from unittest.mock import Mock

from company.domain.company import Company
from company.ports.inbound_port import (
    CompanyCreateInboundPort,
    CompanyDeleteInboundPort,
    CompanyGetInfoInboundPort,
    CompanyModifyInboundPort,
)
from django.test import TestCase


class BaseCompanyInboundPortTest(TestCase):
    def setUp(self) -> None:
        self.save_company_port = Mock()
        self.load_company_port = Mock()
        self.delete_company_port = Mock()

        self.company = Company(id=1, name="test", email_domain="test.com")
        self.load_company_port.get.return_value = self.company
        self.save_company_port.save.return_value = self.company


class CompanyCreateInboundPortTestCase(BaseCompanyInboundPortTest):
    def test_create(self):
        inbound_port = CompanyCreateInboundPort(
            save_company_port=self.save_company_port
        )
        company = inbound_port.create("test", "test.com")

        self.assertEqual(company.name, "test")
        self.assertEqual(company.email_domain, "test.com")

    def test_create_with_invalid_email_domain(self):
        pass


class CompanyGetInfoInboundPortTestCase(BaseCompanyInboundPortTest):
    def test_get_info(self):
        inbound_port = CompanyGetInfoInboundPort(
            load_company_port=self.load_company_port
        )
        company = inbound_port.get_info(1)

        self.assertEqual(company.name, "test")
        self.assertEqual(company.email_domain, "test.com")


class CompanyModifyInboundPortTestCase(BaseCompanyInboundPortTest):
    def test_modify(self):
        inbound_port = CompanyModifyInboundPort(
            load_company_port=self.load_company_port,
            save_company_port=self.save_company_port,
        )
        company = inbound_port.modify(1, name="new_test")

        self.assertEqual(company.name, "new_test")
        self.assertEqual(company.email_domain, "test.com")

    def test_modify_with_invalid_data(self):
        pass


class CompanyDeleteInboundPortTestCase(BaseCompanyInboundPortTest):
    def test_delete(self):
        inbound_port = CompanyDeleteInboundPort(
            load_company_port=self.load_company_port,
            delete_company_port=self.delete_company_port,
        )
        inbound_port.delete(1)

        self.delete_company_port.delete.assert_called_once_with(1)
