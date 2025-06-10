+++
type = "question"
title = "Custom Tile Server Zoom Levels"
description = '''I created an Android Mobile Application which uses OSMDroid Mapview. It loads perfectly fine from zoom levels 18 and larger. However it only rescales and never serves me tiles from 19 and below. I have my own tile server using Mapnik, Renderd, Mod_tile so on and so forth. I&#x27;ve set my application to ...'''
date = "2016-01-21T06:17:00Z"
lastmod = "2016-01-21T08:04:00Z"
weight = 47612
keywords = [ "zoomlevel", "android", "osm", "tileserver" ]
aliases = [ "/questions/47612" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Custom Tile Server Zoom Levels](/questions/47612/custom-tile-server-zoom-levels)

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
<span id="post-47612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47612-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I created an Android Mobile Application which uses OSMDroid Mapview. It loads perfectly fine from zoom levels 18 and larger. However it only rescales and never serves me tiles from 19 and below.</p>
<p>I have my own tile server using Mapnik, Renderd, Mod_tile so on and so forth. I've set my application to use my own tile server too. Using/Checking with .../osm_tiles/{zoom}/{x}/{y} I know it goes down to level 20, as I've set because it returns an image, no error nor 404. It simply doesn't serve it to my mobile device.</p>
<p>I've checked the console logs and if needed, it downloads the tiles. But once it reaches zoom level 19, it stops and rescales instead. Is there some sort of.... Other settings I need to put?</p>
<pre><code>mv.setUseDataConnection(true);
mv.setMinZoomLevel(16);
mv.setMaxZoomLevel(20);
mv.getController().setZoom(17);
mv.setMultiTouchControls(true);
&#10;ITileSource tileSource;
tileSource = new XYTileSource(&quot;custom&quot;, ResourceProxy.string.mapnik, 16, 20, 256, &quot;.png&quot;, custom);
TileSourceFactory.addTileSource(tileSource);</code></pre>
<p>By the way, the last variable "custom" is actually declare like so:</p>
<pre><code>String custom[] = {&quot;http://mytileserver/osm_tiles/&quot;};</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jan '16, 06:17</strong></p>
<img src="https://secure.gravatar.com/avatar/0855423e70fc0fd35f26e9eeecf99e77?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Damian&#39;s gravatar image" />
<p><span>Damian</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Damian has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jan '16, 06:31</strong> </span></p>
</div>
</div>
<div id="comments-container-47612" class="comments-container">
&#10;</div>
<div id="comment-tools-47612" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47612-form-container" class="comment-form-container">
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

<span id="47613"></span>

<div id="answer-container-47613" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47613-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47613-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-47613-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I found the answer, it seems I had forgotten to add the line</p>
<pre><code>mv.setTileSource(TileSourceFactory.getTileSource(&quot;private&quot;));</code></pre>
<p>After creating and adding the source I need to also set it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jan '16, 08:04</strong></p>
<img src="https://secure.gravatar.com/avatar/0855423e70fc0fd35f26e9eeecf99e77?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Damian&#39;s gravatar image" />
<p><span>Damian</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Damian has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47613" class="comments-container">
&#10;</div>
<div id="comment-tools-47613" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47613-form-container" class="comment-form-container">
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

