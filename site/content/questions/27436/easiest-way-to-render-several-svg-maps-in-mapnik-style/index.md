+++
type = "question"
title = "easiest way to render several SVG maps in mapnik style"
description = '''I want to render some SVG maps in original Mapnik style (as seen on the osm.org website). I know already  there are extracts from the whole planet which are much smaller in download size there is something called TileMill to render map images with a GUI – output could be PDF, but are these PDF docum...'''
date = "2013-10-23T12:46:00Z"
lastmod = "2013-10-23T18:48:00Z"
weight = 27436
keywords = [ "rendering", "mapnik", "svg" ]
aliases = [ "/questions/27436" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [easiest way to render several SVG maps in mapnik style](/questions/27436/easiest-way-to-render-several-svg-maps-in-mapnik-style)

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
<span id="post-27436-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27436-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-27436-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to render some <strong>SVG maps</strong> in <strong>original Mapnik style</strong> (as seen on the osm.org website).</p>
<p>I know already</p>
<ul>
<li>there are <a href="http://wiki.openstreetmap.org/wiki/Extract">extracts</a> from the whole planet which are much smaller in download size</li>
<li>there is something called <a href="http://wiki.openstreetmap.org/wiki/Tilemill">TileMill</a> to render map images with a GUI – output could be PDF, but are these PDF documents vector images?</li>
<li><p>several instruction pages which — I assume — wont lead to the same result, as they consist of quite different instructions. Namely there are:</p></li>
<li><p><a href="http://wiki.openstreetmap.org/wiki/Mapnik">http://wiki.openstreetmap.org/wiki/Mapnik</a></p></li>
<li><a href="http://wiki.openstreetmap.org/wiki/Mapnik/Installation">http://wiki.openstreetmap.org/wiki/Mapnik/Installation</a></li>
<li><a href="https://github.com/mapnik/mapnik/wiki/Mapnik-Installation">https://github.com/mapnik/mapnik/wiki/Mapnik-Installation</a></li>
<li><a href="http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/</a></li>
</ul>
<p><a href="http://help.openstreetmap.org/questions/24833/rendering-a-map-with-mapnik-and-postgis/24849">This answer</a> from Andy Allen suggests to use <a href="https://github.com/springmeyer/nik2img">Nik2img.py</a> (where another confusion arises, as there is that just mentioned Nik2img source at Github and another one at <a href="http://code.google.com/p/mapnik-utils/wiki/Nik2Img">Google-Code</a> – both the same?)</p>
<ol>
<li>Can Nik2Img create SVG or any other vector files?</li>
<li>Do I need a database (e.g. PostGIS) or can I render directly from a given osm extract file?</li>
<li>I have read, that some instructions are outdated, because <a href="http://wiki.openstreetmap.org/wiki/Carto">Carto is used in the rendering process</a> of the Mapnik map tiles of OSM.org since August 2013. Where can I find latest instructions on how to install a Mapnik rendering instance?</li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-svg" rel="tag" title="see questions tagged &#39;svg&#39;">svg</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Oct '13, 12:46</strong></p>
<img src="https://secure.gravatar.com/avatar/793c9f0cfb9f3cc6001d73f127644c67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erik&#39;s gravatar image" />
<p><span>erik</span><br />
<span class="score" title="558 reputation points">558</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erik has one accepted answer">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Oct '13, 19:44</strong> </span></p>
</div>
</div>
<div id="comments-container-27436" class="comments-container">
&#10;</div>
<div id="comment-tools-27436" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27436-form-container" class="comment-form-container">
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

<span id="27437"></span>

<div id="answer-container-27437" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27437-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27437-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-27437-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="erik has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li><p>nik2img can create SVG images, however do not assume that you could meaningfully edit them in Inkscape or even Illustrator. The SVG, coming out of the Cairo library, is relatively convoluted and hardly editable at all.</p></li>
<li><p>You need an osm2pgsql-imported database if you want to use the standard OSM style. Mapnik is capable of processing .osm files directly but in that case the syntax for styling is vastly different, and no ready-made style exists that takes you from .osm via Mapnik to a map that looks like standard OSM.</p></li>
<li><p>You can ignore everything you read about Carto and simply get the latest OSM Mapnik style from here <a href="http://svn.openstreetmap.org/applications/rendering/mapnik/">http://svn.openstreetmap.org/applications/rendering/mapnik/</a> - this will then be a few months old but you probably won't notice a difference.</p></li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Oct '13, 12:52</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-27437" class="comments-container">
&#10;</div>
<div id="comment-tools-27437" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27437-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="27452"></span>

<div id="answer-container-27452" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27452-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27452-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-27452-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If I remember correctly, <a href="http://wiki.openstreetmap.org/wiki/Maperitive">Maperitive</a> can produce vector graphic output, and it has a map style available that comes close to mapnik.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Oct '13, 18:48</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-27452" class="comments-container">
&#10;</div>
<div id="comment-tools-27452" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27452-form-container" class="comment-form-container">
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

