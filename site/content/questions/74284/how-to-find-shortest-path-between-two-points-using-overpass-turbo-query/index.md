+++
type = "question"
title = "How to find shortest path between two points using overpass-turbo query?"
description = '''Hello, I&#x27;m using overpass-turbo to download GeoJSON files. I&#x27;m trying to find (shortest) way between two points, but I don&#x27;t know anything about query and can&#x27;t really find how to learn to use that query. So I&#x27;m having two points with their names, how do I download all lines that connect them, makin...'''
date = "2020-04-19T15:27:00Z"
lastmod = "2020-04-19T20:10:00Z"
weight = 74284
keywords = [ "path", "overpass-turbo", "shortest" ]
aliases = [ "/questions/74284" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to find shortest path between two points using overpass-turbo query?](/questions/74284/how-to-find-shortest-path-between-two-points-using-overpass-turbo-query)

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
<span id="post-74284-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74284-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74284-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I'm using overpass-turbo to download GeoJSON files. I'm trying to find (shortest) way between two points, but I don't know anything about query and can't really find how to learn to use that query. So I'm having two points with their names, how do I download all lines that connect them, making the path shorter than certain distance? Two points are really far away from each other, so I can't download all the roads and then load them into QGIS...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-path" rel="tag" title="see questions tagged &#39;path&#39;">path</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-shortest" rel="tag" title="see questions tagged &#39;shortest&#39;">shortest</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Apr '20, 15:27</strong></p>
<img src="https://secure.gravatar.com/avatar/9b2bec14fd75266cfe2ba80cd51a5779?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izili&#39;s gravatar image" />
<p><span>izili</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izili has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74284" class="comments-container">
&#10;</div>
<div id="comment-tools-74284" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74284-form-container" class="comment-form-container">
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

<span id="74285"></span>

<div id="answer-container-74285" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74285-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74285-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74285-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You probably want to use a <a href="https://wiki.openstreetmap.org/wiki/Routing">routing</a> software. You might be able to implement a crude one on top of overpass, but that would be complicated.</p>
<p>There is a lot of <a href="https://wiki.openstreetmap.org/wiki/Routing/online_routers">online routing services</a> based on OSM, and some provide an API.</p>
<p>For reference, the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass doc</a>. Quite a lot to read, but as I said, it's probably not the best option.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Apr '20, 20:10</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-74285" class="comments-container">
&#10;</div>
<div id="comment-tools-74285" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74285-form-container" class="comment-form-container">
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

