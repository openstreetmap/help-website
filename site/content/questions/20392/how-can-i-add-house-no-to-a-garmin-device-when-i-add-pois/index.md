+++
type = "question"
title = "How can I add house no. to a garmin device when I add POIs?"
description = '''Hi, when I add POIs there are some details I want to add like house no., wereda no.,and etc but the device allow me only a name and phone no. is there a way to add some fields? '''
date = "2013-02-28T15:46:00Z"
lastmod = "2013-03-01T04:30:00Z"
weight = 20392
keywords = [ "fields", "garmin" ]
aliases = [ "/questions/20392" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I add house no. to a garmin device when I add POIs?](/questions/20392/how-can-i-add-house-no-to-a-garmin-device-when-i-add-pois)

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
<span id="post-20392-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20392-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20392-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>when I add POIs there are some details I want to add like house no., wereda no.,and etc but the device allow me only a name and phone no. is there a way to add some fields?<br />
</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-fields" rel="tag" title="see questions tagged &#39;fields&#39;">fields</span> <span class="post-tag tag-link-garmin" rel="tag" title="see questions tagged &#39;garmin&#39;">garmin</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Feb '13, 15:46</strong></p>
<img src="https://secure.gravatar.com/avatar/123ba309f933f61ed3f4bad9b26ee8ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AddisMap%20Meti&#39;s gravatar image" />
<p><span>AddisMap Meti</span><br />
<span class="score" title="71 reputation points">71</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AddisMap Meti has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-20392" class="comments-container">
<span id="20398"></span>
<div id="comment-20398" class="comment">
<div id="post-20398-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>What exact device are you using and what software on the device?</p>
</div>
<div id="comment-20398-info" class="comment-info">
<span class="comment-age">(28 Feb '13, 18:09)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
<span id="20403"></span>
<div id="comment-20403" class="comment">
<div id="post-20403-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What is the relation of your question to OpenStreetMap?</p>
</div>
<div id="comment-20403-info" class="comment-info">
<span class="comment-age">(28 Feb '13, 21:16)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-20392" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20392-form-container" class="comment-form-container">
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

<span id="20406"></span>

<div id="answer-container-20406" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20406-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Assuming you are collecting POIs in the field during a survey and will later add them to OSM on via JOSM or Potlach:</p>
<p>I have a very simple GPS device that will not even let me add name and phone number, I use waypoints. Waypoints can be added even on the simplest Garmin device. The name of the waypoint is free text, so you can add whatever information you want. However the text has a limited length. You could also use the description field of the waypoint to add even more information, but then you have to change the JOSM configuration a bit, as the description is not displayed by default.</p>
<p>This technique will also work in the other direction. You can create a GPX file with waypoints from OSM data. This requires some programming in e.g. python</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Mar '13, 04:30</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-20406" class="comments-container">
&#10;</div>
<div id="comment-tools-20406" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20406-form-container" class="comment-form-container">
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

