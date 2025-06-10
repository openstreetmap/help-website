+++
type = "question"
title = "We tried to resolve the data but some nodes are still missing"
description = '''I am trying to get the lat and long of all nodes of a way.  Here is the query : import overpy api = overpy.Overpass() result = api.query(&quot;&quot;&quot;way[&quot;name&quot;=&quot;New York&quot;];out;&quot;&quot;&quot;) result.ways for way in result.ways:  for node in way.nodes:  n_id = node.id  n_id_lat = node.lat  n_id_lon = node.lon The error ...'''
date = "2020-12-16T12:21:00Z"
lastmod = "2020-12-16T15:21:00Z"
weight = 77950
keywords = [ "python", "overpass" ]
aliases = [ "/questions/77950" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [We tried to resolve the data but some nodes are still missing](/questions/77950/we-tried-to-resolve-the-data-but-some-nodes-are-still-missing)

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
<span id="post-77950-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77950-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77950-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to get the lat and long of all nodes of a way. Here is the query :</p>
<p><code>import overpy api = overpy.Overpass() result = api.query("""way["name"="New York"];out;""") result.ways</code></p>
<p><code>for way in result.ways: for node in way.nodes: n_id = node.id n_id_lat = node.lat n_id_lon = node.lon</code></p>
<p>The error occurs when I loop each way:</p>
<p>This is the error I get : <strong><code>We tried to resolve the data but some nodes are still missing DataIncomplete: ('Data incomplete try to improve the query to resolve the missing data', 'Resolve missing nodes is disabled')</code></strong></p>
<p>How could I manage it, any hints will be welcome.<br />
Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Dec '20, 12:21</strong></p>
<img src="https://secure.gravatar.com/avatar/68b001d382235f9caa18384183210af0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dykay&#39;s gravatar image" />
<p><span>Dykay</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dykay has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-77950" class="comments-container">
&#10;</div>
<div id="comment-tools-77950" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77950-form-container" class="comment-form-container">
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

<span id="77952"></span>

<div id="answer-container-77952" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77952-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77952-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77952-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><code>out;</code> on its own doesn't return co-ordinates, try <code>out geom;</code></p>
<p>There are only 66 way with that name in the world; you may have defined your search area to one which doesn't include such an entity?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Dec '20, 15:21</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-77952" class="comments-container">
&#10;</div>
<div id="comment-tools-77952" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77952-form-container" class="comment-form-container">
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

