+++
type = "question"
title = "How to get all nodes of a polygon (for buildings) with one known inside node"
description = '''Hi everyone!  I&#x27;m now using OSMnx to extract data for buildings. What I need is the addresses for buildings along with their footprint data. The question I met is about some of the buildings have multiple addresses, thus there are no address data for that building&#x27;s polygon.  For example, the buildi...'''
date = "2022-04-14T18:02:00Z"
lastmod = "2022-04-15T10:43:00Z"
weight = 84182
keywords = [ "buildings", "osmnx", "polygon", "multipolygon" ]
aliases = [ "/questions/84182" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get all nodes of a polygon (for buildings) with one known inside node](/questions/84182/how-to-get-all-nodes-of-a-polygon-for-buildings-with-one-known-inside-node)

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
<span id="post-84182-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84182-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84182-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone!</p>
<p>I'm now using OSMnx to extract data for buildings. What I need is the addresses for buildings along with their footprint data. The question I met is about some of the buildings have multiple addresses, thus there are no address data for that building's polygon.</p>
<p>For example, the building 'Furutorpsgatan 49A' (in Helsingborg, Sweden) has three nodes you can search for, which are:</p>
<p>Furutorpsgatan 49A; Furutorpsgatan 49B; Gustav Adolfs Gata 23</p>
<p><img src="/upfiles/footprint.png" alt="alt text" /></p>
<p>but if you export the geometry data (polygon), <strong>there's no address data at all!</strong></p>
<p>I was trying to use OSMid for polygons to match the position, but I can't find the building with OSMid 'w483244917'</p>
<p>Then I'm thinking is there any method I can <strong>export the polygon data through one or several nodes inside?</strong></p>
<p>Or could you suggest me some methods to get any building footprint polygons through building addresses?</p>
<p>Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-buildings" rel="tag" title="see questions tagged &#39;buildings&#39;">buildings</span> <span class="post-tag tag-link-osmnx" rel="tag" title="see questions tagged &#39;osmnx&#39;">osmnx</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Apr '22, 18:02</strong></p>
<img src="https://secure.gravatar.com/avatar/d501312e86894094107ddc663e69e3aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Adam%20Qi&#39;s gravatar image" />
<p><span>Adam Qi</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Adam Qi has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Apr '22, 21:50</strong> </span></p>
</div>
</div>
<div id="comments-container-84182" class="comments-container">
<span id="84183"></span>
<div id="comment-84183" class="comment">
<div id="post-84183-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I don't know about OSMnx, but in the particular example you give those addresses are on entrance nodes that form part of the building way so on the OSM side of things there is a direct relationship recorded between the address nodes and the outline. This way has the ID you mentioned in your question: <a href="https://www.openstreetmap.org/way/483244917">https://www.openstreetmap.org/way/483244917</a> , so I'm not sure why it doesn't show through your preferred tool? While w/n/r are frequently used as a shorthand for the element type in question I don't <em>think</em> they form a formal part of the ID in the database.</p>
<p>In general it is acceptable for addresses to exist on nodes as well as ways and relations and for completeness you will have to look at all three. In some cases you will be able to 'recurse up' to find ways that refer to nodes you find, in others this would need to be a spatial query for surrounding building ways or multipolygon relations and in some further cases there may be nodes for which no building outline has been traced yet.</p>
</div>
<div id="comment-84183-info" class="comment-info">
<span class="comment-age">(15 Apr '22, 10:26)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-84182" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84182-form-container" class="comment-form-container">
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

<span id="84184"></span>

<div id="answer-container-84184" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84184-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84184-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84184-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Import data into PostGIS with osm2pgsql, then</p>
<pre><code>SELECT way
FROM planet_osm_polygon
WHERE ST_CONTAINS(way, 
   (SELECT way FROM planet_osm_point 
   WHERE osm_id=1234))
AND building IS NOT NULL;</code></pre>
<p>will find you the building outline that contains the node with the id 1234. Of course you could also query for the node properties with something like <code>WHERE tags-&gt;'addr:street'='something'</code> and so on. (This syntax with <code>tags</code> assumes you have imported with the "hstore" option.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Apr '22, 10:43</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-84184" class="comments-container">
&#10;</div>
<div id="comment-tools-84184" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84184-form-container" class="comment-form-container">
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

