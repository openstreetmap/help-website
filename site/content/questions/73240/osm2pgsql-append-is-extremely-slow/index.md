+++
type = "question"
title = "Osm2pgsql --append is extremely slow"
description = '''So I was following https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/ to load a &quot;gis&quot; database with tiles of Azerbaijan and everything worked RELATIVELY quickly. But after I tried to append a map of central part of Russia the speed of PDB was horrible: Processing: Node(1...'''
date = "2020-02-26T10:23:00Z"
lastmod = "2020-03-03T21:57:00Z"
weight = 73240
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/73240" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Osm2pgsql --append is extremely slow](/questions/73240/osm2pgsql-append-is-extremely-slow)

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
<span id="post-73240-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73240-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73240-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>So I was following <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/</a> to load a "gis" database with tiles of Azerbaijan and everything worked RELATIVELY quickly.</p>
<p>But after I tried to append a map of central part of Russia the speed of PDB was horrible: Processing: Node(1580k 5.1k/s) Way(0k 0.00k/s) Relation(0 0.00/s) And it didn't consume any resources: 3 CPUs were consumed more by x-org then by Osm2pgsql and there was plenty of RAM available (2.2G out of 9 were used) The script I run for this is as follows:</p>
<pre><code>osm2pgsql -d gis --append --slim  -G --hstore --tag-transform-script ~/src/openstreetmap-carto/openstreetmap-carto.lua -C 2500 --number-processes 1 -S ~/src/openstreetmap-carto/openstreetmap-carto.style ~/data/central-fed-district-latest.osm.pbf</code></pre>
<p>When I added Azerbaijan tiles, I used "--create" instead of "--append" option and the speed of Node processing was around 300 kb/sec (whichs extremly low as well, but not THAT low). I can't figure out what might be the reason for this, because there is a plenty of resources available.</p>
<p>So my question is how do I speed this up, if possible. Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Feb '20, 10:23</strong></p>
<img src="https://secure.gravatar.com/avatar/7d9dea8db6c9981b45d28f28bb29f49d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kartman1&#39;s gravatar image" />
<p><span>kartman1</span><br />
<span class="score" title="38 reputation points">38</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kartman1 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Feb '20, 10:27</strong> </span></p>
</div>
</div>
<div id="comments-container-73240" class="comments-container">
&#10;</div>
<div id="comment-tools-73240" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73240-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="73241"></span>

