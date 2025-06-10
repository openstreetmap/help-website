+++
type = "question"
title = "What is the map scale for the shapefiles downloaded from GEOFABRIK?"
description = '''Hi all, May I ask that does there anyone know what is the map scale for the free shapefiles from GEOFABRIK(at the country level)? Thanks for help in advance.'''
date = "2016-04-20T20:30:00Z"
lastmod = "2016-04-20T22:02:00Z"
weight = 49307
keywords = [ "shapefile", "scale", "geofabrik" ]
aliases = [ "/questions/49307" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What is the map scale for the shapefiles downloaded from GEOFABRIK?](/questions/49307/what-is-the-map-scale-for-the-shapefiles-downloaded-from-geofabrik)

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
<span id="post-49307-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49307-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49307-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>May I ask that does there anyone know what is the map scale for the free shapefiles from GEOFABRIK(at the country level)?</p>
<p>Thanks for help in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-scale" rel="tag" title="see questions tagged &#39;scale&#39;">scale</span> <span class="post-tag tag-link-geofabrik" rel="tag" title="see questions tagged &#39;geofabrik&#39;">geofabrik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Apr '16, 20:30</strong></p>
<img src="https://secure.gravatar.com/avatar/4c6b1343c60b83eaa6e7114be590837d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Digmaa&#39;s gravatar image" />
<p><span>Digmaa</span><br />
<span class="score" title="100 reputation points">100</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Digmaa has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49307" class="comments-container">
&#10;</div>
<div id="comment-tools-49307" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49307-form-container" class="comment-form-container">
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

<span id="49316"></span>

<div id="answer-container-49316" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49316-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49316-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-49316-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Shape files do not have a map scale. A map scale determines the relationship between units in reality and units on the map. If you have a map that is 50cm wide and it depicts 50km in reality then its scale is 1:100k; a shape file does not have a scale because you can print it at any resolution.</p>
<p>By convention, certain scales also go along with a certain selection of features. For example, a 1:100k map will <em>usually</em> not show individual trees (even though it totally could, if it made the top of the tree about 0.1mm wide). When you ask "what scale are the shape files in", you probably want to know if there is a certain scale-dependent feature selection or generalisation in the shape files.</p>
<p>The answer to that is no, the Geofabrik shapes have no generalisation or simplification, and the feature selection is based on a very simple tag selection. For example, anything that has an amenity, tourism, shop, office, craft, historic, man_made, railway, or highway tag and is a node will be listed in the "points" shape file. The means that individual trees aren't available (they are <code>natural=tree</code>), while post boxes are (<code>amenity=post_box</code>).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Apr '16, 22:02</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Apr '16, 06:35</strong> </span></p>
</div>
</div>
<div id="comments-container-49316" class="comments-container">
&#10;</div>
<div id="comment-tools-49316" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49316-form-container" class="comment-form-container">
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

