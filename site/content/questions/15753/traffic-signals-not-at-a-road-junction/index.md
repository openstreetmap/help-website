+++
type = "question"
title = "Traffic signals not at a road junction"
description = '''Is it possible to add a &#x27;highway = traffic_signals&#x27; tag at any point on a road, or is it only permissible at junctions? I want to map a point where a minor road crosses the railway on a single-track bridge, with access to the bridge controlled by traffic signals.'''
date = "2012-09-02T20:42:00Z"
lastmod = "2012-09-03T05:08:00Z"
weight = 15753
keywords = [ "junction", "traffic_signals" ]
aliases = [ "/questions/15753" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Traffic signals not at a road junction](/questions/15753/traffic-signals-not-at-a-road-junction)

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
<span id="post-15753-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15753-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15753-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to add a 'highway = traffic_signals' tag at any point on a road, or is it only permissible at junctions?</p>
<p>I want to map a point where a minor road crosses the railway on a single-track bridge, with access to the bridge controlled by traffic signals.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-junction" rel="tag" title="see questions tagged &#39;junction&#39;">junction</span> <span class="post-tag tag-link-traffic_signals" rel="tag" title="see questions tagged &#39;traffic_signals&#39;">traffic_signals</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Sep '12, 20:42</strong></p>
<img src="https://secure.gravatar.com/avatar/c81fd17cde8b2747629b78bdef81a202?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Madryn&#39;s gravatar image" />
<p><span>Madryn</span><br />
<span class="score" title="2241 reputation points"><span>2.2k</span></span><span title="36 badges"><span class="badge1">●</span><span class="badgecount">36</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Madryn has 5 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Sep '12, 21:02</strong> </span></p>
</div>
</div>
<div id="comments-container-15753" class="comments-container">
&#10;</div>
<div id="comment-tools-15753" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15753-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="15756"></span>

<div id="answer-container-15756" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15756-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15756-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15756-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Madryn has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, what you describe is absolutely fine. Just use a node on either side of the bridge and tag as highway=traffic_signals</p>
<p>I'd probably avoid using the exact same node where the way is split for the start/end of the bridge.. I can't say why, but I just think its better practice not to join bridge ends to other things. Therefore your signals will be either on the bridge, or off the bridge - whatever reflects reality!</p>
<p>Other examples I can think of where a traffic signal node is not used at a junction would be simple pedestrian-only traffic signals, or those used on approach to an opening bridge (e.g. a draw bridge).</p>
<p>BJ</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Sep '12, 05:08</strong></p>
<img src="https://secure.gravatar.com/avatar/4200f1aaa4fa9ccd4d02db2e8e670de1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wolftracker&#39;s gravatar image" />
<p><span>wolftracker</span><br />
<span class="score" title="475 reputation points">475</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wolftracker has 2 accepted answers">33%</span></p>
</div>
</div>
<div id="comments-container-15756" class="comments-container">
&#10;</div>
<div id="comment-tools-15756" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15756-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="15754"></span>

<div id="answer-container-15754" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15754-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15754-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15754-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, as long as the signs have anything to do with the traffic movements on the road tag it. Make them the same way as used at the junction and tag the extra specifications. Greetz</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Sep '12, 00:22</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-15754" class="comments-container">
&#10;</div>
<div id="comment-tools-15754" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15754-form-container" class="comment-form-container">
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

