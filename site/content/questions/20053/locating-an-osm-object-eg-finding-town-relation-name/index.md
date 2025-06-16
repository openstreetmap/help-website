+++
type = "question"
title = "Locating an OSM object, e.g. finding town relation-&gt;name"
description = '''Given a node number or a way number, typically a street but also any object, what are the API, XAPI or overpass API HTTP queries to send, and what is the algorithm to process the replies, to determine the relation number of which municipality, province, country, landuse, whichever polygon, etc... wh...'''
date = "2013-02-20T04:28:00Z"
lastmod = "2013-03-08T18:26:00Z"
weight = 20053
keywords = [ "locate", "object", "relation", "number" ]
aliases = [ "/questions/20053" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Locating an OSM object, e.g. finding town relation-\>name](/questions/20053/locating-an-osm-object-eg-finding-town-relation-name)

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
<span id="post-20053-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20053-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20053-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Given a node number or a way number, typically a street but also any object, what are the API, XAPI or overpass API HTTP queries to send, and what is the algorithm to process the replies, to determine the relation number of which municipality, province, country, landuse, whichever polygon, etc... which that object is inside? Only OSM data must be used via the Web. But this may of course be best translatable to a query system of local OSM data, notably inside a mobile device without dialing external sources.<br />
Typical use:<br />
"you are here": given coordinates of where, find municipality boundary and write its name after street name.<br />
POI list: same question for each coordinates of a collected list of POIs, e.g. to add town name to each entry.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-locate" rel="tag" title="see questions tagged &#39;locate&#39;">locate</span> <span class="post-tag tag-link-object" rel="tag" title="see questions tagged &#39;object&#39;">object</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-number" rel="tag" title="see questions tagged &#39;number&#39;">number</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Feb '13, 04:28</strong></p>
<img src="https://secure.gravatar.com/avatar/22d0547d929d81aa90014a6f0aef484a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GentilPapou&#39;s gravatar image" />
<p><span>GentilPapou</span><br />
<span class="score" title="160 reputation points">160</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GentilPapou has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-20053" class="comments-container">
&#10;</div>
<div id="comment-tools-20053" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20053-form-container" class="comment-form-container">
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

<span id="20055"></span>

<div id="answer-container-20055" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20055-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20055-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-20055-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In general, you can get the areas</p>
<ul>
<li>of a given node with: <code>node(ID);is_in;out;</code></li>
<li>of a given way with: <code>way(ID);&gt;;is_in;out;</code></li>
<li>of a given relation with: <code>rel(ID);&gt;;is_in;out;</code></li>
<li>or of a given coordinate with: <code>is_in(LAT,LON);out;</code></li>
</ul>
<p>In all cases, you need to replace ID with the object id, or LAT and LON with latitude and longitude. You need to prepend <a href="http://overpass-api.de/api/interpreter?data="><code>http://overpass-api.de/api/interpreter?data=</code></a> to get a full URL.</p>
<p>For more details, you can have a look at the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Query_for_Areas">documentation of the is_in statement</a>. To make sense of the returned data, you may need to read the <a href="https://wiki.openstreetmap.org/wiki/Key:admin_level#admin_level">documentation of the admin_level</a> key.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Feb '13, 06:56</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span> </br></p>
</div>
</div>
<div id="comments-container-20055" class="comments-container">
<span id="20594"></span>
<div id="comment-20594" class="comment">
<div id="post-20594-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Very, very neat answer, thanks a lot.<br />
I suggest actually working examples below the documentation of those statements. It's always easier to start from a working command towards what you want and get back when it stops working than to start with a non working command ;-)</p>
</div>
<div id="comment-20594-info" class="comment-info">
<span class="comment-age">(08 Mar '13, 18:26)</span> <span class="comment-user userinfo">GentilPapou</span>
</div>
</div>
</div>
<div id="comment-tools-20055" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20055-form-container" class="comment-form-container">
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

