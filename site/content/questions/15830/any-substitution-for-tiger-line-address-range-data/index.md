+++
type = "question"
title = "any substitution for Tiger Line address range data?"
description = '''Hi everyone I am trying to do some routing and locating work with OSM data. I want to locate an address by its street number  for example, I want to locate the address &quot;4103 Walnut St, Philadelphia, PA&quot; &quot;Walnut St&quot; &quot;Philadelphia“ and &quot;PA&quot; can be got easily, but I have no idea how to parse the OSM da...'''
date = "2012-09-05T19:21:00Z"
lastmod = "2012-09-07T03:34:00Z"
weight = 15830
keywords = [ "locations" ]
aliases = [ "/questions/15830" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [any substitution for Tiger Line address range data?](/questions/15830/any-substitution-for-tiger-line-address-range-data)

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
<span id="post-15830-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15830-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15830-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone I am trying to do some routing and locating work with OSM data. I want to locate an address by its street number for example, I want to locate the address "4103 Walnut St, Philadelphia, PA" "Walnut St" "Philadelphia“ and "PA" can be got easily, but I have no idea how to parse the OSM data so that I can find where 4103 is..</p>
<p>I Tiger Line, this is easy, since it has address range data...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-locations" rel="tag" title="see questions tagged &#39;locations&#39;">locations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Sep '12, 19:21</strong></p>
<img src="https://secure.gravatar.com/avatar/b6f92a74168ad26a9b7c9e084b2a3b55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NGEva01&#39;s gravatar image" />
<p><span>NGEva01</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NGEva01 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-15830" class="comments-container">
&#10;</div>
<div id="comment-tools-15830" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15830-form-container" class="comment-form-container">
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

<span id="15842"></span>

<div id="answer-container-15842" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15842-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15842-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15842-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The best way is to use <a href="https://wiki.openstreetmap.org/wiki/Nominatim">Nominatim</a>. Many areas of the US are lacking address data, but the addresses which are present in OSM are generally much better than the TIGER lines. Nominatim has logic which can fall back to the TIGER lines when no OSM data is entered.</p>
<p>For testing, you can use the OpenStreetMap version of Nominatim. For low-medium volumes of lookups, you can also use the <a href="http://devblog.mapquest.com/2012/08/21/new-geocoding-service-and-updated-apis-based-on-open-data-2/">Mapquest Open</a> Geocoding APIs. For rapid response or high volumes of lookups, you will need to set up Nominatim on a server. In this case, you'll need to load the TIGER line address data following the procedure at <a href="/questions/12150/missing-house-numbers-in-local-nominatim-instance">this answer</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Sep '12, 12:22</strong></p>
<img src="https://secure.gravatar.com/avatar/1dd5f61a81b99dd54ec6f33d96aa38b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20N&#39;s gravatar image" />
<p><span>Mike N</span><br />
<span class="score" title="2926 reputation points"><span>2.9k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike N has 16 accepted answers">17%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Sep '12, 03:33</strong> </span></p>
</div>
</div>
<div id="comments-container-15842" class="comments-container">
<span id="15843"></span>
<div id="comment-15843" class="comment">
<div id="post-15843-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Doesn't Nominatim use Tiger data in the US? According to <a href="/questions/12150/missing-house-numbers-in-local-nominatim-instance">this answer</a>, anyway.</p>
</div>
<div id="comment-15843-info" class="comment-info">
<span class="comment-age">(06 Sep '12, 12:28)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="15872"></span>
<div id="comment-15872" class="comment">
<div id="post-15872-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Good catch - I've updated the answer to refer to the other answer.</p>
</div>
<div id="comment-15872-info" class="comment-info">
<span class="comment-age">(07 Sep '12, 03:34)</span> <span class="comment-user userinfo">Mike N</span>
</div>
</div>
</div>
<div id="comment-tools-15842" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15842-form-container" class="comment-form-container">
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

