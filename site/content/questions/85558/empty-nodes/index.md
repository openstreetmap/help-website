+++
type = "question"
title = "Empty nodes"
description = '''Why some number of element id keep empty even the greater number has been used E.g. https://www.openstreetmap.org/node/6358775424 Not found but +1000 https://www.openstreetmap.org/node/6358776424  Is used, as one node that part of the way with id 679072985, tagged as barrier=hedge by Ninjoh on 2019-...'''
date = "2022-09-04T14:40:00Z"
lastmod = "2022-09-04T18:49:00Z"
weight = 85558
keywords = [ "ways", "nodes", "elements", "id", "relations" ]
aliases = [ "/questions/85558" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Empty nodes](/questions/85558/empty-nodes)

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
<span id="post-85558-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85558-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85558-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Why some number of element id keep empty even the greater number has been used</p>
<p>E.g.</p>
<p><a href="https://www.openstreetmap.org/node/6358775424">https://www.openstreetmap.org/node/6358775424</a></p>
<p>Not found</p>
<p>but +1000</p>
<p><a href="https://www.openstreetmap.org/node/6358776424">https://www.openstreetmap.org/node/6358776424</a></p>
<p>Is used, as one node that part of the way with id 679072985, tagged as barrier=hedge by Ninjoh on 2019-03-24T17:46:52Z</p>
<p>Why some number keep from uses? Thanks for explaining.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-elements" rel="tag" title="see questions tagged &#39;elements&#39;">elements</span> <span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Sep '22, 14:40</strong></p>
<img src="https://secure.gravatar.com/avatar/54c91e740f80315f515fd212db923d30?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MY5DVrAr0e599Japan&#39;s gravatar image" />
<p><span>MY5DVrAr0e59...</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MY5DVrAr0e599Japan has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-85558" class="comments-container">
&#10;</div>
<div id="comment-tools-85558" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85558-form-container" class="comment-form-container">
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

<span id="85561"></span>

<div id="answer-container-85561" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85561-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-85561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is an internal implementation detail in the way PostgreSQL manages its unique sequences. Sometimes new IDs are assigned but then not used e.g. because of a transaction rollback or other technical reasons. Therefore, our documentation makes no assurances about IDs other than that they are unique. They can have gaps, and it can even be possible that an object with a smaller ID is created after an object with a larger ID.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Sep '22, 18:49</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-85561" class="comments-container">
&#10;</div>
<div id="comment-tools-85561" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85561-form-container" class="comment-form-container">
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

