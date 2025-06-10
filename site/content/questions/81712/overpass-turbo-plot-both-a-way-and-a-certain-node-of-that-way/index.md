+++
type = "question"
title = "Overpass Turbo: plot both a way and a certain node of that way"
description = '''Hi! I am wondering how I could get Overpass Turbo displaying a node and a way which this node is part of.  Here, an Overpass example. If I delete the line printing the way (line 3), I can see the node on the map. Otherwise, the map will only show the way.  Thanks for your hints!'''
date = "2021-09-10T13:38:00Z"
lastmod = "2021-09-17T14:46:00Z"
weight = 81712
keywords = [ "overpass", "overpass-turbo" ]
aliases = [ "/questions/81712" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass Turbo: plot both a way and a certain node of that way](/questions/81712/overpass-turbo-plot-both-a-way-and-a-certain-node-of-that-way)

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
<span id="post-81712-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81712-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81712-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi! I am wondering how I could get Overpass Turbo displaying a <strong>node</strong> and a <strong>way</strong> which this node is part of.</p>
<p>Here, an <a href="http://overpass-turbo.eu/s/1b3P">Overpass example</a>. If I delete the line printing the way (line 3), I can see the node on the map. Otherwise, the map will only show the way.</p>
<p><strong>Thanks</strong> for your hints!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Sep '21, 13:38</strong></p>
<img src="https://secure.gravatar.com/avatar/ffb12f7c2548687764b2de9e4562d2d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="G%C3%A5seborg&#39;s gravatar image" />
<p><span>Gåseborg</span><br />
<span class="score" title="311 reputation points">311</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gåseborg has 4 accepted answers">50%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jan '22, 16:44</strong> </span></p>
</div>
</div>
<div id="comments-container-81712" class="comments-container">
&#10;</div>
<div id="comment-tools-81712" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81712-form-container" class="comment-form-container">
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

<span id="81715"></span>

<div id="answer-container-81715" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81715-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I consider this to be a bug in Overpass Turbo &amp; appears related to this unsatisfactory explanation to a similar problem: <a href="https://github.com/tyrasd/overpass-turbo/issues/499#issuecomment-756927476">https://github.com/tyrasd/overpass-turbo/issues/499#issuecomment-756927476</a></p>
<p>If you run this routine with the next node id it displays fine. (use Zoom to Data button)</p>
<pre><code>way(35565161);
out geom;
node(416714408);
out geom;</code></pre>
<p>Note it's exactly the same data format as your routine.</p>
<p>;</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Sep '21, 16:31</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-81715" class="comments-container">
<span id="81794"></span>
<div id="comment-81794" class="comment">
<div id="post-81794-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/1532/davef">@DaveF</a>! For me, it does not work if I switch to other nodes belonging to the way. By the way, I guess you have a type in line 3: node 416714408 is in US while way 35565161 is in France ;)</p>
</div>
<div id="comment-81794-info" class="comment-info">
<span class="comment-age">(17 Sep '21, 14:40)</span> <span class="comment-user userinfo">Gåseborg</span>
</div>
</div>
<span id="81795"></span>
<div id="comment-81795" class="comment">
<div id="post-81795-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It's the next node, numerically. It was intentional to show that the routine works, but OSM-carto code interprets the two differently/incorrectly.</p>
</div>
<div id="comment-81795-info" class="comment-info">
<span class="comment-age">(17 Sep '21, 14:46)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-81715" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81715-form-container" class="comment-form-container">
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

