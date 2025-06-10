+++
type = "question"
title = "Mapnik rendering giving odd results as tiles but not as single file"
description = '''I&#x27;m trying to render some data in a .osm file, mainly for debugging purposes at this stage, but it will become a proper overlay. I&#x27;m using this generate_image.py script and defining a simple XML stylesheet, which results in this .png file (screenshotted as follows), which all looks correct (and the ...'''
date = "2016-05-10T19:48:00Z"
lastmod = "2016-05-11T11:05:00Z"
weight = 49650
keywords = [ "rendering", "projection", "mapnik" ]
aliases = [ "/questions/49650" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mapnik rendering giving odd results as tiles but not as single file](/questions/49650/mapnik-rendering-giving-odd-results-as-tiles-but-not-as-single-file)

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
<span id="post-49650-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49650-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-49650-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to render some data in a .osm file, mainly for debugging purposes at this stage, but it will become a proper overlay.</p>
<p>I'm using this <a href="https://github.com/openstreetmap/mapnik-stylesheets/blob/master/generate_image.py"><code>generate_image.py</code> script</a> and defining a simple XML stylesheet, which results in this .png file (screenshotted as follows), which all looks correct (and the .osm file is routable in OSRM too) :</p>
<p><img src="/upfiles/Screen_Shot_2016-05-10_at_19.39.08.png" alt="alt text" /></p>
<p>However, if I use this <a href="http://svn.openstreetmap.org/applications/rendering/mapnik/generate_tiles.py"><code>generate_tiles.py script</code></a> to generate a tile tree (instead of the single .png file as above), only fragments of the ways are shown, in an inconsistent and fragmented form, shown here zoomed into level 12 or so:</p>
<p><img src="/upfiles/Screen_Shot_2016-05-10_at_19.46.28.png" alt="alt text" /></p>
<p>The OSRM routing when zoomed in at this level does follow those line fragments exactly, but obviously goes further than the extent of each fragment.</p>
<p>It's not a browser caching issue - creating a fresh tileset, and creating an incognito instance (which bypasses the cache) gives the same. When I zoom in, different fragments of the ways are shown.</p>
<p>Is this likely to be a projection issue? As far as I can see, it's all set to Google Mercator.</p>
<p>Any other ideas what might be causing this problem? I've been fiddling with this for a day or two now and stuck!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-projection" rel="tag" title="see questions tagged &#39;projection&#39;">projection</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 May '16, 19:48</strong></p>
<img src="https://secure.gravatar.com/avatar/354d4e3cc1b448abb29eb4f1bbac395c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fooquency&#39;s gravatar image" />
<p><span>fooquency</span><br />
<span class="score" title="76 reputation points">76</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fooquency has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 May '16, 22:29</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</img>
</div>
</div>
<div id="comments-container-49650" class="comments-container">
&#10;</div>
<div id="comment-tools-49650" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49650-form-container" class="comment-form-container">
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

<span id="49675"></span>

<div id="answer-container-49675" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49675-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49675-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-49675-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In general I recommend avoiding the OSM input plugin - use osm2pgsql or convert the osm file to shapefiles first. The OSM input plugin is effectively unmaintained.</p>
<p>My only other suggestion would be to check the <code>clip</code> setting in your <code>LineSymbolizer</code> (or <code>line-clip</code> if you are using CartoCSS).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 May '16, 11:05</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-49675" class="comments-container">
&#10;</div>
<div id="comment-tools-49675" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49675-form-container" class="comment-form-container">
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

