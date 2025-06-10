+++
type = "question"
title = "osm2pgsql --append is removing features (when it shouldn&#x27;t)"
description = '''Hello, I created an issue at osm2pgsql&#x27;s GitHub but it&#x27;s probably me not correctly using the tools, so I&#x27;ll ask here as well. I&#x27;m setting up a renderd / Mapnik tile server that I want to keep synced with osmosis / osm2pgsql hourly. Everything seems to work (outputs of osmosis &amp;amp; osm2pgsql looks f...'''
date = "2019-07-10T19:55:00Z"
lastmod = "2019-11-16T15:33:00Z"
weight = 69977
keywords = [ "deleted", "osm2pgsql", "osmosis", "sync" ]
aliases = [ "/questions/69977" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql --append is removing features (when it shouldn't)](/questions/69977/osm2pgsql-append-is-removing-features-when-it-shouldnt)

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
<span id="post-69977-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69977-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69977-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I created an issue at osm2pgsql's GitHub but it's probably me not correctly using the tools, so I'll ask here as well.</p>
<p>I'm setting up a renderd / Mapnik tile server that I want to keep synced with osmosis / osm2pgsql hourly. Everything seems to work (outputs of osmosis &amp; osm2pgsql looks fine, osmosis does download the changes, and osm2pgsql does something to the database). But I have two problems:</p>
<ul>
<li>if I add / edit a feature on OSM iD, my local database does not get the update (openstreetmap.org did get the update)</li>
<li>sometimes features are removed (for instance yesterday I lost the USA boundaries polygon, and today France &amp; Spain boundaries are gone as well). They are removed from the DB, it's not a stylesheet problem</li>
</ul>
<p>What could be wrong?</p>
<p>Here's the complete set of command I'm using:</p>
<p>1°) Database import</p>
<pre><code>osm2pgsql \
    -d osm \
    --create --slim -G --hstore \
    -C 20000 \
    --number-processes 1 \
    --tag-transform-script ~/src/map-styles/openstreetmap-carto/openstreetmap-carto.lua \
    --style ~/src/map-styles/openstreetmap-carto/openstreetmap-carto.style \
    --flat-nodes /ssd/flat-nodes/osm.cache \
    &lt;path/to/planet-osm.pbf&gt;</code></pre>
<p>The process took ~24h, and created a 719GB database (with last week's planet PBF).</p>
<p>2°) Prepare sync (only once)</p>
<pre><code># Set the location
WORKOSM_DIR=~/osm-sync
&#10;# Get the PBF file timestamp
TIMESTAMP=$(osmium fileinfo &lt;path/to/planet-osm.pbf&gt; | grep osmosis_replication_timestamp= | cut -c 35-54)
&#10;YEAR=$(echo $TIMESTAMP | cut -c 1-4)
MONTH=$(echo $TIMESTAMP | cut -c 6-7)
DAY=$(echo $TIMESTAMP | cut -c 9-10)
HOUR=$(echo $TIMESTAMP | cut -c 12-13)
&#10;# Download the initial state.txt
wget &quot;https://replicate-sequences.osm.mazdermind.de/?Y=$YEAR&amp;m=$MONTH&amp;d=$DAY&amp;H=$HOUR&amp;i=00&amp;s=00&amp;stream=hour&quot; -O $WORKOSM_DIR/state.txt
&#10;# Create the config file
rm -f $WORKOSM_DIR/configuration.txt
osmosis --read-replication-interval-init workingDirectory=$WORKOSM_DIR
&#10;# Update the config file
sed -i &#39;s!http:!https:!&#39; $WORKOSM_DIR/configuration.txt sed -i &#39;s!minute!hour!&#39; $WORKOSM_DIR/configuration.txt</code></pre>
<p>3°) Continue to sync (this is called every hour with a CRON task)</p>
<pre><code># Set some variables
WORKOSM_DIR=~/osm-sync
OSM_CARTO_DIR=&lt;path-to-openstreetmap-carto&gt;
EXPIRE_FILE_NAME=expire-list.txt
&#10;# Download changes
osmosis \
    --read-replication-interval workingDirectory=$WORKOSM_DIR \
    --simplify-change \
    --write-xml-change $WORKOSM_DIR/tmp/osmChange.xml
