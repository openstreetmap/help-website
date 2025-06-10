+++
type = "question"
title = "OverpassQL: How can i filter for ways and their related nodes in a given radius?"
description = '''I am struggling with my query setup. What i want is a set of nodes and ways (and their related nodes) in a given radius. This is what i have so far: ( nw(around:1000,52.46989,13.21026)[highway~&quot;^(motorway|trunk|primary|secondary|tertiary|unclassified|residential|living_street|service)$&quot;]; nw(around:...'''
date = "2022-05-09T12:42:00Z"
lastmod = "2022-06-07T17:12:00Z"
weight = 84418
keywords = [ "radius", "around", "overpass-ql" ]
aliases = [ "/questions/84418" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [OverpassQL: How can i filter for ways and their related nodes in a given radius?](/questions/84418/overpassql-how-can-i-filter-for-ways-and-their-related-nodes-in-a-given-radius)

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
<span id="post-84418-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84418-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84418-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am struggling with my query setup. What i want is a set of nodes and ways (and their related nodes) in a given radius.</p>
<p>This is what i have so far:</p>
<pre><code>(
nw(around:1000,52.46989,13.21026)[highway~&quot;^(motorway|trunk|primary|secondary|tertiary|unclassified|residential|living_street|service)$&quot;];
nw(around:1000,52.46989,13.21026)[highway~&quot;^(footway|path|track)$&quot;];
nw(around:1000,52.46989,13.21026)[natural~&quot;^(cave_entrance|spring|peak|rock)$&quot;];
nw(around:1000,52.46989,13.21026)[tourism~&quot;^(wildernis_hut|viewpoint)$&quot;];
);
(._;&gt;;);
out body;</code></pre>
<p>This returns all the related of nodes of the found ways in that radius. But i don't want nodes that are not in the given radius, even if they are related to said ways. How can i achieve this?</p>
<p>Also i am sure there is a more efficient way to use the around-filter (only applying it ones) but i couldn't figure this out either.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-radius" rel="tag" title="see questions tagged &#39;radius&#39;">radius</span> <span class="post-tag tag-link-around" rel="tag" title="see questions tagged &#39;around&#39;">around</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 May '22, 12:42</strong></p>
<img src="https://secure.gravatar.com/avatar/54fb737382e1afa8c9f969d8407fd9b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tibooo&#39;s gravatar image" />
<p><span>Tibooo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tibooo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84418" class="comments-container">
<span id="84435"></span>
<div id="comment-84435" class="comment">
<div id="post-84435-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>IIRC the string of punctuation on the line above <code>out body</code> gives all child nodes for the dataset under consideration. I imagine you would need to re-filter for distance after this stage, but that might give poor results as a straight section of road passing through the area could have no nodes in the search radius even if it goes directly over the point you're querying.</p>
</div>
<div id="comment-84435-info" class="comment-info">
<span class="comment-age">(11 May '22, 08:43)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="84456"></span>
<div id="comment-84456" class="comment">
<div id="post-84456-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thank you for the reply <a href="https://help.openstreetmap.org/users/4426/insertuser"></a><a href="https://help.openstreetmap.org/users/4426/insertuser">@InsertUser</a>, i think this is it. i tried to replace the line with another around filter but if i just add another around filter instead it works! (although it seems very hacky)</p>
</div>
<div id="comment-84456-info" class="comment-info">
<span class="comment-age">(12 May '22, 13:42)</span> <span class="comment-user userinfo">Tibooo</span>
</div>
</div>
<span id="84729"></span>
<div id="comment-84729" class="comment">
<div id="post-84729-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/21743/tibooo">@Tibooo</a> Could you post your solution for others to learn from.</p>
</div>
<div id="comment-84729-info" class="comment-info">
<span class="comment-age">(07 Jun '22, 17:12)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-84418" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84418-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

