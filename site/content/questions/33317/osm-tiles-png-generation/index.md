+++
type = "question"
title = "OSM Tiles (png) generation"
description = '''I want to render tiles and I have a problem. I made postGIS db, succesfully run TileMill with OSMBright style. I read that I need now export mapnik xml from TileMill. I checked Mapnik as in python tutorial- everything works fine.  I&#x27;ve changed generate_tiles.py:   changed the .xml file to read  chan...'''
date = "2014-05-20T11:00:00Z"
lastmod = "2014-05-20T13:22:00Z"
weight = 33317
keywords = [ "tiles", "osm", "mapnik" ]
aliases = [ "/questions/33317" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM Tiles (png) generation](/questions/33317/osm-tiles-png-generation)

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
<span id="post-33317-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33317-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33317-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to render tiles and I have a problem.</p>
<p>I made postGIS db, succesfully run TileMill with OSMBright style. I read that I need now export mapnik xml from TileMill. I checked Mapnik as in python tutorial- everything works fine.</p>
<p>I've changed generate_tiles.py:</p>
<ul>
<li>changed the .xml file to read</li>
<li>changed the bbox (I have checked bbox of small area while exporting to PNG in TileMill)</li>
<li>changed the render line to <code>render_tiles(bbox, mapfile, tile_dir, 15, 16 , "mymap")</code></li>
</ul>
<p>but an error occures:</p>
<p><code>Failed to load fonts from: ./fonts in Map at line 3 of '/home/myacc/bin/mapnik/osm.xml/'</code></p>
<p>I think the .xml is not made properly (it has written path as reference to current path) but maybe I am wrong.</p>
<p>I have checked :</p>
<p><code>python -c "import mapnik;print mapnik.fontscollectionpath"</code></p>
<p>and changed the fontpath in osm.xml, but there is no such fonts registered by Mapnik . I printed out known fonts by:</p>
<p><code>python -c "from mapnik import FontEngine as e;print '\n'.join(e.instance().face_names())"</code></p>
<p>but there isn't a <code>font face 'Free Sans Semibold'</code></p>
<p>My questions:</p>
<ol>
<li>I am doing it wrong (generate xml from tilemill, put it into ~/bin/mapnik and changing generate_tiles.py)</li>
<li>Is there a better way to make this tiles</li>
<li>If not- what I should do to make this work (where are those fonts it cant find (I think there will be more errors with reading files) )</li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 May '14, 11:00</strong></p>
<img src="https://secure.gravatar.com/avatar/f3e2757cff84995712acc9ce092375b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="r2d2&#39;s gravatar image" />
<p><span>r2d2</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="r2d2 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33317" class="comments-container">
&#10;</div>
<div id="comment-tools-33317" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33317-form-container" class="comment-form-container">
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

<span id="33318"></span>

<div id="answer-container-33318" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33318-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33318-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33318-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<pre><code>I think the .xml is not made properly (it has written path as reference to current path) but maybe I am wrong.</code></pre>
<p>When exporting from TileMill, I've seen the same effect when moving to a different machine where paths are different. I got around it (with the "standard" OSM map style, not OSMBright) by editing paths where they varied to match the target machine. Using the "carto" utility to do the export rather than TileMill (as mentioned <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1404_tileserver">here</a>) may also fix the problem, but I've not tried that with OSMBright, and I've not tried that on a machine with TileMill also installed, so I can't guarantee there won't be node.js package mismatches between what TileMill needs and what carto does.</p>
<p>(someone please edit if that last sentence is me worrying unnecessarily).</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 May '14, 11:11</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-33318" class="comments-container">
<span id="33321"></span>
<div id="comment-33321" class="comment">
<div id="post-33321-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have used OSMBright becouse it creates project for TileMill- I dont have to add layers manually. Is there sth. like this for carto?</p>
</div>
<div id="comment-33321-info" class="comment-info">
<span class="comment-age">(20 May '14, 12:54)</span> <span class="comment-user userinfo">r2d2</span>
</div>
</div>
<span id="33323"></span>
<div id="comment-33323" class="comment">
<div id="post-33323-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The <a href="https://github.com/gravitystorm/openstreetmap-carto">OSM standard style</a> can be loaded into TileMill. It's quite big with lots of layers (you'll need to use an external editor to edit files as TileMill will run out of tabs) but it does load and export without problems.</p>
</div>
<div id="comment-33323-info" class="comment-info">
<span class="comment-age">(20 May '14, 13:17)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="33324"></span>
<div id="comment-33324" class="comment">
<div id="post-33324-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>could You tell me how to do this because I'am a bit confused- I use this style when osm2pgsql. And than what I should do? (how to add all the layers)</p>
<p>Ok, I've just pasted the files to my project pff this coses errors ;/ how can it be easily loaded??</p>
</div>
<div id="comment-33324-info" class="comment-info">
<span class="comment-age">(20 May '14, 13:22)</span> <span class="comment-user userinfo">r2d2</span>
</div>
</div>
</div>
<div id="comment-tools-33318" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33318-form-container" class="comment-form-container">
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

