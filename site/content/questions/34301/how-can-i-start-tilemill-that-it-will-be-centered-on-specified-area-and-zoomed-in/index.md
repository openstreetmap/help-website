+++
type = "question"
title = "How can I start TileMill that it will be centered on specified area and zoomed in?"
description = '''I am loading and testing very small area. But currently started TileMill is not centering on area with data, it displays map of the entire world. As it generates tiles it takes some time to reach area that I wanted to see. Is there some way to provide parameters from program or edit some config file...'''
date = "2014-06-25T06:42:00Z"
lastmod = "2014-06-30T21:50:00Z"
weight = 34301
keywords = [ "tilemill" ]
aliases = [ "/questions/34301" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How can I start TileMill that it will be centered on specified area and zoomed in?](/questions/34301/how-can-i-start-tilemill-that-it-will-be-centered-on-specified-area-and-zoomed-in)

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
<span id="post-34301-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34301-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-34301-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am loading and testing very small area. But currently started TileMill is not centering on area with data, it displays map of the entire world. As it generates tiles it takes some time to reach area that I wanted to see.</p>
<p>Is there some way to provide parameters from program or edit some config file that I would not need to pan through entire world looking for this 5km x 5km area that is rendered?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tilemill" rel="tag" title="see questions tagged &#39;tilemill&#39;">tilemill</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jun '14, 06:42</strong></p>
<img src="https://secure.gravatar.com/avatar/fd2f7303e92334ed1eef75268aed7611?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bulwersator&#39;s gravatar image" />
<p><span>Bulwersator</span><br />
<span class="score" title="468 reputation points">468</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bulwersator has one accepted answer">14%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jun '14, 06:42</strong> </span></p>
</div>
</div>
<div id="comments-container-34301" class="comments-container">
&#10;</div>
<div id="comment-tools-34301" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34301-form-container" class="comment-form-container">
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

<span id="34302"></span>

<div id="answer-container-34302" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34302-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34302-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-34302-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Bulwersator has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's a "project.mml" file that controls your layers; it is a JSON file that has, usually right at the beginning, a section like</p>
<pre><code>&quot;center&quot;: [
  -77.036,
  38.9013,
  12
],</code></pre>
<p>change these values to the coordinates and zoom level you require, and you'll be fine.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jun '14, 07:02</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-34302" class="comments-container">
<span id="34303"></span>
<div id="comment-34303" class="comment">
<div id="post-34303-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Is it possible to override it? This file is tracked by repository so I would prefer to not modify it - see <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/project.mml">https://github.com/gravitystorm/openstreetmap-carto/blob/master/project.mml</a></p>
</div>
<div id="comment-34303-info" class="comment-info">
<span class="comment-age">(25 Jun '14, 07:34)</span> <span class="comment-user userinfo">Bulwersator</span>
</div>
</div>
<span id="34305"></span>
<div id="comment-34305" class="comment">
<div id="post-34305-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Not that I'm aware of, but I find it pretty annoying too. If I knew how to write the plugins for Tilemill I'd create a bookmarks plugin, since every time I start work on openstreetmap-carto I spend minutes trying to pan and zoom to where I want to work.</p>
</div>
<div id="comment-34305-info" class="comment-info">
<span class="comment-age">(25 Jun '14, 08:48)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
<span id="34464"></span>
<div id="comment-34464" class="comment">
<div id="post-34464-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My search failed to find relevant ticket so I reported it as <a href="https://github.com/mapbox/tilemill/issues/2358">https://github.com/mapbox/tilemill/issues/2358</a></p>
<p>Not that I expect implementation.</p>
</div>
<div id="comment-34464-info" class="comment-info">
<span class="comment-age">(30 Jun '14, 12:00)</span> <span class="comment-user userinfo">Bulwersator</span>
</div>
</div>
<span id="34466"></span>
<div id="comment-34466" class="comment">
<div id="post-34466-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>You could try to work around this by stashing your "private" coordinates with Git.</p>
<p>See: <a href="http://git-scm.com/book/en/Git-Tools-Stashing">Git - Stashing</a></p>
</div>
<div id="comment-34466-info" class="comment-info">
<span class="comment-age">(30 Jun '14, 12:18)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="34474"></span>
<div id="comment-34474" class="comment not_top_scorer">
<div id="post-34474-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I will also try exporting from command line - see <a href="https://www.mapbox.com/tilemill/docs/manual/exporting/">https://www.mapbox.com/tilemill/docs/manual/exporting/</a></p>
</div>
<div id="comment-34474-info" class="comment-info">
<span class="comment-age">(30 Jun '14, 16:25)</span> <span class="comment-user userinfo">Bulwersator</span>
</div>
</div>
<span id="34476"></span>
<div id="comment-34476" class="comment">
<div id="post-34476-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This is one of the reasons I wrote the (tiny, hackish) Sputnik, so that map views could be bookmarkable: <a href="https://github.com/systemed/sputnik">https://github.com/systemed/sputnik</a></p>
</div>
<div id="comment-34476-info" class="comment-info">
<span class="comment-age">(30 Jun '14, 21:50)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-34302" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-34302-form-container" class="comment-form-container">
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

