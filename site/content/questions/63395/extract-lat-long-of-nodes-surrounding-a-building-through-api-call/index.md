+++
type = "question"
title = "Extract (lat, long) of nodes surrounding a building through API call"
description = '''Hi  I am trying to find a way to automatically export the (lat, long) of the nodes associated with the perimeter of a given building without using the UI, completely through API. The ideal solution would be given an address of a building (way with tag building in OSM terms) to fetch the (lat, long)s...'''
date = "2018-05-09T14:11:00Z"
lastmod = "2018-05-30T10:16:00Z"
weight = 63395
keywords = [ "building", "perimeter", "nodes", "api", "floorplan" ]
aliases = [ "/questions/63395" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extract (lat, long) of nodes surrounding a building through API call](/questions/63395/extract-lat-long-of-nodes-surrounding-a-building-through-api-call)

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
<span id="post-63395-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63395-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63395-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I am trying to find a way to automatically export the (lat, long) of the nodes associated with the perimeter of a given building without using the UI, completely through API. The ideal solution would be given an address of a building (way with tag building in OSM terms) to fetch the (lat, long)s of the associated nodes in an XML or plain text file.</p>
<p>Any insights? Kris</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-perimeter" rel="tag" title="see questions tagged &#39;perimeter&#39;">perimeter</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-floorplan" rel="tag" title="see questions tagged &#39;floorplan&#39;">floorplan</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 May '18, 14:11</strong></p>
<img src="https://secure.gravatar.com/avatar/2d8f03a80d79433ce2aa2809a2048e69?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hectorlavoe&#39;s gravatar image" />
<p><span>hectorlavoe</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hectorlavoe has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63395" class="comments-container">
&#10;</div>
<div id="comment-tools-63395" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63395-form-container" class="comment-form-container">
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

<span id="63396"></span>

<div id="answer-container-63396" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63396-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63396-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63396-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The standard API call</p>
<pre><code>http://api.openstreetmap.org/api/0.6/way/put_way_id_here/full</code></pre>
<p>returns an XML containing the way and all its nodes, though the order of the nodes in the response might be different from the order in which they have to be traversed to form the line (i.e. you will have to traverse them in the right order as given in the way object).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 May '18, 14:48</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-63396" class="comments-container">
<span id="63465"></span>
<div id="comment-63465" class="comment">
<div id="post-63465-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Frederik! That seems to be really helpful! However, the link gives me a 404 error. Could you please re-post?</p>
<p>Many thanks, Kris</p>
</div>
<div id="comment-63465-info" class="comment-info">
<span class="comment-age">(14 May '18, 15:03)</span> <span class="comment-user userinfo">hectorlavoe</span>
</div>
</div>
<span id="63466"></span>
<div id="comment-63466" class="comment">
<div id="post-63466-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You need to replace <code>put_way_id_here</code> with the way ID of your building.</p>
</div>
<div id="comment-63466-info" class="comment-info">
<span class="comment-age">(14 May '18, 15:05)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="63862"></span>
<div id="comment-63862" class="comment">
<div id="post-63862-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great, that's super neat! Thank you.</p>
</div>
<div id="comment-63862-info" class="comment-info">
<span class="comment-age">(30 May '18, 10:16)</span> <span class="comment-user userinfo">hectorlavoe</span>
</div>
</div>
</div>
<div id="comment-tools-63396" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63396-form-container" class="comment-form-container">
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

