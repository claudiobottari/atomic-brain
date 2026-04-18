import pytest
from unittest.mock import MagicMock, patch
from pathlib import Path
from src.vault_manager import VaultManager


@patch('src.vault_manager.get_concepts_table')
@patch('src.vault_manager.shutil.move')
@patch('src.vault_manager.Path.mkdir')
@patch('src.vault_manager.Path.exists')
@patch('src.vault_manager.Path.rglob')
def test_vault_manager_move_concept_new_folder(mock_rglob, mock_exists, mock_mkdir, mock_shutil_move, mock_get_concepts_table):
    """Tests moving a concept to a new folder."""
    mock_exists.return_value = True  # source file exists at base_path/file_name
    mock_table = MagicMock()
    mock_get_concepts_table.return_value = mock_table

    manager = VaultManager(base_path=Path("vault/Concepts"))

    file_name = "my_concept.md"
    target_folder = "Category/SubCategory"
    concept_id = "test-id-123"

    manager.move_concept(file_name, target_folder, concept_id)

    mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)
    expected_src = str(Path("vault/Concepts") / file_name)
    expected_dst = str(Path("vault/Concepts") / target_folder / file_name)
    mock_shutil_move.assert_called_once_with(expected_src, expected_dst)
    expected_new_path = str(Path("vault/Concepts/Category/SubCategory/my_concept.md").absolute())
    mock_table.update.assert_called_once_with(where=f"id = '{concept_id}'", values={"source": expected_new_path})


@patch('src.vault_manager.get_concepts_table')
@patch('src.vault_manager.shutil.move')
@patch('src.vault_manager.Path.mkdir')
@patch('src.vault_manager.Path.exists')
@patch('src.vault_manager.Path.rglob')
def test_vault_manager_move_concept_file_already_exists(mock_rglob, mock_exists, mock_mkdir, mock_shutil_move, mock_get_concepts_table):
    """Tests moving a concept that exists at the root to a target folder."""
    mock_exists.return_value = True  # source exists
    mock_table = MagicMock()
    mock_get_concepts_table.return_value = mock_table

    manager = VaultManager(base_path=Path("vault/Concepts"))

    file_name = "my_concept.md"
    target_folder = "Category"
    concept_id = "test-id-123"

    manager.move_concept(file_name, target_folder, concept_id)

    mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)
    mock_shutil_move.assert_called_once_with(
        str(Path("vault/Concepts") / file_name),
        str(Path("vault/Concepts") / target_folder / file_name),
    )
    mock_table.update.assert_called_once()


@patch('src.vault_manager.get_concepts_table')
@patch('src.vault_manager.shutil.move')
@patch('src.vault_manager.Path.mkdir')
@patch('src.vault_manager.Path.exists')
@patch('src.vault_manager.Path.rglob')
def test_vault_manager_move_concept_already_in_place(mock_rglob, mock_exists, mock_mkdir, mock_shutil_move, mock_get_concepts_table):
    """Tests moving a concept when it's already in the target location (no-op)."""
    mock_exists.return_value = True  # source exists
    mock_table = MagicMock()
    mock_get_concepts_table.return_value = mock_table

    manager = VaultManager(base_path=Path("vault/Concepts"))

    # target_folder="" means target_dir == base_path, so source == target
    file_name = "my_concept.md"
    target_folder = ""
    concept_id = "test-id-123"

    manager.move_concept(file_name, target_folder, concept_id)

    mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)
    mock_shutil_move.assert_not_called()  # already in place, no move
    mock_table.update.assert_not_called()  # early return before index update


@patch('src.vault_manager.get_concepts_table')
@patch('src.vault_manager.shutil.move')
@patch('src.vault_manager.Path.mkdir')
@patch('src.vault_manager.Path.exists')
@patch('src.vault_manager.Path.rglob')
def test_vault_manager_move_concept_source_not_found_in_root(mock_rglob, mock_exists, mock_mkdir, mock_shutil_move, mock_get_concepts_table):
    """Tests moving a concept when the source file is not found anywhere."""
    mock_exists.return_value = False  # source not in root
    mock_rglob.return_value = iter([])  # not found via rglob either
    mock_table = MagicMock()
    mock_get_concepts_table.return_value = mock_table

    manager = VaultManager(base_path=Path("vault/Concepts"))

    with pytest.raises(FileNotFoundError) as excinfo:
        manager.move_concept("nonexistent_concept.md", "Category", "test-id-456")

    assert "Source concept file not found" in str(excinfo.value)
    mock_shutil_move.assert_not_called()
    mock_table.update.assert_not_called()


@patch('src.vault_manager.get_concepts_table')
@patch('src.vault_manager.shutil.move')
@patch('src.vault_manager.Path.mkdir')
@patch('src.vault_manager.Path.exists')
@patch('src.vault_manager.Path.rglob')
def test_vault_manager_move_concept_source_found_via_rglob(mock_rglob, mock_exists, mock_mkdir, mock_shutil_move, mock_get_concepts_table):
    """Tests finding the source file via rglob if not in root."""
    mock_exists.return_value = False  # not at root
    found_file_path = Path("vault/Concepts/SubFolder/my_concept.md")
    mock_rglob.return_value = iter([found_file_path])
    mock_table = MagicMock()
    mock_get_concepts_table.return_value = mock_table

    manager = VaultManager(base_path=Path("vault/Concepts"))

    file_name = "my_concept.md"
    target_folder = "Category"
    concept_id = "test-id-789"

    manager.move_concept(file_name, target_folder, concept_id)

    mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)
    expected_dst = str(Path("vault/Concepts") / target_folder / file_name)
    mock_shutil_move.assert_called_once_with(str(found_file_path), expected_dst)
    expected_abs = str(Path(expected_dst).absolute())
    mock_table.update.assert_called_once_with(where=f"id = '{concept_id}'", values={"source": expected_abs})


@patch('src.vault_manager.get_concepts_table')
@patch('src.vault_manager.shutil.move')
@patch('src.vault_manager.Path.mkdir')
@patch('src.vault_manager.Path.exists')
@patch('src.vault_manager.Path.rglob')
def test_vault_manager_move_concept_index_update_fails(mock_rglob, mock_exists, mock_mkdir, mock_shutil_move, mock_get_concepts_table):
    """Tests that move_concept still moves the file even if index update fails."""
    mock_exists.return_value = True  # source exists
    mock_table = MagicMock()
    mock_get_concepts_table.return_value = mock_table
    mock_table.update.side_effect = Exception("Index update error")

    manager = VaultManager(base_path=Path("vault/Concepts"))

    # Should not raise — VaultManager._update_index_path catches the exception
    manager.move_concept("my_concept.md", "Category", "test-id-123")

    mock_shutil_move.assert_called_once()
    mock_table.update.assert_called_once()
