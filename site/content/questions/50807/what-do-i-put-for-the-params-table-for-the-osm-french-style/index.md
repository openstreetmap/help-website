+++
type = "question"
title = "What do I put for the params table for the OSM French style?"
description = '''I am trying to set up the French OSM style, based on the source code is on cquest&#x27;s github osmfr-carto. I have imported a small country OSM extract with --hstore. Lots of SQL queries in this project depend on a SQL table called params, but it is not included, or created anywhere, and it is not docum...'''
date = "2016-07-11T10:54:00Z"
lastmod = "2016-07-11T11:21:00Z"
weight = 50807
keywords = [ "rendering", "style", "french-osm-style", "stylesheet", "france" ]
aliases = [ "/questions/50807" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What do I put for the params table for the OSM French style?](/questions/50807/what-do-i-put-for-the-params-table-for-the-osm-french-style)

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
<span id="post-50807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50807-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to set up the <a href="https://wiki.openstreetmap.org/wiki/FR:Servers/tile.openstreetmap.fr">French OSM style</a>, based on the source code is on <a href="https://github.com/cquest/osmfr-cartocss">cquest's github osmfr-carto</a>. I have imported a small country OSM extract with <code>--hstore</code>.</p>
<p>Lots of SQL queries in this project depend on a SQL table called <code>params</code>, but it is not included, or created anywhere, and it is not documented.</p>
<p>Does anyone know what this table structure should be like, and what values should be in it? The queries look for several values <code>buffer</code>, <code>x_bleed</code> and <code>y_bleed</code>.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-french-osm-style" rel="tag" title="see questions tagged &#39;french-osm-style&#39;">french-osm-style</span> <span class="post-tag tag-link-stylesheet" rel="tag" title="see questions tagged &#39;stylesheet&#39;">stylesheet</span> <span class="post-tag tag-link-france" rel="tag" title="see questions tagged &#39;france&#39;">france</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jul '16, 10:54</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-50807" class="comments-container">
&#10;</div>
<div id="comment-tools-50807" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50807-form-container" class="comment-form-container">
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

<span id="50809"></span>

<div id="answer-container-50809" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50809-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50809-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50809-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rorym has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>These 2 parameters are used to set the rendering buffer around the metatiles and the "bleed" parameter if you're using mapnik with the "bleed" patch.</p>
<p>This patch tells mapnik/renderd to generate rasters that a a bit larger than your metatile. It avoids many broken text on the edges.</p>
<p>With an unpatched mapnik/renderd:</p>
<ul>
<li>buffer = 128</li>
<li>x_bleed = 0</li>
<li>y_bleed= 0</li>
</ul>
<p>with the bleed patch, I'm using:</p>
<ul>
<li>buffer=256</li>
<li>x_bleed=256</li>
<li>y_bleed=256</li>
</ul>
<p>This is like rendering a 10x10 metatile, but keeping the 8x8 at the center.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jul '16, 11:21</strong></p>
<img src="https://secure.gravatar.com/avatar/53496360a70e1dc9e05f4f0ffb2c13c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cquest&#39;s gravatar image" />
<p><span>cquest</span><br />
<span class="score" title="691 reputation points">691</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cquest has 5 accepted answers">33%</span></p>
</div>
</div>
<div id="comments-container-50809" class="comments-container">
&#10;</div>
<div id="comment-tools-50809" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50809-form-container" class="comment-form-container">
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

