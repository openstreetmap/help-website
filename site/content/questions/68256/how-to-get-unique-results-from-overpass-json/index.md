+++
type = "question"
title = "How to get unique results from Overpass JSON?"
description = '''Hello, on Overpass when I make query and ask for &quot;raw data directly from Overpass API&quot; I get a JSON that contains some extra data that I do not need. For example see the following query: [out:json][timeout:600]; (  node[&quot;shop&quot;=&quot;e-cigarette&quot;];&amp;gt;;  way[&quot;shop&quot;=&quot;e-cigarette&quot;];&amp;gt;;  relation[&quot;shop&quot;=&quot;e...'''
date = "2019-03-04T18:00:00Z"
lastmod = "2019-03-06T17:22:00Z"
weight = 68256
keywords = [ "overpassapi", "overpass", "json", "overpass-turbo", "query" ]
aliases = [ "/questions/68256" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to get unique results from Overpass JSON?](/questions/68256/how-to-get-unique-results-from-overpass-json)

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
<span id="post-68256-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68256-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68256-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, on <a href="http://overpass-turbo.eu">Overpass</a> when I make query and ask for "raw data directly from Overpass API" I get a JSON that contains some extra data that I do not need. For example see the following query:</p>
<p><code>[out:json][timeout:600]; ( node["shop"="e-cigarette"];&gt;; way["shop"="e-cigarette"];&gt;; relation["shop"="e-cigarette"];&gt;; ); out;</code></p>
<p>I would like to get all nodes/way/relation that have tag <code>shop</code> and value <code>e-cigarette</code>, so in this way I should get the count of all shop in the world that sell e-cigarettes.</p>
<p>But I get a lot of extra data, such as nodes that are a part of way/relation and ways that are a part of relation and relations theirself as well. So, is it possibile to get just one occurence for every "entity" (node or way or relation) that has some given properties? How to reach that?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-json" rel="tag" title="see questions tagged &#39;json&#39;">json</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Mar '19, 18:00</strong></p>
<img src="https://secure.gravatar.com/avatar/50334ab2e351e4f5af1917f7f6ef8dc8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andreanovenove&#39;s gravatar image" />
<p><span>Andreanovenove</span><br />
<span class="score" title="126 reputation points">126</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andreanovenove has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68256" class="comments-container">
&#10;</div>
<div id="comment-tools-68256" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68256-form-container" class="comment-form-container">
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

<span id="68269"></span>

<div id="answer-container-68269" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68269-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68269-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68269-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Andreanovenove has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Remove "&gt;;" from every line and you should get what you request.</p>
<p>That statement substantially means "get all the objects referenced by the one you have found". For more info: <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_down_.28.3E.29">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_down_.28.3E.29</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '19, 10:44</strong></p>
<img src="https://secure.gravatar.com/avatar/9c8957ccf79025bf749665ebec2bdfa2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MarcoR&#39;s gravatar image" />
<p><span>MarcoR</span><br />
<span class="score" title="687 reputation points">687</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MarcoR has 5 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-68269" class="comments-container">
<span id="68277"></span>
<div id="comment-68277" class="comment">
<div id="post-68277-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your reply. Yes, it works, but I would like to get a couple of coordinates for every point (node/way/relation). I know that a way or relation could have several coordinates, do you know if is it possible to get just one couple of lat and lon for every object? Then every object should have "type", "id", "lat", "lon" and "tags".</p>
</div>
<div id="comment-68277-info" class="comment-info">
<span class="comment-age">(05 Mar '19, 18:23)</span> <span class="comment-user userinfo">Andreanovenove</span>
</div>
</div>
<span id="68282"></span>
<div id="comment-68282" class="comment">
<div id="post-68282-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Try <code>out center;</code> instead of <code>out</code>.</p>
<p>It calculates the center of the bounding box of the feature or so, so it might not work if you want a better centroid than that.</p>
</div>
<div id="comment-68282-info" class="comment-info">
<span class="comment-age">(05 Mar '19, 19:46)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="68283"></span>
<div id="comment-68283" class="comment">
<div id="post-68283-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I did see it, from here: <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Standalone_queries.">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Standalone_queries.</a> Do you know what does the note mean? "Note: The center point is not guaranteed to lie inside the polygon". Anyway it seems to work but I have to double check it. Thank you so much for your help!</p>
</div>
<div id="comment-68283-info" class="comment-info">
<span class="comment-age">(05 Mar '19, 20:06)</span> <span class="comment-user userinfo">Andreanovenove</span>
</div>
</div>
<span id="68286"></span>
<div id="comment-68286" class="comment">
<div id="post-68286-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's what maxerickson was talking about. Think about an object shaped like a horseshoe. The centre of the bounding box would be in the middle of the open area, not inside the actual area of the object.</p>
</div>
<div id="comment-68286-info" class="comment-info">
<span class="comment-age">(05 Mar '19, 21:45)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="68304"></span>
<div id="comment-68304" class="comment">
<div id="post-68304-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh, I see. The horseshoe example opens my mind about the meaning of that note. Thank you. Do you know a way to get just the first couple of coordinates or any of the nodes' coordinates corrisponding to a way/relation instead of calculated center?</p>
</div>
<div id="comment-68304-info" class="comment-info">
<span class="comment-age">(06 Mar '19, 17:22)</span> <span class="comment-user userinfo">Andreanovenove</span>
</div>
</div>
</div>
<div id="comment-tools-68269" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68269-form-container" class="comment-form-container">
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

