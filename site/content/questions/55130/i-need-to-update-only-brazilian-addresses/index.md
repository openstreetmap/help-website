+++
type = "question"
title = "I need to update only Brazilian addresses"
description = '''I am trying to update only one country (Brazil), but when I follow the instructions and modify the local.php url to http://download.geofabrik.de/south-america/brazil-updates/ I get an error when I run  ./utils/setup.php --osmosis-init  ./utils/setup.php --create-functions --enable-diff-updates  ./ut...'''
date = "2017-03-16T18:38:00Z"
lastmod = "2017-03-16T22:24:00Z"
weight = 55130
keywords = [ "nominatim", "osm", "update" ]
aliases = [ "/questions/55130" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [I need to update only Brazilian addresses](/questions/55130/i-need-to-update-only-brazilian-addresses)

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
<span id="post-55130-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55130-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55130-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to update only one country (Brazil), but when I follow the instructions and modify the local.php url to <a href="http://download.geofabrik.de/south-america/brazil-updates/">http://download.geofabrik.de/south-america/brazil-updates/</a> I get an error when I run</p>
<pre><code> ./utils/setup.php --osmosis-init
 ./utils/setup.php --create-functions --enable-diff-updates
 ./utils/update.php --import-osmosis-all --no-npi
&#10;Allocating dense node cache in one big chunk
Allocating memory for sparse node cache
Sharing dense sparse
Node-cache: cache=2000MB, maxblocks=256000*8192, allocation method=11
Mid: pgsql, scale=10000000 cache=2000
Setting up table: planet_osm_nodes
Setting up table: planet_osm_ways
Setting up table: planet_osm_rels
&#10;Reading in file: /home/osm/Nominatim-2.5.0/data/osmosischange.osc
Using XML parser.
Processing: Node(112k 2.6k/s) Way(7k 0.87k/s) Relation(160 40.00/s)node cache: stored: 109400(100.00%), storage efficiency: 53.83% (dense blocks: 53, sparse nodes: 74475), hit rate: 24.99%
Osm2pgsql failed due to ERROR: insert_rel failed: ERROR:  value &quot;37945&quot; is out of range for type smallint
(7)</code></pre>
<p><strong>I need to update only Brazil.</strong></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Mar '17, 18:38</strong></p>
<img src="https://secure.gravatar.com/avatar/73b5d614a4090bf49df1b9fcdc68bc69?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paulo%20G%C3%BAbio&#39;s gravatar image" />
<p><span>Paulo Gúbio</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paulo Gúbio has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Mar '17, 19:08</strong> </span></p>
</div>
</div>
<div id="comments-container-55130" class="comments-container">
&#10;</div>
<div id="comment-tools-55130" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55130-form-container" class="comment-form-container">
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

<span id="55134"></span>

<div id="answer-container-55134" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55134-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55134-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55134-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There was bad (well too much) data inserted into OpenStreetMap which makes osm2pgsql fail which affected lots of users of Nominatim who do hourly/minutely update. I think those with daily updates were not affected. Have a look at <a href="https://lists.openstreetmap.org/pipermail/geocoding/2017-March/001859.html">https://lists.openstreetmap.org/pipermail/geocoding/2017-March/001859.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Mar '17, 22:16</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-55134" class="comments-container">
<span id="55135"></span>
<div id="comment-55135" class="comment">
<div id="post-55135-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, that looks like the same osm2pgsql error that I saw when updating a rendering DB.</p>
</div>
<div id="comment-55135-info" class="comment-info">
<span class="comment-age">(16 Mar '17, 22:24)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-55134" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55134-form-container" class="comment-form-container">
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

