+++
type = "question"
title = "OSM updates with Osmosis -&gt; Osm2Pgsql resulting in missing features"
description = '''For my project, I have successfully created a PostgreSQL database of the entire planet file using osm2pgsql. My next task was to sucessfuly update the database using daily change files through the well renowned osmosis -&amp;gt; osm2pgsql (append) process chain. To test updates, I added some hiking trai...'''
date = "2018-09-29T02:45:00Z"
lastmod = "2018-10-01T15:48:00Z"
weight = 66092
keywords = [ "diffs", "postgresql", "osm2pgsql", "osmosis", "postgis" ]
aliases = [ "/questions/66092" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [OSM updates with Osmosis -\> Osm2Pgsql resulting in missing features](/questions/66092/osm-updates-with-osmosis-osm2pgsql-resulting-in-missing-features)

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
<span id="post-66092-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66092-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66092-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For my project, I have successfully created a PostgreSQL database of the entire planet file using osm2pgsql. My next task was to sucessfuly update the database using daily change files through the well renowned osmosis -&gt; osm2pgsql (append) process chain.</p>
<p>To test updates, I added some hiking trails to the OpenStreetMap. The end nodes were auto snapped to the edges of existing roads in the forest in the OSM editing session (website). I pulled the change file with osmosis using the sequence id, per standard, and used the osm2pgsql --append command, as outline by numerous help sites and forums. My new trail came through, and was visually proven using a Geoserver platform to serve the postgres data.</p>
<p>Here is the problem...any existing road that was modified was absent in the osm_line data after the update. The two roads to which either end of the newly digitized trail were gone. They are still in the map, as confirmed by a Geofabrik download of the local area, as well as by simply going to the OSM website. Additionally, an existing trail that was incorrect and I moved a few nodes within is also gone. It seems my command (either Osmosis or Osm2pgsql append) is wrong, and is only applying new features and knocking out anything that changed.</p>
<p>Hoping we have some OSM gurus that can help.</p>
<p>My two commands are as follows:</p>
<p>1) osmosis --read-replication-interval workingDirectory=D:\osm_updates --simplify-change --write-xml-change D:\osm_updates\changes.osc.gz</p>
<p>2) osm2pgsql --append -d planet -U postgres -S default.style -E 4326 -C 8000 --slim --number-processes 6 d:\osm_updates\changes.osc.gz</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-diffs" rel="tag" title="see questions tagged &#39;diffs&#39;">diffs</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Sep '18, 02:45</strong></p>
<img src="https://secure.gravatar.com/avatar/bbd0e184c8bbe03544aefb4e57ac5ccd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mykol404&#39;s gravatar image" />
<p><span>mykol404</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mykol404 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Sep '18, 02:46</strong> </span></p>
</div>
</div>
<div id="comments-container-66092" class="comments-container">
<span id="66098"></span>
<div id="comment-66098" class="comment">
<div id="post-66098-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What command line did you use to import the initial data with osm2pgsql?</p>
</div>
<div id="comment-66098-info" class="comment-info">
<span class="comment-age">(29 Sep '18, 21:12)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="66114"></span>
<div id="comment-66114" class="comment">
<div id="post-66114-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>d:\osm2pgsql-bin&gt;osm2pgsql -c -d planet -U postgres -W -H localhost -S default.style c:\osm\planet.pbf -E 4326 -C 8000 -s --flat-nodes D:\nodes.cache --number-processes 6</p>
</div>
<div id="comment-66114-info" class="comment-info">
<span class="comment-age">(01 Oct '18, 15:30)</span> <span class="comment-user userinfo">mykol404</span>
</div>
</div>
</div>
<div id="comment-tools-66092" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66092-form-container" class="comment-form-container">
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

<span id="66115"></span>

<div id="answer-container-66115" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66115-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66115-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-66115-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mykol404 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to be careful to use the same options for update that you used for the import. In your case, you used a flat node file (<code>--flat-nodes</code> option) for the import. You need to keep this file around and use the option for updates as well.</p>
<p>The file contains all the coordinates of all points in your planets. OSC update files only contain the coordinates of points that have actually been changed. If a way is modified then its coordinates are not in the OSC file. They need to be looked up from the import.</p>
<p>If you still have the flatnode file, nothing is lost yet. Simply apply your change files again in chronological order, this time with the <code>--flat-nodes</code> option and the lost ways will reappear in your database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Oct '18, 15:48</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-66115" class="comments-container">
&#10;</div>
<div id="comment-tools-66115" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66115-form-container" class="comment-form-container">
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

