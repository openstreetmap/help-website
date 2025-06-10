+++
type = "question"
title = "RuntimeError: Could not load map file: File does not exist of &#x27;/root/svn.openstreetmap.org/applications/rendering/mapnik/osm-local.xml&#x27;"
description = '''Hi, I am trying to Building Tiles with PostGIS OpenStreetMap data and Mapnik. I followed http://www.bostongis.com/PrinterFriendly.aspx?content_name=generating_osm_tiles As I want to generate for Boston, I have created generate_tiles_boston.py  So when I run generate_tiles_boston.py script, I faced f...'''
date = "2014-06-27T07:32:00Z"
lastmod = "2014-06-27T08:05:00Z"
weight = 34358
keywords = [ "osm.xml", "mapnik", "postgis", "generate_tiles" ]
aliases = [ "/questions/34358" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [RuntimeError: Could not load map file: File does not exist of '/root/svn.openstreetmap.org/applications/rendering/mapnik/osm-local.xml'](/questions/34358/runtimeerror-could-not-load-map-file-file-does-not-exist-of-rootsvnopenstreetmaporgapplicationsrenderingmapnikosm-localxml)

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
<span id="post-34358-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34358-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-34358-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am trying to Building Tiles with PostGIS OpenStreetMap data and Mapnik. I followed <a href="http://www.bostongis.com/PrinterFriendly.aspx?content_name=generating_osm_tiles">http://www.bostongis.com/PrinterFriendly.aspx?content_name=generating_osm_tiles</a></p>
<p>As I want to generate for Boston, I have created generate_tiles_boston.py</p>
<p>So when I run generate_tiles_boston.py script, I faced following error :</p>
<p>/usr/lib/pymodules/python2.7/mapnik2/<strong>init</strong>.py:27: DeprecationWarning: mapnik2 module has been deprecated,</p>
<pre><code>    please use &#39;import mapnik&#39;</code></pre>
<p>warnings.warn(msg, DeprecationWarning)</p>
<p>render_tiles( (-71.2, 42.23, -70.99, 42.4) /root/svn.openstreetmap.org/applications/rendering/mapnik/osm-local.xml /root/osm/tiles/ 10 17 Boston )</p>
<p>Traceback (most recent call last):</p>
<p>File "./generate_tiles_boston.py", line 215, in &lt;module&gt; render_tiles(bbox, mapfile, tile_dir, 10, 17, "Boston")</p>
<p>File "./generate_tiles_boston.py", line 136, in render_tiles renderer = RenderThread(tile_dir, mapfile, queue, printLock, maxZoom)</p>
<p>File "./generate_tiles_boston.py", line 64, in <strong>init</strong> mapnik.load_map(self.m, mapfile, True)</p>
<p>RuntimeError: Could not load map file: File does not exist of '/root/svn.openstreetmap.org/applications/rendering/mapnik/osm-local.xml'</p>
<p>Any help would be kindly appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm.xml" rel="tag" title="see questions tagged &#39;osm.xml&#39;">osm.xml</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-generate_tiles" rel="tag" title="see questions tagged &#39;generate_tiles&#39;">generate_tiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jun '14, 07:32</strong></p>
<img src="https://secure.gravatar.com/avatar/85b567607c96cea9abbd26df93220a3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="unnatip&#39;s gravatar image" />
<p><span>unnatip</span><br />
<span class="score" title="61 reputation points">61</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="unnatip has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jun '14, 08:01</strong> </span></p>
</div>
</div>
<div id="comments-container-34358" class="comments-container">
&#10;</div>
<div id="comment-tools-34358" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34358-form-container" class="comment-form-container">
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

<span id="34359"></span>

<div id="answer-container-34359" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34359-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34359-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-34359-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>change path of osm.xml file in generate_tiles_boston.py Default path given in generate_tiles_boston.py is '/root/svn.openstreetmap.org/applications/rendering/mapnik/osm-local.xml' Hence it search xml file in this path. Instead of that use path to where your osm.xml file is locateed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jun '14, 08:05</strong></p>
<img src="https://secure.gravatar.com/avatar/85b567607c96cea9abbd26df93220a3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="unnatip&#39;s gravatar image" />
<p><span>unnatip</span><br />
<span class="score" title="61 reputation points">61</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="unnatip has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-34359" class="comments-container">
&#10;</div>
<div id="comment-tools-34359" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34359-form-container" class="comment-form-container">
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

