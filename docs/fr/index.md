# Accès aux données géospatiales optimisées pour l'infonuagique

Bonnes pratiques et tutoriels utilisant des bibliothèques libres pour l'accès aux données en format GeoTIFF optimisé pour le nuage (COG) provenant du cube de données du Centre canadien de cartographie et d'observation de la Terre (CCCOT).

!!! info "Lien vers les collections COG du CCCOT"
    API STAC : <https://datacube.services.geo.ca/stac/api/>  
    API STAC via STAC-Browser : <https://radiantearth.github.io/stac-browser/#/external/datacube.services.geo.ca/stac/api/?.language=fr>

---

## Sur ce site...
<div class="grid cards" markdown>
-   __Guides pratiques__

    ---

    **Exemples de code** couvrant les opérations clés et les tâches courantes
    :arrow_right: [guides pratiques](pystac-client.md)

-   __Références externes__

    ---

    :arrow_right: [**références externes**](reference.md)  


    <!-- :arrow_right: [Quick links](reference.md) -->
</div>
---

## Bibliothèques utilisées dans les exemples :

### Pour découvrir les données

De [Radiant Earth] :  

- [pystac-client]

### Pour accéder aux données

Basé sur GDAL :

- [rasterio]
- [rioxarray]

Bibliothèques tierces utilisant des objets STAC :

- [stackstac]
- [odc-stac]

## Signaler un problème

Si vous rencontrez des problèmes, veuillez [créer un nouveau problème](https://github.com/NRCan/cloud-optimized-geospatial/issues/new/choose) en utilisant notre gabarit.

## Licence
Les exemples sont publiés sous la [Licence du gouvernement ouvert - Canada](https://ouvert.canada.ca/fr/licence-du-gouvernement-ouvert-canada).

!!! Note
    Toutes les bibliothèques et ressources présentées ici sont libres et ont leur propre licence.
    Veuillez consulter la documentation des bibliothèques spécifiques pour plus d'informations sur les licences.

[pystac-client]: https://pystac-client.readthedocs.io/en/stable/usage.html
[rasterio]: https://rasterio.readthedocs.io/en/latest/quickstart.html
[stackstac]: https://stackstac.readthedocs.io/en/latest/basic.html
[odc-stac]: https://odc-stac.readthedocs.io/en/latest/
[rioxarray]: https://corteva.github.io/rioxarray/stable/
[Radiant Earth]: https://github.com/radiantearth
*[COG]: GeoTIFF optimisé pour le nuage
*[CCCOT]: Centre canadien de cartographie et d'observation de la Terre, Ressources naturelles Canada
*[STAC]: Catalogue de ressources spatio-temporelles

