+++
type = "question"
title = "accumulated elevation"
description = '''It is not obvious how accumulated elevation should be calculated. More measuring points give higher elevation in the same sense as the coastline paradox. https://en.wikipedia.org/wiki/Coastline_paradox To be it seems adequate to make one measurments maybe every 2,5 meters, a normal length of a strid...'''
date = "2020-04-28T06:28:00Z"
lastmod = "2020-04-28T17:00:00Z"
weight = 74433
keywords = [ "elevation" ]
aliases = [ "/questions/74433" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [accumulated elevation](/questions/74433/accumulated-elevation)

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
<span id="post-74433-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74433-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74433-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>It is not obvious how accumulated elevation should be calculated. More measuring points give higher elevation in the same sense as the coastline paradox. <a href="https://en.wikipedia.org/wiki/Coastline_paradox">https://en.wikipedia.org/wiki/Coastline_paradox</a> To be it seems adequate to make one measurments maybe every 2,5 meters, a normal length of a stride while running...</p>
<p>My question: how is OpenStreetMap calculating accumulated elevation? One measurement every xx meters? I have seen that it differs from Google Maps - why?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-elevation" rel="tag" title="see questions tagged &#39;elevation&#39;">elevation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Apr '20, 06:28</strong></p>
<img src="https://secure.gravatar.com/avatar/638d5e18caf6271addbbbd009e8cf940?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mragel&#39;s gravatar image" />
<p><span>mragel</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mragel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74433" class="comments-container">
&#10;</div>
<div id="comment-tools-74433" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74433-form-container" class="comment-form-container">
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

<span id="74435"></span>

<div id="answer-container-74435" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74435-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74435-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-74435-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap does not calculate elevation. The only elevation data in OSM is added by users as ele-tag. This is typically done when they see a sign on e.g. the top of a mountain displaying the height.</p>
<p>Why do you think OSM is calculating accumulated elevation? Which map are you consulting that has different results than Google Maps?</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Apr '20, 08:45</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-74435" class="comments-container">
<span id="74437"></span>
<div id="comment-74437" class="comment">
<div id="post-74437-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks!</p>
<p>When I let Open Street Map find the way between two locations, I get the distance, and "stigning" and "fall" which (translated from Swedish) is positive and negative elevation. Se the printscreen: www.schackstudion.se/stigning.PNG</p>
<p>It's +18-19 m, and accordning to Google Maps +1-6.</p>
</div>
<div id="comment-74437-info" class="comment-info">
<span class="comment-age">(28 Apr '20, 08:58)</span> <span class="comment-user userinfo">mragel</span>
</div>
</div>
<span id="74438"></span>
<div id="comment-74438" class="comment">
<div id="post-74438-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>The screenshot shows that those results were provided by the GraphHopper routing service. Graphhopper is one of many applications that use OpenStreetMap data but are not directly part of OpenStreetMap. As escada said, there is very little elevation data in OpenStreetMap, certainly not enough for this type of calculation. So GraphHopper must be obtaining elevation data from elsewhere, and using it to carry out this calculation. If you want further details you may need to contact <a href="https://www.graphhopper.com/">https://www.graphhopper.com/</a> directly.</p>
</div>
<div id="comment-74438-info" class="comment-info">
<span class="comment-age">(28 Apr '20, 09:24)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
</div>
<div id="comment-tools-74435" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74435-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74451"></span>

<div id="answer-container-74451" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74451-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74451-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-74451-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>AFAIK most OSM-related software use <a href="https://wiki.openstreetmap.org/wiki/SRTM">SRTM DEM</a> to compute elevation, because it's public domain.</p>
<p>I read this (even if I don't fully understand, I guess that's why you have such a difference with GMaps):</p>
<blockquote>
<p>vertical LE90 accuracy ranging between 5–9 m and less than 16 m.</p>
</blockquote>
<p>Specifically for Graphhopper, they use different models based on the location, if I understand corrrectly this <a href="https://discuss.graphhopper.com/t/elevation-provider-inaccuracy/3398/8">post</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Apr '20, 17:00</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Apr '20, 17:01</strong> </span></p>
</div>
</div>
<div id="comments-container-74451" class="comments-container">
&#10;</div>
<div id="comment-tools-74451" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74451-form-container" class="comment-form-container">
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

