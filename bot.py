# -*- coding: utf-8 -*-
import logging
import os
from typing import List

from tock.bot import TockBot
from tock.bus import TockBotBus
from tock.intent import Intent
from tock.models import Sentence, Card, AttachmentType, Carousel
from tock.story import Story, story

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

# asyncio.get_event_loop().set_debug(True)

namespace = "tock-py-bot-demo"


class DemoBotBus(TockBotBus):

    @property
    def person(self) -> str:
        entity = self.context.entity("person")
        if entity:
            return entity.content


@story(
    intent="biography",
    other_starter_intents=["person"],
    secondary_intents=["birthdate"]
)
def culture(bus: DemoBotBus):
    def ask_person():
        bus.send(
            Sentence.Builder(f"Who do you want to see?")
                .add_suggestion("Mozart")
                .add_suggestion("Molière")
                .add_suggestion("Napoléon")
                .build()
        )

    def answer_birthdate():
        bus.send(
            Sentence.Builder(f"{bus.person} was born on a beautiful day")
                .add_suggestion("En savoir plus")
                .build()
        )

    def answer_biography():
        bus.send(
            Sentence.Builder(f"{bus.person} was a great person !!!")
                .add_suggestion("En savoir plus")
                .build()
        )

    person_undefined: bool = bus.person is None
    ask_birthdate: bool = bus.is_intent("birthdate")

    if person_undefined:
        ask_person()
    elif ask_birthdate:
        answer_birthdate()
    else:
        answer_biography()


class GreetingStory(Story):

    @staticmethod
    def intent() -> Intent:
        return Intent("greetings")

    @staticmethod
    def other_starter_intents() -> List[Intent]:
        return []

    @staticmethod
    def secondary_intents() -> List[Intent]:
        return []

    def answer(self, bus: DemoBotBus):
        bus.send(Sentence.Builder("Hello, I'm a tock-py bot").build())

        great_company_card = Card \
            .Builder() \
            .with_title("Great company") \
            .with_sub_title("with great people") \
            .with_attachment("https://www.sncf.com/themes/sncfcom/img/favicon.png", AttachmentType.IMAGE) \
            .add_action("great website", "http://www.sncf.com") \
            .build()
        bus.send(great_company_card)

        mozart_card = Card \
            .Builder() \
            .with_title("Mozart") \
            .with_attachment("https://cdn.radiofrance.fr/s3/cruiser-production/2018/07/7ad731a9-6d9d-421e-aaad-ecfe52895f50/838_gettyimages-113495083.jpg", AttachmentType.IMAGE) \
            .add_action("Qui est Mozart ?") \
            .build()

        napoleon_card = Card \
            .Builder() \
            .with_title("Napoléon") \
            .with_attachment("https://upload.wikimedia.org/wikipedia/commons/4/40/Francois_Gerard_-_Napoleon_Ier_en_costume_du_Sacre.jpg", AttachmentType.IMAGE) \
            .add_action("Qui est Napoléon ?") \
            .build()

        bus.send(
            Carousel
                .Builder()
                .add_card(mozart_card)
                .add_card(napoleon_card)
                .build()
        )


def goodbye(bus: DemoBotBus):
    bus.send("Goodbye")


def error(bus: DemoBotBus):
    bus.send(Sentence.Builder("Error StoryHander !!!!")
             .add_suggestion("Retry")
             .build())


bot: TockBot = TockBot() \
    .namespace(namespace) \
    .register_bus(DemoBotBus) \
    .register_story(GreetingStory) \
    .register_story(culture()) \
    .add_story('goodbye', goodbye) \
    .error_handler(error)
