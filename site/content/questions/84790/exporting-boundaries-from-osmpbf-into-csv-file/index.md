+++
type = "question"
title = "exporting boundaries from osm.pbf into csv file"
description = '''Hi! I am trying to get boundaries from usa.osm.pbf file using &quot;pyrosm&quot; with the following command: import pyrosm # Initialize the OSM object  osm = pyrosm.OSM(&quot;usa.osm.pbf&quot;)  boundaries = osm.get_boundaries(&#x27;all&#x27;)  boundaries.to_csv(&#x27;usa.csv&#x27;)  I have a PC with 256 GB ram, using Linux, and usa.psm.p...'''
date = "2022-06-16T13:18:00Z"
lastmod = "2022-06-16T14:39:00Z"
weight = 84790
keywords = [ "boundaries", "osm.pbf", "csv", "pyrosm" ]
aliases = [ "/questions/84790" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [exporting boundaries from osm.pbf into csv file](/questions/84790/exporting-boundaries-from-osmpbf-into-csv-file)

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
<span id="post-84790-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84790-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84790-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi!</p>
<p>I am trying to get boundaries from usa.osm.pbf file using "pyrosm" with the following command:</p>
<pre><code>import pyrosm
# Initialize the OSM object 
osm = pyrosm.OSM(&quot;usa.osm.pbf&quot;) 
boundaries = osm.get_boundaries(&#39;all&#39;) 
boundaries.to_csv(&#39;usa.csv&#39;)</code></pre>
<p>I have a PC with 256 GB ram, using Linux, and usa.psm.pbf file allocates 8.3 GB on disc. However, I encounter with memory issues. Ironically, 256 GB RAM is not enough to extract boundaries from 8.3 GB file.</p>
<p>How can I achieve my task in a different way using my luxury and expensive, but not sufficient resources?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-osm.pbf" rel="tag" title="see questions tagged &#39;osm.pbf&#39;">osm.pbf</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-pyrosm" rel="tag" title="see questions tagged &#39;pyrosm&#39;">pyrosm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jun '22, 13:18</strong></p>
<img src="https://secure.gravatar.com/avatar/746acb212d471b49fabb4c3b7f0fc943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hasan90&#39;s gravatar image" />
<p><span>hasan90</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hasan90 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jun '22, 14:27</strong> </span></p>
</div>
</div>
<div id="comments-container-84790" class="comments-container">
<span id="84791"></span>
<div id="comment-84791" class="comment">
<div id="post-84791-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>And what is your question?</p>
</div>
<div id="comment-84791-info" class="comment-info">
<span class="comment-age">(16 Jun '22, 14:02)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="84793"></span>
<div id="comment-84793" class="comment">
<div id="post-84793-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry Frederik, I have just added the question.</p>
</div>
<div id="comment-84793-info" class="comment-info">
<span class="comment-age">(16 Jun '22, 14:08)</span> <span class="comment-user userinfo">hasan90</span>
</div>
</div>
</div>
<div id="comment-tools-84790" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84790-form-container" class="comment-form-container">
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

<span id="84794"></span>

<div id="answer-container-84794" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84794-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84794-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-84794-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have still not explained in what way the resources are insufficient. I do not know about pyrosm but I suspect it will inefficiently try to load all nodes into memory, even those that are not needed for the particular task. It may be possible to first use the <code>osmium</code> command line utility with the <code>tags-filter</code> option to remove everything from the usa.osm.pbf that is not needed for a boundary extract, and then try pyrosm again.</p>
<p>Another option that will definitely work is importing the data into a PostGIS database with <code>osm2pgsql</code> and then using PostGIS SQL queries to extract the boundaries.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jun '22, 14:20</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-84794" class="comments-container">
<span id="84796"></span>
<div id="comment-84796" class="comment">
<div id="post-84796-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you Frederik.</p>
<p>Could you explicitly show me here how I can do it, step by step? I have newly met with OpenStreetMaps.</p>
<p>Best,</p>
</div>
<div id="comment-84796-info" class="comment-info">
<span class="comment-age">(16 Jun '22, 14:25)</span> <span class="comment-user userinfo">hasan90</span>
</div>
</div>
<span id="84797"></span>
<div id="comment-84797" class="comment">
<div id="post-84797-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would be happy if you could show PostGIS method. Thanks!</p>
</div>
<div id="comment-84797-info" class="comment-info">
<span class="comment-age">(16 Jun '22, 14:30)</span> <span class="comment-user userinfo">hasan90</span>
</div>
</div>
<span id="84798"></span>
<div id="comment-84798" class="comment">
<div id="post-84798-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Since administrative boundaries are almost always relations, the <code>osmium</code> approach would probably be (all on one line!)</p>
<pre><code>osmium tags-filter 
  -o usboundaries.osm.pbf
  usa.osm.pbf
  r/boundary=administrative</code></pre>
<p>Then you could try processing the (much smaller) resulting usboundaries.osm.pbf with your existing workflow. Alternatively, install osm2pgsql and follow the instructions on <a href="https://osm2pgsql.org/doc/manual.html">https://osm2pgsql.org/doc/manual.html</a> to load your file into the database, then you can execute a SQL query like</p>
<pre><code>SELECT name,admin_level,way
FROM planet_osm_polygon
WHERE boundary=&#39;administrative&#39;;</code></pre>
<p>to find boundaries.</p>
</div>
<div id="comment-84798-info" class="comment-info">
<span class="comment-age">(16 Jun '22, 14:32)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="84799"></span>
<div id="comment-84799" class="comment">
<div id="post-84799-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Frederik, thank you for your answer! I highly appreciate it.</p>
<p>I would like to get 'all' boundaries, not only administrative.</p>
</div>
<div id="comment-84799-info" class="comment-info">
<span class="comment-age">(16 Jun '22, 14:39)</span> <span class="comment-user userinfo">hasan90</span>
</div>
</div>
</div>
<div id="comment-tools-84794" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84794-form-container" class="comment-form-container">
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

