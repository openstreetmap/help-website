+++
type = "question"
title = "Where is the layers/z7.tif file for the French OSM style?"
description = '''I am trying to set up the French OSM style, which is visible on tile.openstreetmap.fr. I think the source code is on cquest&#x27;s github osmfr-carto. And I am having some errors. I have imported a small country OSM extract with --hstore. I don&#x27;t have a layers/z7.tif raster file. The only thing I can fin...'''
date = "2016-07-11T10:20:00Z"
lastmod = "2016-07-11T11:06:00Z"
weight = 50806
keywords = [ "rendering", "style", "french-osm-style", "stylesheet", "france" ]
aliases = [ "/questions/50806" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Where is the layers/z7.tif file for the French OSM style?](/questions/50806/where-is-the-layersz7tif-file-for-the-french-osm-style)

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
<span id="post-50806-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50806-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50806-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to set up the <a href="https://wiki.openstreetmap.org/wiki/FR:Servers/tile.openstreetmap.fr">French OSM style</a>, which is visible on <a href="http://tile.openstreetmap.fr/">tile.openstreetmap.fr</a>. I think the source code is on <a href="https://github.com/cquest/osmfr-cartocss">cquest's github osmfr-carto</a>. And I am having some errors. I have imported a small country OSM extract with <code>--hstore</code>.</p>
<p>I don't have a <code>layers/z7.tif</code> <a href="https://github.com/cquest/osmfr-cartocss/blob/7c684071b06e150f57df05982c9efd5f9a55d561/project.mml#L78-95">raster file</a>. The only thing I can find is a <a href="https://lists.openstreetmap.org/pipermail/talk/2013-July/067409.html">2013 mailing list post from cquest about lowzoom tiles</a>. Does anyone know where to get this file? I have disabled it for now.</p>
<p>I have <a href="https://github.com/cquest/osmfr-cartocss/issues/15">opened a Github issue on the repo</a>.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-french-osm-style" rel="tag" title="see questions tagged &#39;french-osm-style&#39;">french-osm-style</span> <span class="post-tag tag-link-stylesheet" rel="tag" title="see questions tagged &#39;stylesheet&#39;">stylesheet</span> <span class="post-tag tag-link-france" rel="tag" title="see questions tagged &#39;france&#39;">france</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jul '16, 10:20</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jul '16, 10:41</strong> </span></p>
</div>
</div>
<div id="comments-container-50806" class="comments-container">
&#10;</div>
<div id="comment-tools-50806" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50806-form-container" class="comment-form-container">
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

<span id="50808"></span>

<div id="answer-container-50808" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50808-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50808-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50808-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rorym has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here it is: <a href="http://osm13.openstreetmap.fr/~cquest/z7.tif">http://osm13.openstreetmap.fr/~cquest/z7.tif</a></p>
<p>It's getting old... I need to refresh it !</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jul '16, 11:06</strong></p>
<img src="https://secure.gravatar.com/avatar/53496360a70e1dc9e05f4f0ffb2c13c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cquest&#39;s gravatar image" />
<p><span>cquest</span><br />
<span class="score" title="691 reputation points">691</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cquest has 5 accepted answers">33%</span></p>
</div>
</div>
<div id="comments-container-50808" class="comments-container">
&#10;</div>
<div id="comment-tools-50808" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50808-form-container" class="comment-form-container">
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

