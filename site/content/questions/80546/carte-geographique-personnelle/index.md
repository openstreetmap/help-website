+++
type = "question"
title = "Carte géographique personnelle"
description = '''Bonjour ..je souhaite créer une carte personnelle de données génétiques , puis je remplir sous forme de coloris les différentes régions et y annoter des données mathématiques?.. en laissant bien sur le nom correspondant aux régions ou pays. Merci pour votre réponse'''
date = "2021-06-13T14:41:00Z"
lastmod = "2021-06-13T20:06:00Z"
weight = 80546
keywords = [ "map", "personnelle" ]
aliases = [ "/questions/80546" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Carte géographique personnelle](/questions/80546/carte-geographique-personnelle)

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
<span id="post-80546-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80546-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80546-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Bonjour ..je souhaite créer une carte personnelle de données génétiques , puis je remplir sous forme de coloris les différentes régions et y annoter des données mathématiques?.. en laissant bien sur le nom correspondant aux régions ou pays. Merci pour votre réponse</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-personnelle" rel="tag" title="see questions tagged &#39;personnelle&#39;">personnelle</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jun '21, 14:41</strong></p>
<img src="https://secure.gravatar.com/avatar/3a27f2133ae001ccd76a768fc368680c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Catheloys&#39;s gravatar image" />
<p><span>Catheloys</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Catheloys has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80546" class="comments-container">
&#10;</div>
<div id="comment-tools-80546" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80546-form-container" class="comment-form-container">
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

<span id="80553"></span>

<div id="answer-container-80553" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80553-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80553-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80553-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Bonjour,</p>
<p>Openstreetmap en lui-même n'est pas vraiment adapté à ce genre de besoin.</p>
<p>Vous pouvez utiliser <a href="https://wiki.openstreetmap.org/wiki/UMap">uMap</a>, mais le dessin des différentes régions (à la main ou par import) risque d'être un peu long. Par contre ensuite le remplissage devrait être assez simple.</p>
<p>Le mieux est probablement d'utiliser <a href="https://wiki.openstreetmap.org/wiki/QGIS">QGis</a>. Cette <a href="https://www.youtube.com/watch?v=C-9iQnZH5DY">vidéo</a> présente comment annoter différentes régions, je crois.</p>
<p>Il y a d'autres méthodes, plus ou moins complexes, avec <a href="https://leafletjs.com/examples/choropleth/">Leaflet</a> (en Javascript), "<a href="https://rsandstroem.github.io/GeoMapsFoliumDemo.html">Jupyter Notebook</a>" (en Python), <a href="https://slcladal.github.io/maps.html">R</a>, et pleins d'autres outils que vous connaissez peut-être.</p>
<p>Pour récupérer le tracé des régions, je vous conseille overpass-turbo, avec par exemple cette <a href="http://overpass-turbo.eu/s/18jU">requête</a> (attention c'est très lourd pour le navigateur).</p>
<p>Cordialement</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jun '21, 20:06</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-80553" class="comments-container">
&#10;</div>
<div id="comment-tools-80553" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80553-form-container" class="comment-form-container">
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

