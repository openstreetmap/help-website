+++
type = "question"
title = "Tile server hardware requirements"
description = '''Hello, I&#x27;m in the process to set up my own tile server to reduce the load on OSM, provide my own style, and allow bulk downloads. I&#x27;d like some help to know what dedicated server I have to choose. My requirements are:  low usage, maybe max 20-30 users at the same time during spikes bulk downloads wo...'''
date = "2018-06-27T13:03:00Z"
lastmod = "2019-11-06T10:35:00Z"
weight = 64405
keywords = [ "hardwarerequirements", "tileserver" ]
aliases = [ "/questions/64405" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Tile server hardware requirements](/questions/64405/tile-server-hardware-requirements)

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
<span id="post-64405-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64405-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-64405-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm in the process to set up my own tile server to reduce the load on OSM, provide my own style, and allow bulk downloads. I'd like some help to know what dedicated server I have to choose.</p>
<p>My requirements are:</p>
<ul>
<li>low usage, maybe max 20-30 users at the same time during spikes</li>
<li>bulk downloads would only be possible for paid accounts, so the load would be really small</li>
<li>whole world coverage, limiting max zoom to 16-17 is ok</li>
<li>tiles size is 512*512</li>
<li>updating my db once a month (or even less) is ok</li>
<li>I'd like to provide at least 2 map styles</li>
<li>I won't be able to afford an SSD</li>
</ul>
<p>I can afford this setup:</p>
<ul>
<li>Intel Xeon E3-1270 v6 (4 cores 3.8 Ghz)</li>
<li>32GB of RAM</li>
<li>2TB hard drive</li>
</ul>
<p>Or this one:</p>
<ul>
<li>Intel Xeon E3-1230 v6 (4 cores 3.5 Ghz)</li>
<li>16GB of RAM</li>
<li>4TB hard drive</li>
</ul>
<p>Would they fit? Would they be overkill (I guess they wouldn't, but a man can dream...)? Which would be better?</p>
<p>Other question: how much disk space is needed to execute an update (download the planet.osm pbf file, and insert it in the database while still having the map available for users) ?</p>
<p>Thanks in advance for your help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hardwarerequirements" rel="tag" title="see questions tagged &#39;hardwarerequirements&#39;">hardwarerequirements</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jun '18, 13:03</strong></p>
<img src="https://secure.gravatar.com/avatar/a711e0129f307399a857a6f9b4bfd0e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="timautin&#39;s gravatar image" />
<p><span>timautin</span><br />
<span class="score" title="151 reputation points">151</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="timautin has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jun '18, 13:22</strong> </span></p>
</div>
</div>
<div id="comments-container-64405" class="comments-container">
&#10;</div>
<div id="comment-tools-64405" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64405-form-container" class="comment-form-container">
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

<span id="64406"></span>

<div id="answer-container-64406" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64406-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-64406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="timautin has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You will need about 800 GB (1 TB is better) for the world-wide database and you can update it regularly with incremental updates. You could also do a full import with the <code>--drop</code> option which removes all intermediate data after the import, and then repeat the exercise every time you want a new data set; this only requries ~ 350 GB for the world-wide database but temporarily (during import) more is needed so that you don't come below the 800 GB either way.</p>
<p>32 GB RAM is also the absolute minimum for a planet import; at least 48 GB is recommended.</p>
<p>Without an SSD, your import will take several weeks and it will be impossible to run updates because one day's worth of updates takes longer than a day to apply. The server you listed initially costs EUR 70/month. For the same price, get a Hetzner EX51-SSD (64 GB RAM, 2x500 GB SSD) with Flexipack and an extra 2 TB of SATA disk for the tile cache, or if you're planning to add more styles and/or have styles with hill shading, you can get a 4 TB or 6 TB disk too. This budget option is not as "solid" as the 1+1 offer, it doesn't have ECC RAM and no mirrored disks (though you can add a second SATA drive for an extra 10 EUR, or use the PX-61 with NVMe and ECC RAM for also 10 EUR more), but the SSD and 64 GB of RAM will really make a big difference.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jun '18, 13:59</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-64406" class="comments-container">
<span id="64407"></span>
<div id="comment-64407" class="comment">
<div id="post-64407-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot for that detailed answer! I didn't know about Hetzner, they offer a lot of customisation! Do you have an experience with their support? So you strongly discourage me to go the HDD route, even with 64GB of RAM, even if I'm ok to do monthly updates (or less) and given that the charge is low? I'm a bit scared to go with the no RAID route. I'm not sure how a HDD + SSD RAID1 as you suggest would perform (if I got you correctly?), do you have an experience with that? Also, how much complexity does it adds to have the postgres db on 2 differents SSDs instead of one? Finally, do you have an idea of the size needed for the cache (I plan 1 layer with hill shading, 1 without)?</p>
</div>
<div id="comment-64407-info" class="comment-info">
<span class="comment-age">(27 Jun '18, 15:35)</span> <span class="comment-user userinfo">timautin</span>
</div>
</div>
<span id="64408"></span>
<div id="comment-64408" class="comment">
<div id="post-64408-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Some people do combined SSD+HDD RAIDs but I have no experience with it and would not recommend it. What I recommend is a RAID0 or LVM stripe on the 2x500 GB SSD giving you 1 TB fast storage for the database (looks like one single drive to PostgreSQL), and then storing the operating system and tile cache (and, if required, also hill shading and contour line data) on the additional SATA disk. Having a RAID0 for the data isn't super bad since you can rebuild the database within a day if it should break. RAID1 for the operating system and tile cache is of course a bit safer but hard disks rarely die within their first few years and you'll upgrade the server before that anyway ;) -- I have generally got good service from Hetzner support.</p>
</div>
<div id="comment-64408-info" class="comment-info">
<span class="comment-age">(27 Jun '18, 16:27)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="64409"></span>
<div id="comment-64409" class="comment">
<div id="post-64409-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks again! There's another option with Hetzner for 70€: choose the EX51 (normal one with 2*4TB RAID1) and add a 960GB SSD. Seems the best to me (because the HDD will be RAID-ed). I can even also install osm on the HDD and use it in case the SSD dies (and recreate that say once a year. No updates, and it doesn't matter if it takes weeks to do). Last but not least, does 1 TB of space per layer sounds good to you?</p>
</div>
<div id="comment-64409-info" class="comment-info">
<span class="comment-age">(27 Jun '18, 16:39)</span> <span class="comment-user userinfo">timautin</span>
</div>
</div>
<span id="64410"></span>
<div id="comment-64410" class="comment not_top_scorer">
<div id="post-64410-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not 100% sure if I maybe mixed up prices with and without VAT, Hetzner is a bit unclear about that sometimes. Double-check before you order ;) your configuration works too. You're unlikely to use more than 500 GB per layer of tile cache unless you pre-render like hell. If you do backup your rendering database to SATA disk, make sure to only backup the tables required for rendering and not those only required for updating.</p>
</div>
<div id="comment-64410-info" class="comment-info">
<span class="comment-age">(27 Jun '18, 16:47)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="64412"></span>
<div id="comment-64412" class="comment not_top_scorer">
<div id="post-64412-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh boy you're right for the VAT! First their website was displaying VAT included prices, and now VAT exclusive. If I open the website in privacy mode, I have VAT included prices again... So that setup is 85€ VAT excluded. Thanks for the cache size, I was expecting more! And thanks for the tip on the backup rendering db. Answer accepted!</p>
</div>
<div id="comment-64412-info" class="comment-info">
<span class="comment-age">(27 Jun '18, 16:58)</span> <span class="comment-user userinfo">timautin</span>
</div>
</div>
<span id="71471"></span>
<div id="comment-71471" class="comment">
<div id="post-71471-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi Frederick, your comment is very helpful (and the first actually useful I found!). I am in pretty much the same situation of OP, with the need for several styles. If I just render them on the fly, do I need the additional space you were mentioning? Also, would it be viable or completely nuts?</p>
<p>Please correct me if I'm wrong! Thanks!</p>
</div>
<div id="comment-71471-info" class="comment-info">
<span class="comment-age">(05 Nov '19, 17:47)</span> <span class="comment-user userinfo">phts</span>
</div>
</div>
<span id="71476"></span>
<div id="comment-71476" class="comment not_top_scorer">
<div id="post-71476-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Space requirements have increased a bit since this was posted 18 months ago. If you have multiple styles you will still want to pre-render them at least to about zoom level 12 because doing that on the fly will be too slow. Total tile cache size depends on what your users do, if you have people downloading all tiles for the planet you'll use more! But on an average-use tile server 100 GB per style should be ok for the tile cache. If you need a very large number of styles, check out vector tiles and on-the-fly conversion from vector to raster, but that's a totally different technology from raster tileservers.</p>
</div>
<div id="comment-71476-info" class="comment-info">
<span class="comment-age">(05 Nov '19, 19:34)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="71480"></span>
<div id="comment-71480" class="comment">
<div id="post-71480-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you Frederick for your response! I checked something like Node.js TileServer GL, it seems to be what I'd need.</p>
<p>From the tutorials it seems I'd need mbtiles. Now, I checked on openmaptiles and they aren't free if you have to use them on a commercial website.</p>
<p>If I understood correctly should I need to generate mbtiles myself?</p>
</div>
<div id="comment-71480-info" class="comment-info">
<span class="comment-age">(06 Nov '19, 10:35)</span> <span class="comment-user userinfo">phts</span>
</div>
</div>
</div>
<div id="comment-tools-64406" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-64406-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="64468"></span>

<div id="answer-container-64468" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64468-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should be fine with 32GB RAM if you use the osm2pgsql "--flat-nodes" option, which puts intermediate nodes data on disk instead of storing in RAM.</p>
<p>I recently managed to load the whole of Europe on my 16 GB RAM Core i7 HQ Windows 10 laptop, allocating only 12 GB to an Oracle Virtual Box Ubuntu machine running PostgreSQL and osm2pgsql, and 2x 500GB of virtual disk space for the VM (although the initial Europe import is far smaller than that, I use the additional space for some materialized views).</p>
<p>I wrote about it here: <a href="https://forum.openstreetmap.org/viewtopic.php?id=62495">https://forum.openstreetmap.org/viewtopic.php?id=62495</a></p>
<p>Europe is somewhere between 1/3 to 1/2 of planet, so I am now pretty much 100% convinced that the same setup, if using "--flat-nodes", could also happily import planet.</p>
<p>Mind you, you do need an SSD like Frederik recommended, mine is a 2TB Samsung EVO drive. The import, with "--drop" option as well since I don't need updates, finished in just 17 hours.</p>
<p>As I recommended there as well in the post, keep your osm2pgsql command line as simple as possible, and don't use "-C" cache option or "--number_processes" parameters if you run a limited machine like I did. Leave it to osm2pgsql to figure out its optimal processing settings.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jun '18, 23:22</strong></p>
<img src="https://secure.gravatar.com/avatar/dc8a1ef54d3e25744ee52d1ad1459a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mboeringa&#39;s gravatar image" />
<p><span>mboeringa</span><br />
<span class="score" title="1542 reputation points"><span>1.5k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mboeringa has 4 accepted answers">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jun '18, 23:23</strong> </span></p>
</div>
</div>
<div id="comments-container-64468" class="comments-container">
&#10;</div>
<div id="comment-tools-64468" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64468-form-container" class="comment-form-container">
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

