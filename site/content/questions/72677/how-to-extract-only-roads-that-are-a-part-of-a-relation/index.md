+++
type = "question"
title = "How to extract only roads that are a part of a relation?"
description = '''I want to retrieve a map of all the roads that are a part of a particular relation. This can be a specific public transport route in a city, or its entire public transport network. I have the following input data:  the map of the country downloaded from Geofabrik as country-latest.osm.pbf the relati...'''
date = "2020-01-25T16:57:00Z"
lastmod = "2020-01-25T20:52:00Z"
weight = 72677
keywords = [ "query", "public-transport", "osmosis" ]
aliases = [ "/questions/72677" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to extract only roads that are a part of a relation?](/questions/72677/how-to-extract-only-roads-that-are-a-part-of-a-relation)

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
<span id="post-72677-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72677-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72677-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to retrieve a map of all the roads that are a part of a particular relation. This can be a specific public transport route in a city, or its entire public transport network. I have the following input data:</p>
<ul>
<li>the map of the country downloaded from Geofabrik as <code>country-latest.osm.pbf</code></li>
<li>the relation ID</li>
</ul>
<p>For example, for the country of Moldova, relation <code>6726484</code> includes all the public transport routes in its capital.</p>
<p>Is it possible to filter this data with <code>osmosis</code>, using the command line?</p>
<p>So far my best shot at it is <code>osmosis --rbf moldova-latest.osm.pbf --tf accept-ways highway=* --tf reject-ways highway=steps,footway,pedestrian,service,residential --wx moldova-roads-only.osm</code></p>
<p>In other words, I am removing all the ways that are not likely to be part of any route, but this is a very rough approach, and I suspect that I could get much better results if I could leverage the information about the relation itself.</p>
<p>How can this be accomplished?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-public-transport" rel="tag" title="see questions tagged &#39;public-transport&#39;">public-transport</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jan '20, 16:57</strong></p>
<img src="https://secure.gravatar.com/avatar/f670011755afca7029c6be1f9abe2c98?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ralien&#39;s gravatar image" />
<p><span>ralien</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ralien has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jan '20, 20:53</strong> </span></p>
</div>
</div>
<div id="comments-container-72677" class="comments-container">
&#10;</div>
<div id="comment-tools-72677" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72677-form-container" class="comment-form-container">
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

<span id="72679"></span>

<div id="answer-container-72679" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72679-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72679-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72679-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ralien has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can do this with <a href="https://osmcode.org/osmium-tool/">Osmium</a> using the <a href="https://docs.osmcode.org/osmium/latest/osmium-getid.html">getid</a> command:</p>
<pre><code>osmium getid -r moldova-latest.osm.pbf rRELATION_ID</code></pre>
<p>Osmium also has the tags-filter command to filter by tags if you need that, too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jan '20, 20:13</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jan '20, 20:14</strong> </span></p>
</div>
</div>
<div id="comments-container-72679" class="comments-container">
<span id="72680"></span>
<div id="comment-72680" class="comment">
<div id="post-72680-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, this does exactly what I wanted. I am marking it as the accepted answer, even though it is <code>osmium</code> rather than <code>osmosis</code>. I will edit the question title, to make it easier to find.</p>
</div>
<div id="comment-72680-info" class="comment-info">
<span class="comment-age">(25 Jan '20, 20:52)</span> <span class="comment-user userinfo">ralien</span>
</div>
</div>
</div>
<div id="comment-tools-72679" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72679-form-container" class="comment-form-container">
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

