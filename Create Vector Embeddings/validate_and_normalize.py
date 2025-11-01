#!/usr/bin/env python3
"""
Data Validation and Normalization Script
Validates and normalizes JSON files in the Complete folder before upload to Zilliz.
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, Any, Tuple
from datetime import datetime


class DataValidator:
    """Validate and normalize JSON data before upload."""

    def __init__(
        self,
        complete_folder: str = "Complete",
        default_collection_name: str = "persona_revrebel",
        data_key: str = "data",
        default_persona_id: str = "revrebel_core",
        default_created_ym: str = "2025-10",
        default_status: str = "active",
        default_author: str = "REVREBEL",
        default_version: str = "v1.0",
        default_created_date: str = "2025-10-31",
        default_last_updated: str = "2025-10-31",
        default_version_status: str = "approved",
        default_approved_by: str = "REVREBEL Founder",
    ):
        """
        Initialize the data validator.

        Args:
            complete_folder: Folder containing JSON files to validate
            default_persona_id: Default persona_id value
            default_collection_name: Default collection name for Zilliz
            data_key: The key to hold the records for Zilliz
            default_created_ym: Default created year-month
            default_status: Default status for metadata
            default_author: Default author name
            default_version: Default version number
            default_created_date: Default creation date
            default_last_updated: Default last updated date
            default_version_status: Default status for version_info
            default_approved_by: Default approver name
        """
        self.complete_folder = Path(complete_folder)
        self.defaults = {
            'collection_name': default_collection_name,
            'persona_id': default_persona_id,
            'created_ym': default_created_ym,
            'status': default_status,
            'author': default_author,
            'version': default_version,
            'created_date': default_created_date,
            'last_updated': default_last_updated,
            'version_status': default_version_status,
            'approved_by': default_approved_by,
        }
        self.data_key = data_key


        # Create folder if it doesn't exist
        self.complete_folder.mkdir(exist_ok=True)

        # Statistics
        self.stats = {
            'total_files': 0,
            'files_modified': 0,
            'files_skipped': 0,
            'changes': {
                'id_to_primary_key': 0,
                'persona_id_added': 0,
                'created_ym_added': 0,
                'status_added': 0,
                'author_added': 0,
                'version_added': 0,
                'created_date_added': 0,
                'last_updated_added': 0,
                'version_status_added': 0,
                'approved_by_added': 0,
                'version_info_created': 0,
                'data_wrapped': 0,
                'arrays_fixed': 0,
                'language_fixed': 0,
                'fields_moved_to_metadata': 0,
            },
        }

    def validate_primary_key(self, data: Dict[str, Any]) -> bool:
        """
        Check for id or primary_key field.
        If 'id' exists, rename to 'primary_key'.

        Args:
            data: JSON data dictionary

        Returns:
            True if changes were made
        """
        changed = False

        if 'id' in data and 'primary_key' not in data:
            data['primary_key'] = data.pop('id')
            self.stats['changes']['id_to_primary_key'] += 1
            changed = True
            print("    ✓ Renamed 'id' to 'primary_key'")

        return changed

    def ensure_top_level_fields(self, record: Dict[str, Any]) -> bool:
        """
        Ensure required top-level fields exist and have default values.
        """
        changed = False

        # Check persona_id
        if 'persona_id' not in record:
            record['persona_id'] = self.defaults['persona_id']
            self.stats['changes']['persona_id_added'] += 1
            changed = True
            print(f"    ✓ Added persona_id: {self.defaults['persona_id']}")

        # Check created_ym
        if 'created_ym' not in record:
            record['created_ym'] = self.defaults['created_ym']
            self.stats['changes']['created_ym_added'] += 1
            changed = True
            print(f"    ✓ Added created_ym: {self.defaults['created_ym']}")

        # Check status
        if 'status' not in record:
            record['status'] = self.defaults['status']
            self.stats['changes']['status_added'] += 1
            changed = True
            print(f"    ✓ Added status: {self.defaults['status']}")

        # Check author
        if 'author' not in record:
            record['author'] = self.defaults['author']
            self.stats['changes']['author_added'] += 1
            changed = True
            print(f"    ✓ Added author: {self.defaults['author']}")

        return changed

    def ensure_version_info(self, data: Dict[str, Any]) -> bool:
        """
        Ensure version_info field exists and has required fields.

        Args:
            data: JSON data dictionary

        Returns:
            True if changes were made
        """
        changed = False

        # Create version_info if it doesn't exist
        if 'version_info' not in data:
            data['version_info'] = {}
            self.stats['changes']['version_info_created'] += 1
            changed = True
            print("    ✓ Created 'version_info' object")

        version_info = data['version_info']

        # Check version
        if 'version' not in version_info:
            version_info['version'] = self.defaults['version']
            self.stats['changes']['version_added'] += 1
            changed = True
            print(f"    ✓ Added version: {self.defaults['version']}")

        # Check created_date
        if 'created_date' not in version_info:
            version_info['created_date'] = self.defaults['created_date']
            self.stats['changes']['created_date_added'] += 1
            changed = True
            print(f"    ✓ Added created_date: {self.defaults['created_date']}")

        # Check last_updated
        if 'last_updated' not in version_info:
            version_info['last_updated'] = self.defaults['last_updated']
            self.stats['changes']['last_updated_added'] += 1
            changed = True
            print(f"    ✓ Added last_updated: {self.defaults['last_updated']}")

        # Check status
        if 'status' not in version_info:
            version_info['status'] = self.defaults['version_status']
            self.stats['changes']['version_status_added'] += 1
            changed = True
            print(f"    ✓ Added version_info.status: {self.defaults['version_status']}")

        # Check approved_by
        if 'approved_by' not in version_info:
            version_info['approved_by'] = self.defaults['approved_by']
            self.stats['changes']['approved_by_added'] += 1
            changed = True
            print(f"    ✓ Added approved_by: {self.defaults['approved_by']}")

        return changed

    def ensure_zilliz_structure(self, data: Dict[str, Any]) -> Tuple[Dict[str, Any], bool]:
        """
        Ensure the data is wrapped in the Zilliz structure with collectionName.

        Args:
            data: JSON data dictionary

        Returns:
            A tuple of (potentially new data structure, boolean indicating change)
        """
        changed = False
        # If 'collectionName' is not at the top level, we need to wrap the data.
        if 'collectionName' not in data:
            print(f"    ✓ Wrapping data with '{self.data_key}' key and adding 'collectionName'")
            new_data = {
                'collectionName': self.defaults['collection_name'],
                self.data_key: [data] if isinstance(data, dict) else data
            }
            self.stats['changes']['collection_name_added'] += 1
            self.stats['changes']['data_wrapped'] += 1
            changed = True
            return new_data, changed
        return data, changed

    def warn_on_empty_vector(self, record: Dict[str, Any]) -> bool:
        """
        Checks for an empty vector and prints a warning. Does not modify the file.
        """
        vector = record.get('vector')
        if not vector:
            pk = record.get('primary_key', 'N/A')
            print(f"    ! WARNING: Empty vector found for primary_key: {pk}. Please regenerate embeddings manually.")
        return False # This function never changes the file

    def fix_array_fields(self, record: Dict[str, Any]) -> bool:
        """
        Fix fields that should be arrays but are strings.
        """
        changed = False
        array_fields = ['tone', 'platform', 'channel', 'audience']
        
        for field in array_fields:
            if field in record and isinstance(record[field], str):
                record[field] = [item.strip() for item in record[field].split(',')]
                self.stats['changes']['arrays_fixed'] += 1
                changed = True
                print(f"    ✓ Fixed '{field}': Converted string to array.")

        return changed

    def fix_language_field(self, record: Dict[str, Any]) -> bool:
        """
        Fix the language field from 'English' to 'en'.
        """
        changed = False
        if 'language' in record and isinstance(record['language'], str):
            if record['language'].lower() == 'english':
                record['language'] = 'en'
                self.stats['changes']['language_fixed'] += 1
                changed = True
                print("    ✓ Fixed language: Changed 'English' to 'en'.")
        return changed

    def flatten_record(self, record: Dict[str, Any]) -> bool:
        """
        Pulls all nested keys from 'metadata' or 'dynamic_field' to the top level
        to create a clean, flat structure for processing.
        """
        changed = False
        while True:
            keys_to_flatten = []
            for key, value in record.items():
                # We want to preserve 'version_info' as a nested object.
                if isinstance(value, dict) and key != 'version_info':
                    keys_to_flatten.append(key)

            if not keys_to_flatten:
                break  # Exit loop if no more nested dictionaries are found

            changed = True
            for key in keys_to_flatten:
                nested_dict = record.pop(key)
                # Prioritize values from the nested dict by overwriting.
                record.update(nested_dict)
                print(f"    ✓ Flattened fields from nested '{key}' object.")

        return changed


    def structure_fields(self, record: Dict[str, Any]) -> bool:
        """
        Move any non-schema fields into a 'metadata' object.
        """
        changed = False
        # This is the definitive list of top-level fields for your schema.
        base_schema_keys = {
            'primary_key', 'vector', 'text', 'persona_id', 'persona_version', 'module',
            'submodule', 'status', 'tone', 'platform', 'channel', 'severity',
            'author', 'language', 'created_ym', 'confidence_score', 'weight',
            'use_case', 'audience', 'version_info', '_source_file'
        }
        
        if 'metadata' not in record:
            record['metadata'] = {}

        fields_to_move = [key for key in list(record.keys()) if key not in base_schema_keys and key != 'metadata']
        
        for key in fields_to_move:
            # Avoid overwriting existing keys in metadata if they somehow exist
            if key not in record['metadata']:
                record['metadata'][key] = record.pop(key)
                self.stats['changes']['fields_moved_to_metadata'] += 1
                changed = True
                print(f"    ✓ Moved '{key}' to metadata object.")

        # Clean up empty metadata object
        if not record['metadata']:
            del record['metadata']

        return changed

    def validate_file(self, json_file: Path) -> bool:
        """
        Validate and normalize a single JSON file.

        Args:
            json_file: Path to the JSON file

        Returns:
            True if file was modified, False otherwise
        """
        print(f"\n📄 Validating: {json_file.name}")

        try:
            # Read JSON file
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Track if any changes were made
            file_changed = False

            # Ensure top-level Zilliz structure
            data, wrapped = self.ensure_zilliz_structure(data)
            file_changed |= wrapped

            # The records to validate are now inside the 'data' key
            records = data.get(self.data_key, [])
            for record in records:
                # Run all validation checks on each record
                file_changed |= self.flatten_record(record) # FLATTEN FIRST
                file_changed |= self.validate_primary_key(record)
                file_changed |= self.ensure_top_level_fields(record)
                file_changed |= self.ensure_version_info(record)
                file_changed |= self.fix_array_fields(record)
                file_changed |= self.fix_language_field(record)
                file_changed |= self.structure_fields(record)
                self.warn_on_empty_vector(record) # This just warns, doesn't change file

            # Save if changes were made
            if file_changed:
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"  💾 Saved changes to: {json_file.name}")
                self.stats['files_modified'] += 1
            else:
                print(f"  ✓ No changes needed - file already valid")
                self.stats['files_skipped'] += 1

            return file_changed

        except json.JSONDecodeError as e:
            print(f"  ❌ Error: Invalid JSON - {e}")
            return False
        except Exception as e:
            print(f"  ❌ Error processing file: {e}")
            return False

    def validate_all_files(self) -> None:
        """Validate all JSON files in the Complete folder."""
        json_files = list(self.complete_folder.glob("*.json"))

        if not json_files:
            print(f"No JSON files found in '{self.complete_folder}' folder")
            return

        print(f"\n{'='*80}")
        print(f"DATA VALIDATION AND NORMALIZATION")
        print(f"{'='*80}")
        print(f"Found {len(json_files)} JSON file(s) to validate\n")

        self.stats['total_files'] = len(json_files)

        # Process each file
        for json_file in json_files:
            self.validate_file(json_file)

        # Print summary
        self.print_summary()

    def print_summary(self) -> None:
        """Print validation summary statistics."""
        print(f"\n{'='*80}")
        print(f"VALIDATION SUMMARY")
        print(f"{'='*80}")
        print(f"Total files processed: {self.stats['total_files']}")
        print(f"Files modified: {self.stats['files_modified']}")
        print(f"Files already valid: {self.stats['files_skipped']}")

        print(f"\n📊 Changes Applied:")
        changes = self.stats['changes']
        if sum(changes.values()) == 0:
            print("  No changes were needed - all files are valid!")
        else:
            if changes['id_to_primary_key'] > 0:
                print(f"  • Renamed 'id' to 'primary_key': {changes['id_to_primary_key']} times")
            if changes['data_wrapped'] > 0:
                print(f"  • Wrapped records under 'data' key: {changes['data_wrapped']} times")
            if changes['arrays_fixed'] > 0:
                print(f"  • Converted string fields to arrays: {changes['arrays_fixed']} times")
            if changes['language_fixed'] > 0:
                print(f"  • Fixed 'language' field to 'en': {changes['language_fixed']} times")
            if changes['fields_moved_to_metadata'] > 0:
                print(f"  • Moved non-schema fields to metadata object: {changes['fields_moved_to_metadata']} times")
            if changes['persona_id_added'] > 0:
                print(f"  • Added persona_id: {changes['persona_id_added']} times")
            if changes['created_ym_added'] > 0:
                print(f"  • Added created_ym: {changes['created_ym_added']} times")
            if changes['status_added'] > 0:
                print(f"  • Added status: {changes['status_added']} times")
            if changes['author_added'] > 0:
                print(f"  • Added author: {changes['author_added']} times")
            if changes['version_info_created'] > 0:
                print(f"  • Created 'version_info' object: {changes['version_info_created']} times")
            if changes['version_added'] > 0:
                print(f"  • Added version: {changes['version_added']} times")
            if changes['created_date_added'] > 0:
                print(f"  • Added created_date: {changes['created_date_added']} times")
            if changes['last_updated_added'] > 0:
                print(f"  • Added last_updated: {changes['last_updated_added']} times")
            if changes['version_status_added'] > 0:
                print(f"  • Added version_info.status: {changes['version_status_added']} times")
            if changes['approved_by_added'] > 0:
                print(f"  • Added approved_by: {changes['approved_by_added']} times")

        print(f"\n✅ Validation complete! Files are ready for upload to Zilliz.")


def main():
    """Main entry point for the script."""

    # Create validator with default values
    validator = DataValidator(
        default_collection_name="persona_revrebel",
        data_key="data",
        complete_folder="Complete",
        default_persona_id="revrebel_core",
        default_created_ym="2025-10",
        default_status="active",
        default_author="REVREBEL",
        default_version="v1.0",
        default_created_date="2025-10-31",
        default_last_updated="2025-10-31",
        default_version_status="approved",
        default_approved_by="REVREBEL Founder"
    )

    # Validate all files
    validator.validate_all_files()


if __name__ == "__main__":
    main()
