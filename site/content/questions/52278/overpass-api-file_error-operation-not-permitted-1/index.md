+++
type = "question"
title = "Overpass API FILE_ERROR Operation not permitted 1"
description = '''I am following this http://wiki.openstreetmap.org/wiki/Overpass_API/Installation guide to install OSM3S server on Ubuntu using vagrant. After populating DB whenever i try to Start Dispatcher Deomon using the command: nohup $EXEC_DIR/bin/dispatcher --osm-base --db-dir=$DB_DIR &amp;amp;  I get the followi...'''
date = "2016-09-28T15:22:00Z"
lastmod = "2016-09-28T19:03:00Z"
weight = 52278
keywords = [ "openstreetmap", "overpassapi", "ubuntu" ]
aliases = [ "/questions/52278" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API FILE_ERROR Operation not permitted 1](/questions/52278/overpass-api-file_error-operation-not-permitted-1)

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
<span id="post-52278-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52278-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52278-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am following this <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Installation">http://wiki.openstreetmap.org/wiki/Overpass_API/Installation</a> guide to install OSM3S server on Ubuntu using vagrant.</p>
<p>After populating DB whenever i try to Start Dispatcher Deomon using the command:</p>
<p>nohup $EXEC_DIR/bin/dispatcher --osm-base --db-dir=$DB_DIR &amp;</p>
<p>I get the following error:</p>
<blockquote>
<p>File_Error Operation not permitted 1/vagrant/test/osm-3s_v0.7.52/db//<strong>osm3s_v0.7.52_osm_base</strong>Unix_Socket::4</p>
</blockquote>
<p>If i try to rename the osm file in my db directory from osm_base_version to <strong>osm3s_v0.7.52_osm_base</strong> it gives the following error:</p>
<blockquote>
<p>File_Error Address already in use 98/vagrant/test/osm3s_v0.7.52/db//osm3s_v0.7.52_osm_base Unix_Socket::4</p>
</blockquote>
<p>I tried to run the command after removing the stale lock files /dev/shm and osm file in db directory (mentioned the Troubleshooting section of installation guide) but it shows no success .</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Sep '16, 15:22</strong></p>
<img src="https://secure.gravatar.com/avatar/0a3275060ba32c28948b462c8af3335d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="awais_khan&#39;s gravatar image" />
<p><span>awais_khan</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="awais_khan has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52278" class="comments-container">
<span id="52287"></span>
<div id="comment-52287" class="comment">
<div id="post-52287-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>cross-posted: <a href="https://stackoverflow.com/questions/39748042/overpass-api-file-error-operation-not-permitted-1">https://stackoverflow.com/questions/39748042/overpass-api-file-error-operation-not-permitted-1</a></p>
</div>
<div id="comment-52287-info" class="comment-info">
<span class="comment-age">(28 Sep '16, 19:03)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-52278" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52278-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

