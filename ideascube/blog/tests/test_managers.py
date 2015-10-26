import pytest

from ..models import Content

pytestmark = pytest.mark.django_db


def test_published_should_return_only_published(published, draft, deleted,
                                                published_in_the_future):
    contents = Content.objects.published()
    assert published in contents
    assert draft not in contents
    assert deleted not in contents
    assert published_in_the_future not in contents


def test_draft_should_return_only_draft(published, draft, deleted,
                                        published_in_the_future):
    contents = Content.objects.draft()
    assert draft in contents
    assert published not in contents
    assert deleted not in contents
    assert published_in_the_future not in contents


def test_deleted_should_return_only_deleted(published, draft, deleted,
                                            published_in_the_future):
    contents = Content.objects.deleted()
    assert deleted in contents
    assert published not in contents
    assert draft not in contents
    assert published_in_the_future not in contents


def test_objects_should_return_all_content(published, draft, deleted,
                                           published_in_the_future):
    contents = Content.objects.all()
    assert deleted in contents
    assert published in contents
    assert draft in contents
    assert published_in_the_future in contents
