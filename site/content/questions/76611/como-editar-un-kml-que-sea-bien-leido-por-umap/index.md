+++
type = "question"
title = "Como editar un KML que sea bien leido por Umap?"
description = '''Necesito trabajar los datos para un mapa pero en Excell. Los puedo luego convertir a CSV o TXT pero no sé con qué formato se tienen que escribir los encabezados de columnas o qué otros detalles agregar. Cuando importo un dato de CSV no lo hace bien. Quiero que mis datos sobre DESCRIPCION se inserten...'''
date = "2020-09-15T00:32:00Z"
lastmod = "2020-09-23T01:31:00Z"
weight = 76611
keywords = [ "umap", "kml", "editor", "lang-es" ]
aliases = [ "/questions/76611" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Como editar un KML que sea bien leido por Umap?](/questions/76611/como-editar-un-kml-que-sea-bien-leido-por-umap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76611-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76611-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76611-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Necesito trabajar los datos para un mapa pero en Excell. Los puedo luego convertir a CSV o TXT pero no sé con qué formato se tienen que escribir los encabezados de columnas o qué otros detalles agregar. Cuando importo un dato de CSV no lo hace bien. Quiero que mis datos sobre DESCRIPCION se inserten correctamente en el espacio DESCRIPTION que brinda UMAP por default. Existe algun editor de KML que pueda utilizar para tratar bien los datos y poder insertarlos lo mejor posible? He usado uno pero parece que solo funciona con Google Earth, no funciona con UMAP.</p>
<p>Gracias.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span> <span class="post-tag tag-link-kml" rel="tag" title="see questions tagged &#39;kml&#39;">kml</span> <span class="post-tag tag-link-editor" rel="tag" title="see questions tagged &#39;editor&#39;">editor</span> <span class="post-tag tag-link-lang-es" rel="tag" title="see questions tagged &#39;lang-es&#39;">lang-es</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Sep '20, 00:32</strong></p>
<img src="https://secure.gravatar.com/avatar/5427baefaca950ef9d44f608990c239d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FOTOJUNTIN&#39;s gravatar image" />
<p><span>FOTOJUNTIN</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FOTOJUNTIN has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Sep '20, 00:13</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span></p>
</div>
</div>
<div id="comments-container-76611" class="comments-container">
<span id="76670"></span>
<div id="comment-76670" class="comment">
<div id="post-76670-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://wiki.openstreetmap.org/wiki/UMap/Guide/Import_data_files#Data_format">This page</a> says that you should be able to get <code>name</code> and <code>description</code> from a KML. Do these show in the table after import?</p>
<p>Can you give an example that shows the description the way you want it?</p>
</div>
<div id="comment-76670-info" class="comment-info">
<span class="comment-age">(17 Sep '20, 00:12)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="76776"></span>
<div id="comment-76776" class="comment">
<div id="post-76776-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>gracias. pero a pesar de que yo le asigno el nombre NAME y DESCRIPTION a las columnas que contienen esos datos, cuando Umap importa el archivo CSV no asigna los datos en las casillas originales de NAME y DESCRIPTION en la consola de configuración para cada punto geográfico.</p>
<p>Tengo una lista de sitios localizados geográficamente, todo en una tabla que luego convierto a un archivo con formato CSV, las coordenadas Lat y LONG sí las captura bien y las asigna al registro correcto, sí lo gra ubicar los sitios en el punto preciso. pero los campos de description y name no son asignados, al contrario, son agregados a nuevos registros. Eso provoca que cuando uno hace click en el punto, las descripciones no aparecen, pues están en otro campo o registro.</p>
</div>
<div id="comment-76776-info" class="comment-info">
<span class="comment-age">(22 Sep '20, 22:29)</span> <span class="comment-user userinfo">FOTOJUNTIN</span>
</div>
</div>
<span id="76777"></span>
<div id="comment-76777" class="comment">
<div id="post-76777-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>He visto que hay archivos KML que sí insertan muy bien los datos y asignan adecuadamente la información de DESCRIPTION para que automáticamente los puntos puedan ser bien leídos y las pantallas emergentes muestren bien todo su contenido. Por eso necesito algún editor KML o plantilla que Umap y lógicamente OSM puedan interpretar bien.</p>
</div>
<div id="comment-76777-info" class="comment-info">
<span class="comment-age">(22 Sep '20, 22:31)</span> <span class="comment-user userinfo">FOTOJUNTIN</span>
</div>
</div>
</div>
<div id="comment-tools-76611" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76611-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="76778"></span>

<div id="answer-container-76778" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76778-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76778-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76778-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This works for a small test map I made, but I don't know if it's the best way to do this.</p>
<p>If the data from the imported KML doesn't show then the field names may not match the default.</p>
<p>If you import the KML you can see the data in table form by clicking the Manage layers button <img src="https://wiki.openstreetmap.org/w/images/thumb/7/71/Icon-database.PNG/15px-Icon-database.PNG" alt="Manage layers" /> then clicking on the table icon. The headings show the field names you can use for the pop-ups.</p>
<p>The label key can be edited via "Layer properties" <img src="https://wiki.openstreetmap.org/w/images/thumb/c/c6/Icon-edition.PNG/15px-Icon-edition.PNG" alt="pencil icon" /> &gt; "Advanced properties" &gt; "Label key".</p>
<p>The more expansive pop-up can be edited in "Layer properties" <img src="https://wiki.openstreetmap.org/w/images/thumb/c/c6/Icon-edition.PNG/15px-Icon-edition.PNG" alt="pencil icon" /> &gt; "Interaction options" &gt; "Popup content template".</p>
<p>the correct field name needs to be put in <code>{curly brackets}</code> in place of the default.</p>
<p>Unfortunately I don't know a way to check if the main pop-up has worked properly without saving the map and then clicking on the marker.</p>
<p>A longer explanation of the interaction options can be found <a href="https://wiki.openstreetmap.org/wiki/UMap/Guide/Configure_shape_interaction_(labels%E2%80%A6)">here</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Sep '20, 01:31</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</img>
</div>
</div>
<div id="comments-container-76778" class="comments-container">
&#10;</div>
<div id="comment-tools-76778" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76778-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

