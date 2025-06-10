+++
type = "question"
title = "How to get railway distance"
description = '''Hi. I&#x27;m very new in this map business and I need some guide on where should I start to get a railway distance between two points. I discovered OpenRailwayMap but I&#x27;m not sure how to use the API to get the distance info. Couldn&#x27;t find any documentation about it.. Please help..'''
date = "2018-12-24T00:40:00Z"
lastmod = "2018-12-24T09:27:00Z"
weight = 67333
keywords = [ "distance", "railway", "routing" ]
aliases = [ "/questions/67333" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get railway distance](/questions/67333/how-to-get-railway-distance)

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
<span id="post-67333-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67333-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67333-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi. I'm very new in this map business and I need some guide on where should I start to get a railway distance between two points. I discovered OpenRailwayMap but I'm not sure how to use the API to get the distance info. Couldn't find any documentation about it.. Please help..</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span> <span class="post-tag tag-link-railway" rel="tag" title="see questions tagged &#39;railway&#39;">railway</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Dec '18, 00:40</strong></p>
<img src="https://secure.gravatar.com/avatar/19b5d434a3216d7f734c1a20df0100b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zarulzakuan&#39;s gravatar image" />
<p><span>zarulzakuan</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zarulzakuan has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Dec '18, 09:20</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-67333" class="comments-container">
&#10;</div>
<div id="comment-tools-67333" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67333-form-container" class="comment-form-container">
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

<span id="67340"></span>

<div id="answer-container-67340" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67340-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67340-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67340-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't know of any all-purpose API that gives you the "railway distance" between two points, not least because even more than with car traffic, the exact specifications of the rolling stock limit which tracks you can use. The "railway distance" for a TGV is very different from that for a diesel freight train.</p>
<p>It is likely that you need to run your own server providing railway routing according to the specifications of your use case. Some people have experimented with using standard automobile routing engines and simply feeding them tracks instead of roads, however this can lead to unrealistic results ("make a left turn at this intersection").</p>
<p>Michael Reichert held a talk on this at this year's SotM conference in Milan, in which he also presented an Open Source project (based on the GraphHopper routing engine) for railway routing:</p>
<p><a href="https://2018.stateofthemap.org/slides/T071-Routing_on_rails_with_OpenStreetMap.pdf">https://2018.stateofthemap.org/slides/T071-Routing_on_rails_with_OpenStreetMap.pdf</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Dec '18, 09:27</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-67340" class="comments-container">
&#10;</div>
<div id="comment-tools-67340" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67340-form-container" class="comment-form-container">
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

