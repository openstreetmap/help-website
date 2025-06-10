+++
type = "question"
title = "Delete and recreate a node or rename it ?"
description = '''My question seems simple, however I cannot find any example in nodes definition in connection whith it. Suppose there is a node whith amenity=bar. When new owners come and replace old ones and open à new bar, should I update all node tags or should I delete and create à new node? As There is still a...'''
date = "2017-09-02T08:37:00Z"
lastmod = "2017-09-02T08:53:00Z"
weight = 58920
keywords = [ "node", "policy", "rename", "change", "delete" ]
aliases = [ "/questions/58920" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Delete and recreate a node or rename it ?](/questions/58920/delete-and-recreate-a-node-or-rename-it)

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
<span id="post-58920-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58920-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-58920-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My question seems simple, however I cannot find any example in nodes definition in connection whith it.</p>
<p>Suppose there is a node whith amenity=bar. When new owners come and replace old ones and open à new bar, should I update all node tags or should I delete and create à new node?</p>
<p>As There is still an amenity at the same place, until now I chose the second option.</p>
<p>Now another case: a bar closes and nobody renew it. I did deletion in these cases because otherwhise it appears as existing whereas it is closed. I realize now that maybe I should use the "disused" keyword instead because it is physically still there. I guess the map should display what exists, the fact that it is closed should be tagged in the data. One or those I deleted is a brand new bar and I have to recreate a bar whereas I could have reused the old one with position data.</p>
<p>So in the end, in which cases should I delete a node ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-policy" rel="tag" title="see questions tagged &#39;policy&#39;">policy</span> <span class="post-tag tag-link-rename" rel="tag" title="see questions tagged &#39;rename&#39;">rename</span> <span class="post-tag tag-link-change" rel="tag" title="see questions tagged &#39;change&#39;">change</span> <span class="post-tag tag-link-delete" rel="tag" title="see questions tagged &#39;delete&#39;">delete</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Sep '17, 08:37</strong></p>
<img src="https://secure.gravatar.com/avatar/6617165b639ae9a6455e07f2927cc6b4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cedric%20dinca&#39;s gravatar image" />
<p><span>cedric dinca</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cedric dinca has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-58920" class="comments-container">
&#10;</div>
<div id="comment-tools-58920" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58920-form-container" class="comment-form-container">
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

<span id="58921"></span>

<div id="answer-container-58921" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58921-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58921-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-58921-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cedric dinca has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Simply rename/update the existing node, doing that keeps the object history easily accessible (if you delete it, that is still available, but you need to know the object id to retrieve it).</p>
<p>If things really don't exist any more and there is no chance of reopening, then pls delete the object in question.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Sep '17, 08:53</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-58921" class="comments-container">
&#10;</div>
<div id="comment-tools-58921" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58921-form-container" class="comment-form-container">
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

