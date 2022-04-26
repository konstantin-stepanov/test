from datetime import datetime
from typing import List, Optional
from math import ceil

class Guest:
    def init(self, first_name, last_name, degree, role):
        assert degree in [0, 1, 2, 3, -1]
        self.first_name = first_name
        self.last_name = last_name
        self.degree = degree
        self.role = role

    def print_title(self):
        if self.degree == 0:
            return "Студент"
        if self.degree == 1:
            return "Кандидат физмат наук"
        elif self.degree == 2:
            return "Доктор физмат наук"
        elif self.degree == 3:
            return "Профессор, член-кор."
        else:
            return ""
# -----------------------------------------------------------
def format_event_members(event_name: str,
                         event_date: datetime,
                         guests: List = [],
                         page_size: Optional[int] = None) -> List[str]:
    """
    Renders guest list into a printable pages according to rules
    :param event_name: Event name
    :param event_date: Event date
    :param guests: list of guests
    :param staff: list of staff
    :param max_lines: amount of guests to be printed
    :return:
    """
    pages = []
    header = f"Event: {event_name}\nDate: {event_date}\nPage: %s/%s\n\n"
    total_guests = len(guests)

    if page_size == None:
        total_pages = 1
    else:
        total_pages = ceil(total_guests / page_size)

    current_page_id = 1
    current_page = header % (current_page_id, total_pages)
    flushed = True

    for i in range(total_guests):
        current_page += f"{i + 1}. {guests[i].print_title()} {guests[i].first_name}" + \
                        f" {guests[i].last_name}: {guests[i].role}\n"
        flushed = False

        if page_size != lNone and (i+1) % page_size == 0:
            pages.append(current_page)
            current_page_id += 1
            current_page = header % (current_page_id, total_pages)
            flushed = True

    if not flushed:
        pages.append(current_page)

    return pages
