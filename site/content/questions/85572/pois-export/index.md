+++
type = "question"
title = "POIs export"
description = '''Hey all, new here and non-technical and tasked with getting a dataset for roughly 10,000 POIs in the biggest global cities (NYC, London, LA, Tokyo, Paris, etc). Biased towards areas like public landmarks like townsquares, urban parks, statues, etc. The data should consist of a lat/long at minimum. A...'''
date = "2022-09-06T20:24:00Z"
lastmod = "2022-11-17T12:22:00Z"
weight = 85572
keywords = [ "dataset", "export", "poi" ]
aliases = [ "/questions/85572" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [POIs export](/questions/85572/pois-export)

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
<span id="post-85572-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85572-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85572-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey all, new here and non-technical and tasked with getting a dataset for roughly 10,000 POIs in the biggest global cities (NYC, London, LA, Tokyo, Paris, etc). Biased towards areas like public landmarks like townsquares, urban parks, statues, etc. The data should consist of a lat/long at minimum.</p>
<p>Any suggestions for how to get this / similar in the easiest way?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-dataset" rel="tag" title="see questions tagged &#39;dataset&#39;">dataset</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Sep '22, 20:24</strong></p>
<img src="https://secure.gravatar.com/avatar/5638f36bde22585ab4efa089af9d3526?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cway&#39;s gravatar image" />
<p><span>cway</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cway has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-85572" class="comments-container">
&#10;</div>
<div id="comment-tools-85572" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85572-form-container" class="comment-form-container">
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

<span id="85620"></span>

<div id="answer-container-85620" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85620-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85620-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85620-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't think there is a completely non-technical way. You'll have to learn a bit.</p>
<p>You'll have to identify all tags you are interested in, e. g. like <a href="https://wiki.openstreetmap.org/wiki/Key:leisure">wiki.openstreetmap.org/wiki/Key:leisure</a> and then to query them.</p>
<p>You might get the data from <a href="https://overpass-turbo.eu/">overpass-turbo.eu</a> but you'll have to adopt their query language to</p>
<ol>
<li>get cities by size</li>
<li>list nodes, ways or relations with these tags within the boundaries of the cities by providing all tags of POIs you are interested in.</li>
</ol>
<p>The easiest way to adopt the query language is from examples on <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example">wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example</a></p>
<p>It will be actually a pretty straightforward query, there are similar ones among the examples, but I understand the language might be intimidating on the first look. Trying to understand the similar examples first might help. Or if you can ask a programmer, he will be able do it within an hour.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Sep '22, 09:32</strong></p>
<img src="https://secure.gravatar.com/avatar/09a1a1cd124f201034ea65b3817243b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="myneur&#39;s gravatar image" />
<p><span>myneur</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="myneur has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Sep '22, 17:25</strong> </span></p>
</div>
</div>
<div id="comments-container-85620" class="comments-container">
<span id="86169"></span>
<div id="comment-86169" class="comment">
<div id="post-86169-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for this! Do you know where I could find someone / a service to hire that would be able to search a set of provided cities and find a set of points of interests (ex: all interesting points within Central Park) with their lat/longs?</p>
</div>
<div id="comment-86169-info" class="comment-info">
<span class="comment-age">(16 Nov '22, 17:28)</span> <span class="comment-user userinfo">cway</span>
</div>
</div>
<span id="86172"></span>
<div id="comment-86172" class="comment">
<div id="post-86172-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/22198/cway">@cway</a>: I'd recommend to contact Geofabrik or Thomas Skowron (the latter once developed a poi search api) for your task. You'll find those two and more providers on this (uncurated) list: <a href="https://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services">https://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services</a></p>
</div>
<div id="comment-86172-info" class="comment-info">
<span class="comment-age">(17 Nov '22, 12:22)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
</div>
<div id="comment-tools-85620" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85620-form-container" class="comment-form-container">
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

