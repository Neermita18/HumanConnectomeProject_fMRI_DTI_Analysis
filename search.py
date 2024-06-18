import os

# List of specified prefixes
prefixes = [
    '102311', '105014', '113821', '118528', '123420', '124826', '127630', '128127',
    '132118', '140117', '144832', '146331', '153833', '155635', '161630', '169444',
    '170934', '172938', '173536', '177645', '179346', '180129', '180836', '181232',
    '187547', '189349', '191033', '191841', '194847', '197348', '201818', '211316',
    '212419', '250932', '256540', '268850', '285345', '316633', '334635', '365343',
    '422632', '436239', '441939', '480141', '565452', '613538', '620434', '683256',
    '748662', '770352', '101309', '102008', '103111', '107422', '108828', '109123',
    '113922', '114419', '116524', '121618', '124220', '137027', '137936', '145531',
    '146432', '148941', '150726', '154734', '154936', '159138', '163331', '164131',
    '165032', '168341', '172130', '175035', '725751', '183034', '186141', '187143',
    '192843', '195849', '198855', '199453', '203418', '214726', '303624', '308331',
    '380036', '386250', '395958', '433839', '479762', '540436', '567052', '592455',
    '594156', '601127', '622236', '690152'
]

def check_folders_with_prefixes(directory_path, prefixes):
    # Get all folder names in the directory
    folder_names = [f for f in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, f))]

    # Convert prefixes to set for efficient lookup
    prefixes_set = set(prefixes)

    # Keep track of found and not found prefixes
    found_prefixes = set()
    not_found_prefixes = prefixes_set.copy()

    for folder_name in folder_names:
        for prefix in prefixes_set:
            if folder_name.startswith(prefix):
                found_prefixes.add(prefix)
                if prefix in not_found_prefixes:
                    not_found_prefixes.remove(prefix)

    # Print the prefixes not found
    if not_found_prefixes:
        print("Prefixes not found:")
        for prefix in not_found_prefixes:
            print(prefix)
    else:
        print("All prefixes found in the folder names.")

# Example usage
directory_path = 'D:\images'  # Replace with the path to your directory
check_folders_with_prefixes(directory_path, prefixes)