+++
type = "question"
title = "timeouts using geopy"
description = '''I have an application that has been running successfully but today i keep getting timeouts error and the bottom of the trace has: geopy.exc.GeocoderUnavailable: HTTPSConnectionPool(host=‘nominatim.openstreetmap.org’, port=443): Max retries exceeded with url: /search?q=Moscow&amp;amp;format=json&amp;amp;limi...'''
date = "2023-08-24T18:40:00Z"
lastmod = "2023-08-26T14:36:00Z"
weight = 87754
keywords = [ "timeout" ]
aliases = [ "/questions/87754" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [timeouts using geopy](/questions/87754/timeouts-using-geopy)

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
<span id="post-87754-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87754-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87754-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have an application that has been running successfully but today i keep getting timeouts error and the bottom of the trace has: geopy.exc.GeocoderUnavailable: HTTPSConnectionPool(host=‘nominatim.openstreetmap.org’, port=443): Max retries exceeded with url: /search?q=Moscow&amp;format=json&amp;limit=1&amp;addressdetails=1&amp;namedetails=1&amp;accept-language=en (Caused by ReadTimeoutError(“HTTPSConnectionPool(host=‘nominatim.openstreetmap.org’, port=443): Read timed out. (read timeout=1)”))</p>
<p>I would appreciate some help/suggestion on this matter. Best regards.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-timeout" rel="tag" title="see questions tagged &#39;timeout&#39;">timeout</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Aug '23, 18:40</strong></p>
<img src="https://secure.gravatar.com/avatar/8aa581c3521cb5f5de554e3515442dac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Margherita&#39;s gravatar image" />
<p><span>Margherita</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Margherita has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87754" class="comments-container">
<span id="87765"></span>
<div id="comment-87765" class="comment">
<div id="post-87765-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's likely what InsertUser guessed - or some other party misusing the demo nominatim endpoints. I've seen those timeouts today as well using a browser and the nominatim ui frontend at nominatim.osm.org (or the nominatim search field at osm.org).</p>
<p>If you do need a reliable service you may install nominatim yourself or use a third party provider, some are listed here: <a href="https://wiki.openstreetmap.org/wiki/Nominatim#Alternatives_.2F_Third-party_providers">https://wiki.openstreetmap.org/wiki/Nominatim#Alternatives_.2F_Third-party_providers</a></p>
</div>
<div id="comment-87765-info" class="comment-info">
<span class="comment-age">(26 Aug '23, 14:36)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
</div>
<div id="comment-tools-87754" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87754-form-container" class="comment-form-container">
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

<span id="87763"></span>

<div id="answer-container-87763" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87763-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87763-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87763-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My guess is you are exceeding what is allowed by the nominatim.openstreetmap.org <a href="https://operations.osmfoundation.org/policies/nominatim/">usage policy</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Aug '23, 13:50</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-87763" class="comments-container">
&#10;</div>
<div id="comment-tools-87763" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87763-form-container" class="comment-form-container">
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

