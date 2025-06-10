+++
type = "question"
title = "postalcode should be in uppercase for geocode?"
description = '''In my own setup of nominatim 3.1.0, got empty response for &#x27;http://localhost:8080/search.php?format=json&amp;amp;country=united kingdom&amp;amp;postalcode=st15 0dw&#x27;  But got correct data, if i give postalcode in uppercase &#x27;ST15 0DW&#x27; In https://nominatim.openstreetmap.org/search?format=json&amp;amp;country=unite...'''
date = "2018-08-28T14:42:00Z"
lastmod = "2018-08-28T15:15:00Z"
weight = 65616
keywords = [ "postalcode", "special-phrases", "geocoding", "nominatim" ]
aliases = [ "/questions/65616" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [postalcode should be in uppercase for geocode?](/questions/65616/postalcode-should-be-in-uppercase-for-geocode)

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
<span id="post-65616-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65616-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65616-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In my own setup of nominatim 3.1.0, got empty response for 'http://localhost:8080/search.php?format=json&amp;country=united kingdom&amp;postalcode=st15 0dw'</p>
<p>But got correct data, if i give postalcode in uppercase 'ST15 0DW'</p>
<p>In <a href="https://nominatim.openstreetmap.org/search?format=json&amp;country=united%20kingdom&amp;postalcode=st15%200dw">https://nominatim.openstreetmap.org/search?format=json&amp;country=united%20kingdom&amp;postalcode=st15%200dw</a> both upper &amp; lowercase return result. Am I missed anything in my setup?</p>
<p>Note: Followed nominatim latest document for setup &amp; specialphrases.sql not yet imported, that may be the reason ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postalcode" rel="tag" title="see questions tagged &#39;postalcode&#39;">postalcode</span> <span class="post-tag tag-link-special-phrases" rel="tag" title="see questions tagged &#39;special-phrases&#39;">special-phrases</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Aug '18, 14:42</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Aug '18, 14:51</strong> </span></p>
</div>
</div>
<div id="comments-container-65616" class="comments-container">
&#10;</div>
<div id="comment-tools-65616" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65616-form-container" class="comment-form-container">
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

<span id="65617"></span>

<div id="answer-container-65617" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65617-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65617-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65617-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's possible it got fixed in version 3.2. already, I can't find a specific change though. nominatim.openstreetmap.org runs version 3.2 <a href="https://github.com/openstreetmap/Nominatim/blob/master/ChangeLog">https://github.com/openstreetmap/Nominatim/blob/master/ChangeLog</a> . <a href="https://github.com/openstreetmap/Nominatim/releases/tag/v3.2.0">https://github.com/openstreetmap/Nominatim/releases/tag/v3.2.0</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Aug '18, 15:15</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-65617" class="comments-container">
&#10;</div>
<div id="comment-tools-65617" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65617-form-container" class="comment-form-container">
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

