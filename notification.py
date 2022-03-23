import functools
from copy import copy
from typing import List, Dict, Callable

HANDLERS: Dict[str, List[Callable]] = {}
INTERESTING_STATUSES: List[int] = [10, 13]


def notify_console(message: str, *args, **kwargs) -> None:
    print(f"Notify on {message}")


def handle(entity_type: str, *args, **kwargs) -> None:
    for handler in HANDLERS.get(entity_type, []):
        handler(notify_console, entity_type, *args, **kwargs)


def handler(entity_type: str) -> Callable:
    @functools.wraps(entity_type)
    def wrapper(func) -> Callable:
        HANDLERS.setdefault(entity_type, []).append(func)
        return func
    return wrapper

class Notifiable:
    def handle(self, entity_obj=None, original_entity_obj=None):
        handle(self.__class__.__name__, entity_obj=entity_obj, original_entity_obj=original_entity_obj)

    @classmethod
    def create(cls, *args, **kwargs):
        obj = cls(*args, **kwargs)
        obj.handle(entity_obj=obj, original_entity_obj=None)
        return obj

    def update(self, **kwargs):
        original_entity_obj = copy(self)
        self.__dict__.update(**kwargs)
        self.handle(entity_obj=self, original_entity_obj=original_entity_obj)
    
    def delete(self):
        self.handle(entity_obj=None, original_entity_obj=self)


## HANDLERS

### Company

@handler("Company")
def on_company_created(notify, entity_type, entity_obj=None, original_entity_obj=None):
    if entity_obj is not None and original_entity_obj is None:
        notify(f"Company '{entity_obj}' created")


@handler("Company")
def on_company_updated(notify, entity_type, entity_obj=None, original_entity_obj=None):
    if entity_obj is not None and original_entity_obj is not None:
        if entity_obj.crawling_status != original_entity_obj.crawling_status and entity_obj.crawling_status in INTERESTING_STATUSES:
            notify(f"Company '{entity_obj}' crawling status changed")
        if entity_obj.is_deleted != original_entity_obj.is_deleted:
            notify(f"Company '{entity_obj}' is_deleted changed")


@handler("Company")
def on_company_deleted(notify, entity_type, entity_obj=None, original_entity_obj=None):
    if entity_obj is None and original_entity_obj is not None:
        notify(f"Company {original_entity_obj} deleted")


### Event

@handler("Event")
def on_event_created(notify, entity_type, entity_obj=None, original_entity_obj=None):
    if entity_obj is not None and original_entity_obj is None:
        notify(f"Event '{entity_obj}' created")


@handler("Event")
def on_event_updated(notify, entity_type, entity_obj=None, original_entity_obj=None):
    if entity_obj is not None and original_entity_obj is not None:
        if entity_obj.crawling_status != original_entity_obj.crawling_status and entity_obj.crawling_status in INTERESTING_STATUSES:
            notify(f"Event '{entity_obj}' crawling status changed")
        if entity_obj.is_deleted != original_entity_obj.is_deleted:
            notify(f"Event '{entity_obj}' is_deleted changed")
        if entity_obj.is_blacklisted != original_entity_obj.is_blacklisted:
            notify(f"Event '{entity_obj}' is_blacklisted changed")


@handler("Event")
def on_event_deleted(notify, entity_type, entity_obj=None, original_entity_obj=None):
    if entity_obj is None and original_entity_obj is not None:
        notify(f"Event {original_entity_obj} deleted")


### Webinar

@handler("Webinar")
def on_webinar_created(notify, entity_type, entity_obj=None, original_entity_obj=None):
    if entity_obj is not None and original_entity_obj is None:
        notify(f"Webinar '{entity_obj}' created")


@handler("Webinar")
def on_webinar_updated(notify, entity_type, entity_obj=None, original_entity_obj=None):
    if entity_obj is not None and original_entity_obj is not None:
        if entity_obj.crawling_status != original_entity_obj.crawling_status and entity_obj.crawling_status in INTERESTING_STATUSES:
            notify(f"Webinar '{entity_obj}' crawling status changed")
        if entity_obj.is_deleted != original_entity_obj.is_deleted:
            notify(f"Webinar '{entity_obj}' is_deleted changed")
        if entity_obj.is_blacklisted != original_entity_obj.is_blacklisted:
            notify(f"Webinar '{entity_obj}' is_blacklisted changed")


@handler("Webinar")
def on_webinar_deleted(notify, entity_type, entity_obj=None, original_entity_obj=None):
    if entity_obj is None and original_entity_obj is not None:
        notify(f"Webinar {original_entity_obj} deleted")


### ContentItem

