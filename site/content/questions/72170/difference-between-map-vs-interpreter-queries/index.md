+++
type = "question"
title = "Difference between /map vs /interpreter queries"
description = '''We were previously using http://overpass-api.de/api/map?bbox={bounding box cords} to retrieve data within the provided bounding box coords. To increase our limits and speed we have launched our own instance of the overpass API. This API uses the interpreter and we are making the query like /api/inte...'''
date = "2019-12-19T18:55:00Z"
lastmod = "2019-12-21T18:47:00Z"
weight = 72170
keywords = [ "overpass" ]
aliases = [ "/questions/72170" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Difference between /map vs /interpreter queries](/questions/72170/difference-between-map-vs-interpreter-queries)

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
<span id="post-72170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72170-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We were previously using <a href="http://overpass-api.de/api/map?bbox=%7Bbounding"><code>http://overpass-api.de/api/map?bbox={bounding</code></a><code> box cords}</code> to retrieve data within the provided bounding box coords. To increase our limits and speed we have launched our own instance of the overpass API.</p>
<p>This API uses the interpreter and we are making the query like <code>/api/interpreter?data=[out:xml];node({bbox coords});out;</code></p>
<p>This produces different results and we do not get street data like <code>tag k="highway" v="secondary"</code> or <code>tag k="type" v="multipolygon"</code> for buildings.</p>
<p>What is the different between <code>/api/map</code> vs <code>/api/interpreter</code> and is it possible to get similar data with the interpreter? What would be the equivalent <code>api/map?bbox={bounding box cords}</code> query for the interpreter?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Dec '19, 18:55</strong></p>
<img src="https://secure.gravatar.com/avatar/2bf2921024c31d2d4f66c4b4573f19c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kida001&#39;s gravatar image" />
<p><span>kida001</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kida001 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Dec '19, 10:08</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-72170" class="comments-container">
&#10;</div>
<div id="comment-tools-72170" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72170-form-container" class="comment-form-container">
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

<span id="72175"></span>

<div id="answer-container-72175" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72175-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kida001 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The reason you aren't receiving <a href="https://wiki.openstreetmap.org/wiki/Elements">elements</a> with tags <code>highway=secondary</code> or multipolygon elements is that you are only querying for <em><a href="https://wiki.openstreetmap.org/wiki/Node">nodes</a></em>. To retrieve roads and buildings you need to search for <em><a href="https://wiki.openstreetmap.org/wiki/Way">ways</a></em>, to retrieve multipolygon buildings you need to search for <em><a href="https://wiki.openstreetmap.org/wiki/Relation">relations</a></em>, too.</p>
<p>To search for nodes, ways and relations (<em>nrw</em>) use the following query:</p>
<pre><code>https://.../api/interpreter?data=[out:xml];nwr({{bbox}});out;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Dec '19, 10:15</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Dec '19, 10:15</strong> </span></p>
</div>
</div>
<div id="comments-container-72175" class="comments-container">
<span id="72180"></span>
<div id="comment-72180" class="comment">
<div id="post-72180-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, before your answer I was using <code>[out:xml];(way[highway]({{bbox}});way[building](#{{bbox}}););(._;&gt;;);out;</code></p>
<p>Is either one of the two more efficient? At times if I just want to search for buildings is it best to use the query I have above sans highway?</p>
</div>
<div id="comment-72180-info" class="comment-info">
<span class="comment-age">(20 Dec '19, 18:00)</span> <span class="comment-user userinfo">kida001</span>
</div>
</div>
<span id="72192"></span>
<div id="comment-72192" class="comment">
<div id="post-72192-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not really familiar with Overpass API internals. However personally I would always stick to the more stricter rules as long as it returns all necessary data.</p>
</div>
<div id="comment-72192-info" class="comment-info">
<span class="comment-age">(21 Dec '19, 18:47)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-72175" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72175-form-container" class="comment-form-container">
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

