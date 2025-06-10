+++
type = "question"
title = "Getting empty XML for node"
description = '''Hello I am using the xml information of the nodes for creating my keywords. Now I found a node which have information (and detailed ones) in the frontend at openstretmap . When I am opening the xml file it is responsing nothing and getting a 404. Is there a problem at the server or what is the probl...'''
date = "2013-10-20T10:44:00Z"
lastmod = "2013-10-20T20:20:00Z"
weight = 27349
keywords = [ "xml", "node", "empty" ]
aliases = [ "/questions/27349" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Getting empty XML for node](/questions/27349/getting-empty-xml-for-node)

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
<span id="post-27349-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27349-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-27349-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello</p>
<p>I am using the xml information of the nodes for creating my keywords. Now I found a node which have information (and detailed ones) in the <a href="http://www.openstreetmap.org/browse/node/2423996408">frontend at openstretmap</a> . When I am opening the <a href="http://www.openstreetmap.org/api/0.6/node/2423996408">xml file</a> it is responsing nothing and getting a 404.</p>
<p>Is there a problem at the server or what is the problem there?</p>
<p>Thanks for your help Robert</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-empty" rel="tag" title="see questions tagged &#39;empty&#39;">empty</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Oct '13, 10:44</strong></p>
<img src="https://secure.gravatar.com/avatar/019ee6038ea69bbe8b4571e637dbbdfb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rokdd&#39;s gravatar image" />
<p><span>rokdd</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rokdd has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-27349" class="comments-container">
&#10;</div>
<div id="comment-tools-27349" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27349-form-container" class="comment-form-container">
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

<span id="27357"></span>

<div id="answer-container-27357" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27357-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27357-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-27357-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rokdd has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There was a recently fixed <a href="https://github.com/zerebubuth/openstreetmap-cgimap/commit/e3c3fb1b412d6281f752fced12d8cd8a2eb4ef43">bug</a> with cgimap, the software that powers these API calls. Everything now appears to be working.</p>
<p>Keep in mind that if you need multiple nodes, the <a href="http://wiki.openstreetmap.org/wiki/API_v0.6#Multi_fetch:_GET_.2Fapi.2F0.6.2F.5Bnodes.7Cways.7Crelations.5D.3F.23parameters">nodes call</a> is faster.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Oct '13, 20:20</strong></p>
<img src="https://secure.gravatar.com/avatar/5634c46072077e10f5b7c0da9b4bbb62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pnorman&#39;s gravatar image" />
<p><span>pnorman</span><br />
<span class="score" title="2352 reputation points"><span>2.4k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pnorman has 9 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Oct '13, 18:55</strong> </span></p>
</div>
</div>
<div id="comments-container-27357" class="comments-container">
&#10;</div>
<div id="comment-tools-27357" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27357-form-container" class="comment-form-container">
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

