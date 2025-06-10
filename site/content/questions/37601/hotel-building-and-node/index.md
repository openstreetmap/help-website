+++
type = "question"
title = "Hotel building AND node?"
description = '''Hello, I&#x27;d like to use OSM data to make a simple (printable) city plan with hotels marked. Since the software I render the data in uses NODES for placing map symbols, not the hotel buildings (areas tagged with tourism=hotel), can I add nodes on top of the correctly tagged buildings? Or is it a wrong...'''
date = "2014-10-13T22:11:00Z"
lastmod = "2014-10-13T23:07:00Z"
weight = 37601
keywords = [ "node", "building", "tourism", "hotels" ]
aliases = [ "/questions/37601" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Hotel building AND node?](/questions/37601/hotel-building-and-node)

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
<span id="post-37601-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37601-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-37601-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I'd like to use OSM data to make a simple (printable) city plan with hotels marked. Since the software I render the data in uses NODES for placing map symbols, not the hotel buildings (areas tagged with tourism=hotel), can I add nodes on top of the correctly tagged buildings? Or is it a wrong approach? How would they render on OSM and how would it affect the search?</p>
<p>Thx for answers.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-tourism" rel="tag" title="see questions tagged &#39;tourism&#39;">tourism</span> <span class="post-tag tag-link-hotels" rel="tag" title="see questions tagged &#39;hotels&#39;">hotels</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Oct '14, 22:11</strong></p>
<img src="https://secure.gravatar.com/avatar/3a9a3844499216d67da6863c6a8bcee5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Houmr9&#39;s gravatar image" />
<p><span>Houmr9</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Houmr9 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37601" class="comments-container">
<span id="37603"></span>
<div id="comment-37603" class="comment">
<div id="post-37603-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you'd like nodes instead of ways in OSM data, I'd suggest that you look at the "<code>--all-to-nodes</code>" option of <a href="http://wiki.openstreetmap.org/wiki/Osmconvert">osmconvert</a>.</p>
</div>
<div id="comment-37603-info" class="comment-info">
<span class="comment-age">(13 Oct '14, 22:36)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="37605"></span>
<div id="comment-37605" class="comment">
<div id="post-37605-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Alright, I got ya guys. Cheers.</p>
</div>
<div id="comment-37605-info" class="comment-info">
<span class="comment-age">(13 Oct '14, 23:07)</span> <span class="comment-user userinfo">Houmr9</span>
</div>
</div>
</div>
<div id="comment-tools-37601" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37601-form-container" class="comment-form-container">
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

<span id="37604"></span>

<div id="answer-container-37604" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37604-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37604-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-37604-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Houmr9 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Two frequent <a href="http://wiki.openstreetmap.org/wiki/Good_practice">good practice</a> advice are <em>don't tag for the renderer</em> and <em>one feature, one OSM element</em>. You shouldn't add a hotel node if there already is a hotel area (it's actually common practice to "upgrade" a feature from a node to an area when adding details to the map).</p>
<p>Instead, you should either get your software to handle areas or, as SomeoneElse suggested, convert areas to nodes (in your local import, not in the osm db!) before using osmconvert's --all-to--nodes option.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Oct '14, 22:49</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-37604" class="comments-container">
&#10;</div>
<div id="comment-tools-37604" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37604-form-container" class="comment-form-container">
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

