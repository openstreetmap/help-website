+++
type = "question"
title = "Nominatim place id"
description = '''Hi, What is the place_id returned as part of a Nominatim geocoding result? Where is that reflected in the OSM data? Some sample requests, all containing place_id: http://nominatim.openstreetmap.org/search?format=json&amp;amp;addressdetails=1&amp;amp;q=100%20Easy%20St,%20Carefree,%20AZ%2085377&quot;&amp;gt;http://nom...'''
date = "2013-04-15T11:10:00Z"
lastmod = "2013-04-15T11:59:00Z"
weight = 21542
keywords = [ "nominatim" ]
aliases = [ "/questions/21542" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim place id](/questions/21542/nominatim-place-id)

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
<span id="post-21542-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21542-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21542-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>What is the place_id returned as part of a Nominatim geocoding result? Where is that reflected in the OSM data?</p>
<p>Some sample requests, all containing place_id:</p>
<p><a href="%5B%3Ca%20href=">http://nominatim.openstreetmap.org/search?format=json&amp;addressdetails=1&amp;q=100%20Easy%20St,%20Carefree,%20AZ%2085377"&gt;http://nominatim.openstreetmap.org/search?format=json&amp;addressdetails=1&amp;q=100%20Easy%20St,%20Carefree,%20AZ%2085377]"&gt;http://nominatim.openstreetmap.org/search?format=json&amp;addressdetails=1&amp;q=100%20Easy%20St,%20Carefree,%20AZ%2085377</a></p>
<p><a href="%5B%3Ca%20href=">http://nominatim.openstreetmap.org/search?format=json&amp;addressdetails=1&amp;q=Steinmetzstr%2062,%2010783%20Berlin"&gt;http://nominatim.openstreetmap.org/search?format=json&amp;addressdetails=1&amp;q=Steinmetzstr%2062,%2010783%20Berlin]"&gt;http://nominatim.openstreetmap.org/search?format=json&amp;addressdetails=1&amp;q=Steinmetzstr%2062,%2010783%20Berlin</a></p>
<p><a href="%5B%3Ca%20href=">http://nominatim.openstreetmap.org/search?format=json&amp;addressdetails=1&amp;q=Eiffel%20Tower%20Paris"&gt;http://nominatim.openstreetmap.org/search?format=json&amp;addressdetails=1&amp;q=Eiffel%20Tower%20Paris]"&gt;http://nominatim.openstreetmap.org/search?format=json&amp;addressdetails=1&amp;q=Eiffel%20Tower%20Paris</a></p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Apr '13, 11:10</strong></p>
<img src="https://secure.gravatar.com/avatar/680bc1d9127776b4acb2e6af485a6869?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="konstantin&#39;s gravatar image" />
<p><span>konstantin</span><br />
<span class="score" title="61 reputation points">61</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="konstantin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-21542" class="comments-container">
&#10;</div>
<div id="comment-tools-21542" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21542-form-container" class="comment-form-container">
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

<span id="21543"></span>

<div id="answer-container-21543" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21543-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21543-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-21543-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <code>place_id</code> has no relevance for OSM, it is only an internal Nominatim identifier. Between different Nominatim instances, the <code>place_id</code> for the same OSM object may differ.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Apr '13, 11:59</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-21543" class="comments-container">
&#10;</div>
<div id="comment-tools-21543" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21543-form-container" class="comment-form-container">
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

