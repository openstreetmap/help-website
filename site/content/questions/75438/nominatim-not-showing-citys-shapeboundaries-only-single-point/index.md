+++
type = "question"
title = "Nominatim not showing city&#x27;s shape/boundaries, only single point"
description = '''The title says it all, when I query on the osm page I get the correct represenation of the city and its borders/shape: https://nominatim.openstreetmap.org/search.php?q=Hamburg&amp;amp;polygon_geojson=1&amp;amp;viewbox= But when I do it on my server it just shows the single point in the center of the city. W...'''
date = "2020-06-26T09:45:00Z"
lastmod = "2020-06-26T14:35:00Z"
weight = 75438
keywords = [ "osm", "nominatim", "postgresql" ]
aliases = [ "/questions/75438" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim not showing city's shape/boundaries, only single point](/questions/75438/nominatim-not-showing-citys-shapeboundaries-only-single-point)

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
<span id="post-75438-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75438-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75438-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The title says it all, when I query on the osm page I get the correct represenation of the city and its borders/shape:</p>
<p><a href="https://nominatim.openstreetmap.org/search.php?q=Hamburg&amp;polygon_geojson=1&amp;viewbox=">https://nominatim.openstreetmap.org/search.php?q=Hamburg&amp;polygon_geojson=1&amp;viewbox=</a></p>
<p>But when I do it on my server it just shows the single point in the center of the city. What am I missing?</p>
<p>I should mention that I moved the whole /srv/nominatim/ installation to a different location due to limited space on that mounting point. Tho I did adjust all the symlink and everything seems to work fine, except for this single little issue.</p>
<p>Thank you!</p>
<p>Where can I tell postgres the new file location?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jun '20, 09:45</strong></p>
<img src="https://secure.gravatar.com/avatar/0fb317be587ae76bde2acf31d3bdb3a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dszill&#39;s gravatar image" />
<p><span>dszill</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dszill has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jun '20, 11:01</strong> </span></p>
</div>
</div>
<div id="comments-container-75438" class="comments-container">
&#10;</div>
<div id="comment-tools-75438" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75438-form-container" class="comment-form-container">
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

<span id="75439"></span>

<div id="answer-container-75439" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75439-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75439-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75439-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There where some recent fixes in the software of Nominatim and the OSM data to ensure that state cities like Hamburg are matched correctly against their boundaries. You need at least Nominatim 3.5.0 and OSM data from April 2020 or later to make this work correctly on your server.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '20, 14:35</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jun '20, 14:35</strong> </span></p>
</div>
</div>
<div id="comments-container-75439" class="comments-container">
&#10;</div>
<div id="comment-tools-75439" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75439-form-container" class="comment-form-container">
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

