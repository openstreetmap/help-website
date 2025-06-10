+++
type = "question"
title = "Traveling salesman routing"
description = '''Is there a Traveling Salesman routing program or website where I can feed a list of lat lon coordinates or similar and it outputs the shortest route passing through all points, reordering as necesary, preferably with car, bicycle and walking options.'''
date = "2017-05-02T15:38:00Z"
lastmod = "2017-05-02T16:15:00Z"
weight = 55994
keywords = [ "routing", "traveling_salesman" ]
aliases = [ "/questions/55994" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Traveling salesman routing](/questions/55994/traveling-salesman-routing)

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
<span id="post-55994-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55994-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-55994-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a Traveling Salesman routing program or website where I can feed a list of lat lon coordinates or similar and it outputs the shortest route passing through all points, reordering as necesary, preferably with car, bicycle and walking options.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-traveling_salesman" rel="tag" title="see questions tagged &#39;traveling_salesman&#39;">traveling_salesman</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 May '17, 15:38</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-55994" class="comments-container">
&#10;</div>
<div id="comment-tools-55994" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55994-form-container" class="comment-form-container">
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

<span id="55996"></span>

<div id="answer-container-55996" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55996-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55996-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-55996-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="nevw has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>All major OSM routing engines support this:</p>
<ul>
<li>Mapzen's <a href="https://github.com/valhalla/valhalla">Valhalla</a> ("Valhalla also includes tools like time+distance matrix computation, isochrones, elevation sampling, map matching and tour optimization (Travelling Salesman)."),</li>
<li>Mapbox's <a href="http://project-osrm.org/docs/v5.5.1/api/#trip-service">OSRM</a> ("The trip plugin solves the Traveling Salesman Problem using a greedy heuristic...")</li>
<li>Graphhopper uses the <a href="https://github.com/graphhopper/jsprit/blob/master/docs/Traveling%20salesman%20problem.md">JSPrit library</a> for route optimization ("TSP problem can be modelled by defining a vehicle routing problem...")</li>
</ul>
<p>None of these services have a free and unlimited online offering (it would quickly be abused by people trying to save on their own AWS cost). Mapzen has an offer where you register a free API key and use that. OSRM doesn't need an API key, you can just use it. Graphhopper requires registration and while they have a free trial, I don't think they have a free tier.</p>
<p>All three are Open Source and you can install and use them without limits locally.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 May '17, 16:05</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 May '17, 16:06</strong> </span></p>
</div>
</div>
<div id="comments-container-55996" class="comments-container">
<span id="55997"></span>
<div id="comment-55997" class="comment">
<div id="post-55997-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Frederik, helpful and comprehensive as always.</p>
</div>
<div id="comment-55997-info" class="comment-info">
<span class="comment-age">(02 May '17, 16:15)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
</div>
<div id="comment-tools-55996" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55996-form-container" class="comment-form-container">
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

