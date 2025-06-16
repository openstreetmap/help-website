+++
type = "question"
title = "NOTICE:  table &quot;place&quot; does not exist, skipping"
description = '''In spite of my effort and what is described here  https://help.openstreetmap.org/questions/27498/nominatim-setup-error https://help.openstreetmap.org/questions/11898/nominatim-setup-problem? I still get: Using projection SRS 4326 (Latlong) NOTICE: table &quot;place&quot; does not exist, skipping NOTICE: type ...'''
date = "2014-07-14T11:53:00Z"
lastmod = "2014-07-14T12:07:00Z"
weight = 34880
keywords = [ "table", "non-existent", "errors", "installation" ]
aliases = [ "/questions/34880" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [NOTICE: table "place" does not exist, skipping](/questions/34880/notice-table-place-does-not-exist-skipping)

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
<span id="post-34880-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34880-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-34880-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In spite of my effort and what is described here <a href="/questions/27498/nominatim-setup-error">https://help.openstreetmap.org/questions/27498/nominatim-setup-error</a> <a href="/questions/11898/nominatim-setup-problem?">https://help.openstreetmap.org/questions/11898/nominatim-setup-problem?</a> I still get:</p>
<pre><code>Using projection SRS 4326 (Latlong)
NOTICE:  table &quot;place&quot; does not exist, skipping
NOTICE:  type &quot;keyvalue&quot; does not exist, skipping
NOTICE:  type &quot;wordscore&quot; does not exist, skipping
NOTICE:  type &quot;stringlanguagetype&quot; does not exist, skipping
NOTICE:  type &quot;keyvaluetype&quot; does not exist, skipping
NOTICE:  function get_connected_ways(pg_catalog.int4[]) does not exist, skipping
Allocating memory for dense node cache
Allocating dense node cache in one big chunk
Allocating memory for sparse node cache
Sharing dense sparse
Node-cache: cache=1979MB, maxblocks=253312*8192, allocation method=11
Mid: pgsql, scale=10000000 cache=1979
Setting up table: planet_osm_nodes
NOTICE:  table &quot;planet_osm_nodes&quot; does not exist, skipping
Setting up table: planet_osm_ways
NOTICE:  table &quot;planet_osm_ways&quot; does not exist, skipping
Setting up table: planet_osm_rels
NOTICE:  table &quot;planet_osm_rels&quot; does not exist, skipping</code></pre>
<p>Does anybody know, what the problem could be? knowing that - Yes I have build the software with no error - Yes I have enough memory - file osm2pgsql stated ELF 64-bit</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-table" rel="tag" title="see questions tagged &#39;table&#39;">table</span> <span class="post-tag tag-link-non-existent" rel="tag" title="see questions tagged &#39;non-existent&#39;">non-existent</span> <span class="post-tag tag-link-errors" rel="tag" title="see questions tagged &#39;errors&#39;">errors</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jul '14, 11:53</strong></p>
<img src="https://secure.gravatar.com/avatar/efaf1be942715d825679323e1a698238?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gorgia&#39;s gravatar image" />
<p><span>gorgia</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gorgia has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-34880" class="comments-container">
&#10;</div>
<div id="comment-tools-34880" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34880-form-container" class="comment-form-container">
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

<span id="34883"></span>

<div id="answer-container-34883" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34883-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34883-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-34883-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is not a problem.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jul '14, 12:07</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-34883" class="comments-container">
&#10;</div>
<div id="comment-tools-34883" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34883-form-container" class="comment-form-container">
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

