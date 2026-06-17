from .flow_controller import FlowController

from .character_model import CharacterModel
from .character_service import CharacterService
from .character_validator import CharacterValidator

from .image_loader import ImageLoader


class EditorContext:

    def __init__(self, steps, assets_path):

        # Flow
        self.flow = FlowController(
            steps
        )

        # Character
        self.model = CharacterModel()

        self.service = CharacterService(
            self.model
        )

        self.validator = CharacterValidator(
            self.model
        )

        # Assets
        self.image_loader = ImageLoader(
            assets_path
        )