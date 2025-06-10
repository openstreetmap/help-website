+++
type = "question"
title = "Duplicate city names in US search"
description = '''Many US city names are not unique. For example there are 28 cities named &quot;Dover&quot;, each in a different state, such as Dover, New Jersey, US; Dover, Delaware, US; and Dover, Minnesota, US. Typing &quot;Dover&quot; in SEARCH, the option list pops up with 1 &quot;Dover, UK&quot; and 28 &quot;Dover, US&quot; possibilities. Is there S...'''
date = "2012-10-23T14:49:00Z"
lastmod = "2012-10-23T15:12:00Z"
weight = 17126
keywords = [ "city", "state", "duplicate", "names", "geonames" ]
aliases = [ "/questions/17126" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Duplicate city names in US search](/questions/17126/duplicate-city-names-in-us-search)

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
<span id="post-17126-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17126-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17126-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Many US city names are not unique. For example there are 28 cities named "Dover", each in a different state, such as Dover, New Jersey, US; Dover, Delaware, US; and Dover, Minnesota, US. Typing "Dover" in SEARCH, the option list pops up with 1 "Dover, UK" and 28 "Dover, US" possibilities. Is there State information in GeoNames so that a SEARCH would show the City AND State within US ? How much of an effort would that entail to bring over ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-state" rel="tag" title="see questions tagged &#39;state&#39;">state</span> <span class="post-tag tag-link-duplicate" rel="tag" title="see questions tagged &#39;duplicate&#39;">duplicate</span> <span class="post-tag tag-link-names" rel="tag" title="see questions tagged &#39;names&#39;">names</span> <span class="post-tag tag-link-geonames" rel="tag" title="see questions tagged &#39;geonames&#39;">geonames</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Oct '12, 14:49</strong></p>
<img src="https://secure.gravatar.com/avatar/9cd4c83b40547e31c26db5d68bac158f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Heretik&#39;s gravatar image" />
<p><span>Heretik</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Heretik has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17126" class="comments-container">
&#10;</div>
<div id="comment-tools-17126" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17126-form-container" class="comment-form-container">
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

<span id="17128"></span>

<div id="answer-container-17128" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17128-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17128-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17128-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you try searching for Dover in Geonames for all countries it returns <a href="http://www.geonames.org/search.html?q=dover&amp;country=">these results</a>, so GeoNames contains the data, but their webservice as used by the OSM search box <a href="http://api.geonames.org/search?q=dover&amp;maxRows=10&amp;username=demo">doesn't return as much data</a>, and doesn't include the US state. I've had a quick look at their other API documentation and can only see state mentioned under the country subdivisions when reverse geocoding.</p>
<p>In summary I don't think it is currently possible using the existing GeoNames search webservice.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Oct '12, 15:12</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-17128" class="comments-container">
&#10;</div>
<div id="comment-tools-17128" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17128-form-container" class="comment-form-container">
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