&#10;# Apply the changes
osm2pgsql \
    --database gis \
    --append --slim --multi-geometry --hstore \
    --cache 3000 \
    --tag-transform-script $OSM_CARTO_DIR/openstreetmap-carto.lua \
    --style $OSM_CARTO_DIR/openstreetmap-carto.style \
    --flat-nodes /ssd/flat-nodes/osm.cache \
    --expire-tiles 10-20 \
    --expire-output $WORKOSM_DIR/tmp/$EXPIRE_FILE_NAME \
    --input-reader xml \
    $WORKOSM_DIR/tmp/osmChange.xml
&#10;# Expire tiles in [10-15]
render_expired \
    --tile-dir /hdd/tile-cache/mod_tile \
    --min-zoom=10 \
    --max-zoom=15 \
    --touch-from=10 \
    --socket /var/run/renderd.sock &lt; $WORKOSM_DIR/tmp/$EXPIRE_FILE_NAME
&#10;# Delete tiles in [16-20]
render_expired \
    --tile-dir /hdd/tile-cache/mod_tile \
    --min-zoom=16 \
    --max-zoom=20 \
    --delete-from=16 \
    --socket /var/run/renderd.sock &lt; $WORKOSM_DIR/tmp/$EXPIRE_FILE_NAME</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-deleted" rel="tag" title="see questions tagged &#39;deleted&#39;">deleted</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-sync" rel="tag" title="see questions tagged &#39;sync&#39;">sync</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jul '19, 19:55</strong></p>
