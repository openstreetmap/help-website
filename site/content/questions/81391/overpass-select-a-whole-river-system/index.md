+++
type = "question"
title = "Overpass: select a whole river system"
description = '''I am using the following lines to catch a whole river (main stream, side streams and tributaries): [out:json][timeout:120]; // Set search area {{geocodeArea:Sweden}}-&amp;gt;.a; // Get river (relation) and its tributaries // Skip natural=water (used e.g. for islands) and natural=reservoir ( rel[waterway...'''
date = "2021-08-20T14:11:00Z"
lastmod = "2021-09-06T18:11:00Z"
weight = 81391
keywords = [ "overpass", "waterway", "river", "destination" ]
aliases = [ "/questions/81391" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass: select a whole river system](/questions/81391/overpass-select-a-whole-river-system)

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
<span id="post-81391-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81391-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81391-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using the following lines to <strong>catch a whole river</strong> (main stream, side streams and tributaries):</p>
<pre><code>[out:json][timeout:120];
// Set search area
{{geocodeArea:Sweden}}-&gt;.a;
// Get river (relation) and its tributaries
// Skip natural=water (used e.g. for islands) and natural=reservoir
(
rel[waterway][name=&quot;Luleälven&quot;](area.a); 
wr[waterway][destination=&quot;Luleälven&quot;][!natural](area.a);
) -&gt; .river;
.river out geom;</code></pre>
<p>For "simple" rivers that works fine as long as all parts of the river are added to the <strong>relation</strong> of this river or as long as they have this river stated as <strong>destination</strong>, e.g. for tributaries.</p>
<p>However, many rivers have larger tributaries that form own relations. For example, the biggest tributary of Luleälven (<a href="https://www.openstreetmap.org/relation/6974663)">https://www.openstreetmap.org/relation/6974663)</a> is Lille Luleälven (<a href="https://www.openstreetmap.org/relation/12802656).">https://www.openstreetmap.org/relation/12802656).</a> Lilla Luleälven has a couple of tributaries on its own. As long as the relation "Lilla Luleälven" is tagged as "destination=Luleälven" it works fine with the code above.</p>
<p>What does not work is when <strong>more levels</strong> are added. E.g. if one wants to capture tributaries of the tributary. Ráhpaädno (<a href="https://www.openstreetmap.org/way/30833503)">https://www.openstreetmap.org/way/30833503)</a> which first passes one big lake and one big reservoir before it comes close to yet some other lakes from where one starts calling the river Lilla Luleälven. In this case, the name of the nearest lakes or "Lilla Luleälven" would be a good choice for destination, not "Luleälven" or "Baltic see". (I am sure there are more and better examples.)</p>
<p>Is there any way to <strong>select a whole river system in Overpass</strong> using the relations that are defined for rivers in a <strong>recursive</strong> way? For example a command that adds all tributary relations of a river to the main river including the tributaries of the tributaries? That would be great!</p>
<p>All solutions and ideas are welcome, <strong>thanks</strong> in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-waterway" rel="tag" title="see questions tagged &#39;waterway&#39;">waterway</span> <span class="post-tag tag-link-river" rel="tag" title="see questions tagged &#39;river&#39;">river</span> <span class="post-tag tag-link-destination" rel="tag" title="see questions tagged &#39;destination&#39;">destination</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Aug '21, 14:11</strong></p>
<img src="https://secure.gravatar.com/avatar/ffb12f7c2548687764b2de9e4562d2d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="G%C3%A5seborg&#39;s gravatar image" />
<p><span>Gåseborg</span><br />
<span class="score" title="311 reputation points">311</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gåseborg has 4 accepted answers">50%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Aug '21, 14:15</strong> </span></p>
</div>
</div>
<div id="comments-container-81391" class="comments-container">
&#10;</div>
<div id="comment-tools-81391" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81391-form-container" class="comment-form-container">
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

<span id="81646"></span>

<div id="answer-container-81646" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81646-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81646-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81646-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is <strong>a convenient solution</strong> using the block statment <em>complete</em> and a recourse filter:</p>
<pre><code>[out:json][timeout:120];
// Set search area
{{geocodeArea:Sweden}}-&gt;.a;
// Get river (relation) and its tributaries
// Skip natural=water (used e.g. for islands) and natural=reservoir
(
rel[waterway][name=&quot;Luleälven&quot;](area.a); 
complete { way(r);node(w);way(bn);rel(bw)[type=waterway]; } 
) -&gt; .river;
.river out geom;</code></pre>
<p>This way, it is not important to tag tributaries with <em>destination</em>, they only need to be connected with the main river (or yet another tributary) at their confluence. A very nice function of Overpass! I am <strong>happy</strong> :)</p>
<p><strong>What it does (at least as I understand it):</strong> Starting with the relation of the main river (Luleälven in this case), way(r) collects all ways that are members of this relation and node(w) collects all nodes that are members of the these ways. Then, way(bn) finds all ways linking to these nodes - these ways are the parts of tributaries closest to the confluence - and, finally, rel(bw) gets all relations linking to the just found ways, i.e. the relations of the tributaries, in our case Lilla Luleälven.</p>
<p>For more information, check:</p>
<ul>
<li><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#The_block_statement_complete">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#The_block_statement_complete</a> and</li>
<li><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_.28n.2C_w.2C_r.2C_bn.2C_bw.2C_br.29">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_.28n.2C_w.2C_r.2C_bn.2C_bw.2C_br.29</a></li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Sep '21, 18:11</strong></p>
<img src="https://secure.gravatar.com/avatar/ffb12f7c2548687764b2de9e4562d2d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="G%C3%A5seborg&#39;s gravatar image" />
<p><span>Gåseborg</span><br />
<span class="score" title="311 reputation points">311</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gåseborg has 4 accepted answers">50%</span></p>
</div>
</div>
<div id="comments-container-81646" class="comments-container">
&#10;</div>
<div id="comment-tools-81646" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81646-form-container" class="comment-form-container">
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

