+++
type = "question"
title = "Can I get current neighbourhood using lat and lon?"
description = '''I&#x27;m new to the API, and am having a hard time going through the API documentation. I am using browser JavaScript to get the geolocation (latitude and longitude), and would like to display the current neighbourhood/city based on the lat and long data. For example, having the lat and lon of 43.653225,...'''
date = "2019-11-27T15:50:00Z"
lastmod = "2019-11-27T16:15:00Z"
weight = 71876
keywords = [ "geolocation", "api", "neighbourhood", "javascript" ]
aliases = [ "/questions/71876" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can I get current neighbourhood using lat and lon?](/questions/71876/can-i-get-current-neighbourhood-using-lat-and-lon)

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
<span id="post-71876-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71876-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71876-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm new to the API, and am having a hard time going through the <a href="https://wiki.openstreetmap.org/wiki/API_v0.6">API documentation</a>.</p>
<p>I am using browser JavaScript to get the geolocation (latitude and longitude), and would like to display the current neighbourhood/city based on the lat and long data. For example, having the lat and lon of <code>43.653225, -79.383186</code> would result in <code>Toronto</code>.</p>
<p>Is there a specific API GET request I can make? (i.e. <a href="https://api.openstreetmap.org/api/0.6/lat=$%7Blat%7D&amp;long=$%7Blon%7D..."><code>https://api.openstreetmap.org/api/0.6/lat=${lat}&amp;long=${lon}...</code></a></p>
<p>Any help would be deeply appreciated. Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geolocation" rel="tag" title="see questions tagged &#39;geolocation&#39;">geolocation</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-neighbourhood" rel="tag" title="see questions tagged &#39;neighbourhood&#39;">neighbourhood</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Nov '19, 15:50</strong></p>
<img src="https://secure.gravatar.com/avatar/32b4b321d88eb6704c3739405afda1c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SamSverkoCurate&#39;s gravatar image" />
<p><span>SamSverkoCurate</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SamSverkoCurate has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71876" class="comments-container">
&#10;</div>
<div id="comment-tools-71876" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71876-form-container" class="comment-form-container">
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

<span id="71877"></span>

<div id="answer-container-71877" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71877-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71877-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71877-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SamSverkoCurate has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look <a href="http://nominatim.org/release-docs/latest/api/Reverse/">http://nominatim.org/release-docs/latest/api/Reverse/</a></p>
<p>Example <a href="https://nominatim.openstreetmap.org/reverse.php?format=html&amp;lat=43.653225&amp;lon=-79.383186&amp;zoom=14">https://nominatim.openstreetmap.org/reverse.php?format=html&amp;lat=43.653225&amp;lon=-79.383186&amp;zoom=14</a></p>
<p>You can add &amp;format=json, xml, geojson to the URL for 'raw' data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Nov '19, 16:06</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-71877" class="comments-container">
<span id="71878"></span>
<div id="comment-71878" class="comment">
<div id="post-71878-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is perfect! Thank you :)</p>
</div>
<div id="comment-71878-info" class="comment-info">
<span class="comment-age">(27 Nov '19, 16:15)</span> <span class="comment-user userinfo">SamSverkoCurate</span>
</div>
</div>
</div>
<div id="comment-tools-71877" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71877-form-container" class="comment-form-container">
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

