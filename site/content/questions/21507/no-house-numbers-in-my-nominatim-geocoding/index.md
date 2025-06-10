+++
type = "question"
title = "no house numbers in my Nominatim geocoding"
description = '''Hello, I have set up Nominatim according to the wiki, and indexed Arizona data that I got from here. Now when I try to geocode addresses, no results contain house numbers. E.g. this query is geocoded successfully with the public Nominatim service and contains a house number. Running it against my No...'''
date = "2013-04-13T16:36:00Z"
lastmod = "2013-04-16T08:26:00Z"
weight = 21507
keywords = [ "housenumbers", "nominatim", "geocoding" ]
aliases = [ "/questions/21507" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [no house numbers in my Nominatim geocoding](/questions/21507/no-house-numbers-in-my-nominatim-geocoding)

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
<span id="post-21507-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21507-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21507-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I have set up Nominatim according to the wiki, and indexed Arizona data that I got from <a href="http://download.geofabrik.de/north-america/us/arizona-latest.osm.pbf">here</a>. Now when I try to geocode addresses, no results contain house numbers. E.g. <a href="http://nominatim.openstreetmap.org/search?format=json&amp;addressdetails=1&amp;q=100%20Easy%20St,%20Carefree,%20AZ%2085377">this query</a> is geocoded successfully with the public Nominatim service and contains a house number. Running it against my Nomatim set up only resolves the street. What do I have to do to also index house numbers in my Nomatim instance? Is there a more detailed writeup about how Nomatim works internally? I took a look at the resulted database schema and it is not straight forward to understand.</p>
<p>Thanks, Kosnstantin</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-housenumbers" rel="tag" title="see questions tagged &#39;housenumbers&#39;">housenumbers</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Apr '13, 16:36</strong></p>
<img src="https://secure.gravatar.com/avatar/680bc1d9127776b4acb2e6af485a6869?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="konstantin&#39;s gravatar image" />
<p><span>konstantin</span><br />
<span class="score" title="61 reputation points">61</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="konstantin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-21507" class="comments-container">
&#10;</div>
<div id="comment-tools-21507" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21507-form-container" class="comment-form-container">
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

<span id="21516"></span>

<div id="answer-container-21516" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21516-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21516-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21516-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is possible that the results are coming from the TIGER data that Nominatim uses as a fallback, not from OSM data.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Apr '13, 05:06</strong></p>
<img src="https://secure.gravatar.com/avatar/5634c46072077e10f5b7c0da9b4bbb62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pnorman&#39;s gravatar image" />
<p><span>pnorman</span><br />
<span class="score" title="2352 reputation points"><span>2.4k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pnorman has 9 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-21516" class="comments-container">
<span id="21529"></span>
<div id="comment-21529" class="comment">
<div id="post-21529-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If i read <a href="http://wiki.openstreetmap.org/wiki/TIGER">http://wiki.openstreetmap.org/wiki/TIGER</a> correctly, TIGER data has been imported into OSM in 2005. That means it would be part of the Arizona data that I downloaded and indexed. Or am I missing something?</p>
</div>
<div id="comment-21529-info" class="comment-info">
<span class="comment-age">(14 Apr '13, 22:09)</span> <span class="comment-user userinfo">konstantin</span>
</div>
</div>
<span id="21574"></span>
<div id="comment-21574" class="comment">
<div id="post-21574-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You need the TIGER address data (as opposed to street data which is the one that has been imported into OSM). The process to add this data to your database is described in <a href="https://help.openstreetmap.org/questions/12150/missing-house-numbers-in-local-nominatim-instance">this question</a>.</p>
</div>
<div id="comment-21574-info" class="comment-info">
<span class="comment-age">(16 Apr '13, 08:26)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
</div>
<div id="comment-tools-21516" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21516-form-container" class="comment-form-container">
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

