import shutil
import logging
from pathlib import Path
from .database import get_concepts_table

logger = logging.getLogger(__name__)

class VaultManager:
    """Manages the physical Obsidian vault and index synchronization."""
    
    def __init__(self, base_path: Path = Path("vault/Concepts")):
        self.base_path = base_path

    def get_existing_folders(self) -> list[str]:
        """Returns a list of existing relative folder paths in the vault."""
        if not self.base_path.exists():
            return []
        
        folders = [
            str(p.relative_to(self.base_path)) 
            for p in self.base_path.rglob("*") 
            if p.is_dir()
        ]
        return folders

    def move_concept(self, file_name: str, target_folder: str, concept_id: str):
        """Moves a concept file to a new folder and updates the database index."""
        source_path = self.base_path / file_name
        target_dir = self.base_path / target_folder
        target_path = target_dir / file_name

        if not source_path.exists():
            # Try searching for the file in the whole base_path if not in root
            found_files = list(self.base_path.rglob(file_name))
            if not found_files:
                raise FileNotFoundError(f"Source concept file not found: {file_name}")
            source_path = found_files[0]

        # Create target directory
        target_dir.mkdir(parents=True, exist_ok=True)

        if source_path == target_path:
            logger.info(f"File already at {target_path}")
            return

        # Move file
        logger.info(f"Moving {source_path} to {target_path}")
        shutil.move(str(source_path), str(target_path))

        # Update LanceDB index (Task 2.3)
        self._update_index_path(concept_id, str(target_path.absolute()))

    def _update_index_path(self, concept_id: str, new_source_path: str):
        """Updates the source path in LanceDB."""
        try:
            table = get_concepts_table()
            # LanceDB update: find by ID and update source field
            table.update(where=f"id = '{concept_id}'", values={"source": new_source_path})
            logger.info(f"Updated index for concept {concept_id} with new source: {new_source_path}")
        except Exception as e:
            logger.error(f"Failed to update index for {concept_id}: {e}")
