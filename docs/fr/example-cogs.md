# Accès aux données COG
Exemples sur l'utilisation de bibliothèques Python pour accéder et utiliser les COG. Démonstration d'un des avantages de l'optimisation pour le nuage, soit la possibilité d'accéder à une **[portion des données]** sans avoir à télécharger le fichier complet.

Voir <https://guide.cloudnativegeo.org/>

!!! Note
    Les exemples suivants commencent par une requête à l'API STAC du CCCOT via la bibliothèque pystac-client.

    Pour plus de détails sur la découverte de données via l'API STAC, consultez la section **[Interaction avec l'API STAC du CCCOT]**

## Utilisation de [rasterio]

Les développeurs de la bibliothèque rasterio fournissent des exemples d'utilisation supplémentaires.
Pour plus de détails sur la bibliothèque rasterio, consultez la documentation [rasterio](https://rasterio.readthedocs.io/en/latest/quickstart.html).

``` sh
--8<-- "how-to-guides/rasterio-requirements.txt:2:2"
```

### Lire l'en-tête d'un COG distant

Dans ce code, vous allez :

- Interroger une API STAC avec pystac-client pour obtenir le lien vers un COG
- Lire les métadonnées d'en-tête d'un fichier COG distant

!!! info
    Cet exemple spécifique utilise la collection **mrdem-30** du cube de données du CCCOT

``` py linenums="1" hl_lines="23-35"
--8<-- "how-to-guides/rasterio-header-example.py:code"
```

### Lire une portion d'un COG distant - Rectangle englobant

Pour cet exemple, vous devrez également installer [shapely](https://shapely.readthedocs.io/en/stable/installation.html) :
```bash
pip install shapely
```

Dans ce code, vous allez :

- Interroger une API STAC avec pystac-client pour obtenir le lien vers un COG
- Lire une portion d'un COG distant basée sur une zone d'intérêt avec la fonctionnalité window
- Écrire la portion localement dans un fichier .tif (Optionnel)

!!! info
    Cet exemple spécifique utilise la collection **mrdem-30** du cube de données du CCCOT

!!! Tip
    Le fichier COG contient un carrelage interne qui peut être exploité en itérant sur
    le `src.block_windows()` lors de la lecture. Si la fenêtre de lecture ne s'aligne pas avec
    le carrelage interne du fichier, les données seront rééchantillonnées.

    Exemple : <https://rasterio.readthedocs.io/en/stable/topics/windowed-rw.html#blocks>

    Définition API : <https://rasterio.readthedocs.io/en/stable/topics/windowed-rw.html#blocks>

``` py linenums="1" hl_lines="27-37"
--8<-- "how-to-guides/rasterio-window-example.py:code"
```

### Lire une portion d'un COG distant - Point

Pour cet exemple, vous devrez également installer [shapely](https://shapely.readthedocs.io/en/stable/installation.html) :
```bash
pip install shapely
```

Dans ce code, vous allez :

- Interroger une API STAC avec pystac-client
- Lire les valeurs d'un COG distant basées sur des coordonnées avec la fonctionnalité [sample()](https://rasterio.readthedocs.io/en/stable/api/rasterio.io.html#rasterio.io.DatasetReader.sample)

!!! info
    Cet exemple spécifique utilise la collection **mrdem-30** du cube de données du CCCOT

!!! Tip
    Pour effectuer la même requête en utilisant gdal, consultez l'utilitaire [gdallocationinfo](https://gdal.org/en/stable/programs/gdallocationinfo.html)

``` py linenums="1" hl_lines="34-38"
--8<-- "how-to-guides/rasterio-point-example.py:code"
```

[rasterio installation]: https://rasterio.readthedocs.io/en/stable/installation.html
[rasterio]: https://rasterio.readthedocs.io/en/latest/quickstart.html
[Interaction avec l'API STAC du CCCOT]: pystac-client.md
[portion des données]: #how-to-guides.rasterio-window-example--read-a-portion-of-a-remote-cog

*[COG]: GeoTIFF optimisé pour le nuage
*[STAC]: Catalogue de ressources spatio-temporelles
*[CCCOT]: Centre canadien de cartographie et d'observation de la Terre, Ressources naturelles Canada

