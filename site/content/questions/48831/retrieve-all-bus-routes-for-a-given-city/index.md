+++
type = "question"
title = "Retrieve all bus routes for a given city"
description = '''Hello, I would like to extract a list of all the relations representing bus routes in a given city (i would then access their information via RelationFullRecur(relID) API). Let&#x27;s say I would like all the bus routes in London, how would i do that? I could look at https://wiki.openstreetmap.org/wiki/Bu...'''
date = "2016-03-24T21:38:00Z"
lastmod = "2016-03-24T22:27:00Z"
weight = 48831
keywords = [ "bus", "route", "api" ]
aliases = [ "/questions/48831" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Retrieve all bus routes for a given city](/questions/48831/retrieve-all-bus-routes-for-a-given-city)

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
<span id="post-48831-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48831-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48831-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I would like to extract a list of all the relations representing bus routes in a given city (i would then access their information via RelationFullRecur(relID) API). Let's say I would like all the bus routes in London, how would i do that? I could look at <a href="https://wiki.openstreetmap.org/wiki/Bus_routes_in_London">https://wiki.openstreetmap.org/wiki/Bus_routes_in_London</a> but I'm looking for like something more automatic and programmable</p>
<p>Let's then extend it to include also tram routers, shuttles, and even boat routes (ie, all terrestrial public transportation services, nothing underground).</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Mar '16, 21:38</strong></p>
<img src="https://secure.gravatar.com/avatar/16afbe4d5f7d86de8aa279adae4945d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sandrotosi&#39;s gravatar image" />
<p><span>sandrotosi</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sandrotosi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48831" class="comments-container">
&#10;</div>
<div id="comment-tools-48831" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48831-form-container" class="comment-form-container">
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

<span id="48834"></span>

<div id="answer-container-48834" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48834-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48834-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48834-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It appears you want to process data with the "osmapi" Python package. This package is a Python wrapper around OSM API functions. The RelationFullRecur(relID) method downloads a relation and all its members from the API using the <code>relation/&lt;id&gt;/full</code> API call. This should <strong>not</strong> be used for large scale data retrieval; if you're planning to download the complete surface transport network for one or more cities, or (even worse) if you plan do build that into some application that will be used by more people than just you, think again!</p>
<p>A suitable way to get all relations of a particular kind in a particular area is using the Overpass API; see for example the last answer on <a href="/questions/37461/how-to-get-tram-stops-and-lines-routes">How to get tram stops and lines (routes).</a></p>
<p>Another option is simply downloading the full OSM data file for the region you're interested in and then pull the data from that; if you want to do that with Python, check out the <a href="https://github.com/osmcode/pyosmium">Python bindings for the Osmium library.</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Mar '16, 22:09</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-48834" class="comments-container">
<span id="48835"></span>
<div id="comment-48835" class="comment">
<div id="post-48835-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks for the references, I will look at them</p>
</div>
<div id="comment-48835-info" class="comment-info">
<span class="comment-age">(24 Mar '16, 22:27)</span> <span class="comment-user userinfo">sandrotosi</span>
</div>
</div>
</div>
<div id="comment-tools-48834" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48834-form-container" class="comment-form-container">
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

