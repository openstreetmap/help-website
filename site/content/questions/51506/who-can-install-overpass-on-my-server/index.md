+++
type = "question"
title = "Who can install Overpass on my server?"
description = '''I&#x27;m looking for someone who can install the overpass api on my own server. I use it a lot and I don&#x27;t want to consume too much resources from a public server. I have a server, but I have no idea where I can find someone who is able to install it. Who/Where can I find more help? I don&#x27;t run that much...'''
date = "2016-08-17T19:40:00Z"
lastmod = "2016-08-20T21:42:00Z"
weight = 51506
keywords = [ "openstreetmap", "overpass", "overpass-turbo", "server" ]
aliases = [ "/questions/51506" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Who can install Overpass on my server?](/questions/51506/who-can-install-overpass-on-my-server)

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
<span id="post-51506-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51506-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-51506-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm looking for someone who can install the overpass api on my own server. I use it a lot and I don't want to consume too much resources from a public server. I have a server, but I have no idea where I can find someone who is able to install it.</p>
<p>Who/Where can I find more help?</p>
<p>I don't run that much queries a day but I have three processes doing multiple request simultaneously. So sometimes the api returns: 429 Too Many Requests.</p>
<p>I have a 1U server, Intel Core Duo 6600 2.4 Ghz. 8GB memory, 1.5 TB HDD with Debian. The data I want to query is from the global 'live' database (no history edits). With meta data and area support. A hourly update would be nice.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Aug '16, 19:40</strong></p>
<img src="https://secure.gravatar.com/avatar/cbcec43f8f6c9d5b869aa5bdc56eb673?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NLAnaconda&#39;s gravatar image" />
<p><span>NLAnaconda</span><br />
<span class="score" title="166 reputation points">166</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NLAnaconda has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> reverted <strong>19 Aug '16, 10:10</strong> </span></p>
</div>
</div>
<div id="comments-container-51506" class="comments-container">
<span id="51535"></span>
<div id="comment-51535" class="comment">
<div id="post-51535-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe someone can create a virtual machine containing an Overpass API installation similar to <a href="https://wiki.openstreetmap.org/wiki/Virtual_machine_image">this VM</a> containin Nominatim and Mapnik? However keeping it up-to-date will be an issue.</p>
</div>
<div id="comment-51535-info" class="comment-info">
<span class="comment-age">(19 Aug '16, 09:18)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="51537"></span>
<div id="comment-51537" class="comment">
<div id="post-51537-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You didn't mention (1) how many queries you run per day, (2) what your server looks like (OS, some specs), and (3) what kind of data you want to query (only one country, full history, continuous updates, etc...). That's to find out if an own instance is needed in the first place, and if your server would be suitable to host such an instance.</p>
</div>
<div id="comment-51537-info" class="comment-info">
<span class="comment-age">(19 Aug '16, 10:04)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="51539"></span>
<div id="comment-51539" class="comment">
<div id="post-51539-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've added the information. The mail problem is that I wan't to run multiple queries at once. So, sometimes I hit the 429 Too Many Request response.</p>
</div>
<div id="comment-51539-info" class="comment-info">
<span class="comment-age">(19 Aug '16, 10:11)</span> <span class="comment-user userinfo">NLAnaconda</span>
</div>
</div>
<span id="51540"></span>
<div id="comment-51540" class="comment">
<div id="post-51540-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>As you only encounter some issues "sometimes", the newly introduced endpoint <a href="http://overpass-api.de/api/status">http://overpass-api.de/api/status</a> will come in handy to provide some insight, how much of your quota is already consumed and when you can send the next query without running into a 429 Too Many requests. Question would be, if you could organize your processing in a way to take this status page into account.</p>
</div>
<div id="comment-51540-info" class="comment-info">
<span class="comment-age">(19 Aug '16, 10:16)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-51506" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51506-form-container" class="comment-form-container">
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

<span id="51510"></span>

<div id="answer-container-51510" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51510-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51510-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-51510-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Look on <a href="http://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services">http://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services</a> .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Aug '16, 07:00</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-51510" class="comments-container">
<span id="51526"></span>
<div id="comment-51526" class="comment">
<div id="post-51526-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've found that and mailed a couple of companies but they don't do installations or they ask a couple of hunderd and even thousand euro for it. (I didnt mail all of them but a couple). Thats a bit above my budget.</p>
</div>
<div id="comment-51526-info" class="comment-info">
<span class="comment-age">(19 Aug '16, 00:30)</span> <span class="comment-user userinfo">NLAnaconda</span>
</div>
</div>
<span id="51536"></span>
<div id="comment-51536" class="comment">
<div id="post-51536-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If a couple of hundred Euro is out of budget, then I'd suggest that perhaps you either reevaluate the benefit of the work to your business or learn how to do it yourself. Based on the time and skills that are likely to be involved, €200 seems rather low to me.</p>
<p>(disclaimer - I've never so much as looked at Nominatim but, like many OSMers I suspect, I do do this sort of thing in $dayjob for commercial software)</p>
</div>
<div id="comment-51536-info" class="comment-info">
<span class="comment-age">(19 Aug '16, 09:34)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="51541"></span>
<div id="comment-51541" class="comment">
<div id="post-51541-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>True off course, however its not for a business. Its for a personal project which might become a businesses someday. However that's not the main focus for now. I thought that maybe there would be some fanatic OSM users who know how to setup Overpass in a couple of hours. The wikipages are 2 pages long so I thought it shouldn't be to hard. But I don't know anything about Linux. But maybe it is indeed a big hassle..</p>
</div>
<div id="comment-51541-info" class="comment-info">
<span class="comment-age">(19 Aug '16, 10:16)</span> <span class="comment-user userinfo">NLAnaconda</span>
</div>
</div>
</div>
<div id="comment-tools-51510" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51510-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="51570"></span>

<div id="answer-container-51570" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51570-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51570-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-51570-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I tried to install it myself without any Linux experience and I succeeded with the use of the tutorials and Google. Pretty happy with myself now :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Aug '16, 21:42</strong></p>
<img src="https://secure.gravatar.com/avatar/cbcec43f8f6c9d5b869aa5bdc56eb673?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NLAnaconda&#39;s gravatar image" />
<p><span>NLAnaconda</span><br />
<span class="score" title="166 reputation points">166</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NLAnaconda has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51570" class="comments-container">
&#10;</div>
<div id="comment-tools-51570" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51570-form-container" class="comment-form-container">
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

