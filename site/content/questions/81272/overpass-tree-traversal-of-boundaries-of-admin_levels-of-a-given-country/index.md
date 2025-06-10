+++
type = "question"
title = "Overpass: Tree Traversal of boundaries of admin_levels of a given country"
description = '''Hello, I am fairly new to overpass but I attempt to do a tree traversal of boundaries of admin_levels for a given country.  For example: For UK, I want the UK border. Then on next level the borders of Wales, England, Scotland, Northern Island. Then on next level, for example inside England, I want t...'''
date = "2021-08-11T10:04:00Z"
lastmod = "2021-08-11T13:26:00Z"
weight = 81272
keywords = [ "overpass", "overpass-turbo", "overpass-api", "overpass-ql" ]
aliases = [ "/questions/81272" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass: Tree Traversal of boundaries of admin_levels of a given country](/questions/81272/overpass-tree-traversal-of-boundaries-of-admin_levels-of-a-given-country)

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
<span id="post-81272-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81272-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81272-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I am fairly new to overpass but I attempt to do a tree traversal of boundaries of admin_levels for a given country.</p>
<p>For example: For UK, I want the UK border. Then on next level the borders of Wales, England, Scotland, Northern Island. Then on next level, for example inside England, I want the regions of England. Etc. At the end I would have a tree structure. I don't need to have all data all at once, but would be sufficient to get the data admin_level by admin_level.</p>
<p>I see 2 issues I am currently blocked.</p>
<p>First, I get the borders of 4 countries in UK. Can this query be optimized? I also get the nodes (capital), but I am only interested in the borders?</p>
<pre><code>[out:json];
rel(62149); //UK
map_to_area;
rel(area)[admin_level=4][boundary=administrative];
out geom;</code></pre>
<p>Second, how do I get the children for a given country? I could increment the admin_level but some admin_levels are not used. Is it better to query for admin areas inside an area?</p>
<pre><code>[out:json];
rel(58447); //England
map_to_area;
rel(area)[admin_level=5][boundary=administrative];
out geom;</code></pre>
<p>This seems excessively slow and many queries. What can be optimized?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Aug '21, 10:04</strong></p>
<img src="https://secure.gravatar.com/avatar/e33f937b46905a047cc9335560e0ba15?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Seraphis&#39;s gravatar image" />
<p><span>Seraphis</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Seraphis has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81272" class="comments-container">
&#10;</div>
<div id="comment-tools-81272" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81272-form-container" class="comment-form-container">
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

<span id="81278"></span>

<div id="answer-container-81278" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81278-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81278-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81278-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Unsure what you want your output to contain or what you want to use it for, but that would large amounts of data put a lot of strain on OP servers. If you're after full data <a href="https://osm-boundaries.com/">https://osm-boundaries.com/</a> is recommended.</p>
<p>If you're after a list of names:</p>
<pre><code>[out:csv(name,::id; false; &quot;,&quot;)];
area(3600058447); //England
rel(area)[admin_level=5][boundary=administrative];
out tags;</code></pre>
<p>3600000000 is the start number for relation's ids <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_element_id">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_element_id</a></p>
<p>RegEx can be used to search for different admin_levels in one call.</p>
<pre><code>[out:csv(name,::id; false; &quot;,&quot;)];
area(3600062149); //UK
rel(area)[admin_level~&quot;[4,5]&quot;][boundary=administrative];
out tags;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Aug '21, 13:26</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-81278" class="comments-container">
&#10;</div>
<div id="comment-tools-81278" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81278-form-container" class="comment-form-container">
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

