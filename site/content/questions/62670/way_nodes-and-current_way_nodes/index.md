+++
type = "question"
title = "Way_nodes and current_way_nodes"
description = '''What is the difference between way nodes and current_way nodes table?'''
date = "2018-03-14T09:39:00Z"
lastmod = "2018-03-14T16:05:00Z"
weight = 62670
keywords = [ "table", "nodes", "osm", "database" ]
aliases = [ "/questions/62670" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Way_nodes and current_way_nodes](/questions/62670/way_nodes-and-current_way_nodes)

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
<span id="post-62670-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62670-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62670-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What is the difference between way nodes and current_way nodes table?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-table" rel="tag" title="see questions tagged &#39;table&#39;">table</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Mar '18, 09:39</strong></p>
<img src="https://secure.gravatar.com/avatar/7da63bcb858ed2c1e1f25aa2d3d00106?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_partha&#39;s gravatar image" />
<p><span>_partha</span><br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_partha has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62670" class="comments-container">
<span id="62672"></span>
<div id="comment-62672" class="comment">
<div id="post-62672-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Where do you find those?</p>
</div>
<div id="comment-62672-info" class="comment-info">
<span class="comment-age">(14 Mar '18, 09:44)</span> <span class="comment-user userinfo">Hjart</span>
</div>
</div>
<span id="62673"></span>
<div id="comment-62673" class="comment">
<div id="post-62673-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://wiki.openstreetmap.org/wiki/Database/TableInfoDump">https://wiki.openstreetmap.org/wiki/Database/TableInfoDump</a></p>
</div>
<div id="comment-62673-info" class="comment-info">
<span class="comment-age">(14 Mar '18, 09:47)</span> <span class="comment-user userinfo">_partha</span>
</div>
</div>
<span id="62674"></span>
<div id="comment-62674" class="comment">
<div id="post-62674-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Far from all nodes in the database are visible and the current* could could be those that are (currently) visible</p>
</div>
<div id="comment-62674-info" class="comment-info">
<span class="comment-age">(14 Mar '18, 10:43)</span> <span class="comment-user userinfo">Hjart</span>
</div>
</div>
</div>
<div id="comment-tools-62670" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62670-form-container" class="comment-form-container">
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

<span id="62678"></span>

<div id="answer-container-62678" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62678-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62678-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-62678-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="_partha has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>current_way_nodes describes the links between a currently visible way and its nodes. way_nodes does the same, but for all ways, including older or deleted versions. If you have freshly populated a database with osmosis, both tables will have the same content but if you start editing on your database using the rails port, then the contents will diverge.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Mar '18, 16:05</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-62678" class="comments-container">
&#10;</div>
<div id="comment-tools-62678" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62678-form-container" class="comment-form-container">
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

