+++
type = "question"
title = "I am not geeting city name always in search api response"
description = '''Hello, I am not getting city always in API response when i search for a address. Here is the address: Bahnhofstrasse 1 8001 Zu Here is URL which i am using for search address: https://nominatim.openstreetmap.org/search?q=Bahnhofstrasse%201%208001%20Zu&amp;amp;format=json&amp;amp;polygon=1&amp;amp; addressdetail...'''
date = "2022-07-11T07:02:00Z"
lastmod = "2022-07-11T09:59:00Z"
weight = 85024
keywords = [ "city" ]
aliases = [ "/questions/85024" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [I am not geeting city name always in search api response](/questions/85024/i-am-not-geeting-city-name-always-in-search-api-response)

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
<span id="post-85024-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85024-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85024-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I am not getting city always in API response when i search for a address.</p>
<p>Here is the address: Bahnhofstrasse 1 8001 Zu</p>
<p>Here is URL which i am using for search address:</p>
<p><a href="https://nominatim.openstreetmap.org/search?q=Bahnhofstrasse%201%208001%20Zu&amp;format=json&amp;polygon=1&amp;">https://nominatim.openstreetmap.org/search?q=Bahnhofstrasse%201%208001%20Zu&amp;format=json&amp;polygon=1&amp;</a> addressdetails=1&amp;limit=6&amp;countrycodes=CH&amp;accept-language=de</p>
<p><img src="https://help.openstreetmap.org/upfiles/api-response.png" alt="alt text" /></p>
<p>Can you please help me on this why i am not getting city with this address?</p>
<p>Thanks Siyaram</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jul '22, 07:02</strong></p>
<img src="https://secure.gravatar.com/avatar/94b3e46541d9a0cb5edafe2a8783972c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Siyaram%20Test&#39;s gravatar image" />
<p><span>Siyaram Test</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Siyaram Test has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-85024" class="comments-container">
<span id="85025"></span>
<div id="comment-85025" class="comment">
<div id="post-85025-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What city name would you expect for this location? The results give you the name of the village (which may be the closest thing to a "postal city" here, it is used in the addr:city tags). The results also include various levels of administrative division. It all looks reasonable for a rural area far from a city. I'm not sure anything is missing.</p>
</div>
<div id="comment-85025-info" class="comment-info">
<span class="comment-age">(11 Jul '22, 09:07)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
</div>
<div id="comment-tools-85024" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85024-form-container" class="comment-form-container">
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

<span id="85026"></span>

<div id="answer-container-85026" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85026-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85026-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-85026-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim does not offer autocomplete or autosuggest. So it does not expand your search of "Zu" to "Zurich".</p>
<p>If you need an autosuggest/autocomplete function, you'll have to look to other geocoders, e.g. photon or pelias.</p>
<p>Example:</p>
<p><a href="https://photon.komoot.io/api/?q=Bahnhofstrasse%201%208001%20Zu">https://photon.komoot.io/api/?q=Bahnhofstrasse%201%208001%20Zu</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jul '22, 09:59</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jul '22, 09:59</strong> </span></p>
</div>
</div>
<div id="comments-container-85026" class="comments-container">
&#10;</div>
<div id="comment-tools-85026" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85026-form-container" class="comment-form-container">
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

