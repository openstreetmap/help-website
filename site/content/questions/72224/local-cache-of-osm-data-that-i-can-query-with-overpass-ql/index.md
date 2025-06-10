+++
type = "question"
title = "Local cache of OSM data that I can query with Overpass QL"
description = '''I&#x27;m making an application that will need to query OSM data using Overpass QL. Instead of querying https://overpass-turbo.eu/ for every user request, I would like to query the data once, and cache it in my own database. Future queries in the same area would use the cached data. How can I do this? Wou...'''
date = "2019-12-27T01:52:00Z"
lastmod = "2019-12-27T15:12:00Z"
weight = 72224
keywords = [ "java", "overpass-ql", "offlinemaps" ]
aliases = [ "/questions/72224" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Local cache of OSM data that I can query with Overpass QL](/questions/72224/local-cache-of-osm-data-that-i-can-query-with-overpass-ql)

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
<span id="post-72224-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72224-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72224-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm making an application that will need to query OSM data using Overpass QL. Instead of querying <a href="https://overpass-turbo.eu/">https://overpass-turbo.eu/</a> for every user request, I would like to query the data once, and cache it in my own database. Future queries in the same area would use the cached data.</p>
<p>How can I do this? Would I need to setup some kind of local OSM server with the cached data? Is there a guide somewhere on how to do that?</p>
<p>If that's not readily available and I have to do a lot myself, how much of it do I have to do from scratch? Will I need to design a database model for the data myself, and then query from overpass-turbo and store in my own DB? Do I need to write my own parser for Overpass QL for my application to query from my "osm cache" db?</p>
<p>Is there already a library (for Java) that can do what I'm looking for so I won't have to reinvent the wheel?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span> <span class="post-tag tag-link-offlinemaps" rel="tag" title="see questions tagged &#39;offlinemaps&#39;">offlinemaps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Dec '19, 01:52</strong></p>
<img src="https://secure.gravatar.com/avatar/b963eb1a8b1152bb420093dc2c9bbcc7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="devil0150&#39;s gravatar image" />
<p><span>devil0150</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="devil0150 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72224" class="comments-container">
&#10;</div>
<div id="comment-tools-72224" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72224-form-container" class="comment-form-container">
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

<span id="72233"></span>

<div id="answer-container-72233" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72233-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72233-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72233-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Overpass is open <a href="https://github.com/drolbr/Overpass-API">source</a> and has installation instructions <a href="https://overpass-api.de/no_frills.html">online</a>. I don't know if there is a way to cache as you describe, but the whole database can be cloned during setup and kept up to date with diffs.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Dec '19, 15:12</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-72233" class="comments-container">
&#10;</div>
<div id="comment-tools-72233" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72233-form-container" class="comment-form-container">
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

