+++
type = "question"
title = "Getting lat, lon, admin_level from nodes in planet.osm"
description = '''I&#x27;m testing a script using PyOsmium on australia-oceania-latest.osm.pbf, though I&#x27;m planning to run it on planet.osm.pbf when I&#x27; m done. I have printed the whole tag list of elements I could definitely find on the map, such as New South Wales, which has an admin_level tag on the website, but I can&#x27;t...'''
date = "2021-07-27T11:22:00Z"
lastmod = "2021-07-27T12:05:00Z"
weight = 81084
keywords = [ "openstreetmap", "nodes", "coordinates", "tags" ]
aliases = [ "/questions/81084" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Getting lat, lon, admin_level from nodes in planet.osm](/questions/81084/getting-lat-lon-admin_level-from-nodes-in-planetosm)

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
<span id="post-81084-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81084-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81084-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm testing a script using PyOsmium on <code>australia-oceania-latest.osm.pbf</code>, though I'm planning to run it on <code>planet.osm.pbf</code> when I' m done.</p>
<p>I have printed the whole tag list of elements I could definitely find on the map, such as <a href="https://www.openstreetmap.org/relation/2316593">New South Wales</a>, which has an <code>admin_level</code> tag on the website, but I can't find it when I look into the tags from my script; other tags exist and have values as expected.</p>
<p>Furthermore, the website clearly knows where to center the view, so it has access to the coordinates of New South Wales, but I can't find them on any tag: where am I supposed to look for them?</p>
<p>The files I'm using are downloaded directly from <a href="https://planet.openstreetmap.org/">this page</a> (Latest Weekly Planet PBF File), so I don't think any data is missing. Could it be a bug in PyOsmium?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jul '21, 11:22</strong></p>
<img src="https://secure.gravatar.com/avatar/d089777d2df0dd15dd795f6f274255fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fsaler&#39;s gravatar image" />
<p><span>fsaler</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fsaler has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81084" class="comments-container">
&#10;</div>
<div id="comment-tools-81084" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81084-form-container" class="comment-form-container">
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

<span id="81085"></span>

<div id="answer-container-81085" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81085-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81085-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81085-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="fsaler has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are likely having an issue with indirection. It sounds like you might have made the assumption that there must be nodes for everything of interest? The fact that <em>some</em> interesting objects have a node describing them might have led you astray. NSW is a relation (<a href="https://www.openstreetmap.org/relation/2316593)">https://www.openstreetmap.org/relation/2316593)</a> which consists of around 700 ways (<a href="https://www.openstreetmap.org/way/623279971">https://www.openstreetmap.org/way/623279971</a> being one) and these ways then again have nodes (<a href="https://www.openstreetmap.org/node/5886081754">https://www.openstreetmap.org/node/5886081754</a> being one of thousands of nodes making up the outline of NSW).</p>
<p>So, what you have to do is: find relations (or sometimes ways) that have the tags you are interested in; construct their geometry by digging down into the member ways/nodes; then (if a single lat/lon is what you're after) construct a centre point of the resulting geometry.</p>
<p>Pyosmium can aid you in doing all this - but have you made use of that?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jul '21, 11:47</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-81085" class="comments-container">
<span id="81086"></span>
<div id="comment-81086" class="comment">
<div id="post-81086-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, I am using PyOsmium. The issue is that I will have to do this for pretty much every single town of the planet, and constructing a centre from many related nodes of each node (or relation) sounds really expensive. Is there no way to get an approximate point more quickly? I don't need it to be precise.</p>
</div>
<div id="comment-81086-info" class="comment-info">
<span class="comment-age">(27 Jul '21, 11:57)</span> <span class="comment-user userinfo">fsaler</span>
</div>
</div>
<span id="81088"></span>
<div id="comment-81088" class="comment">
<div id="post-81088-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Apparently the <code>Node</code> class exposes a <code>location</code> property; I hadn't noticed that. I'm yet to test it, but I think that solves my problem.</p>
</div>
<div id="comment-81088-info" class="comment-info">
<span class="comment-age">(27 Jul '21, 12:05)</span> <span class="comment-user userinfo">fsaler</span>
</div>
</div>
</div>
<div id="comment-tools-81085" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81085-form-container" class="comment-form-container">
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

