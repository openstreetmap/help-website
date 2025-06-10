+++
type = "question"
title = "osmium export unexpected osm_ids"
description = '''Hello I&#x27;ve been exporting .osm files to .geojson using the osmium-export tool. I&#x27;m trying to keep the osm_ids(including the osm_type) so that we can lookup the osm objects downstream(e.g. through nominatim: https://nominatim.openstreetmap.org/ui/details.html I&#x27;m using the &#x27;--add-unique-id=type_id&#x27; c...'''
date = "2023-11-13T15:34:00Z"
lastmod = "2023-11-14T08:53:00Z"
weight = 87999
keywords = [ "osmium", "osmtogeojson", "export", "geojson" ]
aliases = [ "/questions/87999" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [osmium export unexpected osm_ids](/questions/87999/osmium-export-unexpected-osm_ids)

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
<span id="post-87999-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87999-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87999-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello</p>
<p>I've been exporting .osm files to .geojson using the osmium-export tool. I'm trying to keep the osm_ids(including the osm_type) so that we can lookup the osm objects downstream(e.g. through nominatim: <a href="https://nominatim.openstreetmap.org/ui/details.html">https://nominatim.openstreetmap.org/ui/details.html</a></p>
<p>I'm using the '--add-unique-id=type_id' command to include osm_ids, so my command is:</p>
<pre><code>osmium export --add-unique-id=&#39;type_id&#39; -o tmp/processed-data/planet-ports-231009.geojson tmp/processed-data/planet-ports-231009.osm --verbose</code></pre>
<p>This produces rich objects and reading the output into a geopandas dataframe does indeed produce an 'id' column as expected.</p>
<p>According to the docs:</p>
<blockquote>
<p>Or the TYPE is type_id in which case the ID is a string, the first character is the type of object (‘n’ for nodes, ‘w’ for linestrings created from ways, and ‘a’ for areas created from ways and/or relations, after that there is a unique ID based on the original OSM object ID(s).</p>
</blockquote>
<p>However, when I look at the output, there are 2 entries with the name 'Heysham Port' (I'd post screenshots here but I'm not allowed) and they represent seemingly the same geographical object, a port in the UK. These 2 objects have different osm_ids in the .geojson output: w974090785 and a1948181570.</p>
<p>I'm able to lookup the former on nominatim: <a href="https://nominatim.openstreetmap.org/ui/details.html?osmtype=W&amp;osmid=974090785">https://nominatim.openstreetmap.org/ui/details.html?osmtype=W&amp;osmid=974090785</a> But the latter is nowhere to be found, neither as node, relation or way. (tried n1948181570, r1948181570 and w1948181570) I might be misunderstanding this part of the docs: <strong>based on the original OSM object ID</strong>.</p>
<p>My question is, can I tell osmium-export to keep the original id? Alternatively, how could I match the true osm_id from the object of type 'a'? (Since I might prefer those objects, there are more of them)</p>
<p>Thanks for any help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-osmtogeojson" rel="tag" title="see questions tagged &#39;osmtogeojson&#39;">osmtogeojson</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-geojson" rel="tag" title="see questions tagged &#39;geojson&#39;">geojson</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Nov '23, 15:34</strong></p>
<img src="https://secure.gravatar.com/avatar/195f5a1aa1d352b48d20ec967546e3c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baldurgaldur&#39;s gravatar image" />
<p><span>baldurgaldur</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baldurgaldur has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87999" class="comments-container">
&#10;</div>
<div id="comment-tools-87999" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87999-form-container" class="comment-form-container">
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

<span id="88001"></span>

<div id="answer-container-88001" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-88001-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88001-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-88001-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="baldurgaldur has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no area datatype in OSM, areas are generated by Osmium from either closed ways or relations of type multipolygon. To still generate unique ids Osmium uses a simple "trick", it multiplies the id of the way or relation by 2 and adds 1 for relations. So if you see an id for an area, divide it by 2 to get the original id. If the id you see is even, it was generated from a way, if it is odd it was generated from a relation. So in your case w974090785 and a1948181570 are both generated from the same way 974090785.</p>
<p>This should be documented in the man page, but isn't. I have put it on my todo list to add that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Nov '23, 08:53</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-88001" class="comments-container">
&#10;</div>
<div id="comment-tools-88001" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88001-form-container" class="comment-form-container">
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

