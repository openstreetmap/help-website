+++
type = "question"
title = "Cómo subir rutas tomadas con GPS MAGELLAN Thales a OpenStreetMap"
description = '''Durante varios años he marcado rutas con un GPS MAGELLAN, el cual da muy buena geometria. Dicho dispositivo guarda los archivos creados con la extensión .MMJ, la cual en el GPSBabel permite cargarlo en el archivo de entrada con varias de las extensiones que este trae, pero en ninguna de todas en las...'''
date = "2016-09-17T05:17:00Z"
lastmod = "2019-06-17T17:56:00Z"
weight = 52077
keywords = [ "thales", "magellan", "lang-es" ]
aliases = [ "/questions/52077" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Cómo subir rutas tomadas con GPS MAGELLAN Thales a OpenStreetMap](/questions/52077/como-subir-rutas-tomadas-con-gps-magellan-thales-a-openstreetmap)

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
<span id="post-52077-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52077-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52077-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Durante varios años he marcado rutas con un GPS MAGELLAN, el cual da muy buena geometria. Dicho dispositivo guarda los archivos creados con la extensión .MMJ, la cual en el GPSBabel permite cargarlo en el archivo de entrada con varias de las extensiones que este trae, pero en ninguna de todas en las que en el archivo de salida sale el letrero "traducción realizada con exito", da un archivo valido, ya que en algunas da una lista de puntos en los cuales todas sus coordenadas son igual a cero; mientras que en los otros casos ni siquiera alcanza a salir alguna ruta ó punto.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-thales" rel="tag" title="see questions tagged &#39;thales&#39;">thales</span> <span class="post-tag tag-link-magellan" rel="tag" title="see questions tagged &#39;magellan&#39;">magellan</span> <span class="post-tag tag-link-lang-es" rel="tag" title="see questions tagged &#39;lang-es&#39;">lang-es</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Sep '16, 05:17</strong></p>
<img src="https://secure.gravatar.com/avatar/b668f686de9379eb0dd1ccd939e62623?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JLOSM&#39;s gravatar image" />
<p><span>JLOSM</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JLOSM has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Sep '16, 00:06</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-52077" class="comments-container">
<span id="52090"></span>
<div id="comment-52090" class="comment">
<div id="post-52090-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>GPSBabel tiene soporte una limitada cantidad de dispositivos, ¿Qué modelo es tu receptor? se puede ver una lista de dispositivos soportados aquí → <a href="https://www.gpsbabel.org/htmldoc-development/fmt_magellan.html">https://www.gpsbabel.org/htmldoc-development/fmt_magellan.html</a> o <a href="https://www.gpsbabel.org/htmldoc-development/fmt_magellanx.html">https://www.gpsbabel.org/htmldoc-development/fmt_magellanx.html</a></p>
<p>¿Con qué versión de gpsbabel probaste? ¿Probaste conectar directo por puerto serial? En qué sistema operativo probaste? Muchas veces es mejor hacer en entornos gnu-linux</p>
</div>
<div id="comment-52090-info" class="comment-info">
<span class="comment-age">(18 Sep '16, 02:06)</span> <span class="comment-user userinfo">5m4u9</span>
</div>
</div>
<span id="52092"></span>
<div id="comment-52092" class="comment">
<div id="post-52092-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>El modelo del receptor es MobileMapper THALES. No se encuentra en la lista de los 2 link enviados.</p>
<p>Probé<img src="/upfiles/Thales.jpg" alt="alt text" /> con todas las posibles opciones de GPSBabel versión 1.5.2, en el sistema operativo Windows 10, sin obtener ningún resultado positivo.</p>
</div>
<div id="comment-52092-info" class="comment-info">
<span class="comment-age">(18 Sep '16, 03:06)</span> <span class="comment-user userinfo">JLOSM</span>
</div>
</div>
<span id="52099"></span>
<div id="comment-52099" class="comment">
<div id="post-52099-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Encontré que este modelo «mobilemapper thales» crea jobs y con su software «mobilemapper office» es posible exportar a formato shape, previa descarga con «mobilemapper transfer». Ver manual → <a href="http://www.manualslib.com/manual/169925/Magellan-Mobile-Mapper.html?page=81#manual">http://www.manualslib.com/manual/169925/Magellan-Mobile-Mapper.html?page=81#manual</a> y <a href="http://www.manualslib.com/manual/169925/Magellan-Mobile-Mapper.html?page=78#manual">http://www.manualslib.com/manual/169925/Magellan-Mobile-Mapper.html?page=78#manual</a></p>
<p>De archivo shape a gpx o geojson ya es más sencillo convertir utilizando ogr2ogr.</p>
</div>
<div id="comment-52099-info" class="comment-info">
<span class="comment-age">(18 Sep '16, 17:44)</span> <span class="comment-user userinfo">5m4u9</span>
</div>
</div>
</div>
<div id="comment-tools-52077" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52077-form-container" class="comment-form-container">
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

<span id="69642"></span>

<div id="answer-container-69642" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69642-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69642-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69642-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hola, para otra referencia aquí, otro manual <a href="https://manualszilla.com/y19j/mobilemapper%E2%84%A2-pro.html">MobileMapper™ Pro</a> Espero que esto te ayude</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jun '19, 17:56</strong></p>
<img src="https://secure.gravatar.com/avatar/4cb98a5b13406f85a60baa374912886f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Reberto99&#39;s gravatar image" />
<p><span>Reberto99</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Reberto99 has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jun '19, 17:57</strong> </span></p>
</div>
</div>
<div id="comments-container-69642" class="comments-container">
&#10;</div>
<div id="comment-tools-69642" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69642-form-container" class="comment-form-container">
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

