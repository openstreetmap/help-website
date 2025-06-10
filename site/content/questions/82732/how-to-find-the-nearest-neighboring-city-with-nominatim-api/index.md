+++
type = "question"
title = "How to find the nearest neighboring city with nominatim API"
description = '''Is there a way to find the nearest neighboring city with nominatim API? If so can anybody provide me with a working URL example? Thank you for your help in advance'''
date = "2021-12-02T10:33:00Z"
lastmod = "2021-12-13T13:34:00Z"
weight = 82732
keywords = [ "api", "nominatim" ]
aliases = [ "/questions/82732" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to find the nearest neighboring city with nominatim API](/questions/82732/how-to-find-the-nearest-neighboring-city-with-nominatim-api)

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
<span id="post-82732-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82732-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82732-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to find the nearest neighboring city with nominatim API?</p>
<p>If so can anybody provide me with a working URL example?</p>
<p>Thank you for your help in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Dec '21, 10:33</strong></p>
<img src="https://secure.gravatar.com/avatar/11db780f9ff48cc7e92d342c1a4c1c34?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pepijn%20Moesker&#39;s gravatar image" />
<p><span>Pepijn Moesker</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pepijn Moesker has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82732" class="comments-container">
&#10;</div>
<div id="comment-tools-82732" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82732-form-container" class="comment-form-container">
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

<span id="82733"></span>

<div id="answer-container-82733" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82733-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82733-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82733-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use the zoom parameter, example:</p>
<p><a href="https://nominatim.openstreetmap.org/ui/reverse.html?lat=52.114939&amp;lon=4.31488&amp;zoom=10">https://nominatim.openstreetmap.org/ui/reverse.html?lat=52.114939&amp;lon=4.31488&amp;zoom=10</a></p>
<p>(The small red circle is the coordinate, the blue circle the found city).</p>
<p>What you can't do with Nominatim: define by city size, e.g. find the nearest city with population &gt; 1 million..</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Dec '21, 11:27</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Dec '21, 11:29</strong> </span></p>
</div>
</div>
<div id="comments-container-82733" class="comments-container">
<span id="82819"></span>
<div id="comment-82819" class="comment">
<div id="post-82819-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/17439/spiekerooger"></a><a href="https://help.openstreetmap.org/users/17439/spiekerooger">@spiekerooger</a> - I'm looking for the nearest alternative town. So for example my coordinates are in Amsterdam but then I like to get the nearest city outside Amsterdam, lets say Zaandam. Is there a way to accomplish that?</p>
</div>
<div id="comment-82819-info" class="comment-info">
<span class="comment-age">(13 Dec '21, 09:33)</span> <span class="comment-user userinfo">Pepijn Moesker</span>
</div>
</div>
<span id="82824"></span>
<div id="comment-82824" class="comment">
<div id="post-82824-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/21118/pepijn-moesker"></a><a href="https://help.openstreetmap.org/users/21118/pepijn-moesker">@Pepijn Moesker</a>: That will not be doable with the Nominatim API. This alternative API here: <a href="http://geodb-cities-api.wirefreethought.com/docs/api/find-near-location">http://geodb-cities-api.wirefreethought.com/docs/api/find-near-location</a> will probably help you out, e.g. "GET /v1/geo/locations/+52.383333+4.9/nearbyCities?limit=5&amp;offset=0&amp;radius=100" has Zaandam as a result.</p>
</div>
<div id="comment-82824-info" class="comment-info">
<span class="comment-age">(13 Dec '21, 13:34)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
</div>
<div id="comment-tools-82733" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82733-form-container" class="comment-form-container">
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

