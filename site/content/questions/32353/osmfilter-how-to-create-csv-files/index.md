+++
type = "question"
title = "osmfilter : how to create csv-files"
description = '''hello dear OpenStreetmap-experts on opensuse 13.1 i try to do some gis-works with a large file: france-latest.osm.bz2 which i gathered from here: http://download.geofabrik.de/europe.html :: what do i do with that file france-latest.osm.bz2 bzcat france-latest.osm.bz2  what is aimed? i want to extrac...'''
date = "2014-04-13T22:45:00Z"
lastmod = "2014-04-13T22:45:00Z"
weight = 32353
keywords = [ "postgis", "linux" ]
aliases = [ "/questions/32353" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [osmfilter : how to create csv-files](/questions/32353/osmfilter-how-to-create-csv-files)

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
<span id="post-32353-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32353-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32353-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hello dear OpenStreetmap-experts</p>
<p>on opensuse 13.1 i try to do some gis-works with a large file: france-latest.osm.bz2 which i gathered from here: <a href="http://download.geofabrik.de/europe.html">http://download.geofabrik.de/europe.html</a> :: what do i do with that file france-latest.osm.bz2</p>
<pre><code>bzcat france-latest.osm.bz2</code></pre>
<p>what is aimed? i want to extract all things that belong to the POI restaurant which is</p>
<pre><code>long lat
name
adress
etc - etx.</code></pre>
<p>i have the following things up and running:</p>
<pre><code>package perl-XML-Twig and run xml_split</code></pre>
<p>with a command available on openSUSE to split xml files named xml_split (it is part of the package perl-XML-Twig) Now i used to run the following command (I hope we have enough hard disk space since the output is roughly 20GB).</p>
<pre><code>bzcat france.osm.bz2 | xml_split -s 100M -b france -n 3 -</code></pre>
<p>but . i well i think i will go and extract (an initially small) geographical area using osmosis, then i will go to look at osmfilter to extract the data (possibly having a look at osmconvert to convert the data into a format that osmfilter can understand). Also perhaps consider osmium.</p>
<p>well - i need to run osmosis and osmfilter besides this i need to have osmconvert</p>
<p>are these packages available for opensuse</p>
<p>btw: i did it - see here</p>
<pre><code>linux-70ce:/home/martin # wget http://bretth.dev.openstreetmap.org/osmosis-build/osmosis-latest.tgz
--2014-04-13 09:54:23--  http://bretth.dev.openstreetmap.org/osmosis-build/osmosis-latest.tgz
Auflösen des Hostnamen »bretth.dev.openstreetmap.org (bretth.dev.openstreetmap.org)«... 128.40.168.103
Verbindungsaufbau zu bretth.dev.openstreetmap.org (bretth.dev.openstreetmap.org)|128.40.168.103|:80... verbunden.
HTTP-Anforderung gesendet, warte auf Antwort... 200 OK
Länge: 9079737 (8,7M) [application/x-gzip]
In »»osmosis-latest.tgz.1«« speichern.
&#10;100%[==========================================================================================================================================&gt;] 9.079.737   1,41MB/s   in 6,3s
&#10;2014-04-13 09:54:29 (1,38 MB/s) - »»osmosis-latest.tgz.1«« gespeichert [9079737/9079737]
&#10;linux-70ce:/home/martin # mkdir osmosis
linux-70ce:/home/martin # cd osmosis
&#10;linux-70ce:/home/martin # mkdir osmosis
linux-70ce:/home/martin # cd osmosis</code></pre>
<p><strong>btw:</strong> regarding the two other toools osmconvert osmfilter - i have had a loook at the corresponding websites. should i have to install it like it is written on here :</p>
<pre><code>Download and build in one run:   wget -O - http://m.m.i24.cc/osmconvert.c | cc -x c - -lz -O3 -o osmconvert
Download and build in one run:   wget -O - http://m.m.i24.cc/osmfilter.c |cc -x c - -O3 -o osmfilter</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Apr '14, 22:45</strong></p>
<img src="https://secure.gravatar.com/avatar/bf4d2d8660e82c4a7387b7d2a8a8cfcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="say_hello_to_the_world&#39;s gravatar image" />
<p><span>say_hello_to...</span><br />
<span class="score" title="19 reputation points">19</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="say_hello_to_the_world has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-32353" class="comments-container">
&#10;</div>
<div id="comment-tools-32353" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32353-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

