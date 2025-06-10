+++
type = "question"
title = "osm2pgsql: Import splits ways in table planet_osm_line"
description = '''I&#x27;m building up working process for analysing addresses in the database. So I use osm2pgsql for import the data from pbf and append osc-files. In the following steps I take this data for generete my own optimized dataset. For getting all ways I need, I used the planet_osm_line table where I have all...'''
date = "2015-02-09T17:12:00Z"
lastmod = "2018-10-31T12:27:00Z"
weight = 40888
keywords = [ "osm2pgsql", "database" ]
aliases = [ "/questions/40888" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql: Import splits ways in table planet_osm_line](/questions/40888/osm2pgsql-import-splits-ways-in-table-planet_osm_line)

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
<span id="post-40888-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40888-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40888-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm building up working process for analysing addresses in the database. So I use osm2pgsql for import the data from pbf and append osc-files. In the following steps I take this data for generete my own optimized dataset.</p>
<p>For getting all ways I need, I used the <code>planet_osm_line</code> table where I have all non closed ways (excluding roundabouts). The documentation of the table in the schema says the following:</p>
<hr />
<p>Additional rows are created for ways which are members of type=route relations:</p>
<ul>
<li>For each relation of type=route, its ways are concatenated into "chunks" of consecutive ways</li>
<li>One row is created for each of these chunks (one or more for each relation which has members of type way)</li>
<li>The osm_id is the negative ID of the relation</li>
<li>The tag columns are filled with the tags of the relation</li>
</ul>
<p>Since there may be multiple chunks per relation, negative IDs are not necessarily unique.</p>
<hr />
<p>I only need ways which meens: I only need elements with <code>osm_id&gt;0</code>. If I filter the data, I've found some <code>osm_id</code>s of twice. The documentation only says, that relations can be contained twice. But sometimes, osm2pgsql splits some ways into different chunks.</p>
<hr />
<p>To reproduce this you can take an extract e.g. bremen: <a href="http://download.geofabrik.de/europe/germany/bremen-150207.osm.pbf">http://download.geofabrik.de/europe/germany/bremen-150207.osm.pbf</a></p>
<p>Now I import it with default style settings:</p>
<p><code>osm2pgsql --create -s --number-processes 4 -C 3500 -H 192.168.0.21 -d osm3 -U osm bremen-150207.osm.pbf</code></p>
<p>Now you can query the table:</p>
<pre><code>SELECT osm_id, count(*) FROM planet_osm_line
WHERE osm_id&gt;0
GROUP BY osm_id
HAVING count(*)&gt;0;</code></pre>
<p>You can found this element: <a href="http://www.openstreetmap.org/way/166985155">http://www.openstreetmap.org/way/166985155</a> this is a simple way, it is defined twice, in 2 chunks. Why does osm2pgsql split this way in two chunks? How can I avoid this behavior?</p>
<p>If I use ST_UNION() a complete way is shown without any gap.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Feb '15, 17:12</strong></p>
<img src="https://secure.gravatar.com/avatar/99ef175794b71f7d10ee58523c5848d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christopher&#39;s gravatar image" />
<p><span>Christopher</span><br />
<span class="score" title="126 reputation points">126</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christopher has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-40888" class="comments-container">
<span id="40889"></span>
<div id="comment-40889" class="comment">
<div id="post-40889-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The reason why I don't use planet_osm_roads is, that this table don't contain all needed ways: see <a href="/questions/13458/does-planet_osm_roads-of-the-osm2pgsqlschema-contain-all-roads/13460">that answer</a></p>
</div>
<div id="comment-40889-info" class="comment-info">
<span class="comment-age">(09 Feb '15, 17:14)</span> <span class="comment-user userinfo">Christopher</span>
</div>
</div>
</div>
<div id="comment-tools-40888" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40888-form-container" class="comment-form-container">
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

<span id="40896"></span>

<div id="answer-container-40896" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40896-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40896-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40896-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>osm2pgsql has code to split up long lines. The limit is set here:</p>
<p><a href="https://github.com/openstreetmap/osm2pgsql/blob/ed86d635cb0e54252881c766ede90a532e63dca0/output-pgsql.cpp#L125-L128">https://github.com/openstreetmap/osm2pgsql/blob/ed86d635cb0e54252881c766ede90a532e63dca0/output-pgsql.cpp#L125-L128</a></p>
<p>to about 100.000 Google Mercator units (roughly meters) which your ferry line might well be above.</p>
<p>Change the source code and recompile.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Feb '15, 20:17</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-40896" class="comments-container">
<span id="66598"></span>
<div id="comment-66598" class="comment">
<div id="post-66598-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, this bugs was fixed? There are an option to say "not split"?</p>
</div>
<div id="comment-66598-info" class="comment-info">
<span class="comment-age">(31 Oct '18, 12:27)</span> <span class="comment-user userinfo">ppKrauss</span>
</div>
</div>
</div>
<div id="comment-tools-40896" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40896-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

