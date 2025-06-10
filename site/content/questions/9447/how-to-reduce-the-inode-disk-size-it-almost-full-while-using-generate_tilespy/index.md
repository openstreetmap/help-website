+++
type = "question"
title = "How to reduce the inode disk size. It almost full while using generate_tiles.py"
description = '''My OSM is ready to generate tiles, Now using mapnik I tried to generate Tiles with the help of following command: baban@baban-desktop:~/Mapserver/bin/mapnik$ ./generate_tiles.py  and it generate lots of tiles, I observed that the disk space and the Inode space is almost full  command : df -ih (going...'''
date = "2011-12-12T07:07:00Z"
lastmod = "2011-12-12T09:04:00Z"
weight = 9447
keywords = [ "generate_tiles", "issue", "inode", "space" ]
aliases = [ "/questions/9447" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to reduce the inode disk size. It almost full while using generate_tiles.py](/questions/9447/how-to-reduce-the-inode-disk-size-it-almost-full-while-using-generate_tilespy)

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
<span id="post-9447-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9447-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9447-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My OSM is ready to generate tiles, Now using mapnik I tried to generate Tiles with the help of following command: baban@baban-desktop:~/Mapserver/bin/mapnik$ ./<a href="http://generate_tiles.py">generate_tiles.py</a> and it generate lots of tiles, I observed that the disk space and the Inode space is almost full command : df -ih (going to be 98% used inode)</p>
<p>Can you Please help to reduce inode size so that I can finish to generate tiles (it is now 11th zoom level and I want to go up to 20th Zoom Level)</p>
<p>disk space : <code>baban@baban-desktop:~$ df -h Filesystem Size Used Avail Use% Mounted on /dev/sda1 61G 45G 13G 78% / udev 501M 180K 501M 1% /dev none 501M 356K 501M 1% /dev/shm none 501M 112K 501M 1% /var/run none 501M 0 501M 0% /var/lock none 501M 0 501M 0% /lib/init/rw /dev/sda4 9.7G 150M 9.0G 2% /data</code></p>
<p>Before I start to generate Tiles AVAIL DISK SPACE is 27GB and Inode space is 90% free</p>
<p>PLEASE HELP ME TO REDUCE INODE USED SIZE</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-generate_tiles" rel="tag" title="see questions tagged &#39;generate_tiles&#39;">generate_tiles</span> <span class="post-tag tag-link-issue" rel="tag" title="see questions tagged &#39;issue&#39;">issue</span> <span class="post-tag tag-link-inode" rel="tag" title="see questions tagged &#39;inode&#39;">inode</span> <span class="post-tag tag-link-space" rel="tag" title="see questions tagged &#39;space&#39;">space</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Dec '11, 07:07</strong></p>
<img src="https://secure.gravatar.com/avatar/6415fd7bc63406c5ab1bc64cc29bb52a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baban&#39;s gravatar image" />
<p><span>baban</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baban has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Dec '11, 07:55</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-9447" class="comments-container">
&#10;</div>
<div id="comment-tools-9447" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9447-form-container" class="comment-form-container">
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

<span id="9449"></span>

<div id="answer-container-9449" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9449-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9449-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-9449-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't know what area you are rendering, but you write that before you start, you have 27 GB free. Then above you write that after generating up to zoom level 11, you have 13 GB left. This means that you have generated about 14 GB worth of tiles for zoom levels 0-11. Given that each zoom level will - very roughly - triple the amount of data, you should expect to require the following amount of space for all tiles:</p>
<ul>
<li>Zoom 0-11: 14 GB (what you already have)</li>
<li>Zoom 12: 42 GB (you don't have that much)</li>
<li>Zoom 13: 126 GB</li>
<li>Zoom 14: 378 GB</li>
<li>Zoom 15: 1 TB</li>
<li>Zoom 16: 3 TB</li>
<li>Zoom 17: 9 TB</li>
<li>Zoom 18: 27 TB</li>
<li>Zoom 19: 81 TB</li>
<li>Zoom 20: 240 TB</li>
</ul>
<p>Since many of the zoom18+ tiles are going to be empty, maybe the total amount of space you need is not <em>that</em> big in reality but you will certainly require several Terabytes if you want to go to z20.</p>
<p>If your problem really were an inode problem only, then the answer would be to either use a proper tile generating system like renderd or tirex and produce metatiles (they put 64 tiles in one file, using less inodes), or else simply format your disk with a different bytes-per-inode ratio (something like "-i 8192" in <code>mkfs.ext2</code>).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Dec '11, 08:04</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-9449" class="comments-container">
<span id="9451"></span>
<div id="comment-9451" class="comment">
<div id="post-9451-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I want to render tiles for India only. I tried India coordinates in <a href="http://generate_tiles.py">generate_tiles.py</a>. But it does not generate tiles. Currently, <a href="http://generate_tiles.py">generate_tiles.py</a> contains following lines. What should I change if I need tiles for India only.</p>
<p>bbox = (-180.0,-90.0, 180.0,90.0) render_tiles(bbox, mapfile, tile_dir, 0, 15, "India")</p>
</div>
<div id="comment-9451-info" class="comment-info">
<span class="comment-age">(12 Dec '11, 09:04)</span> <span class="comment-user userinfo">baban</span>
</div>
</div>
</div>
<div id="comment-tools-9449" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9449-form-container" class="comment-form-container">
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

