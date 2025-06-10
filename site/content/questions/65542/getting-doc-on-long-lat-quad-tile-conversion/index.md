+++
type = "question"
title = "Getting doc on long / lat &lt;-&gt; quad tile conversion"
description = '''I&#x27;d like to save coordinates of points and boundary boxes in my local db, as quadtiles. I am looking for more doc than provided in the link above: a precise guide with code / pseudo code on how to convert long / lat to Quadtile format, and back. Any pointer on this?'''
date = "2018-08-24T13:30:00Z"
lastmod = "2018-08-24T22:43:00Z"
weight = 65542
keywords = [ "quadtile", "coordinates" ]
aliases = [ "/questions/65542" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Getting doc on long / lat \<-\> quad tile conversion](/questions/65542/getting-doc-on-long-lat-quad-tile-conversion)

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
<span id="post-65542-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65542-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65542-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'd like to save coordinates of points and boundary boxes in my local db, as <a href="https://wiki.openstreetmap.org/wiki/QuadTiles">quadtiles</a>.</p>
<p>I am looking for more doc than provided in the link above: a precise guide with code / pseudo code on how to convert long / lat to Quadtile format, and back. Any pointer on this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-quadtile" rel="tag" title="see questions tagged &#39;quadtile&#39;">quadtile</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Aug '18, 13:30</strong></p>
<img src="https://secure.gravatar.com/avatar/e2045f892a60ac37133349e11bb4bba0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="seinecle&#39;s gravatar image" />
<p><span>seinecle</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="seinecle has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65542" class="comments-container">
&#10;</div>
<div id="comment-tools-65542" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65542-form-container" class="comment-form-container">
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

<span id="65543"></span>

<div id="answer-container-65543" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65543-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65543-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65543-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames">This Wiki article</a> discusses conversion between tile names and lat/lon, and also includes pseudocode and example code for various languages.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Aug '18, 16:54</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-65543" class="comments-container">
<span id="65544"></span>
<div id="comment-65544" class="comment">
<div id="post-65544-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... which is linked in the introduction of the wiki article which seincle linked. I just wanted to add it. ;-) <a href="https://help.openstreetmap.org/users/15574/seinecle">@seinecle</a>, did you want something different your just not seen the link?</p>
</div>
<div id="comment-65544-info" class="comment-info">
<span class="comment-age">(24 Aug '18, 20:59)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="65545"></span>
<div id="comment-65545" class="comment">
<div id="post-65545-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! I might be wrong but I thought the slippy tiles are not quad tiles? The logic of the naming conventions are completely different, if I read the page you linked to, and the link I provided?</p>
</div>
<div id="comment-65545-info" class="comment-info">
<span class="comment-age">(24 Aug '18, 22:14)</span> <span class="comment-user userinfo">seinecle</span>
</div>
</div>
<span id="65546"></span>
<div id="comment-65546" class="comment">
<div id="post-65546-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If I understand correctly, the quad system for naming tiles starts with the biggest tile (number from 0 to 3), then adds a 0-3 number for the subtile, et .. until the required level of zoom is achieved. That' the general idea. Now I'd need docs and a lib to play with it! It seems Bing map has the equivalent (search for "quadkey + Bing maps")</p>
</div>
<div id="comment-65546-info" class="comment-info">
<span class="comment-age">(24 Aug '18, 22:21)</span> <span class="comment-user userinfo">seinecle</span>
</div>
</div>
<span id="65548"></span>
<div id="comment-65548" class="comment">
<div id="post-65548-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/15574/seinecle">@seinecle</a> oh, umm, maybe <em>I</em> should have read better ("that's not really what this page is about"). So, you are right, if I understand correctly, slippy map tilenames are not what you are looking for. I have inserted a paragraph break into the wiki page's intro to make that clearer. Let's wait for other answers.</p>
</div>
<div id="comment-65548-info" class="comment-info">
<span class="comment-age">(24 Aug '18, 22:43)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-65543" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65543-form-container" class="comment-form-container">
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

