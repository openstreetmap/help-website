+++
type = "question"
title = "How to create a custom &quot;POI Type&quot; with user-defined tags in OsmAnd"
description = '''How can I create a new &quot;POI Type&quot; (aka &quot;Category&quot;) in OsmAnd by typing the OSM tags that I want to query for? When creating a new &quot;POI Type&quot; in OsmAnd, the UX lets you choose from a bunch of pre-existing categories, and filtering some metadata about those categories. But what I want to do is search ...'''
date = "2024-01-18T22:24:00Z"
lastmod = "2024-01-18T22:24:00Z"
weight = 88171
keywords = [ "category", "osmand", "fabric", "tags" ]
aliases = [ "/questions/88171" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to create a custom "POI Type" with user-defined tags in OsmAnd](/questions/88171/how-to-create-a-custom-poi-type-with-user-defined-tags-in-osmand)

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
<span id="post-88171-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88171-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88171-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I create a new <a href="https://osmand.net/docs/user/search/search-poi#categories-poi-search">"POI Type" (aka "Category")</a> in OsmAnd by typing the OSM tags that I want to query for?</p>
<p>When creating a new "POI Type" in OsmAnd, the UX lets you choose from a bunch of pre-existing categories, and filtering some metadata about those categories. But what I want to do is search by OSM tag name &amp; value.</p>
<p>For example, I'm trying to buy a zipper. On OsmAnd, the closest thing to "a store that sells zippers" that I can find in the "Categories" section of POIs is "Drapery Store". But I'm not sure if a store that sells curtains is going to sell zippers.</p>
<p>If I check the OSM wiki, then I see that there's a <a href="https://wiki.openstreetmap.org/wiki/Tag:shop%3Dsewing">sewing shop that could be tagged</a> in a number of ways:</p>
<ol>
<li>shop=sewing</li>
<li>shop=fabric</li>
<li>shop=wool</li>
<li>shop=craft</li>
<li>shop=haberdashery</li>
<li>craft=sewing</li>
</ol>
<p>I <a href="https://help.openstreetmap.org/questions/88169/how-to-translate-osmand-poi-type-to-osm-wiki-tags">recently learned</a> that, in fact, a "Drapery store" in OsmAnd is merely just</p>
<ul>
<li>shop=fabric</li>
</ul>
<p>...therefore, I think I'm missing all of the other tags, such as</p>
<ul>
<li>shop=sewing</li>
</ul>
<p>What I want to do is to define my own Category using tags, such that one category will include all nodes that have any of the above tags.</p>
<p>But I'm not asking specifically about my query with the drapery store and the finite list of tags enumerated above. I'm asking a more general question:</p>
<p>How can I create a new "POI Type" (or "Category") in OsmAnd by directly defining the tags from the actual OSM dataset?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-category" rel="tag" title="see questions tagged &#39;category&#39;">category</span> <span class="post-tag tag-link-osmand" rel="tag" title="see questions tagged &#39;osmand&#39;">osmand</span> <span class="post-tag tag-link-fabric" rel="tag" title="see questions tagged &#39;fabric&#39;">fabric</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jan '24, 22:24</strong></p>
<img src="https://secure.gravatar.com/avatar/0f7bbdc746034db6f838997f2a85a59c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maltfield&#39;s gravatar image" />
<p><span>maltfield</span><br />
<span class="score" title="55 reputation points">55</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maltfield has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jan '24, 22:27</strong> </span></p>
</div>
</div>
<div id="comments-container-88171" class="comments-container">
&#10;</div>
<div id="comment-tools-88171" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88171-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

