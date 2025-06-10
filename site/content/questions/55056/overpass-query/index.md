+++
type = "question"
title = "Overpass Query"
description = '''I need to perform a query that collects all the nodes and ways that contain a specific tag. I also need, however, to get all the member nodes of the resulting ways even if they do not contain the specified tag. Finally, I need to sort the result in order to have: first the list of all nodes and then...'''
date = "2017-03-14T10:50:00Z"
lastmod = "2017-03-18T15:28:00Z"
weight = 55056
keywords = [ "query", "overpass-api" ]
aliases = [ "/questions/55056" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass Query](/questions/55056/overpass-query)

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
<span id="post-55056-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55056-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55056-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to perform a query that collects all the nodes and ways that contain a specific tag. I also need, however, to get all the member nodes of the resulting ways even if they do not contain the specified tag. Finally, I need to sort the result in order to have: first the list of all nodes and then the list of the ways, removing all duplicates. I did this, but it doesn't work properly.</p>
<pre><code> [out:json];
    (
      node[&#39;amenity&#39; = &#39;bar&#39;](44.943, 7.504, 45.174, 7.887) -&gt; .nodes;
      way[&#39;amenity&#39; = &#39;bar&#39;](44.943, 7.504, 45.174, 7.887) -&gt; .ways;
      node(w) -&gt; .nodesMembersWays;
    );
    (
    .nodes;
    .nodesMembersWays;
    .ways;
    );
    out;</code></pre>
<p>Or, if there is a method to directly download the ways with the coordinates of their member nodes, that would be the top.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Mar '17, 10:50</strong></p>
<img src="https://secure.gravatar.com/avatar/3561366bd49459f5b003a79c5dbee78c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CillaLu&#39;s gravatar image" />
<p><span>CillaLu</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CillaLu has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Mar '17, 11:41</strong> </span></p>
</div>
</div>
<div id="comments-container-55056" class="comments-container">
&#10;</div>
<div id="comment-tools-55056" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55056-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="55066"></span>

<div id="answer-container-55066" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55066-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55066-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-55066-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="CillaLu has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can do this by using more than one print statement and <code>geom</code> output for the ways:</p>
<pre><code>node[&#39;amenity&#39; = &#39;bar&#39;](44.943, 7.504, 45.174, 7.887);
out;
way[&#39;amenity&#39; = &#39;bar&#39;](44.943, 7.504, 45.174, 7.887);
out geom;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Mar '17, 17:27</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-55066" class="comments-container">
<span id="55176"></span>
<div id="comment-55176" class="comment">
<div id="post-55176-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you so much, this is exactly what i was looking for.</p>
</div>
<div id="comment-55176-info" class="comment-info">
<span class="comment-age">(18 Mar '17, 15:28)</span> <span class="comment-user userinfo">CillaLu</span>
</div>
</div>
</div>
<div id="comment-tools-55066" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55066-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55058"></span>

<div id="answer-container-55058" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55058-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55058-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55058-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the Wizard of <a href="http://overpass-turbo.eu/">Overpass-turbo</a> try inserting <strong>amenity=bar &amp; (type:way | type:node)</strong></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Mar '17, 12:29</strong></p>
<img src="https://secure.gravatar.com/avatar/6edf3a421a450237beae62ba93582637?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hjart&#39;s gravatar image" />
<p><span>Hjart</span><br />
<span class="score" title="2961 reputation points"><span>3.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hjart has 14 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-55058" class="comments-container">
&#10;</div>
<div id="comment-tools-55058" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55058-form-container" class="comment-form-container">
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

