+++
type = "question"
title = "osm2pgsql filtering tag"
description = '''We would like to (as an example) import all highway but excluding track and many others. In our filter.style we did this (partial) : ... node,way highway text linear ... node,way highway:track text delete  but track are still there. Where did we miss something ?'''
date = "2015-03-21T09:16:00Z"
lastmod = "2015-03-23T13:27:00Z"
weight = 41836
keywords = [ "filtering", "osm2pgsql", "tagging" ]
aliases = [ "/questions/41836" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql filtering tag](/questions/41836/osm2pgsql-filtering-tag)

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
<span id="post-41836-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41836-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41836-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We would like to (as an example) import all highway but excluding track and many others. In our filter.style we did this (partial) :</p>
<pre><code>...
node,way   highway      text         linear
...
node,way    highway:track           text    delete</code></pre>
<p>but track are still there. Where did we miss something ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filtering" rel="tag" title="see questions tagged &#39;filtering&#39;">filtering</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Mar '15, 09:16</strong></p>
<img src="https://secure.gravatar.com/avatar/186908df976ba9ca356029adea66c86a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maema&#39;s gravatar image" />
<p><span>maema</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maema has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-41836" class="comments-container">
<span id="41846"></span>
<div id="comment-41846" class="comment">
<div id="post-41846-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>So what are you trying with this filtering? To render only real roads or to import for routing?</p>
</div>
<div id="comment-41846-info" class="comment-info">
<span class="comment-age">(22 Mar '15, 13:34)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="41848"></span>
<div id="comment-41848" class="comment">
<div id="post-41848-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just rendering. Not routing.</p>
</div>
<div id="comment-41848-info" class="comment-info">
<span class="comment-age">(22 Mar '15, 16:49)</span> <span class="comment-user userinfo">maema</span>
</div>
</div>
<span id="41851"></span>
<div id="comment-41851" class="comment">
<div id="post-41851-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Any reason why you don't alter the mapnik style? (sry no clie about patching o2p style file :/)</p>
</div>
<div id="comment-41851-info" class="comment-info">
<span class="comment-age">(22 Mar '15, 21:43)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
</div>
<div id="comment-tools-41836" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41836-form-container" class="comment-form-container">
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

<span id="41856"></span>

<div id="answer-container-41856" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41856-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41856-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41856-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>We want to import Europe. In order to have a light database, we would like remove tons of things we dont need, like tree node, track, trafic_lights, crossing.... After we manage everything with QGIS.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Mar '15, 13:27</strong></p>
<img src="https://secure.gravatar.com/avatar/186908df976ba9ca356029adea66c86a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maema&#39;s gravatar image" />
<p><span>maema</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maema has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Mar '15, 13:28</strong> </span></p>
</div>
</div>
<div id="comments-container-41856" class="comments-container">
&#10;</div>
<div id="comment-tools-41856" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41856-form-container" class="comment-form-container">
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

