+++
type = "question"
title = "How to merge maps that were developed independently?"
description = '''Hello. Some time ago I have downloaded pbf map (MAP-1) from geofabrik. Since then I have edited this map for my own purposes (mostly added some ways). Now I have downloaded a new map (MAP-2) of a different region and I would like to merge those maps (to further edit them locally).  The problem is, t...'''
date = "2019-05-06T13:33:00Z"
lastmod = "2019-05-07T12:04:00Z"
weight = 69103
keywords = [ "conflicts", "map", "id", "osmosis", "merge" ]
aliases = [ "/questions/69103" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to merge maps that were developed independently?](/questions/69103/how-to-merge-maps-that-were-developed-independently)

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
<span id="post-69103-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69103-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69103-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello.</p>
<p>Some time ago I have downloaded pbf map (MAP-1) from geofabrik. Since then I have edited this map for my own purposes (mostly added some ways). Now I have downloaded a new map (MAP-2) of a different region and I would like to merge those maps (to further edit them locally).<br />
The problem is, that after using osmosis merge, some of the ways that I have edited in MAP-1 suddenly lead to MAP-2 and back.</p>
<p>What I think happened is that there are node ID conflicts because both maps have a common source, but were later developed independently - I have added some nodes, they got own IDs and official osm MAP-2 was edited at the same time, and nodes with the same IDs were created but in different places. That way depending on the conflict resolution method in osmosis merge command, either the way on the MAP-2 leads to the MAP-1 or vice versa.</p>
<p>Solutions that I have thought about:</p>
<ol>
<li><p>Extract changes done by me (either by finding author, or using timestamp) from local MAP-1, download new MAP-1-new, merge MAP-1-new with MAP-2 and add the changes back</p></li>
<li><p>Increase IDs of objects that were created by me by a huge number, so that no conflict occurs</p></li>
</ol>
<p>Extra suggestions are most welcome.</p>
<p>I have no idea how to implement any of the solutions nor if they are correct. I will be grateful for any hints.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-conflicts" rel="tag" title="see questions tagged &#39;conflicts&#39;">conflicts</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 May '19, 13:33</strong></p>
<img src="https://secure.gravatar.com/avatar/30591e74ea983d1d5f193b588868c497?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JacekDAC&#39;s gravatar image" />
<p><span>JacekDAC</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JacekDAC has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-69103" class="comments-container">
<span id="69106"></span>
<div id="comment-69106" class="comment">
<div id="post-69106-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are the ways that you have added in some way unsuitable for inclusion in OpenStreetMap?</p>
<p>I think that the strategy used by some of the editing software is to use negative IDs for items that hanve't yet been uploaded to avoid conflicts, but my experience is restricted to user-side stuff, not anything on the backend.</p>
</div>
<div id="comment-69106-info" class="comment-info">
<span class="comment-age">(06 May '19, 16:09)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="69109"></span>
<div id="comment-69109" class="comment">
<div id="post-69109-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, the changes are not suitable to be included in OpenStreetMap.</p>
<p>Unfortunately, this is not a case. I run my own OpenStreetMap server and I have published the data there - this means that IDs are not negative.</p>
<p>I think that osmosis --read-apidb-change intervalBegin would be suitable but I need to read file not database. I need something like --read-pbf-change. Of filter by the author</p>
</div>
<div id="comment-69109-info" class="comment-info">
<span class="comment-age">(07 May '19, 08:07)</span> <span class="comment-user userinfo">JacekDAC</span>
</div>
</div>
</div>
<div id="comment-tools-69103" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69103-form-container" class="comment-form-container">
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

<span id="69111"></span>

<div id="answer-container-69111" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69111-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69111-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69111-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would simply renumber one of the datasets see <a href="https://docs.osmcode.org/osmium/latest/osmium-renumber.html">https://docs.osmcode.org/osmium/latest/osmium-renumber.html</a> (starting with ids that are guaranteed to not conflict with what you have used).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 May '19, 12:04</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 May '19, 12:04</strong> </span></p>
</div>
</div>
<div id="comments-container-69111" class="comments-container">
&#10;</div>
<div id="comment-tools-69111" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69111-form-container" class="comment-form-container">
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

