from django.urls import reverse, reverse_lazy
from django.test import TestCase, Client
from task_manager.users.models import CustomUser
from .models import Labels


class LabelsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.label_data = {
            "name": "label test",
        }
        self.user = CustomUser.objects.create(
            username="test1", password="test1")
        self.client.force_login(self.user)
        self.label = Labels.objects.create(name="test")

    def test_create_label(self):
        response = self.client.post(
            reverse_lazy("create_label"),
            self.label_data
        )
        self.assertEqual(response.status_code, 302)
        labels = Labels.objects.get(name=self.label_data["name"])
        self.assertEqual(labels.name, self.label_data["name"])
        self.assertRedirects(response, reverse_lazy("labels"))

    def test_label_update(self):
        url = reverse("update_label", kwargs={"pk": self.label.pk})
        response = self.client.post(url, self.label_data)
        update_label = Labels.objects.get(pk=self.label.pk)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(update_label.name, self.label_data["name"])
        self.assertRedirects(response, reverse_lazy("labels"))
