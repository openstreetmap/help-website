+++
type = "question"
title = "Are intersecting ways possible?"
description = '''Is it possible for a set of two consecutive nodes to be part of more than one &#x27;way&#x27;? I am trying to identify a unique &#x27;way&#x27; that contains these two consecutive nodes.'''
date = "2021-11-10T07:14:00Z"
lastmod = "2021-11-10T10:58:00Z"
weight = 82535
keywords = [ "ways", "nodes", "osm" ]
aliases = [ "/questions/82535" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Are intersecting ways possible?](/questions/82535/are-intersecting-ways-possible)

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
<span id="post-82535-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82535-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82535-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible for a set of two consecutive nodes to be part of more than one 'way'? I am trying to identify a unique 'way' that contains these two consecutive nodes.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Nov '21, 07:14</strong></p>
<img src="https://secure.gravatar.com/avatar/dc43ae77e987854246ab4f6c496da9a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ayuz&#39;s gravatar image" />
<p><span>ayuz</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ayuz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Nov '21, 07:22</strong> </span></p>
</div>
</div>
<div id="comments-container-82535" class="comments-container">
&#10;</div>
<div id="comment-tools-82535" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82535-form-container" class="comment-form-container">
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

<span id="82536"></span>

<div id="answer-container-82536" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82536-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82536-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-82536-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ayuz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That happens a lot, actually, when objects share a common border, e.g. adjacent buildings or adjacent landuses. Each object will have its own way but they share common nodes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Nov '21, 08:01</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-82536" class="comments-container">
<span id="82537"></span>
<div id="comment-82537" class="comment">
<div id="post-82537-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hm I see. Thanks for the answer. I think in my use case, I am only interested in roads so if the roads are guaranteed to be unique that is fine. Can you explain if that is the case?</p>
</div>
<div id="comment-82537-info" class="comment-info">
<span class="comment-age">(10 Nov '21, 08:17)</span> <span class="comment-user userinfo">ayuz</span>
</div>
</div>
<span id="82538"></span>
<div id="comment-82538" class="comment">
<div id="post-82538-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't know of any specific examples, but I know there are places in the world that have elevated highways with other roads underneath, so you might also need to consider the layer tag. Apart from that I can't immediately think of why two different roads would contain the same two consecutive nodes.</p>
</div>
<div id="comment-82538-info" class="comment-info">
<span class="comment-age">(10 Nov '21, 10:21)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="82539"></span>
<div id="comment-82539" class="comment">
<div id="post-82539-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Stacked highways should be mapped separately with separate nodes in my opinion. But of course my opinion does not rule out that such roads have been mapped differently.</p>
<p>I guess there will be a significant amount of road "loops" where one road separates from another roads only to re-join it shortly after (e.g. a separate lane at a bus stop). In that case two consecutive nodes of one way will be shared with one other way (on that way the nodes should not be consecutive, though).</p>
<p>Sometimes highways are mapped not as line features but as areas. That is often done for pedestrian areas but also for other roads. There are different ways of tagging but such area could just be tagged with <code>highway=xyz</code> and <code>area=yes</code>. Such areas may be joined to other road areas or line roads on their boarders.</p>
<p>There are some highway features (not highways in a strict sense) like <code>highway_rest_area</code> or <code>highway_emergency_bay</code> that could again overlap with real roads or one and other.</p>
<p>And of course you may be faced with mapping errors where for example an angled intersection is not mapped properly but the two intersecting roads share a short way.</p>
</div>
<div id="comment-82539-info" class="comment-info">
<span class="comment-age">(10 Nov '21, 10:58)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-82536" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82536-form-container" class="comment-form-container">
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

