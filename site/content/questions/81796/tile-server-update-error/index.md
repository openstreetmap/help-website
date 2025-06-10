+++
type = "question"
title = "Tile server update error"
description = '''We have an error situation in the update process (openstreetmap-tiles-update-expire). At certain times, the update process crashes and does not proceed. The error message in the file /var/log/tiles/osm2pgsql.log is shown below: Reading in file: /var/lib/mod_tile/changes.osc.gz Using XML parser. Proc...'''
date = "2021-09-17T15:30:00Z"
lastmod = "2021-09-17T16:11:00Z"
weight = 81796
keywords = [ "table", "tiles", "error", "osm2psg", "field" ]
aliases = [ "/questions/81796" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tile server update error](/questions/81796/tile-server-update-error)

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
<span id="post-81796-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81796-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81796-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We have an error situation in the update process (openstreetmap-tiles-update-expire). At certain times, the update process crashes and does not proceed. The error message in the file /var/log/tiles/osm2pgsql.log is shown below:</p>
<p>Reading in file: /var/lib/mod_tile/changes.osc.gz</p>
<p>Using XML parser.</p>
<p>Processing: Node(10k 0.0k/s) Way(3k 3.66k/s) Relation(40 20.00/s) parse time: 407s</p>
<p>Node stats: total(10020), max(9090048720) in 404s</p>
<p>Way stats: total(3661), max(983093395) in 1s</p>
<p>Relation stats: total(81), max(13209476) in 2s</p>
<p>DB writer thread failed due to ERROR: result COPY_END for planet_osm_polygon failed: ERROR: invalid input &gt; syntax for type integer: "2.75"</p>
<p>CONTEXT: COPY planet_osm_polygon, line 26, column layer: "2.75"</p>
<p>The message above seems to indicate that a double value (2.75) is being written to the layer field of the planet_osm_polygon table, which is set to integer.</p>
<p>To work around this, we decreased the value of the maxInterval parameter in the configuration file /var/lib/mod_tile/.osmosis/configuration.txt And we manually increment the sequenceNumber value of the /var/lib/mod_tile/.osmosis/state.txt file, so that it advances in the update. We believe there may be some information recorded wrong in the update files, which are available at <a href="https://planet.openstreetmap.org/replication/minute">https://planet.openstreetmap.org/replication/minute</a></p>
<p>However, this is impacting our environment as it requires a lot of technical intervention.</p>
<p>Our environment is Ubuntu 20.04 LTS. The osm2pgsql version is shown below:</p>
<p>osm2pgsql version 1.2.1 (64 bit id space)</p>
<p>Compiled using the following library versions:</p>
<p>Libosmium 2.15.4</p>
<p>Lua 5.2.4</p>
<p>We would appreciate if you can guide us on how to solve the problem.</p>
<p>Yours sincerely,</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-table" rel="tag" title="see questions tagged &#39;table&#39;">table</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span> <span class="post-tag tag-link-osm2psg" rel="tag" title="see questions tagged &#39;osm2psg&#39;">osm2psg</span> <span class="post-tag tag-link-field" rel="tag" title="see questions tagged &#39;field&#39;">field</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Sep '21, 15:30</strong></p>
<img src="https://secure.gravatar.com/avatar/43c57b8e57582528997b4e552579118a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FPintoA&#39;s gravatar image" />
<p><span>FPintoA</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FPintoA has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81796" class="comments-container">
<span id="81797"></span>
<div id="comment-81797" class="comment">
<div id="post-81797-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(see <a href="https://github.com/openstreetmap/osm2pgsql/issues/1571">https://github.com/openstreetmap/osm2pgsql/issues/1571</a> for context)</p>
</div>
<div id="comment-81797-info" class="comment-info">
<span class="comment-age">(17 Sep '21, 15:59)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-81796" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81796-form-container" class="comment-form-container">
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

<span id="81798"></span>

<div id="answer-container-81798" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81798-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81798-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81798-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Something in your map style can't cope with non-integer layer values. You've not said what style it is, so we can't directly help with that, but maybe this example will help:</p>
<p><a href="https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/19395d61743babc8a5311a624677bc78e0f2315a/style.lua#L15">this line</a> in a lua style file makes sure that only seinsible layer values are used for z_order and tthe lines below <a href="https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/19395d61743babc8a5311a624677bc78e0f2315a/style.lua#L71">here</a> in a lua style file try and guess at layers from invalid values. See <a href="https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/19395d61743babc8a5311a624677bc78e0f2315a/style.lua#L407">other uses</a> of "tonumber" in that lua style file.</p>
<p>One other point to mention, since your seeing this in openstreetmap-tiles-update-expire - are you definitely calling the lua transforms from that and not the C transforms?</p>
<p>For completeness, the offending data in OSM is <a href="https://overpass-turbo.eu/s/1bgg">here</a>, and it's not "a bug in OSM" as such - anything that consumes OSM data needs to be able to consume whatever is there. Scroll to the end of the list in <a href="https://taginfo.openstreetmap.org/keys/layer#values">taginfo</a> and you'll see all sorts of values there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Sep '21, 16:11</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Sep '21, 16:12</strong> </span></p>
</div>
</div>
<div id="comments-container-81798" class="comments-container">
&#10;</div>
<div id="comment-tools-81798" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81798-form-container" class="comment-form-container">
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

