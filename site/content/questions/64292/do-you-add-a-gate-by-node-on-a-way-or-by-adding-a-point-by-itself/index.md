+++
type = "question"
title = "Do you add a gate by node on a way, or by adding a point by itself?"
description = '''I see two ways of adding a barrier (gate):  1. Click on the road way, add vertex and then designate this node as a barrier  2. Choose the Point editing tool and add a separate node, tag as barrier --&amp;gt; gate. Which is the recommended approach? I&#x27;m thinking a node on the road way would be best, is t...'''
date = "2018-06-20T23:09:00Z"
lastmod = "2018-06-22T01:19:00Z"
weight = 64292
keywords = [ "node", "gate", "way", "barrier" ]
aliases = [ "/questions/64292" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Do you add a gate by node on a way, or by adding a point by itself?](/questions/64292/do-you-add-a-gate-by-node-on-a-way-or-by-adding-a-point-by-itself)

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
<span id="post-64292-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64292-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-64292-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I see two ways of adding a barrier (gate): 1. Click on the road way, add vertex and then designate this node as a barrier 2. Choose the Point editing tool and add a separate node, tag as barrier --&gt; gate.</p>
<p>Which is the recommended approach? I'm thinking a node on the road way would be best, is this node associated with road way? I see a lot of instances where a user will add a point as the gate/barrier but it's not on the road way itself, but may be very close in proximity. How do routing engines handle this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-gate" rel="tag" title="see questions tagged &#39;gate&#39;">gate</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span> <span class="post-tag tag-link-barrier" rel="tag" title="see questions tagged &#39;barrier&#39;">barrier</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jun '18, 23:09</strong></p>
<img src="https://secure.gravatar.com/avatar/146f9c2b954b5bbe3c30ae5f4be407e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="markzawi&#39;s gravatar image" />
<p><span>markzawi</span><br />
<span class="score" title="71 reputation points">71</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="markzawi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64292" class="comments-container">
<span id="64294"></span>
<div id="comment-64294" class="comment">
<div id="post-64294-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>"How do routing engines handle this?" They don't if it is not part of the way.</p>
</div>
<div id="comment-64294-info" class="comment-info">
<span class="comment-age">(21 Jun '18, 07:47)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-64292" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64292-form-container" class="comment-form-container">
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

<span id="64293"></span>

<div id="answer-container-64293" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64293-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64293-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-64293-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I always put it on the way. I believe JOSM even complains with a warning for barrier nodes that are not placed on a way. It is an obstacle on a road, so it also belongs there.</p>
<p>It is also described as such on the <a href="https://wiki.openstreetmap.org/wiki/Key:barrier">wiki</a>.</p>
<p>AFAIK, there are not a lot of routing engines that block routing over a way when there is only a node with access restrictions. They only use access restrictions on the way. IMHO, this is a bug and not a reason to add a short OSM way with restrictions. An example is a bollard in the middle of the road that can be approached from both sides. In such case it should be suffcient to add a node with e.g. barrier=bollard; motor_vehicle=no</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jun '18, 04:22</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jun '18, 06:20</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/15d45a99f101e06c9e79916af33f8336?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Privatemajory&#39;s gravatar image" />
<p><span>Privatemajory</span><br />
<span class="score" title="1125 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span></p>
</div>
</div>
<div id="comments-container-64293" class="comments-container">
<span id="64295"></span>
<div id="comment-64295" class="comment">
<div id="post-64295-score" class="comment-score">
5
</div>
<div class="comment-text">
<p>Both OSRM and Graphhopper, the two most popular routing engines, will block routes through barrier nodes if configured appropriately. (For example, cycle.travel, which uses OSRM, will not route bikes past a barrier=stile.)</p>
</div>
<div id="comment-64295-info" class="comment-info">
<span class="comment-age">(21 Jun '18, 08:17)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="64296"></span>
<div id="comment-64296" class="comment">
<div id="post-64296-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Richard, thank you for this info. It's great to hear that they start to implement this.</p>
</div>
<div id="comment-64296-info" class="comment-info">
<span class="comment-age">(21 Jun '18, 08:20)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="64313"></span>
<div id="comment-64313" class="comment">
<div id="post-64313-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for the replies, much appreciated <a href="https://help.openstreetmap.org/users/5390/escada">@escada</a></p>
</div>
<div id="comment-64313-info" class="comment-info">
<span class="comment-age">(22 Jun '18, 01:19)</span> <span class="comment-user userinfo">markzawi</span>
</div>
</div>
</div>
<div id="comment-tools-64293" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64293-form-container" class="comment-form-container">
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

