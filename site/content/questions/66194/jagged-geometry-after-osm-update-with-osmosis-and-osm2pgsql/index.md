+++
type = "question"
title = "Jagged geometry after OSM update with Osmosis and Osm2pgsql"
description = '''In my previous question https://help.openstreetmap.org/questions/66092, I asked for help concerning why edited features were missing after applying a daily changefile to my OSM postgis dataset. It was determined that I used the flat nodes option upon initial planet.pbf import to postgres (--flat-nod...'''
date = "2018-10-06T18:54:00Z"
lastmod = "2018-10-13T14:40:00Z"
weight = 66194
keywords = [ "changeset", "postgresql", "osm2pgsql", "osmosis", "postgis" ]
aliases = [ "/questions/66194" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Jagged geometry after OSM update with Osmosis and Osm2pgsql](/questions/66194/jagged-geometry-after-osm-update-with-osmosis-and-osm2pgsql)

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
<span id="post-66194-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66194-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66194-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In my previous question <a href="https://help.openstreetmap.org/questions/66092,">https://help.openstreetmap.org/questions/66092,</a> I asked for help concerning why edited features were missing after applying a daily changefile to my OSM postgis dataset. It was determined that I used the flat nodes option upon initial planet.pbf import to postgres (--flat-nodes D:\nodes.cache), and this option was also required in the osm2pgsql --append command.</p>
<p>I was able to successfully append a daily changefile to my database using the flat nodes option in the append command. However, after viewing the data through a localhost Geoserver service, all of the database geometry is corrupted. Specifically, what were once smooth curves in the osm_line layer are now jagged and blocky. Polygons are incorrectly shaped as well. Rectangular building footprints are now often triangular. It looks like some sort of generalization process is happening to the nodes.</p>
<p>Graphical examples:</p>
<p>Lines - <a href="https://imgur.com/YJeDrMg">https://imgur.com/YJeDrMg</a><br />
Red is the original linework (before the append command). Thin purple is what the osm_line layer looks like after the append command.</p>
<p>Polygons - <a href="https://imgur.com/fXtftjk">https://imgur.com/fXtftjk</a><br />
Blue is the original linework (before append). Thin blue is what osm_polygon looks like after the append command.</p>
<p>Here are my commands used:</p>
<p>1) Initial planet import<br />
osm2pgsql -c -d planet -U postgres -W -H localhost -S default.style c:\osm\planet.pbf -E 4326 -C 8000 -s --flat-nodes D:\osm_updates\nodes.cache --number-processes 6</p>
<p>2) Osmosis pull changefile based on local db state id<br />
osmosis --read-replication-interval workingDirectory=d:\osm_updates --simplify-change --write-xml-change d:\osm_updates\changes.osc.gz</p>
<p>3) Osm2pgql append changefile to local postgres db<br />
osm2pgsql --append d:\osm_updates\changes.osc.gz -d planet -U postgres -S default.style -E 4326 -C 8000 --slim --flat-nodes d:\osm_updates\nodes.cache --number-processes 6</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Oct '18, 18:54</strong></p>
<img src="https://secure.gravatar.com/avatar/bbd0e184c8bbe03544aefb4e57ac5ccd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mykol404&#39;s gravatar image" />
<p><span>mykol404</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mykol404 has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-66194" class="comments-container">
<span id="66195"></span>
<div id="comment-66195" class="comment">
<div id="post-66195-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This looks interesting. Can you tell us which version of osm2pgsql and which versions of PostgreSQL/PostGIS you are using? I am not sure if it is going to be relevant but someone who wants to debug this would likely want to use the same versions. Also, are you sure that between the original import and the update, you have not updated osm2pgsql, postgres, postgis, or the GEOS library on your system? Again, this would not necessarily be a problem but it could be.</p>
</div>
<div id="comment-66195-info" class="comment-info">
<span class="comment-age">(06 Oct '18, 21:38)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="66196"></span>
<div id="comment-66196" class="comment">
<div id="post-66196-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What if you look at the actual coordinates of an affected feature through a database IDE like DBeaver? Does it indeed show simplication for e.g. for a building now displayed as triangle. In DBeaver you can easily view this information by opening the table and looking at the "way" column. You can even copy the contents to some text editor to view the full coordinate info.</p>
</div>
<div id="comment-66196-info" class="comment-info">
<span class="comment-age">(06 Oct '18, 21:57)</span> <span class="comment-user userinfo">mboeringa</span>
</div>
</div>
<span id="66197"></span>
<div id="comment-66197" class="comment">
<div id="post-66197-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I had a suspicion that there might be a flatnode precision issue with <code>-E 4326</code> which is not widely used, but I ran an import followed by an update using the same setup as you (albeit for a small area) and I saw no problems. This was using the latest osm2pgsql from github. My theory would also not explain how in your setup <em>all</em> nodes seem to be affected by an update, not only those whose coordinates have actually changed.</p>
</div>
<div id="comment-66197-info" class="comment-info">
<span class="comment-age">(06 Oct '18, 22:14)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="66224"></span>
<div id="comment-66224" class="comment">
<div id="post-66224-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am running the latest version of osm2pgsql (0.96.0).<br />
PostgreSQL version 10.4, and PostGIS 2.4.4 Not sure what the GEOS library is.</p>
</div>
<div id="comment-66224-info" class="comment-info">
<span class="comment-age">(08 Oct '18, 18:39)</span> <span class="comment-user userinfo">mykol404</span>
</div>
</div>
<span id="66225"></span>
<div id="comment-66225" class="comment">
<div id="post-66225-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Have you looked at the actual coordinates of affected features at the database level as I suggested? This is crucial. E.g. if the buildings now having become triangular in display, turn out to be unaffected in the database, than the problem is not with osm2pgsql, osmosis or your append workflow, but can solely be in the Geoserver service.</p>
</div>
<div id="comment-66225-info" class="comment-info">
<span class="comment-age">(08 Oct '18, 19:00)</span> <span class="comment-user userinfo">mboeringa</span>
</div>
</div>
</div>
<div id="comment-tools-66194" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66194-form-container" class="comment-form-container">
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

<span id="66327"></span>

<div id="answer-container-66327" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66327-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66327-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66327-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mykol404 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Good you managed to solve your issues.</p>
<p>As to DBeaver: yes, it takes a little bit of time to get used to, however, once you have used it a bit longer, there is much to like about the application. I have also found the developer very responsive and pro-active regarding bug reports and enhancement suggestions. At least it is a much better application than pgAdmin3. I haven't yet looked at pgAdmin4, so can't compare them yet.</p>
<p>As to coordinate read-out in DBeaver, simply switch to Data view and select the way column and a record, then choose "Copy" from the right-click context menu. You can subsequently paste in Notepad, as I did in this screenshot.</p>
<p><img src="https://help.openstreetmap.org/upfiles/DBeaver.jpg" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Oct '18, 14:40</strong></p>
<img src="https://secure.gravatar.com/avatar/dc8a1ef54d3e25744ee52d1ad1459a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mboeringa&#39;s gravatar image" />
<p><span>mboeringa</span><br />
<span class="score" title="1542 reputation points"><span>1.5k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mboeringa has 4 accepted answers">9%</span> </br></br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Oct '18, 14:47</strong> </span></p>
</div>
</div>
<div id="comments-container-66327" class="comments-container">
&#10;</div>
<div id="comment-tools-66327" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66327-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="66321"></span>

<div id="answer-container-66321" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66321-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66321-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66321-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks for the help everyone. It ended up being duplicate Java environment variables in Windows causing conflict for Geoserver to serve out the data. I guess it was jumping the math around when calling upon Geoserver to feed the data? Who knows.</p>
<p>I tried DBeaver, as suggested by a member. I was able to query a feature but couldn't figure out how to view it or export the coords in this utility.</p>
<p>I then came across a release note for PostgreSQL's pgAdmin4 database management console. They came out with a new version in September that allows you to directly view geometric features through the PostGIS extension, displaying the queried feature in a map window (overlaid on OSM, too!).</p>
<p>I jumped to a given jagged road or triangular building and they were fine!</p>
<p><img src="https://help.openstreetmap.org/upfiles/image_(1).png" alt="alt text" /></p>
<p>This is when we learned that Geoserver was likely the culprit. Looks like it was two conflicting Java path variables (not sure how that happened, but other people share the machine).</p>
<p>Thanks for everyone's help! Cheers</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Oct '18, 20:17</strong></p>
<img src="https://secure.gravatar.com/avatar/bbd0e184c8bbe03544aefb4e57ac5ccd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mykol404&#39;s gravatar image" />
<p><span>mykol404</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mykol404 has no accepted answers">0%</span> </br></br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Oct '18, 20:21</strong> </span></p>
</div>
</div>
<div id="comments-container-66321" class="comments-container">
&#10;</div>
<div id="comment-tools-66321" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66321-form-container" class="comment-form-container">
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

