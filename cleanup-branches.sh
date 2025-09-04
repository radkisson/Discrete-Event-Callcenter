#!/bin/bash
# Branch Cleanup Script
# This script will delete all branches except 'main' from the remote repository
# 
# WARNING: This will permanently delete 41 branches. Make sure this is intended.
# 
# To run this script:
# 1. Ensure you have push permissions to the repository
# 2. Run: chmod +x cleanup-branches.sh
# 3. Run: ./cleanup-branches.sh

set -e

echo "WARNING: This will delete all branches except 'main' from the remote repository."
echo "This action cannot be undone. Are you sure you want to continue? (y/N)"
read -r response

if [[ ! "$response" =~ ^[Yy]$ ]]; then
    echo "Operation cancelled."
    exit 0
fi

echo "Fetching latest branch list..."
git fetch origin

echo "Getting list of branches to delete..."
BRANCHES_TO_DELETE=$(git ls-remote --heads origin | grep -v refs/heads/main | awk '{print $2}' | sed 's|refs/heads/||')

echo "The following branches will be deleted:"
echo "$BRANCHES_TO_DELETE"
echo ""
echo "Total branches to delete: $(echo "$BRANCHES_TO_DELETE" | wc -l)"
echo ""
echo "Press Enter to continue or Ctrl+C to cancel..."
read -r

echo "Deleting branches..."
for branch in $BRANCHES_TO_DELETE; do
    echo "Deleting branch: $branch"
    if git push origin --delete "$branch"; then
        echo "✓ Successfully deleted: $branch"
    else
        echo "✗ Failed to delete: $branch"
    fi
done

echo ""
echo "Branch cleanup completed!"
echo "Remaining branches:"
git ls-remote --heads origin