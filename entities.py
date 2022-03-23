from datetime import datetime
from typing import Optional

import notification

ENTITY_TYPES = [
    "Event",
    "Company",
    "Webinar",
    "ContentItem",
    "CompanyForEvent",
    "CompanyForWebinar",
    "CompanyCompetitor"
]


class CRAWLING_STATUSES:
    NOT_CRAWLED = 0
    ERROR_REQUESTING_LINK = 1
    UPDATING_LINK = 2
    MARKED_AS_DUPLICATE = 3
    UPDATED_LINK = 4
    CRAWLING = 5
    CRAWLING_FAILED = 6
    RESCHEDULED_LONG_CRAWLING = 7
    CRAWLING_TOO_LONG = 8
    HAS_NO_PAGES = 9
    TEXT_UPLOADED = 10
    AWAITING_CRAWL = 11
    INDEXED_BY_ELASTIC = 12
    TEXT_ANALYZED = 13
    DOMAIN_INVALID = 14
    NO_LINKS_IN_PAGE = 15
    UNCRAWLABLE = 16


class CrawlableEntity(notification.Notifiable):
    link: str
    name: str
    crawling_status: int # from CRAWLING_STATUSES
    is_deleted: bool
    is_blacklisted: bool
    last_crawled: Optional[datetime]

    def __init__(self, *, link, name, crawling_status=CRAWLING_STATUSES.NOT_CRAWLED, is_deleted=False, is_blacklisted=False, last_crawled=None):
        self.link = link
        self.name = name
        self.crawling_status = crawling_status
        self.is_blacklisted = is_blacklisted
        self.is_deleted = is_deleted
        self.last_crawled = last_crawled

    def __str__(self):
        return self.name


class Event(CrawlableEntity):
    start_date: datetime
    end_date: Optional[datetime]
    description: Optional[str]
    location: Optional[str]

    def __init__(self, *, start_date, description=None, location=None, end_date=None, **kwargs):
        super().__init__(**kwargs)
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.location = location


class Webinar(CrawlableEntity):
    start_date: datetime
    description: Optional[str]
    language: str

    def __init__(self, *, start_date, description=None, language="en", **kwargs):
        super().__init__(**kwargs)
        self.start_date = start_date
        self.description = description
        self.language = language


class Company(CrawlableEntity):
    employees_min: int
    employees_max: int

    def __init__(self, *, employees_min, employees_max, **kwargs):
        super().__init__(**kwargs)
        self.employees_min = employees_min
        self.employees_max = employees_max


class ContentItem(CrawlableEntity):
    snippet: Optional[str]
    company: Company

    def __init__(self, *, company, snippet=None, **kwargs):
        super().__init__(**kwargs)
        self.company = company
        self.snippet = snippet


class CompanyForEvent(notification.Notifiable):
    event: Event
    company: Company
    is_deleted: bool
    is_blacklisted: bool

    def __init__(self, *, event, company, is_deleted=False, is_blacklisted=False):
        self.event = event
        self.company = company
        self.is_blacklisted = is_blacklisted
        self.is_deleted = is_deleted
        

class CompanyForWebinar(notification.Notifiable):
    webinar: Webinar
    company: Company
    is_deleted: bool
    is_blacklisted: bool

    def __init__(self, *, webinar, company, is_deleted=False, is_blacklisted=False):
        self.webinar = webinar
        self.company = company
        self.is_blacklisted = is_blacklisted
        self.is_deleted = is_deleted


class CompanyCompetitor(notification.Notifiable):
    company: Company
    competitor: Company
    is_deleted: bool

    def __init__(self, *, company, competitor, is_deleted=False):
        self.company = company
        self.competitor = competitor
        self.is_deleted = is_deleted
