+++
type = "question"
title = "Any advices on OSRM Server API"
description = '''I utilise OSRM Server API to obtain a car path between two point and I use REST. I create the link: http://router.project-osrm.org/viaroute?loc=lat1,lon1&amp;amp;loc=lat2,loc2 and it returns me a json file and my question is how I can specify, how I can obtain the fattest path o shortest path? the defau...'''
date = "2014-10-22T17:16:00Z"
lastmod = "2014-10-22T17:20:00Z"
weight = 37874
keywords = [ "osrm", "json", "geojson" ]
aliases = [ "/questions/37874" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Any advices on OSRM Server API](/questions/37874/any-advices-on-osrm-server-api)

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
<span id="post-37874-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37874-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37874-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I utilise OSRM Server API to obtain a car path between two point and I use REST. I create the link: <a href="http://router.project-osrm.org/viaroute?loc=lat1,lon1&amp;loc=lat2,loc2">http://router.project-osrm.org/viaroute?loc=lat1,lon1&amp;loc=lat2,loc2</a> and it returns me a json file and my question is how I can specify, how I can obtain the fattest path o shortest path? the default is fatest path?Anyone can help me?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-json" rel="tag" title="see questions tagged &#39;json&#39;">json</span> <span class="post-tag tag-link-geojson" rel="tag" title="see questions tagged &#39;geojson&#39;">geojson</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Oct '14, 17:16</strong></p>
<img src="https://secure.gravatar.com/avatar/3f61c27a1a925da107eb8c38d3392b6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scupetta18&#39;s gravatar image" />
<p><span>scupetta18</span><br />
<span class="score" title="-3 reputation points">-3</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scupetta18 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37874" class="comments-container">
&#10;</div>
<div id="comment-tools-37874" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37874-form-container" class="comment-form-container">
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

<span id="37875"></span>

<div id="answer-container-37875" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37875-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37875-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-37875-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSRM can only optimize for one metric. The publicly available server optimizes for travel time. If you set up your own copy of OSRM you could also optimize for length and thereby find the shortest route.</p>
<p>There are other routing engines that are more flexible, but you usually pay for that flexibility by having slower routing. You might want to check out gosmore/yournavigation, or GraphHopper.</p>
<p>You can also check out the OSRM-specific IRC channel or mailing list mentioned at the <a href="http://project-osrm.org">project's website</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Oct '14, 17:20</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Oct '14, 18:04</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-37875" class="comments-container">
&#10;</div>
<div id="comment-tools-37875" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37875-form-container" class="comment-form-container">
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

