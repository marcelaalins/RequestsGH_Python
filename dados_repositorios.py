import requests

owner = 'amzn'
url = f'https://api.github.com/users/{owner}'

response = requests.get(url)
response.json()

response.json()['public_repos']

from math import ceil

ceil(response.json()['public_repos']/30)

def lista_repositorios(self):
        repos_list = []

        # calculando a quantidade de paginas
        response = requests.get(f'https://api.github.com/users/{self.owner}')
        num_pages = ceil(response.json()['public_repos']/30)

        for page_num in range(1, num_pages):
            try:
                url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url, headers=self.headers)
                repos_list.append(response.json())
            except:
                repos_list.append(None)

        return repos_list