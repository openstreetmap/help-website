+++
type = "question"
title = "nominatim Same Coordinate from different house number"
description = '''Hi, I have tried to retrieve the gps coordinate from the street name with nominatim. The first time I have used this query url: http://nominatim.openstreetmap.org/search?q=via+augusto+dulceri+56&amp;amp;format=json The result it&#x27;s perfect. If I change the url with another house number but the same stree...'''
date = "2016-02-11T18:04:00Z"
lastmod = "2016-02-12T08:26:00Z"
weight = 48060
keywords = [ "nominatim" ]
aliases = [ "/questions/48060" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [nominatim Same Coordinate from different house number](/questions/48060/nominatim-same-coordinate-from-different-house-number)

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
<span id="post-48060-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48060-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48060-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have tried to retrieve the gps coordinate from the street name with nominatim. The first time I have used this query url: <a href="http://nominatim.openstreetmap.org/search?q=via+augusto+dulceri+56&amp;format=json">http://nominatim.openstreetmap.org/search?q=via+augusto+dulceri+56&amp;format=json</a></p>
<p>The result it's perfect.</p>
<p>If I change the url with another house number but the same street for example:</p>
<p><a href="http://nominatim.openstreetmap.org/search?q=via+augusto+dulceri+66&amp;format=json">http://nominatim.openstreetmap.org/search?q=via+augusto+dulceri+66&amp;format=json</a></p>
<p>The gps coordinate it's the same.</p>
<p>I have tried some other street and the result it's the same. The first time nominatim retrieve the exactly position, but if I change the house number and use the same name street the result is always the same.</p>
<p>Where is the problem?</p>
<p>Regards Daniele</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Feb '16, 18:04</strong></p>
<img src="https://secure.gravatar.com/avatar/e99f35ca60a600d0cf541e2225f79722?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Devilhunter&#39;s gravatar image" />
<p><span>Devilhunter</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Devilhunter has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48060" class="comments-container">
&#10;</div>
<div id="comment-tools-48060" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48060-form-container" class="comment-form-container">
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

<span id="48061"></span>

<div id="answer-container-48061" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48061-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48061-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-48061-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim is only matching the input to the street. See the class:highway in the json.</p>
<p>There isn't much house number data available in OSM there, so I guess most similar searches will only return the street (you can just delete the format=json from the URL to quickly take a look at this visually).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '16, 18:52</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-48061" class="comments-container">
<span id="48068"></span>
<div id="comment-48068" class="comment">
<div id="post-48068-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>For comparison you may have a look how Nominatim works with two existing different house numbers: <a href="https://nominatim.openstreetmap.org/search.php?q=brand-erbisdorf%2C+Kirchweg+4">Kirchweg 4</a> and <a href="https://nominatim.openstreetmap.org/search.php?q=brand-erbisdorf%2C+Kirchweg+24">Kirchweg 24</a>.</p>
</div>
<div id="comment-48068-info" class="comment-info">
<span class="comment-age">(12 Feb '16, 08:26)</span> <span class="comment-user userinfo">malenki</span>
</div>
</div>
</div>
<div id="comment-tools-48061" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48061-form-container" class="comment-form-container">
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

