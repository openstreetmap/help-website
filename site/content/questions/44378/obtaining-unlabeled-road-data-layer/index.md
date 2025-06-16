+++
type = "question"
title = "Obtaining unlabeled road data layer"
description = '''I&#x27;ve been downloading OSM unlabeled road image data through Mathematica and processing it so it only includes main roads.  For example, here&#x27;s an image of Sao Paulo at zoom 13, pre and post segmentation.    The results are ok, but I want to know how can I skip this segmentation effort.  Is there a w...'''
date = "2015-07-23T01:16:00Z"
lastmod = "2015-07-23T09:38:00Z"
weight = 44378
keywords = [ "roads" ]
aliases = [ "/questions/44378" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Obtaining unlabeled road data layer](/questions/44378/obtaining-unlabeled-road-data-layer)

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
<span id="post-44378-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44378-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44378-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been downloading OSM unlabeled road image data through Mathematica and processing it so it only includes main roads.</p>
<p>For example, here's an image of Sao Paulo at zoom 13, pre and post segmentation. <img src="/upfiles/SaoPaulo.png" alt="alt text" /> <img src="/upfiles/saoPaulo-MainAndSecondaryRoads-15Km.png" alt="alt text" /></p>
<p>The results are ok, but I want to know how can I skip this segmentation effort.</p>
<p>Is there a way to download only the road layer with Maperitive or other 3rd party application?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-roads" rel="tag" title="see questions tagged &#39;roads&#39;">roads</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jul '15, 01:16</strong></p>
<img src="https://secure.gravatar.com/avatar/c6697bd1a5287052d4c9dc193f2dbc7f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="antonio_rt&#39;s gravatar image" />
<p><span>antonio_rt</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="antonio_rt has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-44378" class="comments-container">
&#10;</div>
<div id="comment-tools-44378" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44378-form-container" class="comment-form-container">
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

<span id="44380"></span>

<div id="answer-container-44380" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44380-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44380-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-44380-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In short, yes. The better approach will vary based on what you are trying to do. Here's a quick Overpass Turbo query that extracts some of the major road vectors:</p>
<p><a href="http://overpass-turbo.eu/s/ayj">http://overpass-turbo.eu/s/ayj</a></p>
<p>Perhaps the vector representation there is better suited to what you are doing than a rendering.</p>
<p>(The Overpass api can return the data in a variety or formats, see <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL</a> for more)</p>
<p>If you want to render a small to medium sized area, using something like Maperative with a <a href="https://wiki.openstreetmap.org/wiki/Planet.osm">country or regional extract</a> would be a reasonable idea.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jul '15, 03:41</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</img>
</div>
</div>
<div id="comments-container-44380" class="comments-container">
<span id="44381"></span>
<div id="comment-44381" class="comment">
<div id="post-44381-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, that overpass query would be ok if it were without text labels and coloring. I want an output like the one shown in the binary mask</p>
</div>
<div id="comment-44381-info" class="comment-info">
<span class="comment-age">(23 Jul '15, 04:56)</span> <span class="comment-user userinfo">antonio_rt</span>
</div>
</div>
<span id="44386"></span>
<div id="comment-44386" class="comment">
<div id="post-44386-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The geojson from Overpass-Turbo can be processed anyway you like (or you can save GPX etc), e.g., with QGIS. Furthermore you can use MapCSS to style the data directly in Overpass-Turbo. It really depends what it is that you want to do.</p>
</div>
<div id="comment-44386-info" class="comment-info">
<span class="comment-age">(23 Jul '15, 09:38)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-44380" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44380-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44383"></span>

<div id="answer-container-44383" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44383-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44383-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-44383-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Options:</p>
<ol>
<li>Download OSM extract for region of interest. Import into osm2pgsql. Use Kosmtik or Tilemill (not Tilemill 2 aka Mapbox Studio) to develop a map style (in MapCSS) that shows only (main) highways. Render image, done.</li>
<li>Download OSM extract for region of interest. Use osmosis with the <code>--tag-filter</code> option, or use osmfilter, to extract just the highways from the file. Then load and render in Maperitive.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jul '15, 07:11</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-44383" class="comments-container">
&#10;</div>
<div id="comment-tools-44383" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44383-form-container" class="comment-form-container">
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

