+++
type = "question"
title = "Is there an osm indoor routing engine/api for android?"
description = '''I am developing indoor navigation application on android smartphones . I have created indoor map of the building using JOSM editor . I dont want to spend much time on implementation of routing is any ready to use engine/api that i can use? -&amp;gt; I would prefer it offline but online would also do'''
date = "2012-01-15T15:44:00Z"
lastmod = "2012-01-16T17:06:00Z"
weight = 9984
keywords = [ "android", "indoor", "routing" ]
aliases = [ "/questions/9984" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Is there an osm indoor routing engine/api for android?](/questions/9984/is-there-an-osm-indoor-routing-engineapi-for-android)

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
<span id="post-9984-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9984-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9984-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am developing indoor navigation application on android smartphones . I have created indoor map of the building using JOSM editor . I dont want to spend much time on implementation of routing is any ready to use engine/api that i can use?</p>
<p>-&gt; I would prefer it offline but online would also do</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-indoor" rel="tag" title="see questions tagged &#39;indoor&#39;">indoor</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jan '12, 15:44</strong></p>
<img src="https://secure.gravatar.com/avatar/a56f90750476bb5d076033dd5b0822f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="teksan&#39;s gravatar image" />
<p><span>teksan</span><br />
<span class="score" title="45 reputation points">45</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="teksan has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Nov '13, 17:26</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-9984" class="comments-container">
&#10;</div>
<div id="comment-tools-9984" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9984-form-container" class="comment-form-container">
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

<span id="10003"></span>

<div id="answer-container-10003" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10003-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10003-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-10003-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="teksan has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For Android, there are two routing engines available that are currently working off-line to my knowledge.</p>
<p>There is the Navit engine. Navit is coded in C, with a Java shell around it to work on Android.</p>
<p>And there is the OsmAnd engine. OsmAnd is a native Android app, so it is coded in Java. But the devs are thinking about porting it to C (or C++) for better performance.</p>
<p>Both engines require a different, quite specific, file type and handling libraries.</p>
<p>The Navit engine has a better performance (I doubt it is important for indoor routing), but the OsmAnd code is probably easier to adapt or integrate into your project (as in OsmAnd you can choose the routing engine from various on-line routers, or the off-line one).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jan '12, 17:06</strong></p>
<img src="https://secure.gravatar.com/avatar/1fe9a0c696a5000fb304ababea9f83af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanderd17&#39;s gravatar image" />
<p><span>Sanderd17</span><br />
<span class="score" title="1111 reputation points"><span>1.1k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanderd17 has 15 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-10003" class="comments-container">
&#10;</div>
<div id="comment-tools-10003" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10003-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9985"></span>

<div id="answer-container-9985" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9985-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9985-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-9985-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please spend a little bit of time and have an intensive look at the <a href="http://wiki.openstreetmap.org/wiki/Routing">routing</a> page in the OSM wiki.</p>
<p>If you have any detailed questions then, come to OSM forum or te Routing mailigng list.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jan '12, 19:09</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Jan '12, 19:10</strong> </span></p>
</div>
</div>
<div id="comments-container-9985" class="comments-container">
&#10;</div>
<div id="comment-tools-9985" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9985-form-container" class="comment-form-container">
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

