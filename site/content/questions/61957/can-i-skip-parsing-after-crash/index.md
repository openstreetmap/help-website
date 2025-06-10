+++
type = "question"
title = "Can I skip parsing after crash?"
description = '''Output of osm2pgsql: Node stats: total(4235496629), max(5290747187) in 33793s Way stats: total(458618737), max(547543126) in 1300890s Relation stats: total(5442482), max(7820612) in 741417s Committing transaction for planet_osm_point Committing transaction for planet_osm_line Committing transaction ...'''
date = "2018-02-05T10:57:00Z"
lastmod = "2018-02-05T10:57:00Z"
weight = 61957
keywords = [ "crash", "osm2pgsql" ]
aliases = [ "/questions/61957" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can I skip parsing after crash?](/questions/61957/can-i-skip-parsing-after-crash)

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
<span id="post-61957-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61957-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61957-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Output of osm2pgsql:</p>
<pre><code>Node stats: total(4235496629), max(5290747187) in 33793s
Way stats: total(458618737), max(547543126) in 1300890s
Relation stats: total(5442482), max(7820612) in 741417s
Committing transaction for planet_osm_point
Committing transaction for planet_osm_line
Committing transaction for planet_osm_polygon
Committing transaction for planet_osm_roads
Setting up table: planet_osm_nodes
Setting up table: planet_osm_ways
Setting up table: planet_osm_rels
Using built-in tag processing pipeline
Setting up table: planet_osm_nodes
Setting up table: planet_osm_ways
Setting up table: planet_osm_rels
Using built-in tag processing pipeline
Killed</code></pre>
Can I modify osm2pgsql.cpp file by comment lines from 78 to 94, for restore progress of importing data? Which options I need for run osm2pgsql again? same issue on github <a href="https://github.com/openstreetmap/osm2pgsql/issues/799">https://github.com/openstreetmap/osm2pgsql/issues/799</a>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Feb '18, 10:57</strong></p>
<img src="https://secure.gravatar.com/avatar/0874ff26b6add932e22271612bc57c4e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="molofeev&#39;s gravatar image" />
<p><span>molofeev</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="molofeev has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Feb '18, 12:21</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-61957" class="comments-container">
&#10;</div>
<div id="comment-tools-61957" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61957-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