<div id="answer-container-73241" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73241-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73241-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-73241-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Don't use <code>--append</code>. Merge the .osm.pbf files you want to import with <code>osmium</code> (or <code>osmosis</code>), and then import the combined file. Appending is super slow because it uses the same processing chain as updating, and for every new object that comes in the update processing chain needs to check if the new information causes a change to existing data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Feb '20, 10:36</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-73241" class="comments-container">
<span id="73243"></span>
<div id="comment-73243" class="comment">
<div id="post-73243-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Then why (if this operation is so ineffecient) doesn't it consume more processing power? I don't really mind it doing some extra work, it's just weird that it refuses to use any resources. That is just being lazy at best.</p>
</div>
<div id="comment-73243-info" class="comment-info">
<span class="comment-age">(26 Feb '20, 11:57)</span> <span class="comment-user userinfo">kartman1</span>
</div>
</div>
<span id="73244"></span>
<div id="comment-73244" class="comment">
<div id="post-73244-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My suspicion is that it is limited by disk I/O.</p>
</div>
<div id="comment-73244-info" class="comment-info">
<span class="comment-age">(26 Feb '20, 12:00)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="73256"></span>
<div id="comment-73256" class="comment">
<div id="post-73256-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OMG I downloaded the PBF file for the whole Asia (7.7 Gb) and left it working for the night and when I got back, the speed of the Node Processing was 12 kb/s!!! Wtf is that! Wtf is that application! How do people even use it! My pc is a production grade machine and even though I run a VM it was configured to use more than a half of everything from the host system! Wtf is going on! Do I have to wait a whole month (if I'm lucky!) to load the database every time something small changes as well?!!</p>
</div>
<div id="comment-73256-info" class="comment-info">
<span class="comment-age">(27 Feb '20, 07:46)</span> <span class="comment-user userinfo">kartman1</span>
</div>
</div>
<span id="73266"></span>
<div id="comment-73266" class="comment">
<div id="post-73266-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Please, calm down. Lose the "OMG"s and the "Wtf"s and the multiple exclamation marks. This is not high school. -- OSM data import is very I/O intensive. You absolutely must have a (local, not SAN) SSD/NVMe disk if you want to get any performance out of it, and when using virtualisation you must make sure that you have the right settings (disk drivers, emulation, whatever) as to not interfere with disk I/O performance. You can have the fattest production grade machine with 256 GB RAM and 64 CPU cores, the Asia import will still run for a week if you have rotating hard disk or bad virtualization. -- There are also some recommendations about tuning your PostgreSQL database for faster imports which you can find using your favourite search engine.</p>
</div>
<div id="comment-73266-info" class="comment-info">
<span class="comment-age">(27 Feb '20, 10:09)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="73271"></span>
<div id="comment-73271" class="comment">
<div id="post-73271-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/17942/kartman1">@kartman1</a> Thanks for giving everyone a laugh this morning!</p>
<p>To take a step back, the answer suggested "Merge the .osm.pbf files you want to import with osmium (or osmosis), and then import the combined file". You at the time were trying to process Azerbaijan and part of Russia. No-one suggested "download the whole of Asia and try and load that. I'd suggest that you browse around <a href="http://download.geofabrik.de/asia.html">http://download.geofabrik.de/asia.html</a> and decide what bits you want. If it's just 2 or more downloadable regions, then download them and merge using osmium or osmosis. If it's part of a larger area, then perhaps cut the bit you want out of that larger area. There's documentation linked from the OSM wiki - for example <a href="https://wiki.openstreetmap.org/wiki/Osmium#Osmium_Tool">https://wiki.openstreetmap.org/wiki/Osmium#Osmium_Tool</a> points to <a href="https://osmcode.org/osmium-tool/">https://osmcode.org/osmium-tool/</a> and one of the things that that mentions is "Create geographical extracts from OSM files".</p>
</div>
<div id="comment-73271-info" class="comment-info">
<span class="comment-age">(27 Feb '20, 10:31)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="73273"></span>
<div id="comment-73273" class="comment not_top_scorer">
<div id="post-73273-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Helpfully, <a href="/questions/73252/how-to-download-the-newest-osmpbf-file-of-seattle-wa-directly">another question</a> has more detail about "how to obtain a smaller area from within a larger download".</p>
</div>
<div id="comment-73273-info" class="comment-info">
<span class="comment-age">(27 Feb '20, 10:40)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="73275"></span>
<div id="comment-73275" class="comment not_top_scorer">
<div id="post-73275-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"Thanks for giving everyone a laugh this morning!" - you are welcome, I had to pay with something.</p>
</div>
<div id="comment-73275-info" class="comment-info">
<span class="comment-age">(27 Feb '20, 13:17)</span> <span class="comment-user userinfo">kartman1</span>
</div>
</div>
</div>
<div id="comment-tools-73241" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-73241-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73320"></span>

<div id="answer-container-73320" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73320-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73320-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73320-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well...no postgres optimization helped, I moved vm from expanding disk to a fixed one, still had no impprovements. After searching a bit more carefully on this topick I found similar issues (on machines far more superior) with the way processing on a vm. So there is no surprise that playing around/tweaking/tiddling/widdling/etc. with conf files didn't help at all. As a result I had to borrow a machine with an I7-8700 CPU, 32 gb ram, samsung 970 evo 1TB SSD, Windows 10. And the performance was:</p>
<p>Processing: Node(1160123k 321.1k/s) Way(146288k 7.23k/s) Relation(1128670 634.08/s) parse time: 25620s Node stats: total(1160123207) , max(7248671584) in 3613s Way stats: total(146288690) , max(776865119) in 20227s Relation stats: total(1128706), max(10758453) in 1780s</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Mar '20, 07:53</strong></p>
<img src="https://secure.gravatar.com/avatar/7d9dea8db6c9981b45d28f28bb29f49d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kartman1&#39;s gravatar image" />
<p><span>kartman1</span><br />
<span class="score" title="38 reputation points">38</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kartman1 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Mar '20, 08:22</strong> </span></p>
</div>
</div>
<div id="comments-container-73320" class="comments-container">
<span id="73321"></span>
<div id="comment-73321" class="comment">
<div id="post-73321-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Is this for Asia, and using a similar <code>osm2pgsql</code> command line as shown in your initial post (minus the --append)? Can you share the output of "osm2pgsql -v"?</p>
</div>
<div id="comment-73321-info" class="comment-info">
<span class="comment-age">(03 Mar '20, 08:54)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="73323"></span>
<div id="comment-73323" class="comment">
<div id="post-73323-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It is for Asia with the following command: osm2pgsql -d gis --create --slim -G --hstore --tag-transform-script ~/src/openstreetmap-carto/openstreetmap-carto.lua -C 10500 --drop --disable-parallel-indexing --number-processes 5 -S ~/src/openstreetmap-carto/openstreetmap-carto.style ~/data/asia-latest.osm.pbfA</p>
</div>
<div id="comment-73323-info" class="comment-info">
<span class="comment-age">(03 Mar '20, 11:50)</span> <span class="comment-user userinfo">kartman1</span>
</div>
</div>
<span id="73324"></span>
<div id="comment-73324" class="comment">
<div id="post-73324-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Silly question - do you actually want to load data for the whole of Asia?</p>
</div>
<div id="comment-73324-info" class="comment-info">
<span class="comment-age">(03 Mar '20, 11:52)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="73326"></span>
<div id="comment-73326" class="comment">
<div id="post-73326-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah I needed Asian maps from the start.</p>
</div>
<div id="comment-73326-info" class="comment-info">
<span class="comment-age">(03 Mar '20, 12:00)</span> <span class="comment-user userinfo">kartman1</span>
</div>
</div>
<span id="73328"></span>
<div id="comment-73328" class="comment not_top_scorer">
<div id="post-73328-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do you have the osm2pgsql version for us (osm2pgsql -v)?</p>
</div>
<div id="comment-73328-info" class="comment-info">
<span class="comment-age">(03 Mar '20, 12:30)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="73329"></span>
<div id="comment-73329" class="comment not_top_scorer">
<div id="post-73329-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>osm2pgsql version 1.2.0 (1.2.0-269-g7892613) (64 bit id space)</p>
</div>
<div id="comment-73329-info" class="comment-info">
<span class="comment-age">(03 Mar '20, 12:34)</span> <span class="comment-user userinfo">kartman1</span>
</div>
</div>
<span id="73333"></span>
<div id="comment-73333" class="comment">
<div id="post-73333-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This import, with this osm2pgsql version and this command line (though dropping the -C10500 and adding a <code>--flat-nodes</code> file on the SSD) took 3 hours and 25 minutes on a reasonably big SSD machine here, without virtualisation, plain Ubuntu 16.04. (Node stats: total(1161737945), max(7259603803) in 432s; Way stats: total(146494361), max(777866045) in 3440s; Relation stats: total(1129804), max(10780102) in 490s). This matches my expectations from importing full planet files. I tried the same import without --flat-nodes and everything else the same, and it took 8 hours 25 minutes instead (Node stats: total(1161737945), max(7259603803) in 2173s; Way stats: total(146494361), max(777866045) in 18040s; Relation stats: total(1129804), max(10780102) in 1755s).</p>
</div>
<div id="comment-73333-info" class="comment-info">
<span class="comment-age">(03 Mar '20, 16:19)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-73320" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-73320-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73345"></span>

<div id="answer-container-73345" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73345-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73345-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73345-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should definitely upgrade to osm2pgsql 1.2.1 (<a href="https://github.com/openstreetmap/osm2pgsql/releases).">https://github.com/openstreetmap/osm2pgsql/releases).</a> Although that may appear as a "minor" release, it actually fixes an important memory related bug caused by libosmium, that could cause out of memory issues running osm2pgsql due to GBs of RAM needed for area building. I personally experienced that issue, upgrading to 1.2.1 fixed it.</p>
<p>As others stated: harddisks are <strong><em>totally</em></strong> dead for this kind of work. Building ways and relations requires fast random access to data stored on disk. Best is NVMe SSD, but I run osm2pgsql happily against a USB3 connected 2TB SATA EVO.</p>
<p>VMs are not evil perse. I have successfully imported the whole of Europe (&gt; 20GB PBF) on a 12 GB RAM (+ swap configured) Ubuntu 19.10 Virtualbox instance running PostgreSQL 11, running on an eight year old Core i7-2600 with 16GB RAM and Windows 10 as host system, with the described USB3 connected disk.</p>
<p>Took about 2-3 days for the import if I remember well, not to bad, stats for nodes/ways/relation per sec were comparable to your figures I think. Building osm2pgsql with LUAJIT supports, seemed indeed to improve processing speed by about 25%, as mentioned on the osm2pgsql github site: <a href="https://github.com/openstreetmap/osm2pgsql">https://github.com/openstreetmap/osm2pgsql</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Mar '20, 21:57</strong></p>
<img src="https://secure.gravatar.com/avatar/dc8a1ef54d3e25744ee52d1ad1459a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mboeringa&#39;s gravatar image" />
<p><span>mboeringa</span><br />
<span class="score" title="1542 reputation points"><span>1.5k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mboeringa has 4 accepted answers">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Mar '20, 08:25</strong> </span></p>
</div>
</div>
<div id="comments-container-73345" class="comments-container">
&#10;</div>
<div id="comment-tools-73345" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73345-form-container" class="comment-form-container">
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

