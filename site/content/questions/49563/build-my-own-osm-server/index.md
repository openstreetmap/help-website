+++
type = "question"
title = "Build my own osm server"
description = '''I&#x27;m going to build my own nominatim and tile server, and I&#x27;d like to add POI to my own database(just for nominatim) to be used by my project. I have the following problems:  Can data be shared amount nominatim and tile server? How to add POI to my nominatim database, and at the same time, keep updat...'''
date = "2016-05-04T02:05:00Z"
lastmod = "2016-05-04T10:07:00Z"
weight = 49563
keywords = [ "nominatim", "tileserver" ]
aliases = [ "/questions/49563" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Build my own osm server](/questions/49563/build-my-own-osm-server)

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
<span id="post-49563-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49563-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49563-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm going to build my own nominatim and tile server, and I'd like to add POI to my own database(just for nominatim) to be used by my project. I have the following problems:</p>
<ol>
<li>Can data be shared amount nominatim and tile server?</li>
<li>How to add POI to my nominatim database, and at the same time, keep updating from osm server?</li>
<li>Need I install API like Rails Port on my server?</li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 May '16, 02:05</strong></p>
<img src="https://secure.gravatar.com/avatar/abfc3fd1ed62e96f328d93e006eeab89?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LAmour&#39;s gravatar image" />
<p><span>LAmour</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LAmour has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49563" class="comments-container">
&#10;</div>
<div id="comment-tools-49563" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49563-form-container" class="comment-form-container">
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

<span id="49566"></span>

<div id="answer-container-49566" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49566-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49566-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-49566-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can create an .osc file that contains your extra POIs, and add that file to both your Nominatim and tile databases with a manual invocation of <code>osm2pgsql</code>. You can use the JOSM editor to map your POIs and save as a .osm file, then convert that file manually to .osc format, renumbering all IDs to values so high that they won't conflict with OSM's values in the near future. You can then continue applying updates from OSM and your database will have both your data and OSM's data. However, if a POI is created in OSM that already exists in your private POI collection, then your database will have two instances of that POI.</p>
<p>You do not have to install the rails port unless you want multiple users to be able to connect to your database and edit the data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 May '16, 08:10</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-49566" class="comments-container">
<span id="49567"></span>
<div id="comment-49567" class="comment">
<div id="post-49567-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks! I also want to ask if it is possible to write an API to insert(via http) POI directly to nominatim database?</p>
</div>
<div id="comment-49567-info" class="comment-info">
<span class="comment-age">(04 May '16, 09:36)</span> <span class="comment-user userinfo">LAmour</span>
</div>
</div>
<span id="49570"></span>
<div id="comment-49570" class="comment">
<div id="post-49570-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>For info, the thing that handles updates to a rendering database is at <a href="https://github.com/openstreetmap/mod_tile/blob/master/openstreetmap-tiles-update-expire">https://github.com/openstreetmap/mod_tile/blob/master/openstreetmap-tiles-update-expire</a> - you can see how that calls osmosis.</p>
</div>
<div id="comment-49570-info" class="comment-info">
<span class="comment-age">(04 May '16, 10:07)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-49566" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49566-form-container" class="comment-form-container">
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