@handler("ContentItem")
def on_content_item_created(notify, entity_type, entity_obj=None, original_entity_obj=None):
    if entity_obj is not None and original_entity_obj is None:
        notify(f"Company '{entity_obj.company}'")


@handler("ContentItem")
def on_content_item_updated(notify, entity_type, entity_obj=None, original_entity_obj=None):
    if entity_obj is not None and original_entity_obj is not None:
        if entity_obj.crawling_status != original_entity_obj.crawling_status and entity_obj.crawling_status in INTERESTING_STATUSES:
            notify(f"Company '{entity_obj.company}' crawling status changed")
        if entity_obj.is_deleted != original_entity_obj.is_deleted:
            notify(f"Company '{entity_obj.company}' is_deleted changed")
        if entity_obj.is_blacklisted != original_entity_obj.is_blacklisted:
            notify(f"Company '{entity_obj.company}' is_blacklisted changed")


@handler("ContentItem")
def on_content_item_deleted(notify, entity_type, entity_obj=None, original_entity_obj=None):
    if entity_obj is None and original_entity_obj is not None:
        notify(f"Company '{original_entity_obj.company}' deleted")


### CompanyForEvent

@handler("CompanyForEvent")
def on_company_for_event_created(notify, entity_type, entity_obj=None, original_entity_obj=None):
    if entity_obj is not None and original_entity_obj is None:
        notify(f"Company '{entity_obj.company}' for event '{entity_obj.event}' created")


@handler("CompanyForEvent")
def on_company_for_event_updated(notify, entity_type, entity_obj=None, original_entity_obj=None):
    if entity_obj is not None and original_entity_obj is not None:
        if entity_obj.is_deleted != original_entity_obj.is_deleted:
            notify(f"Company '{entity_obj.company}' for event '{entity_obj.event}' is_deleted changed")
        if entity_obj.is_blacklisted != original_entity_obj.is_blacklisted:
            notify(f"Company '{entity_obj.company}' for event '{entity_obj.event}' is_blacklisted changed")


@handler("CompanyForEvent")
def on_company_for_event_deleted(notify, entity_type, entity_obj=None, original_entity_obj=None):
    if entity_obj is None and original_entity_obj is not None:
        notify(f"Company '{original_entity_obj.company}' for event '{original_entity_obj.event}' deleted")


### CompanyForWebinar

@handler("CompanyForWebinar")
def on_company_for_webinar_created(notify, entity_type, entity_obj=None, original_entity_obj=None):
    if entity_obj is not None and original_entity_obj is None:
        notify(f"Company '{entity_obj.company}' for webinar '{entity_obj.webinar}' created")


@handler("CompanyForWebinar")
def on_company_for_webinar_updated(notify, entity_type, entity_obj=None, original_entity_obj=None):
    if entity_obj is not None and original_entity_obj is not None:
        if entity_obj.is_deleted != original_entity_obj.is_deleted:
            notify(f"Company '{entity_obj.company}' for webinar '{entity_obj.webinar}' is_deleted changed")
        if entity_obj.is_blacklisted != original_entity_obj.is_blacklisted:
            notify(f"Company '{entity_obj.company}' for webinar '{entity_obj.webinar}' is_blacklisted changed")


@handler("CompanyForWebinar")
def on_company_for_webinar_deleted(notify, entity_type, entity_obj=None, original_entity_obj=None):
    if entity_obj is None and original_entity_obj is not None:
        notify(f"Company '{original_entity_obj.company}' for webinar '{original_entity_obj.webinar}' deleted")


### CompanyCompetitor

@handler("CompanyCompetitor")
def on_company_competitor_created(notify, entity_type, entity_obj=None, original_entity_obj=None):
    if entity_obj is not None and original_entity_obj is None:
        notify(f"Company '{entity_obj.company}' competitor '{entity_obj.competitor}' created")


@handler("CompanyCompetitor")
def on_company_competitor_updated(notify, entity_type, entity_obj=None, original_entity_obj=None):
    if entity_obj is not None and original_entity_obj is not None:
        if entity_obj.is_deleted != original_entity_obj.is_deleted:
            notify(f"Company '{entity_obj.company}' competitor '{entity_obj.competitor}' is_deleted changed")
        if entity_obj.is_blacklisted != original_entity_obj.is_blacklisted:
            notify(f"Company '{entity_obj.company}' competitor '{entity_obj.competitor}' is_blacklisted changed")


@handler("CompanyCompetitor")
def on_company_competitor_deleted(notify, entity_type, entity_obj=None, original_entity_obj=None):
    if entity_obj is None and original_entity_obj is not None:
        notify(f"Company '{original_entity_obj.company}' competitor '{original_entity_obj.competitor}' deleted")
