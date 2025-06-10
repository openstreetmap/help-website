+++
type = "question"
title = "Getting specific POI data - and keeping them up to date."
description = '''This is a follow-up to another question on this site, where someone asked about getting (specific) POIs from the OSM data. The suggested ideal method is to get a recent copy of the Planet file and use osmosis to extract the data you&#x27;re interested in.  I do heartily agree that this is the preferred w...'''
date = "2011-03-25T10:20:00Z"
lastmod = "2014-05-20T22:53:00Z"
weight = 4065
keywords = [ "update", "osmosis", "poi" ]
aliases = [ "/questions/4065" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Getting specific POI data - and keeping them up to date.](/questions/4065/getting-specific-poi-data-and-keeping-them-up-to-date)

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
<span id="post-4065-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4065-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-4065-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
4
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This is a follow-up to <a href="http://help.openstreetmap.org/questions/15/getting-point-of-interest-data-from-openstreetmap">another question</a> on this site, where someone asked about getting (specific) POIs from the OSM data. The suggested ideal method is to get a recent copy of the <a href="http://wiki.openstreetmap.org/wiki/Planet">Planet</a> file and use <a href="http://wiki.openstreetmap.org/wiki/Osmosis">osmosis</a> to extract the data you're interested in.</p>
<p>I do heartily agree that this is the preferred way to go, especially since XAPI availability has been intermittent and performance has been slow to the point that it's no longer usable - although the <a href="http://wiki.openstreetmap.org/wiki/Xapi#Java_version_.28new.29--">new Java implementation</a> may alleviate this situation.</p>
<p>One of the unique qualities of OpenStreetMap is its continuous updating by all those thousands of contributors around the globe. Ideally you would want to reflect that in your POI extract. My question is:</p>
<p><strong>What is the workflow for keeping an up-to-date OSM-based POI database that performs well?</strong></p>
<p>To make this a little more concrete, here's what I currently do:</p>
<ul>
<li>Get an initial planet file from OSM</li>
<li>Extract the POIs that I want to be available using the osmosis <a href="http://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage#--tag-filter_.28--tf.29">--tag-filter</a> option</li>
<li>In the same operation, write the POIs to a PostGIS database using <a href="http://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage#--write-pgsql_.28--wp.29">--write-pgsql</a></li>
<li>Initialize a replication environment using <a href="http://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage#--read-replication-interval-init_.28--rrii.29-">--read-replication-interval-init</a>, following the instructions on the wiki</li>
<li>Set up periodical replication using osmosis <a href="http://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage#--read-replication-interval_.28--rri.29">--rri</a> <a href="http://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage#--write-pgsql-change_.28--wpc.29">--wpc</a> in <a href="http://en.wikipedia.org/wiki/Cron">crontab</a></li>
</ul>
<p>This works, but the database grows because the --rri task replicates all changes and not just the POIs I'm interested in. So derived questions are:</p>
<ul>
<li><strong>Is there a way to filter change streams in osmosis before writing them to an output stream?</strong></li>
<li><strong>Is the workflow described a good way to approach this challenge?</strong></li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Mar '11, 10:20</strong></p>
<img src="https://secure.gravatar.com/avatar/acea3c9fd5908d7ff09596d16b8724d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mvexel&#39;s gravatar image" />
<p><span>mvexel</span><br />
<span class="score" title="762 reputation points">762</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mvexel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-4065" class="comments-container">
<span id="33330"></span>
<div id="comment-33330" class="comment">
<div id="post-33330-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>dear mvexel - very good outline of your needs. let us know if you have any success. please share with us all your insights and all your further needs.</p>
</div>
<div id="comment-33330-info" class="comment-info">
<span class="comment-age">(20 May '14, 21:17)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
</div>
<div id="comment-tools-4065" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4065-form-container" class="comment-form-container">
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

<span id="4076"></span>

<div id="answer-container-4076" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4076-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4076-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-4076-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mvexel has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is currently no ready-made solution for what you want to do. If you are a programmer then the easiest way to accomplish what you want is to write a small parser for OSM/OSMChange files yourself (you will be able to re-use the code for both) and follow this logic:</p>
<ul>
<li>Get an initial planet file from OSM</li>
<li>Extract the POIs that you want to be available using your own program and write to PostGIS</li>
<li>Initialize a replication environment using <code>--read-replication-interval-init</code></li>
<li>Periodically, retrieve updates and process them.</li>
</ul>
<p>The logic to apply when processing updates is:</p>
<ul>
<li>Change file contains node deletion - then delete the node on your side.</li>
<li>Change file contains node creation - then check if the tags are of interest and create the node on your side if applicable.</li>
<li>Change file contains node modification - check if the tags are of interest; if not, then delete the node in your local database if it is there (this means somebody has removed the tags of interest from the node); if the node has interesting tags, then update or create it on your side.</li>
</ul>
<p>You could of course also amend Osmosis to do what you want.</p>
<p>This procedure has a disadvantage in that it is hard to cope with POIs that are modeled as ways in OSM (because you might theoretically receive an OsmChange file that says "way #1234 now has these tags" and you go "wow, I need that in my database", but you don't know about that way's geometry because you ignored it on import since it didn't have the right tags...)</p>
<p>One way to avoid programming, but at the cost of more processing overhead, is this:</p>
<ul>
<li>Get an initial planet file from OSM</li>
<li>Extract the POIs that you want to be available using the osmosis <code>--tag-filter</code> option; save to new file (e.g. <code>--write-pbf myfile.osm.pbf</code>)</li>
<li>Import new file into some kind of database using whatever process you fancy (could also be osm2pgsql or imposm, both of which may be faster than osmosis)</li>
<li>Initialize a replication environment using <code>--read-replication-interval-init</code></li>
<li>Periodically call Osmosis to append an update to your local file <em>and immediately tag-filter the result in the same step</em> (i.e. <code>--rri --simc --read-pbf myfile.osm.pbf --ac --tag-filter ... --write-pbf myfile-new.osm.pbf</code>), then again make a full import of the resulting file into a database of your choice. Afterwards, rename <code>myfile-new.osm.pbf</code> to <code>myfile.osm.pbf</code> and use that as the basis onto which you apply the next update.</li>
</ul>
<p>This wastes resources by always doing a full import, but the import will always be "clean" and only contain the things you really want. Plus, it has the capacity to work with way-POIs as well.</p>
<p>When using a local .osm.pbf file as your master database like in this example, it is advisable to use the <code>--compress=none</code> switch on <code>--write-pbf</code> which will speed up writing.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Mar '11, 12:27</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Apr '12, 19:03</strong> </span></p>
</div>
</div>
<div id="comments-container-4076" class="comments-container">
<span id="4136"></span>
<div id="comment-4136" class="comment">
<div id="post-4136-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I wrote a <a href="https://docs.google.com/document/pub?id=1paaYsOakgJEYP380R70s4SGYq8ME3ASl-mweVi1DlQ4">tutorial</a> based on my own experiences and the second method you described.</p>
</div>
<div id="comment-4136-info" class="comment-info">
<span class="comment-age">(27 Mar '11, 20:28)</span> <span class="comment-user userinfo">mvexel</span>
</div>
</div>
<span id="4207"></span>
<div id="comment-4207" class="comment">
<div id="post-4207-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>mvexel: Do you import the geometry of the ways? Just using <code>--tf accept-nodes man_made=surveillance</code> will remove the nodes of the ways.</p>
</div>
<div id="comment-4207-info" class="comment-info">
<span class="comment-age">(30 Mar '11, 15:33)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
<span id="33337"></span>
<div id="comment-33337" class="comment">
<div id="post-33337-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>many thanks for this answer..</p>
</div>
<div id="comment-33337-info" class="comment-info">
<span class="comment-age">(20 May '14, 22:53)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
</div>
<div id="comment-tools-4076" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4076-form-container" class="comment-form-container">
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

