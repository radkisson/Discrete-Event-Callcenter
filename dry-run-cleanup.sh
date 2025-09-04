#!/bin/bash
# Branch Cleanup Script - DRY RUN MODE
# This script shows what branches would be deleted without actually deleting them

set -e

echo "DRY RUN: Showing what branches would be deleted..."
echo "Fetching latest branch list..."

echo "Getting list of branches to delete..."
BRANCHES_TO_DELETE=$(git ls-remote --heads origin | grep -v refs/heads/main | awk '{print $2}' | sed 's|refs/heads/||')

echo "The following branches WOULD be deleted:"
echo "$BRANCHES_TO_DELETE"
echo ""
echo "Total branches to delete: $(echo "$BRANCHES_TO_DELETE" | wc -l)"
echo ""
echo "Current branches:"
git ls-remote --heads origin

echo ""
echo "This was a DRY RUN - no branches were actually deleted."
echo "To perform the actual cleanup, run: ./cleanup-branches.sh"