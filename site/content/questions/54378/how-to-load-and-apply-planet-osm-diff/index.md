+++
type = "question"
title = "How to load and apply planet osm diff?"
description = '''Few months ago I donwloaded full planet.osm dump and imported it in postgresql database via osm2pgsql. Later I removed the dump file. Thats why I don&#x27;t know the timestamp of my current osm data. How can I get this timestamp? If I will know this timestamp, how can I download and import to my postgres...'''
date = "2017-01-31T19:32:00Z"
lastmod = "2017-01-31T21:06:00Z"
weight = 54378
keywords = [ "osm2pgsql", "dump" ]
aliases = [ "/questions/54378" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to load and apply planet osm diff?](/questions/54378/how-to-load-and-apply-planet-osm-diff)

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
<span id="post-54378-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54378-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-54378-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Few months ago I donwloaded full planet.osm dump and imported it in postgresql database via osm2pgsql. Later I removed the dump file. Thats why I don't know the timestamp of my current osm data. How can I get this timestamp?</p>
<p>If I will know this timestamp, how can I download and import to my postgresql database the diff between this timestamp and now?</p>
<p>P.S.: import the full dump again is bad idea, it is too slow.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-dump" rel="tag" title="see questions tagged &#39;dump&#39;">dump</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Jan '17, 19:32</strong></p>
<img src="https://secure.gravatar.com/avatar/91f51616367436f400039e73daac62cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kz_sergey&#39;s gravatar image" />
<p><span>kz_sergey</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kz_sergey has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54378" class="comments-container">
<span id="54379"></span>
<div id="comment-54379" class="comment">
<div id="post-54379-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>crossposting at <a href="http://gis.stackexchange.com/questions/226511/how-to-load-and-apply-planet-osm-diff">http://gis.stackexchange.com/questions/226511/how-to-load-and-apply-planet-osm-diff</a></p>
</div>
<div id="comment-54379-info" class="comment-info">
<span class="comment-age">(31 Jan '17, 21:00)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-54378" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54378-form-container" class="comment-form-container">
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

<span id="54380"></span>

<div id="answer-container-54380" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54380-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54380-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-54380-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kz_sergey has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Applying diffs is much slower than the full planet load; if you want to apply diffs for a few <em>months</em> then it is almost certainly going to be faster to drop the database and load it again. (It could be that applying one day's worth of diffs takes more than a day!)</p>
<p>Having said that, here's how to update:</p>
<ol>
<li>Find out the highest node ID you have in your database (if you have used flatnodes, then running <code>nodecachefilereader</code> will tell you, else do a <code>select max(id) from planet_osm_nodes</code>).</li>
<li>Get <a href="https://svn.openstreetmap.org/applications/utils/whichdiff/whichdiff.pl">https://svn.openstreetmap.org/applications/utils/whichdiff/whichdiff.pl</a></li>
<li>Run <code>perl whichdiff.pl [highest_node_id]</code></li>
<li>Install <code>osmosis</code>, run <code>osmosis --rrii</code> do initialize a status directory, and copy the state.txt file that you got in step 3 into that directory. Check the max_interval setting in configuration.txt and perhaps set it to 3600 (update only one hour) initially to see how long it takes to update one hour. You can re-run the following as often as you want until you arrive at the current end of the data:</li>
<li>run <code>osmosis --rri --write-xml-change mydiff.osc.gz</code></li>
<li>load mydiff.osc.gz into your database using the same <code>osm2pgsql</code> and same options as you used when doing the initial load, just use <code>--append</code> istead of <code>--create</code></li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jan '17, 21:06</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-54380" class="comments-container">
&#10;</div>
<div id="comment-tools-54380" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54380-form-container" class="comment-form-container">
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

