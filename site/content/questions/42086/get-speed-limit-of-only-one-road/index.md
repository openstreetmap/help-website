+++
type = "question"
title = "Get speed limit of only one road ?"
description = '''I search and found query of overpass-api to get speed limit of roads but it get by bounding box. I want to get speed limit of only one road by latitude and longitude of road. How can i do that ? '''
date = "2015-04-01T02:40:00Z"
lastmod = "2015-04-02T20:31:00Z"
weight = 42086
keywords = [ "speedlimit", "query", "ways", "overpass-api", "road" ]
aliases = [ "/questions/42086" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Get speed limit of only one road ?](/questions/42086/get-speed-limit-of-only-one-road)

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
<span id="post-42086-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42086-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42086-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I search and found query of overpass-api to get speed limit of roads but it get by bounding box. I want to get speed limit of only one road by latitude and longitude of road. How can i do that ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-speedlimit" rel="tag" title="see questions tagged &#39;speedlimit&#39;">speedlimit</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Apr '15, 02:40</strong></p>
<img src="https://secure.gravatar.com/avatar/1850b625f5e9503974773125ba7e6a63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KimNamCham&#39;s gravatar image" />
<p><span>KimNamCham</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KimNamCham has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Apr '15, 02:41</strong> </span></p>
</div>
</div>
<div id="comments-container-42086" class="comments-container">
&#10;</div>
<div id="comment-tools-42086" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42086-form-container" class="comment-form-container">
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

<span id="42097"></span>

<div id="answer-container-42097" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42097-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42097-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42097-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a closer look at the overpass-api parameter "<strong>around</strong>" ... maybe at <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL">Overpass_API/Overpass_QL</a></p>
<p>BUT: How will you differentiate when there are other ways around your position that hou have lat lon from?</p>
<p>And: what is the source of your lat/lon?</p>
<p>Is it sure that each coordinate is a single node wich is an element of a certain way?</p>
<p>Or is your lat/lon only "near" any posible street?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Apr '15, 17:13</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Apr '15, 17:13</strong> </span></p>
</div>
</div>
<div id="comments-container-42097" class="comments-container">
&#10;</div>
<div id="comment-tools-42097" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42097-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="42099"></span>

<div id="answer-container-42099" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42099-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42099-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42099-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My problem is when get information by boundingbox, the information of 1 road is repeated like speedlimits or oneway - when repeated, oneway information of road has different. So, i want to get information of road by 1 latitude and 1 longtidue, example when you click 1 point in map view, you can get information of this road. And i scare when boudingbox is to large, data get so slowly such as query on mobile.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Apr '15, 18:14</strong></p>
<img src="https://secure.gravatar.com/avatar/1850b625f5e9503974773125ba7e6a63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KimNamCham&#39;s gravatar image" />
<p><span>KimNamCham</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KimNamCham has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Apr '15, 18:18</strong> </span></p>
</div>
</div>
<div id="comments-container-42099" class="comments-container">
<span id="42114"></span>
<div id="comment-42114" class="comment">
<div id="post-42114-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This should have been a comment instead of an answer. But OSQA just throws an error when trying to convert it to a comment :\</p>
</div>
<div id="comment-42114-info" class="comment-info">
<span class="comment-age">(02 Apr '15, 20:31)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-42099" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42099-form-container" class="comment-form-container">
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

