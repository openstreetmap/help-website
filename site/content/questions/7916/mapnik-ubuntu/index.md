+++
type = "question"
title = "Mapnik, Ubuntu"
description = '''I am trying to install mapnik and generate tiles for a given country using this tutorial http://weait.com/content/build-your-own-openstreetmap-server But what a pity thing. Despite I have downloaded all boundary files and unpacked it , but a strange error is disturbing me to do it .  root@ks356390:/...'''
date = "2011-09-16T07:25:00Z"
lastmod = "2012-01-05T09:16:00Z"
weight = 7916
keywords = [ "tiles", "gis", "mapnik" ]
aliases = [ "/questions/7916" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Mapnik, Ubuntu](/questions/7916/mapnik-ubuntu)

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
<span id="post-7916-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7916-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7916-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to install mapnik and generate tiles for a given country using this tutorial</p>
<p><a href="http://weait.com/content/build-your-own-openstreetmap-server">http://weait.com/content/build-your-own-openstreetmap-server</a></p>
<p>But what a pity thing. Despite I have downloaded all boundary files and unpacked it , but a strange error is disturbing me to do it .</p>
<pre><code>root@ks356390:/home/bin/mapnik# sudo ./generate_image.py Traceback
(most recent call last):   File &quot;./generate_image.py&quot;, line 42, in
&lt;module&gt;
    mapnik.load_map(m,mapfile) RuntimeError:
/home/bin/mapnik/world_boundaries/10m_populated_places does not exist
(encountered during parsing of layer &#39;nepopulated&#39;)</code></pre>
<p>but see ...</p>
<pre><code>root@ks356390:/home/bin/mapnik# cd world_boundaries
Sie haben neue Post in /var/mail/root.
root@ks356390:/home/bin/mapnik/world_boundaries# ls
10m_populated_places                      places.shx
110m_admin_0_boundary_lines_land.dbf      processed_p.dbf
110m_admin_0_boundary_lines_land.prj      processed_p.index
110m_admin_0_boundary_lines_land.sbn      processed_p.shp
110m_admin_0_boundary_lines_land.sbx      processed_p.shx
110m_admin_0_boundary_lines_land.shp      shoreline_300.dbf
110m_admin_0_boundary_lines_land.shp.xml  shoreline_300.index
110m_admin_0_boundary_lines_land.shx      shoreline_300.shp
builtup_area.dbf                          shoreline_300.shx
builtup_area.index                        world_bnd_m.dbf
builtup_area.prj                          world_bnd_m.index
builtup_area.shp                          world_bnd_m.prj
builtup_area.shx                          world_bnd_m.shp
ne_10m_populated_places.dbf               world_bnd_m.shx
ne_10m_populated_places.prj               world_boundaries_m.dbf
ne_10m_populated_places.shp               world_boundaries_m.index
ne_10m_populated_places.shx               world_boundaries_m.prj
places.dbf                                world_boundaries_m.shp
places.prj                                world_boundaries_m.shx
places.shp root@ks356390:/home/bin/mapnik/world_boundaries#</code></pre>
<p>I tried to make generate_image with sudo also... Any idea why mapnik is making this in ubuntu??????? It seems it doesn't see 10M nepopulated , despite the folder and files exist</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-gis" rel="tag" title="see questions tagged &#39;gis&#39;">gis</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Sep '11, 07:25</strong></p>
<img src="https://secure.gravatar.com/avatar/d5392fe7a68088f8c8e3bdc43a16f156?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gevork&#39;s gravatar image" />
<p><span>Gevork</span><br />
<span class="score" title="234 reputation points">234</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gevork has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Sep '11, 07:34</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-7916" class="comments-container">
&#10;</div>
<div id="comment-tools-7916" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7916-form-container" class="comment-form-container">
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

<span id="7917"></span>

<div id="answer-container-7917" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7917-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7917-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7917-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Gevork has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You seem to have a directory or a file called <code>10m_populated_places</code>. This is not right. What you need would look like this:</p>
<pre><code>10m_populated_places.dbf
10m_populated_places.prj
10m_populated_places.shp
10m_populated_places.shx</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Sep '11, 07:38</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-7917" class="comments-container">
<span id="7918"></span>
<div id="comment-7918" class="comment">
<div id="post-7918-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>it seems inside the archive files start with ne_ like ne_10m_....</p>
<p><a href="http://tinypic.com/view.php?pic=wa6bg0&amp;s=7">http://tinypic.com/view.php?pic=wa6bg0&amp;s=7</a></p>
<p>Maybe this is the problem. I will try now to rename them all...and will vote for you :)))</p>
</div>
<div id="comment-7918-info" class="comment-info">
<span class="comment-age">(16 Sep '11, 07:48)</span> <span class="comment-user userinfo">Gevork</span>
</div>
</div>
<span id="7919"></span>
<div id="comment-7919" class="comment">
<div id="post-7919-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://gevork.ru/2011/09/16/mapnikubuntu-a…ted-places-zip/">http://gevork.ru/2011/09/16/mapnikubuntu-a…ted-places-zip/</a> thank you <span>@Frederik Ramm</span> !!</p>
</div>
<div id="comment-7919-info" class="comment-info">
<span class="comment-age">(16 Sep '11, 08:45)</span> <span class="comment-user userinfo">Gevork</span>
</div>
</div>
</div>
<div id="comment-tools-7917" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7917-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9813"></span>

<div id="answer-container-9813" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9813-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9813-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9813-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>hi, I also experienced a Runtime Error, but the problem is like this:</p>
<blockquote>
<p>dewi@dewi-laptop:/src/bin/planet/mapnik-stylesheets$ ./<a href="http://generate_image.py">generate_image.py</a> Traceback (most recent call last): File "./<a href="http://generate_image.py">generate_image.py</a>", line 42, in &lt;module&gt; mapnik.load_map(m,mapfile) RuntimeError: This map uses features only present in Mapnik version 0.7.1 and newer (in node Map)</p>
</blockquote>
<p>thank's</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jan '12, 09:16</strong></p>
<img src="https://secure.gravatar.com/avatar/10d20bc95a8d93f3b4240b33232ac314?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dewi%20Robiatul%20mubararah&#39;s gravatar image" />
<p><span>Dewi Robiatu...</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dewi Robiatul mubararah has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9813" class="comments-container">
&#10;</div>
<div id="comment-tools-9813" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9813-form-container" class="comment-form-container">
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

