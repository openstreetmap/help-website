+++
type = "question"
title = "How can I geocode addresses reliably?"
description = '''I tried using Nominatim to geocode addresses. It turns out that Nominatim cannot handle partial street names in query. That is to get location, street name has to be matched fully. It means I have to provide street&#x27;s full name (e.g. Miley Cyrus Street) if it&#x27;s saved that way in OSM. If street name i...'''
date = "2015-10-10T13:07:00Z"
lastmod = "2015-10-10T18:48:00Z"
weight = 45825
keywords = [ "nominatim", "geocoding", "streetname" ]
aliases = [ "/questions/45825" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I geocode addresses reliably?](/questions/45825/how-can-i-geocode-addresses-reliably)

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
<span id="post-45825-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45825-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45825-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I tried using Nominatim to geocode addresses. It turns out that Nominatim cannot handle partial street names in query. That is to get location, street name has to be matched fully. It means I have to provide street's full name (e.g. Miley Cyrus Street) if it's saved that way in OSM. If street name in OSM is not full (e.g. Cyrus Street), to get location from Nominatim I have to provide only part of street's name. How can I deal with this problem?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-streetname" rel="tag" title="see questions tagged &#39;streetname&#39;">streetname</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Oct '15, 13:07</strong></p>
<img src="https://secure.gravatar.com/avatar/d986d3a7b3da49643505a18f7f3a6978?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanitas2&#39;s gravatar image" />
<p><span>sanitas2</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanitas2 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Oct '15, 13:57</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span></p>
</div>
</div>
<div id="comments-container-45825" class="comments-container">
&#10;</div>
<div id="comment-tools-45825" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45825-form-container" class="comment-form-container">
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

<span id="45829"></span>

<div id="answer-container-45829" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45829-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45829-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45829-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As a user the next best approach is to query again removing words from the address/street.</p>
<p>Related to your other question (<a href="https://help.openstreetmap.org/questions/45823/geocoding-engines)">https://help.openstreetmap.org/questions/45823/geocoding-engines)</a> no other free/open source geocoder can't handle that either. Maybe <a href="https://github.com/etalab/addok">https://github.com/etalab/addok</a> for France or geocod.io (not free) for US addresses but none for Poland (your use case in the Nominatim bugs you filed) or the rest of the world.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Oct '15, 18:48</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-45829" class="comments-container">
&#10;</div>
<div id="comment-tools-45829" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45829-form-container" class="comment-form-container">
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

