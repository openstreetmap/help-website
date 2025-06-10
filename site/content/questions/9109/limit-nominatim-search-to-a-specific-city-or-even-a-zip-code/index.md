+++
type = "question"
title = "limit nominatim search to a specific city or even a zip code"
description = '''Hello, the search for address birkenstrasse in berlin even matches items outside berlin: http://nominatim.openstreetmap.org/search?q=Birkenstrasse%2CBerlin&amp;amp;format=json&amp;amp;addressdetails=1 How can I limit the search to a specific city or even a zip code: http://nominatim.openstreetmap.org/search...'''
date = "2011-11-18T12:55:00Z"
lastmod = "2011-11-19T15:30:00Z"
weight = 9109
keywords = [ "city", "search", "nominatim", "zip" ]
aliases = [ "/questions/9109" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [limit nominatim search to a specific city or even a zip code](/questions/9109/limit-nominatim-search-to-a-specific-city-or-even-a-zip-code)

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
<span id="post-9109-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9109-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-9109-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>the search for address birkenstrasse in berlin even matches items outside berlin: <a href="http://nominatim.openstreetmap.org/search?q=Birkenstrasse%2CBerlin&amp;format=json&amp;addressdetails=1">http://nominatim.openstreetmap.org/search?q=Birkenstrasse%2CBerlin&amp;format=json&amp;addressdetails=1</a></p>
<p>How can I limit the search to a specific city or even a zip code: <a href="http://nominatim.openstreetmap.org/search?q=Birkenstrasse%2CBerlin%2C10551&amp;format=json&amp;addressdetails=1">http://nominatim.openstreetmap.org/search?q=Birkenstrasse%2CBerlin%2C10551&amp;format=json&amp;addressdetails=1</a></p>
<p>Thanx steffen</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-zip" rel="tag" title="see questions tagged &#39;zip&#39;">zip</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Nov '11, 12:55</strong></p>
<img src="https://secure.gravatar.com/avatar/c26644bcd5cfe58505af134851b8e0d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="steffen&#39;s gravatar image" />
<p><span>steffen</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="steffen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9109" class="comments-container">
&#10;</div>
<div id="comment-tools-9109" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9109-form-container" class="comment-form-container">
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

<span id="9126"></span>

<div id="answer-container-9126" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9126-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9126-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-9126-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have to specify a bounding box (<em>viewbox=</em>) and bound the search to that area (<em>bounded=1</em>) as in <a href="http://nominatim.openstreetmap.org/search?q=Birkenstraße,%2CBerlin&amp;format=json&amp;addressdetails=1&amp;viewbox=13.58%2C52.66%2C13.6%2C52.64&amp;bounded=1.">http://nominatim.openstreetmap.org/search?q=Birkenstraße,%2CBerlin&amp;format=json&amp;addressdetails=1&amp;viewbox=13.58%2C52.66%2C13.6%2C52.64&amp;bounded=1.</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Nov '11, 15:30</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-9126" class="comments-container">
&#10;</div>
<div id="comment-tools-9126" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9126-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9113"></span>

<div id="answer-container-9113" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9113-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9113-score" class="post-score" title="current number of votes">
-3
</div>
<span id="post-9113-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you own an android device (or you can use the iso from <a href="http://www.android-x86.org">http://www.android-x86.org</a> in <a href="http://Virtualbox.org">Virtualbox.org</a> or VMware) then you can benefit from the app called OsmAnd that has the second best offline search function for OSM based data.</p>
<p>It is only topped by MapFactor Navigator free version 11 where you can also use offline maps on any PC with Windows, Linux via Wine, or WindowsMobile.</p>
<p>See <a href="http://wiki.osm.org">wiki.osm.org</a> for more details.</p>
<p>Unfortunately I cannot give you a solution about Nominatim, but have a look at <a href="http://wiki.openstreetmap.org/wiki/Nominatim">Nominatim</a> and all its sub pages for more information.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Nov '11, 14:29</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-9113" class="comments-container">
&#10;</div>
<div id="comment-tools-9113" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9113-form-container" class="comment-form-container">
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

