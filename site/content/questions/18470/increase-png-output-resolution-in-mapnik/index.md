+++
type = "question"
title = "Increase PNG output resolution in Mapnik"
description = '''We would like to print maps using Mapnik. The SVG export seems not to be perfect, but PNG is nice - the only problem is the low resulution. Is there an &quot;easy&quot; way to export in a around 300dpi instead of screen resolution? Basically in the OSM Mapnik stylesheet all values are pixels. Using the scale ...'''
date = "2012-12-15T16:04:00Z"
lastmod = "2014-11-20T19:37:00Z"
weight = 18470
keywords = [ "print", "tilemill", "mapnik" ]
aliases = [ "/questions/18470" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Increase PNG output resolution in Mapnik](/questions/18470/increase-png-output-resolution-in-mapnik)

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
<span id="post-18470-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18470-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-18470-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We would like to print maps using Mapnik.</p>
<p>The SVG export seems not to be perfect, but PNG is nice - the only problem is the low resulution.</p>
<p>Is there an "easy" way to export in a around 300dpi instead of screen resolution?</p>
<p>Basically in the OSM Mapnik stylesheet all values are pixels. Using the scale parameter in the TileMill project file, caused strange results.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-print" rel="tag" title="see questions tagged &#39;print&#39;">print</span> <span class="post-tag tag-link-tilemill" rel="tag" title="see questions tagged &#39;tilemill&#39;">tilemill</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Dec '12, 16:04</strong></p>
<img src="https://secure.gravatar.com/avatar/9ac1de0d402dfdf47bd4c4d664156c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AddisMap_Alexander&#39;s gravatar image" />
<p><span>AddisMap_Ale...</span><br />
<span class="score" title="1120 reputation points"><span>1.1k</span></span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AddisMap_Alexander has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18470" class="comments-container">
<span id="18493"></span>
<div id="comment-18493" class="comment">
<div id="post-18493-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Interesting feature requests in tile mill: <a href="https://github.com/mapnik/mapnik/issues/1582">https://github.com/mapnik/mapnik/issues/1582</a> <a href="https://github.com/mapbox/tilemill/issues/1819">https://github.com/mapbox/tilemill/issues/1819</a></p>
</div>
<div id="comment-18493-info" class="comment-info">
<span class="comment-age">(16 Dec '12, 14:05)</span> <span class="comment-user userinfo">AddisMap_Ale...</span>
</div>
</div>
</div>
<div id="comment-tools-18470" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18470-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="18471"></span>

<div id="answer-container-18471" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18471-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18471-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-18471-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AddisMap_Alexander has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This may be no complete answer - but hopefully still good help: You could <a href="https://startpage.com/do/search?q=tiles+retina">search the web for tiles retina</a> - it is quite a similar (same) problem for high-resolution displays (popular through Apple's high-resolution displays, named "retina"). <a href="http://openstreetmap.at/content/hires">http://openstreetmap.at/content/hires</a> is a good example of high-res <span>tiles</span>. A <a href="https://startpage.com/do/search?q=high-res+tiles+openstreetmap">search for high-res tiles openstreetmap</a> is also promising. ;-)</p>
<p>Also see <span>our wiki entry on printing</span>. If you want to print OSM for personal use - did you try the pdf version of the export tab on our main map page?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Dec '12, 17:00</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Nov '14, 13:32</strong> </span></p>
</div>
</div>
<div id="comments-container-18471" class="comments-container">
&#10;</div>
<div id="comment-tools-18471" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18471-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="18475"></span>

<div id="answer-container-18475" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18475-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18475-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-18475-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Explain "strange results" - I use the --scale-factor parameter on nik2img and I believe that should do the same as TileMill's scale parameter. Of course you have to adjust the output size accordingly; if you specify --scale-factor 4 and want the same detail then you need to quadruple your width and height as well.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Dec '12, 19:02</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-18475" class="comments-container">
<span id="18492"></span>
<div id="comment-18492" class="comment">
<div id="post-18492-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Actually it looks like this strange results only happen in the tile view in TileMill. When I export it is actually all fine, as long as I zoom in more according to the current scale.</p>
</div>
<div id="comment-18492-info" class="comment-info">
<span class="comment-age">(16 Dec '12, 14:04)</span> <span class="comment-user userinfo">AddisMap_Ale...</span>
</div>
</div>
</div>
<div id="comment-tools-18475" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18475-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="38689"></span>

<div id="answer-container-38689" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38689-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38689-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-38689-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Recently found: <a href="https://wiki.openstreetmap.org/wiki/Nik4">Nik4</a> ... there you can choose ppi or dpi value, I think.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Nov '14, 19:37</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-38689" class="comments-container">
&#10;</div>
<div id="comment-tools-38689" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38689-form-container" class="comment-form-container">
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

