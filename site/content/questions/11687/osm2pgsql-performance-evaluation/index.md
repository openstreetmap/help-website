+++
type = "question"
title = "osm2pgsql performance evaluation"
description = '''Hi, I just got a dedicated server for our planet osm2pgsql database. It has 32 GB RAM, two Opteron processors (6212) (16 cores in total), a software RAID1 for the system and a software RAID0 for the database. The database disks are 10k Raptor drives, so nothing too slow. I tested an import of the pl...'''
date = "2012-04-02T09:04:00Z"
lastmod = "2014-12-03T02:55:00Z"
weight = 11687
keywords = [ "planet", "import", "osm2pgsql", "performance" ]
aliases = [ "/questions/11687" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql performance evaluation](/questions/11687/osm2pgsql-performance-evaluation)

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
<span id="post-11687-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11687-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-11687-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I just got a dedicated server for our planet osm2pgsql database. It has 32 GB RAM, two Opteron processors (6212) (16 cores in total), a software RAID1 for the system and a software RAID0 for the database. The database disks are 10k Raptor drives, so nothing too slow. I tested an import of the planet during the weekend and I think the performance of the import could be better, especially when reviewing Frederiks <a href="https://wiki.openstreetmap.org/wiki/SotM_2010_session:Tuning_the_Mapnik_Rendering_Chain">SotM presentation</a> in 2010 where the import is done within some hours (regard the slim planet import whith R0, -C8000).</p>
<p>The planet.osm.bz2 is on the RAID1, the import command was:</p>
<blockquote>
<p>osm2pgsql -d osm -s -S /home/brfr/default.style -C 16000 -U postgres -H localhost -k --number-processes 16 planet-latest.osm.bz2</p>
</blockquote>
<p>so actually plenty of cache available. During the process I observed that the node processing speed never got over 80k/s which is somewhat low I think for that machine. Using top I watched the osm2pgsql process and it was always at 100%. In order to find out if there's a disk speed limit I used iostat and the values I saw let me assume that the drives were never near to their limits. So I tend to believe that I run into a CPU limit while processing the XML. Unfortunately the import process was interrupted. There were too many connections on the database (the limit was set too low by the pgtune tool). So I don't have any final numbers, just the XML processing stats below. So finally my question. Can someone confirm that Opterons suck at XML processing? Does someone have experience with Opterons and a osmpgsql import? What's your node processing speed?</p>
<p>The <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server/">switch2osm</a> site has a quote which shows a nearly tripled speed (200k/s), that's mainly why I ask here for experience values from other planet "importers" ...</p>
<p>My stats for the processing:</p>
<blockquote>
<p>Node stats: total(1403664658), max(1684121047) in 18315s<br />
Way stats: total(129971557), max(156125599) in 14955s<br />
Relation stats: total(1342628), max(2092829) in 18429s</p>
</blockquote>
<p>Many thanks</p>
<p>Frank</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Apr '12, 09:04</strong></p>
<img src="https://secure.gravatar.com/avatar/30b87850d86c99d1c4f1f72c9abaeb52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frabron&#39;s gravatar image" />
<p><span>frabron</span><br />
<span class="score" title="361 reputation points">361</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frabron has 2 accepted answers">16%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Apr '12, 09:06</strong> </span></p>
</div>
</div>
<div id="comments-container-11687" class="comments-container">
<span id="11692"></span>
<div id="comment-11692" class="comment">
<div id="post-11692-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks all, I am downloading the planet.pbf and will post the results probably on wednesday and also in the wiki. Right now I want to test if my Intel (i4) at home performs better than the Opteron at work on processing nodes</p>
</div>
<div id="comment-11692-info" class="comment-info">
<span class="comment-age">(02 Apr '12, 20:03)</span> <span class="comment-user userinfo">frabron</span>
</div>
</div>
<span id="11696"></span>
<div id="comment-11696" class="comment">
<div id="post-11696-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, I downloaded great-britain.osm.bz2 and the node processing speed definitely faster than the Opterons speed. Right now it processes nodes with 93,6k/s and the ways between 10 and 11k/s. My testing setup is simple, I use a Virtualbox with the latest Ubuntu server release and osm2pgsql from source. The host is a i4 2400 Intel processor and 8GB RAM with 4GB given to the machine. Osm2pgsl runs with -C 2048 ...</p>
</div>
<div id="comment-11696-info" class="comment-info">
<span class="comment-age">(02 Apr '12, 20:59)</span> <span class="comment-user userinfo">frabron</span>
</div>
</div>
<span id="11718"></span>
<div id="comment-11718" class="comment">
<div id="post-11718-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Today I started a new import with the latest planet.osm.pbf. Node import speed is at approx. 140k/s, already much better than the XML import. One thing I notice though, now the postgres process is at 100%. It is the</p>
<blockquote>
<pre><code>      query_start          | procpid | waiting |           substring</code></pre>
<p>-------------------------------+---------+---------+-------------------------------</p>
<p>2012-04-04 10:44:12.982371+02 | 63618 | f | COPY planet_osm_nodes FROM ST</p>
</blockquote>
<p>action that now is limiting a faster import. Disks are nowhere at their limits and osm2pgsql is between 30% - 60% CPU usage</p>
</div>
<div id="comment-11718-info" class="comment-info">
<span class="comment-age">(04 Apr '12, 10:48)</span> <span class="comment-user userinfo">frabron</span>
</div>
</div>
<span id="11858"></span>
<div id="comment-11858" class="comment">
<div id="post-11858-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>FYI: I added my server and results (~50hrs) to the <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql/benchmarks">benchmark</a> table ...</p>
</div>
<div id="comment-11858-info" class="comment-info">
<span class="comment-age">(10 Apr '12, 08:14)</span> <span class="comment-user userinfo">frabron</span>
</div>
</div>
<span id="39014"></span>
<div id="comment-39014" class="comment">
<div id="post-39014-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Dear frabron, I'm so glad you have solved you problem. And now I run into the same qusetion like yours, so your advice is using the .pbf format data to import instead of the .bz2 ? Do you have some method to accelerate the importing speed of the bz2 file? Does the command " --number-processes 16" in you command line count a lot?</p>
<p>With many thanks!! David</p>
</div>
<div id="comment-39014-info" class="comment-info">
<span class="comment-age">(03 Dec '14, 02:55)</span> <span class="comment-user userinfo">studiousdavid</span>
</div>
</div>
</div>
<div id="comment-tools-11687" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11687-form-container" class="comment-form-container">
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

<span id="11689"></span>

<div id="answer-container-11689" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11689-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11689-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-11689-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First of all, forget my performance figures, they are two years old and that's a very long time in OSM!</p>
<p>You can use the .pbf planet instead of the .osm.bz2, this will save the time used for bz2 decompression and XML parsing. However, I would expect over 80% of processing time to be spent building geometries and indexes, so even if your system should be slow while reading the file, that should not impact overall performance too much.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Apr '12, 09:27</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-11689" class="comments-container">
&#10;</div>
<div id="comment-tools-11689" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11689-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11691"></span>

<div id="answer-container-11691" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11691-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11691-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-11691-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You might check this wiki page collecting several osm2pgsql performance measurements (and add yours):</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql/benchmarks">https://wiki.openstreetmap.org/wiki/Osm2pgsql/benchmarks</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Apr '12, 12:21</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Apr '12, 22:49</strong> </span></p>
</div>
</div>
<div id="comments-container-11691" class="comments-container">
&#10;</div>
<div id="comment-tools-11691" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11691-form-container" class="comment-form-container">
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

