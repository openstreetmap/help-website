+++
type = "question"
title = "How do contributors decide whether to create a node + relation for a city as opposed to just a relation?"
description = '''There are many cities in OSM that only (seem to) exist as relations and other cities that exist as both relations and nodes. What determines which type of elements are appropriate for a particular city? (This may apply to places larger or smaller than cities, it&#x27;s just what I&#x27;m focused on at the mom...'''
date = "2020-09-15T00:26:00Z"
lastmod = "2020-09-15T20:34:00Z"
weight = 76610
keywords = [ "data" ]
aliases = [ "/questions/76610" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How do contributors decide whether to create a node + relation for a city as opposed to just a relation?](/questions/76610/how-do-contributors-decide-whether-to-create-a-node-relation-for-a-city-as-opposed-to-just-a-relation)

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
<span id="post-76610-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76610-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-76610-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There are many cities in OSM that only (seem to) exist as relations and other cities that exist as both relations and nodes. What determines which type of elements are appropriate for a particular city?</p>
<p>(This may apply to places larger or smaller than cities, it's just what I'm focused on at the moment).</p>
<p>Here's a brief example:</p>
<ul>
<li>Relation and node for Seattle: <a href="https://www.openstreetmap.org/relation/237385">https://www.openstreetmap.org/relation/237385</a> <a href="https://www.openstreetmap.org/node/29546940">https://www.openstreetmap.org/node/29546940</a></li>
<li>Relation for Olympia (WA state capital, has no node): <a href="https://www.openstreetmap.org/relation/238005">https://www.openstreetmap.org/relation/238005</a></li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Sep '20, 00:26</strong></p>
<img src="https://secure.gravatar.com/avatar/fc2462740819de18b4ce1ea5fc6f83d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nocathere&#39;s gravatar image" />
<p><span>nocathere</span><br />
<span class="score" title="61 reputation points">61</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nocathere has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76610" class="comments-container">
<span id="76614"></span>
<div id="comment-76614" class="comment">
<div id="post-76614-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Think this question points to the issue of whether to tag <code>place=city</code> on it.</p>
</div>
<div id="comment-76614-info" class="comment-info">
<span class="comment-age">(15 Sep '20, 03:05)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
<span id="76635"></span>
<div id="comment-76635" class="comment">
<div id="post-76635-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's quite likely. I'm new to OSM, so I'm still figuring out the nomenclature and definitions.</p>
</div>
<div id="comment-76635-info" class="comment-info">
<span class="comment-age">(15 Sep '20, 16:21)</span> <span class="comment-user userinfo">nocathere</span>
</div>
</div>
</div>
<div id="comment-tools-76610" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76610-form-container" class="comment-form-container">
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

<span id="76618"></span>

<div id="answer-container-76618" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76618-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76618-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-76618-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="nocathere has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The relations in your example represent administrative areas. In some places administrative boundaries may not be available in a form that allows people to map them (or they may be available now but not in earlier years of OpenStreetMap). Even if they are available, the areas may not represent what people generally refer to as the "city". Some countries may not have an administrative division that closely matches the concept of a city, or the city limits may not be very meaningful due to accidents of geography. For example the municipal boundary where I live includes a heavily populated strip along the coast, but also a far larger unpopulated area inland, so that the centre of the admin area is far from the urban area. Use of a node and a relation allows users of the map to find both concepts depending on what they are looking for (admin boundaries and the urban settlement).</p>
<p>By the way, in your example Olympia does in fact have a place=city node: <a href="https://www.openstreetmap.org/node/2638988934">https://www.openstreetmap.org/node/2638988934</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Sep '20, 08:55</strong></p>
<img src="https://secure.gravatar.com/avatar/8da3fc19d7250ff5fbdbcbf467f9458f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alan_gr&#39;s gravatar image" />
<p><span>alan_gr</span><br />
<span class="score" title="2623 reputation points"><span>2.6k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="45 badges"><span class="bronze">●</span><span class="badgecount">45</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alan_gr has 10 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-76618" class="comments-container">
<span id="76637"></span>
<div id="comment-76637" class="comment">
<div id="post-76637-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. I'll dig in to the data some more to see how to get what I'm looking for. I'm leaning towards using nodes for my "city database" and relations to provide boundaries where possible.</p>
<p>Regarding Olympia -- that's interesting. It doesn't show up here:</p>
<p><a href="https://www.openstreetmap.org/relation/238005">https://www.openstreetmap.org/relation/238005</a></p>
<p>whereas Seattle's node does appear in its relation. The node also does not show up when you search for Olympia. Is this just a data issue or some choice based on some criteria? e.g. Seattle is way bigger, so is it eligible for some data structures not available to smaller nodes or relations, that allow its nodes to be surfaced by searches?</p>
</div>
<div id="comment-76637-info" class="comment-info">
<span class="comment-age">(15 Sep '20, 16:26)</span> <span class="comment-user userinfo">nocathere</span>
</div>
</div>
<span id="76643"></span>
<div id="comment-76643" class="comment">
<div id="post-76643-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You'll find such situations often in OSM. Someone created a stub relation, someone else extended it, a third person created the city node but did not care about the relation. Map quality and completeness is constantly improving with every edit made.</p>
<p>Feel free to be the next mapper adding that node to the relation. It is already in the relations for the state and the county.</p>
</div>
<div id="comment-76643-info" class="comment-info">
<span class="comment-age">(15 Sep '20, 18:49)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="76644"></span>
<div id="comment-76644" class="comment">
<div id="post-76644-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I see, OK. Thanks. I'd like to try to contribute. I'm having no luck so far but I'll keep at it. This is obviously an issue for a separate post, if it comes to that.</p>
</div>
<div id="comment-76644-info" class="comment-info">
<span class="comment-age">(15 Sep '20, 20:34)</span> <span class="comment-user userinfo">nocathere</span>
</div>
</div>
</div>
<div id="comment-tools-76618" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76618-form-container" class="comment-form-container">
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

