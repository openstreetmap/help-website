+++
type = "question"
title = "Pending Ways, How long should it take?"
description = '''I have seen references to this all over the internet, but I am just trying to figure out how long this may take if it works, and if not, then what setting to go with. The Server I am setting up is just to display some offline maps, nothing super fancy or critical, so I tried to throw OSM on an old s...'''
date = "2018-07-29T09:36:00Z"
lastmod = "2018-07-29T17:25:00Z"
weight = 65000
keywords = [ "ways", "osm2pgsql", "pending" ]
aliases = [ "/questions/65000" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Pending Ways, How long should it take?](/questions/65000/pending-ways-how-long-should-it-take)

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
<span id="post-65000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65000-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have seen references to this all over the internet, but I am just trying to figure out how long this may take if it works, and if not, then what setting to go with. The Server I am setting up is just to display some offline maps, nothing super fancy or critical, so I tried to throw OSM on an old server I had lying around. everything went smooth until Time to import data into the database, and after around 3 days the Process killed itself. I tried changing a few specs in the command but it once again failed after a few days, so I decided to dig out a pretty decent workstation running a 4 core Xenon processor and 16Gb of RAM. I am very new to OSM and I am following the tutorial on teh OSM site to get this up and running, so I used the basic command that was given on the tutorial <code>osm2pgsql -d gis --create --slim -G --hstore --tag-transform-script ~/src/openstreetmap-carto/openstreetmap-carto.lua -C 2500 --number-processes 1 -S ~/src/openstreetmap-carto/openstreetmap-carto.style ~/data/north-america-latest.osm.pbfcode</code> just edited for the North america file that I downloaded. if this fails this time, should I modify the memory amount to more than 2500, and change the processes to more than 1, or do I have a good chance that this will wrap up without issues in a day or 2?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-pending" rel="tag" title="see questions tagged &#39;pending&#39;">pending</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jul '18, 09:36</strong></p>
<img src="https://secure.gravatar.com/avatar/231ce5a82292640ac0faa68994879c84?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KD7VEA&#39;s gravatar image" />
<p><span>KD7VEA</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KD7VEA has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jul '18, 09:47</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-65000" class="comments-container">
<span id="65001"></span>
<div id="comment-65001" class="comment">
<div id="post-65001-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>North America's quite large - I'd suggest testing on something small first (a small US state, perhaps). With 16Gb memory you can probably allocate more cache. With 4 cores you can probably allocate more processes.</p>
<p>How long your current import will take will depend on a number of other issues, such as speed of disk.</p>
</div>
<div id="comment-65001-info" class="comment-info">
<span class="comment-age">(29 Jul '18, 09:46)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="65008"></span>
<div id="comment-65008" class="comment">
<div id="post-65008-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I did test with a small file each time that I have done this, just to be sure everything was running correctly, and it did work. So for now while I assume it is still running, I assume all I can really do is wait and see what happens. Here is the last block of info I have since loading the data to the database.</p>
<p>Reading in file: /home/k7msh/data/north-america-latest.osm.pbf Using PBF parser. Processing: Node(995524k 190.9k/s) Way(75654k 0.89k/s) Relation(762060 17.39/s) parse time: 134134s Node stats: total(995524996), max(5787934253) in 5216s Way stats: total(75654254), max(611291042) in 85089s Relation stats: total(762074), max(8479578) in 43829s Committing transaction for planet_osm_point Committing transaction for planet_osm_line Committing transaction for planet_osm_polygon Committing transaction for planet_osm_roads Setting up table: planet_osm_nodes Setting up table: planet_osm_ways Setting up table: planet_osm_rels Using lua based tag processing pipeline with script /home/k7msh/src/openstreetmap-carto/openstreetmap-carto.lua</p>
<p>Going over pending ways... 36685077 ways are pending</p>
<p>Using 1 helper-processes</p>
</div>
<div id="comment-65008-info" class="comment-info">
<span class="comment-age">(29 Jul '18, 17:25)</span> <span class="comment-user userinfo">KD7VEA</span>
</div>
</div>
</div>
<div id="comment-tools-65000" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65000-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

