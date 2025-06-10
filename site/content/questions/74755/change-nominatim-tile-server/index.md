+++
type = "question"
title = "Change nominatim tile server"
description = '''Good afternoon, please help reconfigure local.php nominatim to the local tile server At the moment I have 2 fully working servers installed:  1. nominatim server &#x27;http://localhost:7070&#x27; example URL: http://localhost:7070/search.php?q=Moscow&amp;amp;polygon_geojson=1&amp;amp;viewbox=  2. OpenMapTiles server ...'''
date = "2020-05-12T12:31:00Z"
lastmod = "2020-05-12T17:26:00Z"
weight = 74755
keywords = [ "nominatim", "openmaptiles", "tileserver" ]
aliases = [ "/questions/74755" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Change nominatim tile server](/questions/74755/change-nominatim-tile-server)

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
<span id="post-74755-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74755-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74755-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Good afternoon, please help reconfigure local.php nominatim to the local tile server</p>
<p>At the moment I have 2 fully working servers installed:<br />
1. nominatim server 'http://localhost:7070' example URL:<br />
<a href="http://localhost:7070/search.php?q=Moscow&amp;polygon_geojson=1&amp;viewbox=">http://localhost:7070/search.php?q=Moscow&amp;polygon_geojson=1&amp;viewbox=</a><br />
<br />
2. OpenMapTiles server 'http://localhost:8080' Example png URL<br />
<a href="http://localhost:8080/styles/klokantech-basic/10/598/297.png">http://localhost:8080/styles/klokantech-basic/10/598/297.png</a></p>
<p>I tried editing the local.php file adding it to it:<br />
@define ('CONST_Map_Tile_URL', 'http://localhost:8080/styles/klokantech-basic/{z}/{x}/{y}.png')<br />
But my nominatim site still uses tiles from <a href="https://openstreetmap.org.png">https://openstreetmap.org.png</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-openmaptiles" rel="tag" title="see questions tagged &#39;openmaptiles&#39;">openmaptiles</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 May '20, 12:31</strong></p>
<img src="https://secure.gravatar.com/avatar/0f74346ddbb786aa15a232dc85ad5201?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nimistren&#39;s gravatar image" />
<p><span>nimistren</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nimistren has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 May '20, 12:38</strong> </span></p>
</div>
</div>
<div id="comments-container-74755" class="comments-container">
&#10;</div>
<div id="comment-tools-74755" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74755-form-container" class="comment-form-container">
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

<span id="74773"></span>

<div id="answer-container-74773" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74773-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74773-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74773-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It looks alright. If you look at the HTML of <a href="http://localhost:7070/search.php?q=Moscow&amp;polygon_geojson=1">http://localhost:7070/search.php?q=Moscow&amp;polygon_geojson=1</a> do you see a section <code>var nominatim_map_init</code> that lists the tile URL?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 May '20, 17:26</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span> </br></br></p>
</div>
</div>
<div id="comments-container-74773" class="comments-container">
&#10;</div>
<div id="comment-tools-74773" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74773-form-container" class="comment-form-container">
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

