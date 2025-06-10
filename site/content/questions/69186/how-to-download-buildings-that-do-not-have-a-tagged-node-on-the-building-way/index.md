+++
type = "question"
title = "How to download buildings that do not have a tagged node on the building way?"
description = '''I want to use a JOSM overpass query to exclude from a &quot;building=&quot; download all buildings that have an &quot;entrance=&quot; node that has &quot;addr:housenumber&quot; or &quot;addr:street&quot;. .'''
date = "2019-05-14T12:33:00Z"
lastmod = "2019-05-15T21:38:00Z"
weight = 69186
keywords = [ "josm", "overpass" ]
aliases = [ "/questions/69186" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to download buildings that do not have a tagged node on the building way?](/questions/69186/how-to-download-buildings-that-do-not-have-a-tagged-node-on-the-building-way)

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
<span id="post-69186-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69186-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69186-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to use a JOSM overpass query to exclude from a "building=<em>" download all buildings that have an "entrance=</em>" node that has "addr:housenumber" or "addr:street".</p>
<p>.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 May '19, 12:33</strong></p>
<img src="https://secure.gravatar.com/avatar/75cc9956f060892f585352e9011cd26e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alan01730&#39;s gravatar image" />
<p><span>Alan01730</span><br />
<span class="score" title="464 reputation points">464</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alan01730 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69186" class="comments-container">
&#10;</div>
<div id="comment-tools-69186" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69186-form-container" class="comment-form-container">
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

<span id="69192"></span>

<div id="answer-container-69192" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69192-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69192-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-69192-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://overpass-turbo.eu/s/IZO">Here's</a> a basic sketch of how to do it:</p>
<pre><code>[bbox:{{bbox}}];
// find buildings
way[building]-&gt;.buildings;
// nodes that are part of a building that also have an entrance tag
node(w.buildings)[entrance]-&gt;.entrances;
// buildings that have entrances
way(bn.entrances)[building]-&gt;.entranced;
// the difference between the sets
(.buildings; - .entranced;);
out geom;</code></pre>
<p>You can see that the Walmart in the bounding box is not in the result set, as it does have an entrance. You'll need to add some rules to deal with the requirement for an address component and you might want to handle relations in addition to ways, but the basic pattern is to find the buildings, use the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_.28n.2C_w.2C_r.2C_bn.2C_bw.2C_br.29">node recursion filter</a> to find the entrances, use the way (and maybe relation) recursion filters to find the buildings those nodes are members of, and then take the difference between that and the initial set of buildings.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 May '19, 02:35</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-69192" class="comments-container">
<span id="69202"></span>
<div id="comment-69202" class="comment">
<div id="post-69202-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a> that's a great answer, especially with the sample code. You are a good teacher. I always knew I'd have to learn more than just the "Wizard"</p>
</div>
<div id="comment-69202-info" class="comment-info">
<span class="comment-age">(15 May '19, 21:38)</span> <span class="comment-user userinfo">Alan01730</span>
</div>
</div>
</div>
<div id="comment-tools-69192" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69192-form-container" class="comment-form-container">
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

