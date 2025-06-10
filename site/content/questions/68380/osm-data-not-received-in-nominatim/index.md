+++
type = "question"
title = "OSM data not received in nominatim"
description = '''Hi, I have added few address points(2 weeks ago) in osm.org. But still, can&#x27;t receive data in nominatim geocode API. Refer below nodes detail: https://www.openstreetmap.org/node/6311187515 https://www.openstreetmap.org/node/6308639224 Data not received in nominatim: https://nominatim.openstreetmap.o...'''
date = "2019-03-15T10:39:00Z"
lastmod = "2019-03-15T13:59:00Z"
weight = 68380
keywords = [ "geocoding", "search", "nominatim", "osm" ]
aliases = [ "/questions/68380" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM data not received in nominatim](/questions/68380/osm-data-not-received-in-nominatim)

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
<span id="post-68380-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68380-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68380-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have added few address points(2 weeks ago) in osm.org.</p>
<p>But still, can't receive data in nominatim geocode API.</p>
<p>Refer below nodes detail: <a href="https://www.openstreetmap.org/node/6311187515">https://www.openstreetmap.org/node/6311187515</a> <a href="https://www.openstreetmap.org/node/6308639224">https://www.openstreetmap.org/node/6308639224</a></p>
<p>Data not received in nominatim: <a href="https://nominatim.openstreetmap.org/search?format=json&amp;q=Vikrant">https://nominatim.openstreetmap.org/search?format=json&amp;q=Vikrant</a> Palace, Solapur <a href="https://nominatim.openstreetmap.org/search?format=json&amp;q=Cowrks,">https://nominatim.openstreetmap.org/search?format=json&amp;q=Cowrks,</a> Aerocity, New Delhi</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Mar '19, 10:39</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Mar '19, 10:39</strong> </span></p>
</div>
</div>
<div id="comments-container-68380" class="comments-container">
&#10;</div>
<div id="comment-tools-68380" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68380-form-container" class="comment-form-container">
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

<span id="68386"></span>

<div id="answer-container-68386" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68386-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68386-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68386-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Adding the city or any other address parts into the name isn't necessary. 'Vikrant Palace' and 'Cowrks' is enough. Nominatim can't handle names containing commas. That's a limitation unlikely to be fixed anytime soon.</p>
<p>When adding new places it would be great if you add tags what they represent. 'Cowkrs' could be <code>amenity=coworking_space</code> <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dcoworking_space">https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dcoworking_space</a> The palace could be a <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity=place%20of%20worship?uselang=en-US">https://wiki.openstreetmap.org/wiki/Tag:amenity=place%20of%20worship?uselang=en-US</a> or <a href="https://wiki.openstreetmap.org/wiki/Key:historic">https://wiki.openstreetmap.org/wiki/Key:historic</a> or maybe both are hotels or tourist attractions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Mar '19, 13:59</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-68386" class="comments-container">
&#10;</div>
<div id="comment-tools-68386" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68386-form-container" class="comment-form-container">
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

