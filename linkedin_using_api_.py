# -*- coding: utf-8 -*-
"""linkedin_using_api_.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RTqQMVITp_w7nDuv55WIgTAB0Cn1I9Mi
"""

pip install requests

import requests
#this is a funtionn using link for find this names using vanity_names.
def retrieve_profiles_by_vanity_name(access_token, vanity_name):
    url = f"https://api.linkedin.com/v2/people?q=vanityName&vanityName={vanity_name}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            profiles = response.json()
            return profiles
        else:
            print(f"Error retrieving profiles: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Error retrieving profiles: {e}")
        return None

if __name__ == "__main__":

    access_token = "AQUOUZ4NalKsNp_IkT0vZsp5OKG7e_nhyGEXQ0ULdxfQz1WwPfESOXnb7QPxZMybqvoD6G1XLxyWtVFsrccSNuO4aMLgH6krIa5_LRLcUDQp8Y_FEKH_R9ByMpn8yLYFV_ONs4btjOZLPCaMeCrsRNqDOQt4M2wdbjH7rWz0ujftu1jPHW4R2A-CVPId5WkCVNbmP58nL4aM_M3vJiM8S6xU4aHjrFrABSNCFaXuiADKqv7PCS3przW69xEcKAcXav8kK7BVXYZykfKMunU6c0RILzZLRu9r-r9RvTNkcylxN5huIai5S0SSwZE4QHuzHoJapFMVVaXOyDuxT5yhBu99QsrQlA"
    vanity_name = "bharat kumawat"  #vanity name
    profiles = retrieve_profiles_by_vanity_name(access_token, vanity_name)
    if profiles:
        print("Retrieved profiles successfully:")
        print(profiles)
    else:
        print("Failed to retrieve profiles.")