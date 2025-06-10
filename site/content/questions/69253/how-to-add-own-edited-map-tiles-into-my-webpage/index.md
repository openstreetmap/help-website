+++
type = "question"
title = "How to add own edited map tiles into my webpage"
description = '''Hello! I edited a map by drawing roads using JOSM and created the map tiles with Maperitive. Now, I have to add this map into my web site and allow navigation using the edited map. Where do I start and what are the applications I need to do this? Thank you in advance!'''
date = "2019-05-21T05:52:00Z"
lastmod = "2019-05-21T21:56:00Z"
weight = 69253
keywords = [ "openstreetmap", "website", "maperitive", "navigation", "tileserver" ]
aliases = [ "/questions/69253" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to add own edited map tiles into my webpage](/questions/69253/how-to-add-own-edited-map-tiles-into-my-webpage)

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
<span id="post-69253-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69253-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69253-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello!</p>
<p>I edited a map by drawing roads using JOSM and created the map tiles with Maperitive. Now, I have to add this map into my web site and allow navigation using the edited map.</p>
<p>Where do I start and what are the applications I need to do this?</p>
<p>Thank you in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-website" rel="tag" title="see questions tagged &#39;website&#39;">website</span> <span class="post-tag tag-link-maperitive" rel="tag" title="see questions tagged &#39;maperitive&#39;">maperitive</span> <span class="post-tag tag-link-navigation" rel="tag" title="see questions tagged &#39;navigation&#39;">navigation</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 May '19, 05:52</strong></p>
<img src="https://secure.gravatar.com/avatar/75bfa1e4f41ffdd694ed68100d668b1b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Feruses&#39;s gravatar image" />
<p><span>Feruses</span><br />
<span class="score" title="15 reputation points">15</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Feruses has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69253" class="comments-container">
<span id="69265"></span>
<div id="comment-69265" class="comment">
<div id="post-69265-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I just noticed that you mentioned "allow navigation" in your question. Did you mean turn-by-turn navigations for cars (or other vehicles) by that? I responded based on the assumption that you were just interested in an interactive online map. Can you clarify?</p>
</div>
<div id="comment-69265-info" class="comment-info">
<span class="comment-age">(21 May '19, 21:56)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-69253" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69253-form-container" class="comment-form-container">
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

<span id="69264"></span>

<div id="answer-container-69264" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69264-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69264-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-69264-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are conventions for <a href="https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames">slippy map tilenames</a>, specifically:</p>
<blockquote>
<ul>
<li>Tiles are 256 × 256 pixel PNG files</li>
<li>Each zoom level is a directory, each column is a subdirectory, and each tile in that column is a file</li>
<li>Filename (or url) format is /zoom/x/y.png</li>
</ul>
</blockquote>
<p>Do the tiles you created with Maperitive follow these? If yes, there are only two more things you need to do:</p>
<ol>
<li>Move all the tiles to a webserver. Verify that the server allows you to view the individual tiles in a web browser, and to embed them as images in your website.</li>
<li>Add a JavaScript library for maps, such as <a href="https://leafletjs.com/">Leaflet</a>, to the source code of your website. Have a look at the tutorials for using the library. There usually is some location in the code that calls the library where you can specify which URL the tiles come from. Point that URL to the webserver you set up in step 1. (With Leaflet, you probably want a <a href="https://leafletjs.com/reference-1.5.0.html#tilelayer">TileLayer</a>.)</li>
</ol>
<p>That's it, your map should work now!</p>
<hr />
<p>Notes:</p>
<ul>
<li>The above assumes that your website is essentially some HTML you wrote yourself. If you're using a CMS or a framework, there may be specific instructions for embedding maps into it. See <a href="https://wiki.openstreetmap.org/wiki/Deploying_your_own_Slippy_Map#Embedding_OSM_in_a_CMS.2Fframework">this</a> list, for example.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 May '19, 21:37</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-69264" class="comments-container">
&#10;</div>
<div id="comment-tools-69264" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69264-form-container" class="comment-form-container">
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

