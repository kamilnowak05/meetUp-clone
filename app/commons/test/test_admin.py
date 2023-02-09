from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class AdminSiteTest(TestCase):
    def setUp(self):
        self.Client = Client()
        self.admin_user = get_user_model().objects.create_superuser(email="test@test.com", password="Testpass123")

        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="test1@test.com", password="pass123", first_name="Test Name", last_name="Test Last Name"
        )

    # def test_users_listed(self):
    #     """Test that users are listed on user page"""
    #     url = reverse('admin:core_user_changelist')
    #     res = self.client.get(url)

    #     self.assertContains(res, self.user.first_name)
    #     self.assertContains(res, self.user.last_name)
    #     self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse("admin:core_user_change", args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse("admin:core_user_add")
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
