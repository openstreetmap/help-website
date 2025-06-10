+++
type = "question"
title = "How to work with traffic data on OpenStreetMap?"
description = '''I am trying to create a software to show traffic information on OpenStreetMap. Considering that the traffic information is temporary, the data is changed in a certain frequency. Does anyone has a suggestion to make this work? My first try was to use the postgre/postgis/openlayer on the server, and u...'''
date = "2012-12-19T18:44:00Z"
lastmod = "2016-06-08T15:21:00Z"
weight = 18634
keywords = [ "development", "traffic" ]
aliases = [ "/questions/18634" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to work with traffic data on OpenStreetMap?](/questions/18634/how-to-work-with-traffic-data-on-openstreetmap)

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
<span id="post-18634-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18634-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-18634-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to create a software to show traffic information on OpenStreetMap. Considering that the traffic information is temporary, the data is changed in a certain frequency. Does anyone has a suggestion to make this work?</p>
<p>My first try was to use the postgre/postgis/openlayer on the server, and update the information about the traffic on the database. But I had too much problems to show the route on map. So I am interested in ideas to the server.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Dec '12, 18:44</strong></p>
<img src="https://secure.gravatar.com/avatar/8e7f1400bb44d566c364e6342cbc80ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roberto%20Ferraz&#39;s gravatar image" />
<p><span>Roberto Ferraz</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roberto Ferraz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jun '16, 21:09</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-18634" class="comments-container">
<span id="18635"></span>
<div id="comment-18635" class="comment">
<div id="post-18635-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What format is your traffic data in ? What kind of server do you have to deliver the data ? Are you wondering about code on the client to refresh the data, or code on the server to sustain the load ?</p>
</div>
<div id="comment-18635-info" class="comment-info">
<span class="comment-age">(19 Dec '12, 18:51)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="18636"></span>
<div id="comment-18636" class="comment">
<div id="post-18636-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry vincent, I have updated my question to make to improve it. I am using the postgre/postgis/openlayer solution. But I am facing the following problem during: The user selects a destination and origin point, but as the scripts works with nodes, the route starts and ends after (or before) the place it would. So I want to find another solution. My traffic information is a float value that goes from 0 to 1 on each road, where 0 is free, and 1 is stand still..</p>
</div>
<div id="comment-18636-info" class="comment-info">
<span class="comment-age">(19 Dec '12, 19:21)</span> <span class="comment-user userinfo">Roberto Ferraz</span>
</div>
</div>
</div>
<div id="comment-tools-18634" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18634-form-container" class="comment-form-container">
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

<span id="18638"></span>

<div id="answer-container-18638" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18638-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18638-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18638-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The only webservice I know about that is <a href="http://openrouteservice.org">openrouteservice.org</a> ... there is a display (and maybe routing) with TMC data for Germany. Ask the guys from univerity Heidelberg who offer this service.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Dec '12, 20:36</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-18638" class="comments-container">
&#10;</div>
<div id="comment-tools-18638" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18638-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="50086"></span>

<div id="answer-container-50086" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50086-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50086-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50086-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is <a href="http://opentraffic.io/">http://opentraffic.io/</a> which seems like a great initiative, but I have not seen it actually running so I can't say anything about its quality. It seems their code repository (on Github) may have implemented something like what you're trying to do.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jun '16, 15:21</strong></p>
<img src="https://secure.gravatar.com/avatar/89c08d552cf49cbb152cb01d991ff563?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TwoD&#39;s gravatar image" />
<p><span>TwoD</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TwoD has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50086" class="comments-container">
&#10;</div>
<div id="comment-tools-50086" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50086-form-container" class="comment-form-container">
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

