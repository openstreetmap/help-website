+++
type = "question"
title = "Getting way-id from its nodes id"
description = '''Hi, I need to get the id of a &quot;way&quot; when I only have the way&#x27;s node IDs, at least two such nodes that are given to be associated with, or sit exactly on that way. What would you recommend as the procedure to achieve this? I&#x27;m in-familiar with OSM&#x27;s API and couldn&#x27;t find an answer here. Thanks!'''
date = "2013-01-23T08:20:00Z"
lastmod = "2013-01-23T12:56:00Z"
weight = 19276
keywords = [ "api" ]
aliases = [ "/questions/19276" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Getting way-id from its nodes id](/questions/19276/getting-way-id-from-its-nodes-id)

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
<span id="post-19276-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19276-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19276-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I need to get the id of a "way" when I only have the way's node IDs, at least two such nodes that are given to be associated with, or sit exactly on that way.</p>
<p>What would you recommend as the procedure to achieve this? I'm in-familiar with OSM's API and couldn't find an answer here.</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jan '13, 08:20</strong></p>
<img src="https://secure.gravatar.com/avatar/838b397db3fd84dd13be207a88699f99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Boaz&#39;s gravatar image" />
<p><span>Boaz</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Boaz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19276" class="comments-container">
&#10;</div>
<div id="comment-tools-19276" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19276-form-container" class="comment-form-container">
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

<span id="19277"></span>

<div id="answer-container-19277" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19277-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19277-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19277-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try "<a href="https://wiki.openstreetmap.org/wiki/Api06#Ways_for_node:_GET_.2Fapi.2F0.6.2Fnode.2F.23id.2Fways">ways for node</a>" perhaps.</p>
<p>Edit: Sorry, I read "in-familiar" as familiar. So, for example, for node 1818806301</p>
<p><a href="http://api.openstreetmap.org/api/0.6/node/1818806301/ways">http://api.openstreetmap.org/api/0.6/node/1818806301/ways</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jan '13, 08:29</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jan '13, 08:31</strong> </span></p>
</div>
</div>
<div id="comments-container-19277" class="comments-container">
<span id="19278"></span>
<div id="comment-19278" class="comment">
<div id="post-19278-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>that's great, but i'll need locally run, best performance solution. What schema do you recommend for installation and what API package would you use? Also, given the way-id i'll need to create/update a tag for the way. maybe that has implications on the API package. Thanks!</p>
</div>
<div id="comment-19278-info" class="comment-info">
<span class="comment-age">(23 Jan '13, 08:40)</span> <span class="comment-user userinfo">Boaz</span>
</div>
</div>
<span id="19281"></span>
<div id="comment-19281" class="comment">
<div id="post-19281-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I saw your discussion on the #osm IRC channel, where I think pgsnapshot schema was recommended. That's beyond me at the moment though as I've not tried it.</p>
</div>
<div id="comment-19281-info" class="comment-info">
<span class="comment-age">(23 Jan '13, 10:18)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="19282"></span>
<div id="comment-19282" class="comment">
<div id="post-19282-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Gotcha. Indeed, that was me on the IRC. I'm going to give the recommendations given through IRC a shot. Thanks!</p>
</div>
<div id="comment-19282-info" class="comment-info">
<span class="comment-age">(23 Jan '13, 12:56)</span> <span class="comment-user userinfo">Boaz</span>
</div>
</div>
</div>
<div id="comment-tools-19277" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19277-form-container" class="comment-form-container">
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

