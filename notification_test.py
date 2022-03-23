from datetime import datetime

import entities
import notification

if __name__ == "__main__":
    company = entities.Company.create(name="ABC Inc", link="http://abc.com", employees_min=1, employees_max=200)
    
    company.update(crawling_status=entities.CRAWLING_STATUSES.TEXT_ANALYZED)
    assert company.crawling_status == entities.CRAWLING_STATUSES.TEXT_ANALYZED
    
    company.update(is_deleted=True)
    assert company.is_deleted
    
    company.delete()

    event = entities.Event.create(name="Event 1", link="http://event1.com", start_date=datetime.now(), description="Event 1 description", location="Event 1 location")

    event.update(is_blacklisted=True)
    assert event.is_blacklisted

    webinar = entities.Webinar.create(name="Webinar 1", link="http://webinar1.com", start_date=datetime.now(), description="Webinar 1 description", language="en")

    webinar.delete()

    content_item = entities.ContentItem.create(name="Content Item 1", link="http://content1.com", snippet="Content Item 1 snippet", company=company)
    content_item.update(crawling_status=entities.CRAWLING_STATUSES.TEXT_ANALYZED)
    assert content_item.crawling_status == entities.CRAWLING_STATUSES.TEXT_ANALYZED

