+++
type = "question"
title = "customise osmosis database structure - add columns for ALL tags"
description = '''My project is to build a series of map layers showing developments over an extended period, bronze age to 19th century with primary features of the present, covering the area of Cornwall, Devon, Dorset &amp;amp; Somerset. I am trying to import sections of OSM into a postgis database using osm2postgresql...'''
date = "2011-10-16T06:30:00Z"
lastmod = "2011-10-17T08:13:00Z"
weight = 8466
keywords = [ "postgis", "osmosis" ]
aliases = [ "/questions/8466" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [customise osmosis database structure - add columns for ALL tags](/questions/8466/customise-osmosis-database-structure-add-columns-for-all-tags)

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
<span id="post-8466-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8466-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8466-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My project is to build a series of map layers showing developments over an extended period, bronze age to 19th century with primary features of the present, covering the area of Cornwall, Devon, Dorset &amp; Somerset.</p>
<p>I am trying to import sections of OSM into a postgis database using osm2postgresql-04.sh with osmosis but am finding a combination of the default schema and 'free spirited' tagging is resulting in the loss of significant information. (e.g. created_by, source, note, comment, etc. tags causing the tags field in the db to be truncated before relevant tags are reached).</p>
<p>4 months of manually hacking at the data has failed to solve the problem and convinced my the solution is to be able to configure the db to have columns for EVERY tag in the data and the use sql queries to pick what I need.</p>
<p>The problem is I have no knowledge of postgres and can just barely get by with mysql.</p>
<p>my present procedure is using osm2postgresql-04.sh to load the data, Qgis to convert it to MapInfo files for editing.</p>
<p>Can SKS point me to a primer or other help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Oct '11, 06:30</strong></p>
<img src="https://secure.gravatar.com/avatar/e34a746be3d2d692055b59c8d0c11848?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sparrowhawk&#39;s gravatar image" />
<p><span>sparrowhawk</span><br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sparrowhawk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8466" class="comments-container">
&#10;</div>
<div id="comment-tools-8466" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8466-form-container" class="comment-form-container">
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

<span id="8468"></span>

<div id="answer-container-8468" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8468-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-8468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You do not want columns for ALL tags as this would mean tens of thousands of columns.</p>
<p>There are various ways of importing OSM data into a database and which one you choose depends largely on what you want to do with the database. What you describe above - having all tags in one text field - is something nobody does nowadays and I am intrigued that you should try that at all; you must have been following a 4 year old README or so.</p>
<p>Basically, we have importers geared towards rendering the data - these will tend to drop everything not needed for map drawing, and will make sure to create "geometry" objects for quick access. Having a "geometry" object e.g. for a road in the database means that you can quickly access the road as a whole, and have the database answer questions like "does road A intersect with forest B" or so, without having to first read and process all the nodes making up the road. Examples of such importers are the widely-used osm2pgsql or the newer Imposm. With both you have considerable control over which tags get imported into their own columns, by way of a config file. osm2pgsql will always create exactly four database tables holding your geometries, whereas with Imposm this is configurable.</p>
<p>The other kind of importers we have is geared towards further processing of the data and these will usually make an effort to presever <em>all</em> information about an OSM object, including all tags and meta data like who created it when, and can optionally also preserve history, i.e. they can keep older versions of the same object. Osmosis is the prime example of such importers.</p>
<p>Both areas are not 100% distinct. osm2pgsql for example allows you, by way of extra commandline switches, to store all tags - not only those for which a separate column is created - in a so-called "hstore" column. This is a feature of PostgreSQL where you can have an unlimited number of key-value pairs in one database column. osm2pgsql also has a feature where you can request some metadata (user id, date of last modification) to be recorded in a separate column. On the other hand, Osmosis offers two distinct database schemas, one being the "API DB" schema where all tags and all metadata are stored (tags have their own database tables with one row per tag nowadays - not the old "all tags in one text field" scheme anymore!), and the other being the "Snapshot" schema which optionally includes built geometries.</p>
<p>Additionally, there are specialist importers like osm2pgrouting that import data optimized for specialist purposes.</p>
<p>If you plan to edit in Mapinfo, you could also use osm2shp or osmjs to convert OSM data to shape files and edit those, or you could use the OSM plugin for QGis to load OSM data directly into QGis.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Oct '11, 10:41</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-8468" class="comments-container">
<span id="8473"></span>
<div id="comment-8473" class="comment">
<div id="post-8473-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In addition to Frederick's excelent pointers, I'd advise you to browse the postres docs (<a href="http://www.postgresql.org/docs/current/static/)">http://www.postgresql.org/docs/current/static/)</a> and postgis docs (<a href="http://www.postgis.org/docs/)">http://www.postgis.org/docs/)</a> they are very high quality and should help you understand what can be done with th db.</p>
</div>
<div id="comment-8473-info" class="comment-info">
<span class="comment-age">(16 Oct '11, 14:10)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-8468" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8468-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8477"></span>

<div id="answer-container-8477" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8477-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8477-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8477-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks for your response, you have given me a lot to digest. The process is going to be far more complex than I had thought</p>
<blockquote>
<p>You do not want columns for ALL tags as this would mean tens of thousands of columns.</p>
</blockquote>
<p>Not in the finished product but I need to simplify the extraction and sorting of significant objects.</p>
<p>In a perfect world, there would be a clearly defined hiarachy of tags and no one would make typos but we are stuck in the real world, full of human fraility and creativity.</p>
<p>The area I am working with contains 60,000 unique tag key = value sets covering about 300 tag keys that can be reduced to about 80-100 keys by merging various ways of saying the same thing.</p>
<p>I have been using grep to find the key = value sets in the .osm file then using awk to delete the unwanted tags but this takes 3 days for the grep/awk and another 2 -3 days to manually cut/paste the unprocessed tags into separate columns just for a mapinfo table of highway = primary, trunk, secondary, &amp; tertiary</p>
<blockquote>
<p>What you describe above - having all tags in one text field - is something nobody does nowadays and I am intrigued that you should try that at all; you must have been following a 4 year old README or so.</p>
</blockquote>
<p>This is done by both osm2postgresql-04.sh (which seems to be a fronted to osmosis-0.38) and the Qgis OSM importer. I did wonder why anyone would want to roll all tags into a single field.</p>
<blockquote>
<p>If you plan to edit in Mapinfo, you could also use osm2shp or osmjs to convert OSM data to shape files and edit those, or you could use the OSM plugin for QGis to load OSM data directly into QGis.</p>
</blockquote>
<p>I use MapInfo for editing as I find it the most comfortable to use, I find QGis painfully slow for editing when it lets me select edit mode, but mapinfo is plagued by the 254 character limitation for text fields and I can't get it to search containing quote or equals symbols.</p>
<p>The final product for this phase of the process is to produce a db with tables for places, motor vehicle roads, borders, coastline &amp; waterways to anchor the present, buildings, archealogical sites, etc. to illustrate the past.</p>
<p>I hope this clarifies things.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Oct '11, 04:03</strong></p>
<img src="https://secure.gravatar.com/avatar/e34a746be3d2d692055b59c8d0c11848?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sparrowhawk&#39;s gravatar image" />
<p><span>sparrowhawk</span><br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sparrowhawk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8477" class="comments-container">
&#10;</div>
<div id="comment-tools-8477" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8477-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8479"></span>

<div id="answer-container-8479" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8479-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I see. osm2postgis uses Osmosis to import data into PostgreSQL, and Osmosis duly creates a "hstore" column that contains <em>all</em> tags, but then osm2postgresql-04.sh flattens that into a single text column. Unless you have a very good reason to use this program (i.e. unless you really need exactly the data structure it creates) - <em>do</em> <em>not</em> <em>use</em> <em>osm2postgresql-04.sh</em>. If you use Osmosis directly then you get a database with a "hstore" column and you could easily break that out into "proper" columns for the 80 or so tags you are interested in, with a few lines of SQL. Or else use osm2pgsql which already creates any number of columns for you, you just have to add them to the config file.</p>
<p>It sounds as if you should really discuss your project in depth with someone more familiar with OSM and databases. Maybe there's a local pub meet or some other OSM event that you could go to?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Oct '11, 08:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-8479" class="comments-container">
&#10;</div>
<div id="comment-tools-8479" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8479-form-container" class="comment-form-container">
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

