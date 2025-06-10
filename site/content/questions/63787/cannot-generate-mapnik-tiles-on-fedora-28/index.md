+++
type = "question"
title = "Cannot generate mapnik tiles on Fedora 28"
description = '''I have followed all the steps mentioned in https://wiki.openstreetmap.org/wiki/Mapnik/Installation_on_Fedora_18 install a tile server on my Fedora 28 workstation. Although the tutorial is a bit old, almost all steps are applicable and I have gone through them with ease. However, in the last step, wh...'''
date = "2018-05-28T11:59:00Z"
lastmod = "2018-05-28T20:01:00Z"
weight = 63787
keywords = [ "tile-server", "fedora", "mapnik" ]
aliases = [ "/questions/63787" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot generate mapnik tiles on Fedora 28](/questions/63787/cannot-generate-mapnik-tiles-on-fedora-28)

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
<span id="post-63787-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63787-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63787-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have followed all the steps mentioned in <a href="https://wiki.openstreetmap.org/wiki/Mapnik/Installation_on_Fedora_18">https://wiki.openstreetmap.org/wiki/Mapnik/Installation_on_Fedora_18</a> install a tile server on my Fedora 28 workstation. Although the tutorial is a bit old, almost all steps are applicable and I have gone through them with ease. However, in the last step, when I am going to test Mapnik to see if it works (by running generate_tiles.py), I get the following error:</p>
<pre><code>[postgres@localhost mapnik]$ ./z0_generate_tiles.py /usr/lib64/python2.7/site-packages/mapnik2/init.py:27: DeprecationWarning: mapnik2 module has been deprecated, please use &#39;import mapnik&#39; warnings.warn(msg, DeprecationWarning) render_tiles( (-180.0, -90.0, 180.0, 90.0) /var/lib/pgsql/mapnik/osm.xml /var/lib/pgsql/mapnik/tiles/ 0 0 World ) Traceback (most recent call last): File &quot;./z0_generate_tiles.py&quot;, line 215, in render_tiles(bbox, mapfile, tile_dir, 0, 0, &quot;World&quot;) File &quot;./z0_generate_tiles.py&quot;, line 136, in render_tiles renderer = RenderThread(tile_dir, mapfile, queue, printLock, maxZoom) File &quot;./z0_generate_tiles.py&quot;, line 64, in init mapnik.load_map(self.m, mapfile, True) RuntimeError: XML document not well formed: Entity &#39;prefix&#39; not defined at line 4064 of &#39;/var/lib/pgsql/mapnik/osm.xml&#39;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tile-server" rel="tag" title="see questions tagged &#39;tile-server&#39;">tile-server</span> <span class="post-tag tag-link-fedora" rel="tag" title="see questions tagged &#39;fedora&#39;">fedora</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 May '18, 11:59</strong></p>
<img src="https://secure.gravatar.com/avatar/d49b3ab1b3f2f4ddfc069a6da590b9b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="powergame&#39;s gravatar image" />
<p><span>powergame</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="powergame has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63787" class="comments-container">
<span id="63790"></span>
<div id="comment-63790" class="comment">
<div id="post-63790-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What version of Mapnik are you running and what osm.xml are you using?</p>
<p>If a recent osm.xml from OSM Carto, it probably won't work with old versions of Mapnik. How did you obtain or create it?</p>
</div>
<div id="comment-63790-info" class="comment-info">
<span class="comment-age">(28 May '18, 12:35)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63792"></span>
<div id="comment-63792" class="comment">
<div id="post-63792-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse"></a><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> running mapnik-config --version gives me 2.3.0-pre. Regarding osm.xml, I guess I am using the one I checked out from <a href="http://svn.openstreetmap.org/applications/rendering/mapnik.">http://svn.openstreetmap.org/applications/rendering/mapnik.</a> By the way, I don't understand why the guide mentioned in the question installs mapnik from Fedora repos but checks out its svn repo and works with it. Do you think I need to remove installed mapnik packages and build it from source?</p>
</div>
<div id="comment-63792-info" class="comment-info">
<span class="comment-age">(28 May '18, 13:25)</span> <span class="comment-user userinfo">powergame</span>
</div>
</div>
<span id="63795"></span>
<div id="comment-63795" class="comment">
<div id="post-63795-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>To be honest, if you actually want to get something working I wouldn't start from Fedora. Everything's nicely packaged up for Ubuntu; either of the two latest LTS releases will work just fine. See <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/manually-building-a-tile-server-18-04-lts/</a> .</p>
<p>As for the XML file you're using, that apparently dates from "26 October 2013". I'd be surprised if that's what you really want.</p>
</div>
<div id="comment-63795-info" class="comment-info">
<span class="comment-age">(28 May '18, 14:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63816"></span>
<div id="comment-63816" class="comment">
<div id="post-63816-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> the problem is that we have a Centos server for our website and we want to use the same server as map tile server for our app users. After some failures with CentOS, I felt maybe I could use another OS of the family i.e. Fedora, because it's rather easy to move our site to Fedora (tested).</p>
</div>
<div id="comment-63816-info" class="comment-info">
<span class="comment-age">(28 May '18, 18:42)</span> <span class="comment-user userinfo">powergame</span>
</div>
</div>
<span id="63817"></span>
<div id="comment-63817" class="comment">
<div id="post-63817-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> what is osm.xml used for anyways? I checked out the latest version I guess, but you said it is for around 2013, why?</p>
</div>
<div id="comment-63817-info" class="comment-info">
<span class="comment-age">(28 May '18, 18:44)</span> <span class="comment-user userinfo">powergame</span>
</div>
</div>
<span id="63819"></span>
<div id="comment-63819" class="comment not_top_scorer">
<div id="post-63819-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>osm.xml is the file that tells mapnik how to render things.</p>
<p>The one in subversion from 2013 is just an old file. Everything is in git now. Usually osm.xml is generated from a mote manageable series of source files. See the switch2osm guides and the "osm carto" project in github.</p>
</div>
<div id="comment-63819-info" class="comment-info">
<span class="comment-age">(28 May '18, 20:01)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-63787" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-63787-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

