+++
type = "question"
title = "Intégrer open street map dans Autopanotour"
description = '''Bonjour, Comment intégrer openstreetmap dans Autopanotour? En Français SVP Merci'''
date = "2013-03-11T11:10:00Z"
lastmod = "2013-03-11T17:49:00Z"
weight = 20632
keywords = [ "intégrer", "lang-fr", "autopanotour" ]
aliases = [ "/questions/20632" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Intégrer open street map dans Autopanotour](/questions/20632/integrer-open-street-map-dans-autopanotour)

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
<span id="post-20632-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20632-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20632-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Bonjour, Comment intégrer openstreetmap dans Autopanotour? En Français SVP Merci</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-intégrer" rel="tag" title="see questions tagged &#39;intégrer&#39;">intégrer</span> <span class="post-tag tag-link-lang-fr" rel="tag" title="see questions tagged &#39;lang-fr&#39;">lang-fr</span> <span class="post-tag tag-link-autopanotour" rel="tag" title="see questions tagged &#39;autopanotour&#39;">autopanotour</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Mar '13, 11:10</strong></p>
<img src="https://secure.gravatar.com/avatar/8c0201c8af368573755881d965edbf4a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Airlium&#39;s gravatar image" />
<p><span>Airlium</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Airlium has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Mar '13, 13:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span></p>
</div>
</div>
<div id="comments-container-20632" class="comments-container">
&#10;</div>
<div id="comment-tools-20632" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20632-form-container" class="comment-form-container">
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

<span id="20639"></span>

<div id="answer-container-20639" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20639-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20639-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20639-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>J'imagine que vous voulez créer une interface similaire à Google Streetview ? D'autres s'y sont essayé avec plus ou moins de succès, la tache n'est pas simple. Voir <a href="http://openstreetview.org/">openstreetview</a> et <a href="http://sightwalk.com/">sightwalk</a>, mais il y en a probablement d'autres.</p>
<p>Dans un premier temps il vaut mieux ne rien entrer dans la bdd d'OSM, et travailler avec votre propre bdd (ou avec un fichier statique), qui associerais un panorama à une position géographique. Ensuite utiliser <a href="http://openlayers.org/dev/examples/">OpenLayers</a> ou <a href="http://leafletjs.com/examples.html">Leaflet</a> pour afficher une carte OSM avec des POIs qui pointeraient vers un panorama que vous avez créé. La question de comment passer d'un panorama à un autre depuis l'interface du panorama est à poser sur le forum d'Autopanotour, pas celui d'OSM.</p>
<p>Pour une petite quantité de données (le campus d'une université par exemple), leaflet avec un fichier geojson statique écrit à la main devrais suffire. Après avoir expérimenté un peu, vous aurez sans doute des questions plus précises à poser.</p>
<p>Par contre monter en charge est une autre paire de manches. Je vous conseille de contacter les projets existants, et de voir si vous pouvez collaborer avec eux pour intégrer vos améliorations.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Mar '13, 17:49</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-20639" class="comments-container">
&#10;</div>
<div id="comment-tools-20639" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20639-form-container" class="comment-form-container">
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

