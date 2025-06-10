+++
type = "question"
title = "Bug carte après import fichier"
description = '''Bonjour, J&#x27;ai importé un fichier dans ma carte http://umap.openstreetmap.fr/fr/map/carte-deci-maj-16022021_476363#6/51.000/2.000 et depuis cela plante pour accéder à mon compte et à la carte. avez-vous la possibilité de la supprimer svp ? Merci, Mathieu'''
date = "2021-07-30T11:04:00Z"
lastmod = "2021-08-04T15:43:00Z"
weight = 81116
keywords = [ "openstreetmap-carto" ]
aliases = [ "/questions/81116" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Bug carte après import fichier](/questions/81116/bug-carte-apres-import-fichier)

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
<span id="post-81116-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81116-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81116-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Bonjour,</p>
<p>J'ai importé un fichier dans ma carte <a href="http://umap.openstreetmap.fr/fr/map/carte-deci-maj-16022021_476363#6/51.000/2.000">http://umap.openstreetmap.fr/fr/map/carte-deci-maj-16022021_476363#6/51.000/2.000</a> et depuis cela plante pour accéder à mon compte et à la carte.</p>
<p>avez-vous la possibilité de la supprimer svp ?</p>
<p>Merci,</p>
<p>Mathieu</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap-carto" rel="tag" title="see questions tagged &#39;openstreetmap-carto&#39;">openstreetmap-carto</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jul '21, 11:04</strong></p>
<img src="https://secure.gravatar.com/avatar/d78d4cf33c5197729e42fd69b84fb339?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mathieu%20SDIS&#39;s gravatar image" />
<p><span>Mathieu SDIS</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mathieu SDIS has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81116" class="comments-container">
&#10;</div>
<div id="comment-tools-81116" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81116-form-container" class="comment-form-container">
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

<span id="81198"></span>

<div id="answer-container-81198" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81198-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81198-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81198-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Bonjour,</p>
<p>vous pouvez tenter un ticket dans le dépôt <a href="https://github.com/umap-project/umap/issues">umap</a>, il arrive que des admins répondent.</p>
<p>Mais de mon côté, la carte ne plante pas tout à fait, elle est juste très (très) lente. En attendant un peu, j'arrive à accéder à la liste des couches (l'icône des disques empilés), pour cacher les couche "hydrants*", ce qui rend la carte à nouveau utilisable.</p>
<p>Vous pourrez ainsi supprimer les couches problématiques.</p>
<p>De fait umap n'est pas l'outil adapté pour afficher un trop grand nombre d'objets (pas de limite précise, ça dépend surtout du navigateur client).</p>
<p>Cordialement.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Aug '21, 15:43</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-81198" class="comments-container">
&#10;</div>
<div id="comment-tools-81198" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81198-form-container" class="comment-form-container">
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

