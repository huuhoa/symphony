from .etr import Extractor, Transformer
from .etr_fsblog import FsblogExtractor
from .etr_increment import IncrementDotComExtractor
from .etr_medium import MediumExtractor, MediumTransformer
from .etr_morning import TheMorningPaperExtractor
from .etr_slack_engineering import SlackEngineeringExtractor
from .etr_unintendedconsequences import UnintendedConsequencesExtractor
from .etr_untools import UntoolsExtractor


def create_extractor(url_path, bs):
    if 'untools.co' in url_path:
        return UntoolsExtractor(bs)
    if 'unintendedconsequenc' in url_path:
        return UnintendedConsequencesExtractor(bs)
    if 'blog.acolyer.org' in url_path:
        return TheMorningPaperExtractor(bs)
    if '://fs.blog' in url_path:
        return FsblogExtractor(bs)
    if '://increment.com' in url_path:
        return IncrementDotComExtractor(bs)
    if '//slack.engineering' in url_path:
        return SlackEngineeringExtractor(bs)
    if '//medium.com' in url_path:
        return MediumExtractor(bs)
    return Extractor(bs)


def create_transformer(url_path, bs, content, root):
    config = {
        "src_url": url_path,
        "output_dir": root
    }
    if 'untools.co' in url_path:
        return Transformer(config, bs, content)
    if 'unintendedconsequenc' in url_path:
        return Transformer(config, bs, content)
    if 'blog.acolyer.org' in url_path:
        return Transformer(config, bs, content)
    if '//medium.com' in url_path:
        return MediumTransformer(config, bs, content)
    return Transformer(config, bs, content)