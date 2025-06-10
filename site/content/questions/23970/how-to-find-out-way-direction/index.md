+++
type = "question"
title = "How to find out way direction"
description = '''Hi, i&#x27;m using the overpass api to query for ways around a given gps position with the ultimative aim to extract maxspeed values.  However, i came across a way that had different maxspeed tags for forward and backward direction. Now how do i find out, wich direction (i.e. heading in degrees) is forwa...'''
date = "2013-07-04T12:24:00Z"
lastmod = "2013-07-04T12:57:00Z"
weight = 23970
keywords = [ "overpass", "direction", "maxspeed", "way" ]
aliases = [ "/questions/23970" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to find out way direction](/questions/23970/how-to-find-out-way-direction)

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
<span id="post-23970-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23970-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-23970-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>i'm using the overpass api to query for ways around a given gps position with the ultimative aim to extract maxspeed values. However, i came across a way that had different maxspeed tags for forward and backward direction. Now how do i find out, wich direction (i.e. heading in degrees) is forward and which is backwards for a given way(-segment)? Is there some general rule to that like increasing node ids or similar? regards,d</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-direction" rel="tag" title="see questions tagged &#39;direction&#39;">direction</span> <span class="post-tag tag-link-maxspeed" rel="tag" title="see questions tagged &#39;maxspeed&#39;">maxspeed</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jul '13, 12:24</strong></p>
<img src="https://secure.gravatar.com/avatar/400da7747a91949c1173e09aeb963076?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dlr_ts&#39;s gravatar image" />
<p><span>dlr_ts</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dlr_ts has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-23970" class="comments-container">
&#10;</div>
<div id="comment-tools-23970" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23970-form-container" class="comment-form-container">
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

<span id="23973"></span>

<div id="answer-container-23973" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23973-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23973-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-23973-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dlr_ts has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is just the sorting of the nodes. "A way is an <em>ordered</em> list of nodes […]" (<span>way</span> in wiki; emphasis by me). Also see: <span>the methods to see the direction (rather targeted towards mappers)</span>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jul '13, 12:46</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jul '13, 12:51</strong> </span></p>
</div>
</div>
<div id="comments-container-23973" class="comments-container">
<span id="23975"></span>
<div id="comment-23975" class="comment">
<div id="post-23975-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>does "ordered" refers to node-id (numerical ordering) or is the order in which the nodes appear in the xml-output is meant?</p>
</div>
<div id="comment-23975-info" class="comment-info">
<span class="comment-age">(04 Jul '13, 12:53)</span> <span class="comment-user userinfo">dlr_ts</span>
</div>
</div>
<span id="23976"></span>
<div id="comment-23976" class="comment">
<div id="post-23976-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>no, there is no numercial ordering. The node ids (numbers) are not related to a way, they are independent object identifiers. If a node is also used by other ways (e.g. way intersections) the ways list the same node id.</p>
<p>The direction is set by the "order in which the nodes appear in the xml-output".</p>
</div>
<div id="comment-23976-info" class="comment-info">
<span class="comment-age">(04 Jul '13, 12:57)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-23973" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23973-form-container" class="comment-form-container">
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

