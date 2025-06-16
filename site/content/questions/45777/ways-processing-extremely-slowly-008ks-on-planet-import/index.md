+++
type = "question"
title = "Ways processing extremely slowly (0.08k/s) on planet import"
description = '''I&#x27;m doing a full planet import on an Ubuntu machine with 28GB of RAM. I&#x27;ve changed the postgres.conf proportionally to what is recommended on the wiki and kicked off the import process with the following options: sudo -u postgres ./utils/setup.php --osm-file /datadrive/downloadedfilesforimport/plane...'''
date = "2015-10-07T14:15:00Z"
lastmod = "2018-05-05T18:19:00Z"
weight = 45777
keywords = [ "planet_osm_ways", "osm2pgsql", "planet_osm" ]
aliases = [ "/questions/45777" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Ways processing extremely slowly (0.08k/s) on planet import](/questions/45777/ways-processing-extremely-slowly-008ks-on-planet-import)

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
<span id="post-45777-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45777-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45777-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm doing a full planet import on an Ubuntu machine with 28GB of RAM. I've changed the postgres.conf proportionally to <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation#PostgreSQL_Tuning">what is recommended on the wiki</a> and kicked off the import process with the following options:</p>
<pre><code>sudo -u postgres ./utils/setup.php --osm-file /datadrive/downloadedfilesforimport/planet-latest.osm.bz2 --all --osm2pgsql-cache 21000 2&gt;&amp;1 | sudo tee setup.log</code></pre>
<p>Nodes import quickly enough, but Ways are moving at less than 1/1000th the speed in terms of k/s. The process is chugging along and using lot's of memory but relatively little CPU compared to when it was importing Nodes. I know that Ways are supposed to take longer than Nodes to import but what I've read in the <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql/benchmarks">benchmarks</a> and elsewhere, this doesn't seem right. Here's the current output:</p>
<pre><code>Import
osm2pgsql SVN version 0.89.0-dev (64bit id space)
&#10;Using projection SRS 4326 (Latlong)
NOTICE:  table &quot;place&quot; does not exist, skipping
Allocating memory for dense node cache
Allocating dense node cache in one big chunk
Allocating memory for sparse node cache
Sharing dense sparse
Node-cache: cache=21000MB, maxblocks=2688000*8192, allocation method=11
Mid: pgsql, scale=10000000 cache=21000
Setting up table: planet_osm_nodes
Setting up table: planet_osm_ways
Setting up table: planet_osm_rels
&#10;Reading in file: /datadrive/downloadedfilesforimport/planet-latest.osm.bz2
Using XML parser.
Processing: Node(3046040k 107.4k/s) Way(3566k 0.08k/s) Relation(0 0.00/s)</code></pre>
<p>Ways started processing about 12 hours ago. Any idea what could be going on here? Should I just be patient?</p>
<p><strong>EDIT:</strong> being that I'm from the Windows world, the muscle memory around Ctrl+C to copy is strong and as a result has caused me to kill the import. If I need to adjust settings and restart the import, that's no longer a problem.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet_osm_ways" rel="tag" title="see questions tagged &#39;planet_osm_ways&#39;">planet_osm_ways</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-planet_osm" rel="tag" title="see questions tagged &#39;planet_osm&#39;">planet_osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Oct '15, 14:15</strong></p>
<img src="https://secure.gravatar.com/avatar/9b2b0a805463173c9cb4a740aefbac55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joelmdev&#39;s gravatar image" />
<p><span>joelmdev</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joelmdev has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Oct '15, 16:46</strong> </span></p>
</div>
</div>
<div id="comments-container-45777" class="comments-container">
<span id="45783"></span>
<div id="comment-45783" class="comment">
<div id="post-45783-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Have you checked if/how much your system is paging? (In linux getting it wrong terms "swaping") 28GB is likely not really enough memory for a current planet all things considered.</p>
</div>
<div id="comment-45783-info" class="comment-info">
<span class="comment-age">(07 Oct '15, 15:33)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="45785"></span>
<div id="comment-45785" class="comment">
<div id="post-45785-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/2053/simonpoole"></a><a href="https://help.openstreetmap.org/users/2053/simonpoole">@SimonPoole</a> swap is not currently configured on the machine. It's a fresh VM, and I tried to use proportional RAM settings for postgres and osm2pgsql as what were outlined in the wiki. The wiki had also pointed out that swapping should be avoided, so I didn't pursue it any further. I'm assuming I could create a swap file via the instructions here <a href="https://www.digitalocean.com/community/tutorials/how-to-add-swap-on-ubuntu-14-04">https://www.digitalocean.com/community/tutorials/how-to-add-swap-on-ubuntu-14-04</a> but I'd need some guidance on how large to make it and how to tweak the kernel. I can also bump the machine up to 56GB during the import if needed. Also worth noting that I intend to drop the resources on the machine significantly after the import is finished.</p>
</div>
<div id="comment-45785-info" class="comment-info">
<span class="comment-age">(07 Oct '15, 16:26)</span> <span class="comment-user userinfo">joelmdev</span>
</div>
</div>
<span id="45787"></span>
<div id="comment-45787" class="comment">
<div id="post-45787-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not really answer, but someone else was looking at the same thing <a href="https://www.openstreetmap.org/user/baditaflorin/diary/35848">https://www.openstreetmap.org/user/baditaflorin/diary/35848</a> and <a href="https://www.openstreetmap.org/user/baditaflorin/diary/35848">https://www.openstreetmap.org/user/baditaflorin/diary/35848</a></p>
</div>
<div id="comment-45787-info" class="comment-info">
<span class="comment-age">(07 Oct '15, 16:54)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="45798"></span>
<div id="comment-45798" class="comment">
<div id="post-45798-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Bumping up the memory would likely be a good idea in any case.</p>
</div>
<div id="comment-45798-info" class="comment-info">
<span class="comment-age">(08 Oct '15, 09:48)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="45818"></span>
<div id="comment-45818" class="comment">
<div id="post-45818-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm sure that more memory would be good, but would memory alone be enough to cause the Ways to import this slowly?</p>
</div>
<div id="comment-45818-info" class="comment-info">
<span class="comment-age">(09 Oct '15, 15:35)</span> <span class="comment-user userinfo">joelmdev</span>
</div>
</div>
</div>
<div id="comment-tools-45777" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45777-form-container" class="comment-form-container">
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

<span id="63327"></span>

<div id="answer-container-63327" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63327-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63327-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63327-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Would like to make some contribution here on exactly the same problem: my semi-production nominatim installation test setup initially included 2GB of RAM for VM with Ubuntu 16.04. While installing using <a href="http://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-16/">the guideline</a> I kept all postgresql buffer sizes to their defaults (e.g. did not increase them to 2G/10G/24G as <a href="http://nominatim.org/release-docs/latest/admin/Installation/#postgresql-tuning">this manual</a> suggests), and also decreased --osm2pgsql-cache setting by 10x, e.g. running:</p>
<pre><code>./utils/setup.php --osm-file /srv/nominatim/Nominatim-3.1.0/data/russia-latest.osm.pbf
--all --osm2pgsql-cache 2800 2&gt;&amp;1 | tee setup.log</code></pre>
<p>However this attempt failed with exactly the same problem as Op described, producing processing speed as follows (approx. values, as I did not keep the 1st attempt logs):</p>
<pre><code>Processing: Node(290006k 73.0k/s) Way(1003k 0.11k/s) Relation(0 0.0/s)</code></pre>
<p>The thread was stuck for hours at this stage with 0,11k/s throughput for Way processing, so I cancelled the import, decided to increase VM RAM from 2GB to 8GB. This lead to success: both import speed doubled and the processing stage was finished, overall import continued to next stages:</p>
<pre><code>Reading in file: /srv/nominatim/Nominatim-3.1.0/data/russia-latest.osm.pbf
Using PBF parser.
Processing: Node(290006k 154.0k/s) Way(25978k 47.15k/s) Relation(744260 515.77/s)  parse time: 3877s
Node stats: total(290006204), max(5597166795) in 1883s
Way stats: total(25978618), max(585757808) in 551s
Relation stats: total(745112), max(8271126) in 1443s</code></pre>
<p>While writing this lines I'm waiting for Load Data stage completion:</p>
<pre><code>2018-05-05 19:09:29 == Loading word list
 count
--------
 885590
(1 row)
&#10; count
-------
 46228
(1 row)
&#10;2018-05-05 19:19:29 == Load Data
.......................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 May '18, 18:19</strong></p>
<img src="https://secure.gravatar.com/avatar/469f1370fd837b672771f5e5234eaf24?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ivan%20M3&#39;s gravatar image" />
<p><span>Ivan M3</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ivan M3 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63327" class="comments-container">
&#10;</div>
<div id="comment-tools-63327" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63327-form-container" class="comment-form-container">
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

