+++
type = "question"
title = "Local Tile Server from Packages: 404 when displaying tiles"
description = '''Hi Everyboy, Thanks for reading this and for any help you can provide! I am trying to setup my own tile server on Ubuntu 14.04 following the following guide link text. I believe i followed the instructions and everything completed without error. However, i am getting 404 responses when trying to dow...'''
date = "2014-07-30T19:20:00Z"
lastmod = "2014-07-30T22:14:00Z"
weight = 35317
keywords = [ "not_shown", "renderd", "mod_tile", "server", "tileserver" ]
aliases = [ "/questions/35317" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Local Tile Server from Packages: 404 when displaying tiles](/questions/35317/local-tile-server-from-packages-404-when-displaying-tiles)

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
<span id="post-35317-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35317-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35317-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi Everyboy,</p>
<p>Thanks for reading this and for any help you can provide!</p>
<p>I am trying to setup my own tile server on Ubuntu 14.04 following the following guide <a href="http://www.distrogeeks.com/build-your-own-tile-server-ubuntu/2/">link text</a>.</p>
<p>I believe i followed the instructions and everything completed without error. However, i am getting 404 responses when trying to download tiles (both through slippymap and through /osm_tiles/0/0/0.png).</p>
<p>Looking at the comments on that guide, it seems lots of people are having a similar problem to me but no solutions have been posted :-(</p>
<p>Any help would be greatly appreciated!</p>
<p><strong>Commands and log output</strong></p>
<p>I have gone to the mod_tile/renderd status page at /mod_tile/. It displays correctly but shows 0 tiles have been rendered.</p>
<p>I have started renderd in the forground to watch its messages. There where no obvious error messages but there are also no messages displayed when i request tiles.</p>
<pre><code> 
chris@www:~$ renderd -f
renderd[2355]: Rendering daemon started
renderd[2355]: Initiating reqyest_queue
renderd[2355]: Parsing section renderd
renderd[2355]: Parsing render section 0
renderd[2355]: Parsing section mapnik
renderd[2355]: Parsing section default
renderd[2355]: config renderd: unix socketname=/var/run/renderd/renderd.sock
renderd[2355]: config renderd: num_threads=4
renderd[2355]: config renderd: num_slaves=0
renderd[2355]: config renderd: tile_dir=/var/lib/mod_tile
renderd[2355]: config renderd: stats_file=/var/run/renderd/renderd.stats
renderd[2355]: config mapnik:  plugins_dir=/usr/lib/mapnik/2.2/input
renderd[2355]: config mapnik:  font_dir=/usr/share/fonts/truetype/
renderd[2355]: config mapnik:  font_dir_recurse=1
renderd[2355]: config renderd(0): Active
renderd[2355]: config renderd(0): unix socketname=/var/run/renderd/renderd.sock
renderd[2355]: config renderd(0): num_threads=4
renderd[2355]: config renderd(0): tile_dir=/var/lib/mod_tile
renderd[2355]: config renderd(0): stats_file=/var/run/renderd/renderd.stats
renderd[2355]: config map 0:   name(default) file(/etc/mapnik-osm-carto-data/osm.xml) uri(/osm/) htcp() host()
renderd[2355]: Initialising unix server socket on /var/run/renderd/renderd.sock
renderd[2355]: Created server socket 4
renderd[2355]: Renderd is using mapnik version 2.2.0
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//padauk/Padauk-bold.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//padauk/Padauk.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//padauk/Padauk-bookbold.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//padauk/Padauk-book.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-dejavu/DejaVuSans-Oblique.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-dejavu/DejaVuSans-BoldOblique.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-dejavu/DejaVuSansMono-Oblique.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-dejavu/DejaVuSerifCondensed-BoldItalic.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-dejavu/DejaVuSansCondensed-Bold.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-dejavu/DejaVuSans.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-dejavu/DejaVuSansMono-Bold.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-dejavu/DejaVuSerifCondensed-Italic.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-dejavu/DejaVuSerif-Bold.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-dejavu/DejaVuSansCondensed-BoldOblique.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-dejavu/DejaVuSerif-BoldItalic.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-dejavu/DejaVuSerifCondensed.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-dejavu/DejaVuSerifCondensed-Bold.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-dejavu/DejaVuSansMono-BoldOblique.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-dejavu/DejaVuSansMono.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-dejavu/DejaVuSans-ExtraLight.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-dejavu/DejaVuSans-Bold.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-dejavu/DejaVuSansCondensed-Oblique.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-dejavu/DejaVuSerif-Italic.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-dejavu/DejaVuSerif.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-dejavu/DejaVuSansCondensed.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-khmeros/KhmerOSbattambang.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-khmeros/KhmerOSmuolpali.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-khmeros/KhmerOSmetalchrieng.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-khmeros/KhmerOSfreehand.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-khmeros/KhmerOSmuollight.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-khmeros/KhmerOSmuol.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-khmeros/KhmerOSsiemreap.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-khmeros/KhmerOSfasthand.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-khmeros/KhmerOSbokor.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-khmeros/KhmerOScontent.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//dejavu/DejaVuSans-Oblique.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//dejavu/DejaVuSans-BoldOblique.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//dejavu/DejaVuSansMono-Oblique.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//dejavu/DejaVuSerifCondensed-BoldItalic.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//dejavu/DejaVuSansCondensed-Bold.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//dejavu/DejaVuSans.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//dejavu/DejaVuSansMono-Bold.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//dejavu/DejaVuSerifCondensed-Italic.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//dejavu/DejaVuSerif-Bold.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//dejavu/DejaVuSansCondensed-BoldOblique.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//dejavu/DejaVuSerif-BoldItalic.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//dejavu/DejaVuSerifCondensed.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//dejavu/DejaVuSerifCondensed-Bold.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//dejavu/DejaVuSansMono-BoldOblique.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//dejavu/DejaVuSansMono.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//dejavu/DejaVuSans-ExtraLight.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//dejavu/DejaVuSans-Bold.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//dejavu/DejaVuSansCondensed-Oblique.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//dejavu/DejaVuSerif-Italic.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//dejavu/DejaVuSerif.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//dejavu/DejaVuSansCondensed.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-kannada-fonts/Kedage-t.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-kannada-fonts/Malige-i.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-kannada-fonts/lohit_kn.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-kannada-fonts/Malige-t.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-kannada-fonts/Kedage-i.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-khmeros-core/KhmerOSsys.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-khmeros-core/KhmerOS.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-indic-fonts-core/lohit_bn.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-indic-fonts-core/Pothana2000.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-indic-fonts-core/Vemana.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-indic-fonts-core/gargi.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-indic-fonts-core/lohit_ta.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-indic-fonts-core/MuktiNarrowBold.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-indic-fonts-core/Meera_04.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-indic-fonts-core/Malige-n.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-indic-fonts-core/lohit_hi.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-indic-fonts-core/Kedage-b.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-indic-fonts-core/Rachana_04.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-indic-fonts-core/utkal.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-indic-fonts-core/lohit_gu.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-indic-fonts-core/MuktiNarrow.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-indic-fonts-core/Malige-b.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-indic-fonts-core/Kedage-n.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-indic-fonts-core/Rekha.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//ttf-tamil-fonts/Samyak-Tamil.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//droid/DroidSansJapanese.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//droid/DroidSansArmenian.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//droid/DroidSerif-Regular.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//droid/DroidNaskh-Bold.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//droid/DroidSans-Bold.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//droid/DroidSansEthiopic-Regular.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//droid/DroidSerif-Bold.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//droid/DroidSansHebrew-Regular.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//droid/DroidSansFallbackFull.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//droid/DroidNaskh-Regular.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//droid/DroidSans.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//droid/DroidSerif-BoldItalic.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//droid/DroidSansEthiopic-Bold.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//droid/DroidSansMono.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//droid/DroidSerif-Italic.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//droid/DroidSansThai.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//droid/DroidSansHebrew-Bold.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//droid/DroidSansGeorgian.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//unifont/unifont_sample.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//unifont/unifont.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//arundina/ArundinaSansMono-Oblique.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//arundina/ArundinaSansMono-Bold.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//arundina/ArundinaSerif-Bold.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//arundina/ArundinaSerif.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//arundina/ArundinaSans-BoldOblique.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//arundina/ArundinaSans-Bold.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//arundina/ArundinaSansMono.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//arundina/ArundinaSans-Oblique.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//arundina/ArundinaSans.ttf
renderd[2355]: DEBUG: Loading font: /usr/share/fonts/truetype//arundina/ArundinaSansMono-BoldOblique.ttf
Running in foreground mode...
renderd[2355]: Starting stats thread
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[2355]: Loading parameterization function for debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[2355]: Loading parameterization function for
&#10;debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[2355]: Loading parameterization function for
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[2355]: Loading parameterization function for
&#10;renderd[2355]: Using web mercator projection settings
renderd[2355]: Using web mercator projection settings
renderd[2355]: Using web mercator projection settings
renderd[2355]: Using web mercator projection settings</code></pre>
<p>ls -la /var/lib/mod_tile shows folder "default" and planet-import-complete; all owned by www-data.</p>
<pre><code> 
drwxr-xr-x  3 www-data www-data 4096 Jul 29 19:16 default
-rw-r--r--  1 www-data www-data    0 Jul 29 22:36 planet-import-complete</code></pre>
<p>Apache 2 shows the following on restart:</p>
<p><code> </code></p>
<pre><code>  * Restarting web server apache2                                                [Wed Jul 30 19:04:57.877419 2014] [tile:notice] [pid 2499:tid 140236885788544] Loading tile config default at /osm/ for zooms 0 - 20 from tile directory /var/lib/mod_tile with extension .png and mime type image/png
AH00558: apache2: Could not reliably determine the server&#39;s fully qualified domain name, using 127.0.1.1. Set the &#39;ServerName&#39; directive globally to suppress this message</code></pre>
<p>Let me know if there is anything else i can post that would help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-not_shown" rel="tag" title="see questions tagged &#39;not_shown&#39;">not_shown</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jul '14, 19:20</strong></p>
<img src="https://secure.gravatar.com/avatar/ff5ea5be18c6c2bab9d7c1dcbb829bc8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BobBobson&#39;s gravatar image" />
<p><span>BobBobson</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BobBobson has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jul '14, 19:21</strong> </span></p>
</div>
</div>
<div id="comments-container-35317" class="comments-container">
&#10;</div>
<div id="comment-tools-35317" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35317-form-container" class="comment-form-container">
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

<span id="35323"></span>

<div id="answer-container-35323" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35323-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-35323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="BobBobson has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your renderd claims to serve the default style under /osm:</p>
<pre><code>renderd[2355]: config map 0:   name(default) file(/etc/mapnik-osm-carto-data/osm.xml) uri(/osm/) htcp() host()</code></pre>
<p>Therefore your tile URL is not /osm_tiles/0/0/0.png but /osm/0/0/0.png.</p>
<p>If you've done that right and still encounter problems, look at the Apache log file and check if there's maybe a communications problem between mod_tile and renderd.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jul '14, 21:07</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-35323" class="comments-container">
<span id="35325"></span>
<div id="comment-35325" class="comment">
<div id="post-35325-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Ok, i feel a bit silly now but I'm very happy its working :-) The /osm/ line in the render logs sticks out as clear as day, but I've spent the last two days looking at this and didnt spot it.</p>
<p>I have updated slippymap accordingly and its working perfectly. I will post a comment on the tutorial incase the others are having the same problem.</p>
<p>Many thanks for your help!</p>
<p>Bob</p>
</div>
<div id="comment-35325-info" class="comment-info">
<span class="comment-age">(30 Jul '14, 22:14)</span> <span class="comment-user userinfo">BobBobson</span>
</div>
</div>
</div>
<div id="comment-tools-35323" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35323-form-container" class="comment-form-container">
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

