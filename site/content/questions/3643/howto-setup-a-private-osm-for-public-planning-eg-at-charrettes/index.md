+++
type = "question"
title = "howto setup a private OSM for public planning, e.g., at charrettes?"
description = '''How to setup a local, &quot;private&quot; OpenStreetMap for planning purposes, e.g., at public charrettes? Since this would be used to &quot;map&quot; hypothetical features, I am advised not to use the public instance of OSM, but to &quot;create your own OSM stack and run it locally.&quot; I am also advised that &quot;There&#x27;s lots of...'''
date = "2011-03-08T16:22:00Z"
lastmod = "2011-03-08T17:13:00Z"
weight = 3643
keywords = [ "private_osm", "charrettes", "planning", "private_server", "local_osm" ]
aliases = [ "/questions/3643" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [howto setup a private OSM for public planning, e.g., at charrettes?](/questions/3643/howto-setup-a-private-osm-for-public-planning-eg-at-charrettes)

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
<span id="post-3643-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3643-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3643-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How to setup a local, "private" OpenStreetMap for planning purposes, e.g., at public charrettes? Since this would be used to "map" hypothetical features, I am advised <strong>not</strong> to use the public instance of OSM, but to "create your own OSM stack and run it locally." I am also advised that "There's lots of documentation on the wiki," which is certainly true :-) Unfortunately my searches of <a href="http://wiki.openstreetmap.org">wiki.openstreetmap.org</a>, <a href="http://lists.openstreetmap.org">lists.openstreetmap.org</a>, and <a href="http://help.openstreetmap.org">help.openstreetmap.org</a> have not found answers to this question, nor am I seeing anything about this in the <a href="http://wiki.openstreetmap.org/wiki/FAQ">FAQ</a>.</p>
<p>Can someone point me to the appropriate documentation page(s), or other channel(s) for getting answers to this question? Regarding appropriateness: I have considerable background in systems (esp linux) and informatics generally, but not much specifically in GIS or OSM (of which I am mostly a read-only user, though I have edited).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-private_osm" rel="tag" title="see questions tagged &#39;private_osm&#39;">private_osm</span> <span class="post-tag tag-link-charrettes" rel="tag" title="see questions tagged &#39;charrettes&#39;">charrettes</span> <span class="post-tag tag-link-planning" rel="tag" title="see questions tagged &#39;planning&#39;">planning</span> <span class="post-tag tag-link-private_server" rel="tag" title="see questions tagged &#39;private_server&#39;">private_server</span> <span class="post-tag tag-link-local_osm" rel="tag" title="see questions tagged &#39;local_osm&#39;">local_osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Mar '11, 16:22</strong></p>
<img src="https://secure.gravatar.com/avatar/7dfc0f59d3bd13e7eb692fac1586d458?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomRoche&#39;s gravatar image" />
<p><span>TomRoche</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomRoche has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-3643" class="comments-container">
&#10;</div>
<div id="comment-tools-3643" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3643-form-container" class="comment-form-container">
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

<span id="3644"></span>

<div id="answer-container-3644" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3644-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3644-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-3644-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want so set up your own OSM database server that can then be edited with standard OSM editors like JOSM, you need the <a href="http://wiki.openstreetmap.org/wiki/Rails_port">Rails Port</a>. If you want to fill that with some "real" data to begin with, you will need <a href="http://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a>. These steps however give you only the database side of things; if you then further want to create web maps from your database, you will need to set up a <a href="http://wiki.openstreetmap.org/wiki/Mapnik">tile server</a>, too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Mar '11, 17:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-3644" class="comments-container">
&#10;</div>
<div id="comment-tools-3644" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3644-form-container" class="comment-form-container">
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

