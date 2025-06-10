+++
type = "question"
title = "Best Practice for Super Relations"
description = '''Dear All, I am in the process of splitting a large relation (previously 523 members and I understand 300 is the maximum recommended) into a super relation made up of two children. The relation describes a ring road which has twin one-way ways throughout its route. I propose to have one child with al...'''
date = "2013-04-12T00:06:00Z"
lastmod = "2013-04-12T11:05:00Z"
weight = 21419
keywords = [ "super-relations", "relations" ]
aliases = [ "/questions/21419" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Best Practice for Super Relations](/questions/21419/best-practice-for-super-relations)

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
<span id="post-21419-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21419-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21419-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear All,</p>
<p>I am in the process of splitting a large relation (previously 523 members and I understand 300 is the maximum recommended) into a super relation made up of two children. The relation describes a ring road which has twin one-way ways throughout its route. I propose to have one child with all members in the role of "forward" (clockwise righthand carriageway) and another as "backward" (anticlockwise lefthand carriageway). I understand the mechanics of how to do this with JOSM but the question is, what is best practice for the order of the "backward" child? As a trivial example, if the first four members of "forward" are A, B, C, D, should "backward" have the same order or should it be reversed i.e. D, C, B, A?</p>
<p>Many thanks in advance,</p>
<p>Feilipu</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-super-relations" rel="tag" title="see questions tagged &#39;super-relations&#39;">super-relations</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Apr '13, 00:06</strong></p>
<img src="https://secure.gravatar.com/avatar/4afbcc50f5d94cce5f85c1da49f3de6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Feilipu&#39;s gravatar image" />
<p><span>Feilipu</span><br />
<span class="score" title="90 reputation points">90</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Feilipu has one accepted answer">10%</span></p>
</div>
</div>
<div id="comments-container-21419" class="comments-container">
<span id="21426"></span>
<div id="comment-21426" class="comment">
<div id="post-21426-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>A link to the actual relation might help here, so that people can see the way direction on each carriageway among other things.</p>
</div>
<div id="comment-21426-info" class="comment-info">
<span class="comment-age">(12 Apr '13, 00:56)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-21419" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21419-form-container" class="comment-form-container">
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

<span id="21420"></span>

<div id="answer-container-21420" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21420-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21420-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21420-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It should be forward and forward, otherwise the anticlockwise left-hand carriageway would be going backwards - Cars don't drive backwards!</p>
<p>The first four members, or the order of each child, should be according to the customary direction of the ways, and the roles of the children relations should both be "forward", hence:</p>
<p>A---&gt;B---&gt;C---&gt;D D---&gt;C---&gt;B---&gt;A</p>
<p>Where letters represent junctions they pass through.</p>
<p>A backwards relation would only be necessary if the route was entirely two-way. Of course a motorway isn't usually two way in the UK. The only one that was a single carriageway that was (A6144(M)) was downgraded some time ago.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '13, 00:09</strong></p>
<img src="https://secure.gravatar.com/avatar/8f5a4305a1d89bc4eb700ced34e5b3e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amaroussi&#39;s gravatar image" />
<p><span>Amaroussi</span><br />
<span class="score" title="141 reputation points">141</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amaroussi has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Apr '13, 03:27</strong> </span></p>
</div>
</div>
<div id="comments-container-21420" class="comments-container">
<span id="21421"></span>
<div id="comment-21421" class="comment">
<div id="post-21421-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the quick reponse but traffic is flowing in opposite directions - there is no question of cars driving backwards. D&lt;---C&lt;---B&lt;---A D---&gt;C---&gt;B---&gt;A</p>
</div>
<div id="comment-21421-info" class="comment-info">
<span class="comment-age">(12 Apr '13, 00:20)</span> <span class="comment-user userinfo">Feilipu</span>
</div>
</div>
<span id="21422"></span>
<div id="comment-21422" class="comment">
<div id="post-21422-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is it a dual carriageway or single? The order for anti clockwise dual carriageways should be DCBA and the role generally forward for the customary direction of the one-way route. Sorry for the hurry but I am nearly going to bed.</p>
</div>
<div id="comment-21422-info" class="comment-info">
<span class="comment-age">(12 Apr '13, 00:21)</span> <span class="comment-user userinfo">Amaroussi</span>
</div>
</div>
<span id="21423"></span>
<div id="comment-21423" class="comment">
<div id="post-21423-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It is a motorway in both directions</p>
</div>
<div id="comment-21423-info" class="comment-info">
<span class="comment-age">(12 Apr '13, 00:28)</span> <span class="comment-user userinfo">Feilipu</span>
</div>
</div>
<span id="21424"></span>
<div id="comment-21424" class="comment">
<div id="post-21424-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The first four members, or the order of each child, should be according to the customary direction of the ways, and the roles of the children relations should both be "forward", hence:</p>
<p>A---&gt;B---&gt;C---&gt;D D---&gt;C---&gt;B---&gt;A</p>
<p>Where letters represent junctions they pass through.</p>
</div>
<div id="comment-21424-info" class="comment-info">
<span class="comment-age">(12 Apr '13, 00:35)</span> <span class="comment-user userinfo">Amaroussi</span>
</div>
</div>
<span id="21430"></span>
<div id="comment-21430" class="comment">
<div id="post-21430-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK, seems logical. I thought that a backward relation might be used by route finding apps etc. Is it superfluous in this case?</p>
</div>
<div id="comment-21430-info" class="comment-info">
<span class="comment-age">(12 Apr '13, 01:30)</span> <span class="comment-user userinfo">Feilipu</span>
</div>
</div>
<span id="21431"></span>
<div id="comment-21431" class="comment not_top_scorer">
<div id="post-21431-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A backwards relation would only be necessary if the route was entirely two-way. Of course a motorway isn't usually two way in the UK. The only one that was a single carriageway that was (A6144(M)) was downgraded some time ago.</p>
</div>
<div id="comment-21431-info" class="comment-info">
<span class="comment-age">(12 Apr '13, 01:51)</span> <span class="comment-user userinfo">Amaroussi</span>
</div>
</div>
<span id="21433"></span>
<div id="comment-21433" class="comment not_top_scorer">
<div id="post-21433-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Amaroussi, I'm clear now.</p>
</div>
<div id="comment-21433-info" class="comment-info">
<span class="comment-age">(12 Apr '13, 02:16)</span> <span class="comment-user userinfo">Feilipu</span>
</div>
</div>
<span id="21449"></span>
<div id="comment-21449" class="comment not_top_scorer">
<div id="post-21449-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Amaroussi</span> - isn't there still the A601(M)?</p>
</div>
<div id="comment-21449-info" class="comment-info">
<span class="comment-age">(12 Apr '13, 11:05)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-21420" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-21420-form-container" class="comment-form-container">
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

