+++
type = "question"
title = "Trying to figure out how to make a non-routable map with mkgmap that will display on my garmin device."
description = '''I am Trying to figure out how to make a non-routable map with mkgmap that will display on my Garmin Nuvi (series 50) along with a routeable map (make both files selectable in the options--&amp;gt;map--&amp;gt;info screen).  I have done this before with my state (--merge-lines not set(very, very, messy map))...'''
date = "2016-01-16T20:43:00Z"
lastmod = "2016-01-16T20:43:00Z"
weight = 47540
keywords = [ "non-routeable", "mkgmap", "garmin", "nuvi50" ]
aliases = [ "/questions/47540" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Trying to figure out how to make a non-routable map with mkgmap that will display on my garmin device.](/questions/47540/trying-to-figure-out-how-to-make-a-non-routable-map-with-mkgmap-that-will-display-on-my-garmin-device)

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
<span id="post-47540-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47540-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47540-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am Trying to figure out how to make a non-routable map with mkgmap that will display on my Garmin Nuvi (series 50) along with a routeable map (make both files selectable in the options--&gt;map--&gt;info screen).</p>
<p>I have done this before with my state (--merge-lines not set(very, very, messy map)), but the other routable map wasn't accessible. The gps would recognize the img file but only show a description.</p>
<p>Currently I am trying to make a routable map and a non-routable map. I download the pbf file from geofabrik and running it through osmconvert and osmfilter, then through mkgmap to make boundary files. Finally I run the file through splitter and mkgmap to make the final map img file. (This is all run through a shell script, I run linux.)</p>
<p>Here is the process I go through to get the map files:</p>
<pre><code>aria2c -c -imaps (maps is the text file I use to get the pbf file from geofabrik: us-west-latest.osm.pbf)
osmconvert us-west-latest.osm.pbf -o=us-west-latest.o5m
osmconvert us-west-latest.o5m --drop-author --drop-version -o=us-west-latest-version.o5m
osmfilter us-west-latest-version.o5m --keep-nodes= --keep-ways-relations=&quot;boundary=administrative =postal_code postal_code=&quot; -o=us-west-latest-version-bounds.o5m
mv *.pbf pbf/
&#10;java -Xmx2000M -cp /usr/share/java/mkgmap/mkgmap.jar uk.me.parabola.mkgmap.reader.osm.boundary.BoundaryPreprocessor us-west-latest-version-bounds.o5m usa/bounds
java -Xmx3000M -jar /usr/share/java/splitter/splitter.jar --output-dir=/home/USER/mkgmap/usa/ --geonames-file=/home/USER/mkgmap/cities15000.zip --max-nodes=500000 --output=o5m /home/USER/mkgmap/us-west-latest-version.o5m</code></pre>
<p>This is the point when mkgmap starts making the maps. This is the routeable map:</p>
<pre><code>cd usa/
java -Xmx3000M -jar /usr/share/java/mkgmap/mkgmap.jar --road-name-pois --remove-short-arcs --index --add-pois-to-areas --drive-on=right --bounds=../bounds.zip --process-exits --reduce-point-density=4 --reduce-point-density-polygon=8 --min-size-polygon=12 --max-jobs=5 --unicode --process-destination --check-roundabouts --link-pois-to-ways --location-autofill=2 --merge-lines --family-name=&quot;US-West&quot; --description=&quot;USA-West -- C:$day&quot; --gmapsupp --route --remove-ovm-work-files --housenumbers --generate-sea=multipolygon,extend-sea-sectors,floodblocker --gmapsupp  6324*.o5m</code></pre>
<p>This is the non-routeable map:</p>
<pre><code>cd NRM/
java -Xmx3000M -jar /usr/share/java/mkgmap/mkgmap.jar --max-jobs=5  --bounds=../../bounds.zip --merge-lines --gmapsupp --family-name=&quot;USA-West-NRM&quot; --description=&quot;USA West Non-Routable Map -- C:$day&quot; --remove-ovm-work-files ../6324*.o5m</code></pre>
<p>These are some of the other options I have used for mkgmap:</p>
<pre><code>--reduce-point-density=4 --reduce-point-density-polygon=8 --min-size-polygon=12 --country-name=&quot;United States&quot; --country-abbr=&quot;USA&quot; --region-name=&quot;US West&quot; --region-abbr=&quot;USW&quot; --family-id=2000 (for the routable) --family-id=1500 (for the non-routeable)</code></pre>
<p>I have made the family-id option different for each map but only one file is accessible. Any hints/help would be appreciated.</p>
<p>Update: I recently tried the IMGs on my gps. The routeable map shows up as selectable in either with both map (non-routeable unselectable) files on the gps or just the routeable file alone. I tried the non-routeable alone and it shows up as selectable, but the gps complains that there is no detailed map on the unit.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-non-routeable" rel="tag" title="see questions tagged &#39;non-routeable&#39;">non-routeable</span> <span class="post-tag tag-link-mkgmap" rel="tag" title="see questions tagged &#39;mkgmap&#39;">mkgmap</span> <span class="post-tag tag-link-garmin" rel="tag" title="see questions tagged &#39;garmin&#39;">garmin</span> <span class="post-tag tag-link-nuvi50" rel="tag" title="see questions tagged &#39;nuvi50&#39;">nuvi50</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jan '16, 20:43</strong></p>
<img src="https://secure.gravatar.com/avatar/1b5de11d3b604def817b81ff48ec06fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gckaibab&#39;s gravatar image" />
<p><span>gckaibab</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gckaibab has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Feb '16, 23:30</strong> </span></p>
</div>
</div>
<div id="comments-container-47540" class="comments-container">
&#10;</div>
<div id="comment-tools-47540" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47540-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

