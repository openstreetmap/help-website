+++
type = "question"
title = "Error using Nominatim reverse geocoding node - node xml present, but not output"
description = '''Hi - I want to use Nominatim&#x27;s reverse geocoder to get a lat/lon for this node: 269908858 (Mérida, Yucatán, Mexico) Here&#x27;s the node on OSM: https://www.openstreetmap.org/node/269908858 The node has lat/lon data according the XML provided by OSM API:  https://www.openstreetmap.org/api/0.6/node/269908...'''
date = "2018-02-21T10:37:00Z"
lastmod = "2018-02-21T15:58:00Z"
weight = 62244
keywords = [ "reversegeocoding", "nodes", "nominatim", "error" ]
aliases = [ "/questions/62244" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error using Nominatim reverse geocoding node - node xml present, but not output](/questions/62244/error-using-nominatim-reverse-geocoding-node-node-xml-present-but-not-output)

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
<span id="post-62244-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62244-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62244-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi - I want to use Nominatim's reverse geocoder to get a lat/lon for this node: 269908858 (Mérida, Yucatán, Mexico)</p>
<p>Here's the node on OSM:</p>
<p><a href="https://www.openstreetmap.org/node/269908858"><code>https://www.openstreetmap.org/node/269908858</code></a></p>
<p>The node has lat/lon data according the XML provided by OSM API:</p>
<p><a href="https://www.openstreetmap.org/api/0.6/node/269908858"><code>https://www.openstreetmap.org/api/0.6/node/269908858</code></a></p>
<p>However, when I pass it to Nominatim it returns an error:</p>
<p><a href="https://nominatim.openstreetmap.org/reverse?osm_type=N&amp;osm_id=269908858&amp;format=json"><code>https://nominatim.openstreetmap.org/reverse?osm_type=N&amp;osm_id=269908858&amp;format=json</code></a></p>
<p>(the code format tag on this board is subbing "&amp;" for "<code>&amp;amp;</code>" so correct this manually before opening)</p>
<p>Error message:</p>
<p><code>Output:{"error":"Unable to geocode"}</code></p>
<p>What's missing from this node that causes this error, and what can I do about it?</p>
<p>Thanks loads for the help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Feb '18, 10:37</strong></p>
<img src="https://secure.gravatar.com/avatar/6b6c480688a03e67db06d3b620edab19?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="case_the_joint&#39;s gravatar image" />
<p><span>case_the_joint</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="case_the_joint has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62244" class="comments-container">
&#10;</div>
<div id="comment-tools-62244" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62244-form-container" class="comment-form-container">
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

<span id="62245"></span>

<div id="answer-container-62245" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62245-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62245-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62245-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think you want to use the /lookup method since you're not supplying a lat,lon in the search. <a href="https://nominatim.openstreetmap.org/lookup?osm_ids=R6265959&amp;format=json">https://nominatim.openstreetmap.org/lookup?osm_ids=R6265959&amp;format=json</a></p>
<p>When you do a forward search <a href="https://nominatim.openstreetmap.org/search?q=M%C3%A9rida&amp;countrycodes=mx">https://nominatim.openstreetmap.org/search?q=M%C3%A9rida&amp;countrycodes=mx</a> you'll note that Nominatim uses the city relation (<a href="https://www.openstreetmap.org/relation/5961522),">https://www.openstreetmap.org/relation/5961522),</a> not the city node (<a href="https://www.openstreetmap.org/node/269908858).">https://www.openstreetmap.org/node/269908858).</a></p>
<blockquote>
<blockquote>
<p>What's missing from this node</p>
</blockquote>
</blockquote>
<p>Nothing. The relation has a <code>Node Mérida (269908858) as admin_centre</code> set. For Nominatim that means both describe the same place. Nominatim chooses to ignore the node in this case.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Feb '18, 11:06</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Feb '18, 13:27</strong> </span></p>
</div>
</div>
<div id="comments-container-62245" class="comments-container">
<span id="62247"></span>
<div id="comment-62247" class="comment">
<div id="post-62247-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi <a href="https://help.openstreetmap.org/users/150/mtmail"></a><a href="https://help.openstreetmap.org/users/150/mtmail">@mtmail</a> thanks so much for the quick response and advice. I forget why I used the reverse and not the lookup. For completeness' sake, the lookup has a slightly different syntax than you suggest:</p>
<p><a href="https://nominatim.openstreetmap.org/lookup?osm_ids=R6265959&amp;format=json"><code>https://nominatim.openstreetmap.org/lookup?osm_ids=R6265959&amp;format=json</code></a></p>
<p>So if I wanted to get a set of coordinates for the <code>Merida</code> node itself, and Nominatim won't return that, then is the best substitute I can get from OSM the centre point of the <code>Merida</code> relation (5961522)?</p>
</div>
<div id="comment-62247-info" class="comment-info">
<span class="comment-age">(21 Feb '18, 11:28)</span> <span class="comment-user userinfo">case_the_joint</span>
</div>
</div>
<span id="62250"></span>
<div id="comment-62250" class="comment">
<div id="post-62250-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You're right, thanks, I updated the URL in my answer. For a relation result Nominatim tries to use the linked admin_center or admin_label roles (nodes) to set the center. So it knows about those nodes just merges the information. For example for "Hamburg" (the state, <a href="https://www.openstreetmap.org/relation/62782)">https://www.openstreetmap.org/relation/62782)</a> which is split into two parts it returns the center point of the admin_center not the geographic center <a href="https://nominatim.openstreetmap.org/lookup.php?osm_ids=R62782">https://nominatim.openstreetmap.org/lookup.php?osm_ids=R62782</a> because that wouldn't even be inside the relation/multi-polygon.</p>
</div>
<div id="comment-62250-info" class="comment-info">
<span class="comment-age">(21 Feb '18, 13:37)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="62257"></span>
<div id="comment-62257" class="comment">
<div id="post-62257-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the clarification! You've been very helpful, thank you.</p>
</div>
<div id="comment-62257-info" class="comment-info">
<span class="comment-age">(21 Feb '18, 15:58)</span> <span class="comment-user userinfo">case_the_joint</span>
</div>
</div>
</div>
<div id="comment-tools-62245" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62245-form-container" class="comment-form-container">
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

