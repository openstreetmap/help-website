+++
type = "question"
title = "Insert map based on direction"
description = '''Hi all,  I want to implement a litle map viewer with one marker: the user&#x27;s address. I know that i can insert a marker with OpenLayers with Latitude and Longitude values, but i want to give &#x27;OpenLayers&#x27; the address instead of GPS coordinates. Its for a user profile of a new website i am working for....'''
date = "2013-09-24T16:06:00Z"
lastmod = "2013-09-24T21:08:00Z"
weight = 26683
keywords = [ "openstreetmap", "website", "viewer", "openlayers" ]
aliases = [ "/questions/26683" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Insert map based on direction](/questions/26683/insert-map-based-on-direction)

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
<span id="post-26683-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26683-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26683-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I want to implement a litle map viewer with one marker: the user's address. I know that i can insert a marker with OpenLayers with Latitude and Longitude values, but i want to give 'OpenLayers' the address instead of GPS coordinates.</p>
<p>Its for a user profile of a new website i am working for. (User inserts its address in his profile).</p>
<p>Thank you very much.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-website" rel="tag" title="see questions tagged &#39;website&#39;">website</span> <span class="post-tag tag-link-viewer" rel="tag" title="see questions tagged &#39;viewer&#39;">viewer</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Sep '13, 16:06</strong></p>
<img src="https://secure.gravatar.com/avatar/b5ed6e179d6cb6d6dfae86175ae902f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="walo&#39;s gravatar image" />
<p><span>walo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="walo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26683" class="comments-container">
&#10;</div>
<div id="comment-tools-26683" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26683-form-container" class="comment-form-container">
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

<span id="26686"></span>

<div id="answer-container-26686" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26686-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26686-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26686-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you just have the address then you have to do reverse-geocoding for each address first. This can be done by using <a href="http://wiki.openstreetmap.org/wiki/Nominatim#Reverse_Geocoding_.2F_Address_lookup">Nominatim</a>.</p>
<p>But take a look at the <a href="http://wiki.openstreetmap.org/wiki/Nominatim_usage_policy">usage policy</a> first before you try to start bulk queries for all of your addresses. Instead of OSM's official Nominatim instance you can either use an <a href="http://wiki.openstreetmap.org/wiki/Nominatim_usage_policy#Alternatives">alternative instance</a> with a less-restrictive usage policy or <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Installation">install</a> your own one.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Sep '13, 17:01</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-26686" class="comments-container">
<span id="26693"></span>
<div id="comment-26693" class="comment">
<div id="post-26693-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I know Nominatim, but i just wanted a single line of code added to openlayers' code, instead of adding coordinates.</p>
<p>Thanks.</p>
</div>
<div id="comment-26693-info" class="comment-info">
<span class="comment-age">(24 Sep '13, 20:17)</span> <span class="comment-user userinfo">walo</span>
</div>
</div>
<span id="26694"></span>
<div id="comment-26694" class="comment">
<div id="post-26694-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There is no such OpenLayers feature out of the box. And bulk-querying all addresses each time would clearly violate Nominatim's usage policy and it would be very slow and unnecessary, too.</p>
</div>
<div id="comment-26694-info" class="comment-info">
<span class="comment-age">(24 Sep '13, 21:08)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-26686" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26686-form-container" class="comment-form-container">
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

