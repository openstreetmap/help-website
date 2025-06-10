+++
type = "question"
title = "pbf file missing &#x27;osmosis_replication_sequence_number&#x27; in header"
description = '''I downloaded the latest pbf file(dated 27-Aug-2020 23:37) from a mirror and read its header using a python wrapper to osmium (v3.0.1) import osmium  f = osmium.io.Reader(&quot;path/to/pbf_file.osm.pbf&quot;) header = f.header() seqnum = header.get(&quot;osmosis_replication_sequence_number&quot;, &quot;&quot;) timestamp = header....'''
date = "2020-09-04T09:37:00Z"
lastmod = "2020-09-12T15:35:00Z"
weight = 76430
keywords = [ "osmium", "header", "pbf", "python" ]
aliases = [ "/questions/76430" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [pbf file missing 'osmosis_replication_sequence_number' in header](/questions/76430/pbf-file-missing-osmosis_replication_sequence_number-in-header)

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
<span id="post-76430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76430-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I downloaded the latest pbf file(dated 27-Aug-2020 23:37) from <a href="https://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/pbf/">a mirror</a> and read its header using <a href="https://pypi.org/project/osmium/">a python wrapper to osmium</a> (v3.0.1)</p>
<pre><code>import osmium
&#10;f = osmium.io.Reader(&quot;path/to/pbf_file.osm.pbf&quot;)
header = f.header()
seqnum = header.get(&quot;osmosis_replication_sequence_number&quot;, &quot;&quot;)
timestamp = header.get(&quot;osmosis_replication_timestamp&quot;, &quot;&quot;)
print(f&#39;{seqnum!r},{timestamp!r}&#39;)
# output: &#39;&#39;, &#39;2020-08-23T23:59:50Z&#39;</code></pre>
<p>The sequence number was missing. Is this expected behaviour?</p>
<p>In the <a href="https://wiki.openstreetmap.org/wiki/PBF_Format#What_are_the_replication_fields_for.3F">documentation</a>, all the replication fields in OSMHeader seem to be set as optional. What pbf files are expected to have these values set?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-header" rel="tag" title="see questions tagged &#39;header&#39;">header</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Sep '20, 09:37</strong></p>
<img src="https://secure.gravatar.com/avatar/ab24d4200eae973dd66c10684f25f767?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="M_T_&#39;s gravatar image" />
<p><span>M_T_</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="M_T_ has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Sep '20, 10:26</strong> </span></p>
</div>
</div>
<div id="comments-container-76430" class="comments-container">
&#10;</div>
<div id="comment-tools-76430" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76430-form-container" class="comment-form-container">
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

<span id="76466"></span>

<div id="answer-container-76466" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76466-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76466-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-76466-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="M_T_ has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The sequence field in the headers are currently set only on extracts from <a href="http://download.geofabrik.de/">Geofabrik</a>. pyosmium-up-to-date also sets them when you update a PBF file.</p>
<p>There is a good reason that the sequence number is not set on the official planet file: there is no exact sequence number that corresponds to the state of a planet file. Planet files are created independently of the change files. So the content of the planet might correspond to something like sequence number "4164164 3/4".</p>
<p>When you want to use updates with a downloaded planet file, the usual way is to look at the creation time and find a change sequence number that is far enough in the past that you get all new changes that are not yet contained in the planet. You don't have to do the math yourself, pyosmium-get-changes, which is included in the python osmium package, can do that for you. Just run</p>
<pre><code>pyosmium-get-changes -O planet-latest.osm.pbf</code></pre>
<p>and it prints a single number. This is the recommended sequence number where you should start with the updates.</p>
<p>See the <a href="https://docs.osmcode.org/pyosmium/latest/updating_osm_data.html">section on updating OSM data</a> in the pyosmium manual for more information.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Sep '20, 20:25</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-76466" class="comments-container">
<span id="76479"></span>
<div id="comment-76479" class="comment">
<div id="post-76479-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>AFAIU the sequence number you get from a call to <code>pyosmium-get-changes</code> is the minutely sequence number. How would you translate this to a daily or hourly sequence number? It seems that some minute updates have been skipped, so one can't do a simple multiplication to translate between the two</p>
</div>
<div id="comment-76479-info" class="comment-info">
<span class="comment-age">(07 Sep '20, 10:15)</span> <span class="comment-user userinfo">M_T_</span>
</div>
</div>
<span id="76560"></span>
<div id="comment-76560" class="comment">
<div id="post-76560-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You can't directly translate to hourly/daily sequence ID. You need to compute the appropriate ID in the same way as for the minutely replication. Use the parameter <code>--server</code> with <code>pyosmium-get-changes</code> to choose a different replication source. For example, to get the sequence ID for daily updates run <code>pyosmium-get-changes --server </code><a href="https://planet.osm.org/replication/day/"><code>https://planet.osm.org/replication/day/</code></a><code> -O planet-latest.osm.pbf</code>.</p>
</div>
<div id="comment-76560-info" class="comment-info">
<span class="comment-age">(12 Sep '20, 15:35)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
</div>
<div id="comment-tools-76466" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76466-form-container" class="comment-form-container">
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

