+++
type = "question"
title = "how to get multiple roads for one GPS point in nominatim reverse geocoding API"
description = '''Hi all I&#x27;m trying to get max speed information for a simple routing app I&#x27;m programming. I can do this using the nominatim reverse geocoding RESt-API. However, when I send a request to nominatim for a certain GPS point it can happen that at this point there are several roads and therefore several ma...'''
date = "2016-08-06T06:00:00Z"
lastmod = "2016-08-07T10:03:00Z"
weight = 51273
keywords = [ "api", "reversegeocoding", "nominatim", "multiple", "results" ]
aliases = [ "/questions/51273" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to get multiple roads for one GPS point in nominatim reverse geocoding API](/questions/51273/how-to-get-multiple-roads-for-one-gps-point-in-nominatim-reverse-geocoding-api)

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
<span id="post-51273-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51273-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51273-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all</p>
<p>I'm trying to get max speed information for a simple routing app I'm programming. I can do this using the nominatim reverse geocoding RESt-API. However, when I send a request to nominatim for a certain GPS point it can happen that at this point there are several roads and therefore several max speed informations valid. Think for example at a bride over a motorway. At the exact same GPS point on top of that bridge there are two valid roads. What I'd like to get as response is some kind of array of all valid roads (actually openstreetmap id's) and not just one. Does anybody know for some way how to achieve this?</p>
<p>Thanks a lot for your help and best regards, Patrick</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-results" rel="tag" title="see questions tagged &#39;results&#39;">results</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Aug '16, 06:00</strong></p>
<img src="https://secure.gravatar.com/avatar/da66e7dadcb3310bdd2213bc1ff3e8e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wengerp&#39;s gravatar image" />
<p><span>wengerp</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wengerp has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51273" class="comments-container">
&#10;</div>
<div id="comment-tools-51273" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51273-form-container" class="comment-form-container">
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

<span id="51280"></span>

<div id="answer-container-51280" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51280-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51280-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51280-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim's /reverse endpoint will only return a single feature (e.g. road), setting &amp;limit has no effect. The reverse search logic tries to exclude bridges, tunnels and other man-made features, it doesn't always work and roads can have several names (and/or reference numbers).</p>
<p>In <a href="https://github.com/twain47/Nominatim/issues/459">https://github.com/twain47/Nominatim/issues/459</a> there's a pull request which might to in that direction (even after reading several times I'm not entirely sure what that developer is looking for). I've seen your request before, sometimes it's about roads, sometimes points-of-interest and that would need a new, let's say /nearby, endpoint. Currently Nominatim can't do that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Aug '16, 14:14</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-51280" class="comments-container">
&#10;</div>
<div id="comment-tools-51280" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51280-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="51293"></span>

<div id="answer-container-51293" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51293-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51293-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51293-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim is the wrong tool for querying specific information from OSM. Nominatim is a geocoder and designed to transform addresses into coordinates and coordinates back into addresses.</p>
<p>If you want to build a routing engine then better start working with offline data. If you still need to qeury for specific data then take a look at <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a> and the <a href="https://overpass-turbo.eu">overpass-turbo</a> frontend. These tools are very powerful and a lot better suited for your task.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Aug '16, 10:03</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-51293" class="comments-container">
&#10;</div>
<div id="comment-tools-51293" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51293-form-container" class="comment-form-container">
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