<img src="https://secure.gravatar.com/avatar/2a936bbff59e8151128d083b194a0fd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tim%20Autin&#39;s gravatar image" />
<p><span>Tim Autin</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tim Autin has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jul '19, 13:18</strong> </span></p>
</div>
</div>
<div id="comments-container-69977" class="comments-container">
<span id="70047"></span>
<div id="comment-70047" class="comment">
<div id="post-70047-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If it helps you to compare with one that works, I run <a href="https://github.com/SomeoneElseOSM/mod_tile/blob/zoom/openstreetmap-tiles-update-expire">https://github.com/SomeoneElseOSM/mod_tile/blob/zoom/openstreetmap-tiles-update-expire</a> every 5 minutes and I haven't seen the problem that you're seeing.</p>
</div>
<div id="comment-70047-info" class="comment-info">
<span class="comment-age">(13 Jul '19, 15:59)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="70049"></span>
<div id="comment-70049" class="comment">
<div id="post-70049-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I already wrote my script based on this one, they are very similar (osmosis + osm2pgsql and then render_expired). It's even worse, my planet_osm_nodes table is now empty -_- ... What did you use to get the PBF file date, to know when to start?</p>
</div>
<div id="comment-70049-info" class="comment-info">
<span class="comment-age">(13 Jul '19, 18:59)</span> <span class="comment-user userinfo">Tim Autin</span>
</div>
</div>
<span id="70050"></span>
<div id="comment-70050" class="comment">
<div id="post-70050-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you mean "before applying any updates" then it will have been downloaded from Geofabrik. The database load script is actually <a href="https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/master/update_render.sh">https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/master/update_render.sh</a> .</p>
</div>
<div id="comment-70050-info" class="comment-info">
<span class="comment-age">(13 Jul '19, 19:59)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="70052"></span>
<div id="comment-70052" class="comment">
<div id="post-70052-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I meant how did you get timestamp to feed the openstreetmap-tiles-update-expire script the first time, to init osmosis with --read-replication-interval-init?</p>
</div>
<div id="comment-70052-info" class="comment-info">
<span class="comment-age">(13 Jul '19, 20:05)</span> <span class="comment-user userinfo">Tim Autin</span>
</div>
</div>
<span id="70053"></span>
<div id="comment-70053" class="comment">
<div id="post-70053-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The timestamp is scraped from the page: <a href="https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/master/update_render.sh#L141">https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/master/update_render.sh#L141</a> .</p>
</div>
<div id="comment-70053-info" class="comment-info">
<span class="comment-age">(13 Jul '19, 20:07)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="70054"></span>
<div id="comment-70054" class="comment not_top_scorer">
<div id="post-70054-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh I see thanks. I'm downloading world data from <a href="https://planet.openstreetmap.org">https://planet.openstreetmap.org</a>, where the timestamp is not given. I'm using "osmium fileinfo $1 | grep osmosis_replication_timestamp=" which seems accurate. Appart from that I can't see what could go wrong :/</p>
</div>
<div id="comment-70054-info" class="comment-info">
<span class="comment-age">(13 Jul '19, 20:56)</span> <span class="comment-user userinfo">Tim Autin</span>
</div>
</div>
<span id="70059"></span>
<div id="comment-70059" class="comment not_top_scorer">
<div id="post-70059-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Re, the problem is still occuring with your script. I have the same behavior on 3 different servers. I'm using version 0.96.0 of osm2pgsql, what's yours?</p>
</div>
<div id="comment-70059-info" class="comment-info">
<span class="comment-age">(14 Jul '19, 10:51)</span> <span class="comment-user userinfo">Tim Autin</span>
</div>
</div>
<span id="70060"></span>
<div id="comment-70060" class="comment not_top_scorer">
<div id="post-70060-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The same - "osm2pgsql version 0.96.0 (64 bit id space)", built locally from <span>git://github.com/openstreetmap/osm2pgsql.git</span> I believe.</p>
<p>(for completeness) the map is <a href="https://map.atownsend.org.uk/">here</a> and the update progress is <a href="https://map.atownsend.org.uk/munin/renderd-day.html">here</a>.</p>
</div>
<div id="comment-70060-info" class="comment-info">
<span class="comment-age">(14 Jul '19, 12:41)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="70061"></span>
<div id="comment-70061" class="comment not_top_scorer">
<div id="post-70061-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. I re-built osm2pgsql to get the latest updates of the master branch, ran an apt upgrade, and I'm (again) re-creating my planet db to retry. You created your data with line 205 of your update_render.sh, right? Mine is very similar, but I'm using --hstore and --flat-nodes (without this I get an OOME, despite my 64GB of RAM). Do you know if one of these option could cause the bug?</p>
</div>
<div id="comment-70061-info" class="comment-info">
<span class="comment-age">(14 Jul '19, 12:59)</span> <span class="comment-user userinfo">Tim Autin</span>
</div>
</div>
<span id="70062"></span>
<div id="comment-70062" class="comment not_top_scorer">
<div id="post-70062-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes - <a href="https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/master/update_render.sh#L204">https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/master/update_render.sh#L204</a> creates the database, and then appends the two .osm files that contain the map legend. My guess is that "--flat-nodes" is causing the effect that you're seeing. Maybe try with a smaller file (that won't run out of memory) without "--flat-nodes"?</p>
</div>
<div id="comment-70062-info" class="comment-info">
<span class="comment-age">(14 Jul '19, 13:26)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="70063"></span>
<div id="comment-70063" class="comment not_top_scorer">
<div id="post-70063-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The problem with a smaller file is that it's harder to see if features have disappeared: it's easy to spot a missing country, less to see a missing restaurant. I'm trying a planet import without --flat-nodes but with --number-processes 1, I never tried that, and it could work.</p>
</div>
<div id="comment-70063-info" class="comment-info">
<span class="comment-age">(14 Jul '19, 13:45)</span> <span class="comment-user userinfo">Tim Autin</span>
</div>
</div>
<span id="71623"></span>
<div id="comment-71623" class="comment not_top_scorer">
<div id="post-71623-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Tim, did you solve this while using a more recent osm2pgsql version?</p>
<p>I'm actually seeing the same behavior with osm2pgsql 0.96 and flat-nodes option - at least regarding your second point of (multi-)polygons getting lost while I can't confirm the first one (new nodes not being added). And I can add the oddity of running servers in parallel - same stack - same updates but polygon losts are different between the systems ...</p>
</div>
<div id="comment-71623-info" class="comment-info">
<span class="comment-age">(14 Nov '19, 01:01)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="71666"></span>
<div id="comment-71666" class="comment not_top_scorer">
<div id="post-71666-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Problem is still there for me, I ended up recreating the whole database roughly every 3 monthes, and I redirect my users to the backup server during the process. A bit cubersome, but at least it works.</p>
</div>
<div id="comment-71666-info" class="comment-info">
<span class="comment-age">(16 Nov '19, 12:14)</span> <span class="comment-user userinfo">Tim Autin</span>
</div>
</div>
<span id="71675"></span>
<div id="comment-71675" class="comment not_top_scorer">
<div id="post-71675-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Tim,</p>
<p>thanks for answering.</p>
<p>So I'll try to investigate further what's going one there and report back here.</p>
</div>
<div id="comment-71675-info" class="comment-info">
<span class="comment-age">(16 Nov '19, 15:33)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
</div>
<div id="comment-tools-69977" class="comment-tools">
<span class="comments-showing"> showing 5 of 14 </span> <a href="#" class="show-all-comments-link">show 9 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-69977-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

