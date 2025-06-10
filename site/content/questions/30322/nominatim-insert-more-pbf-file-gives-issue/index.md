+++
type = "question"
title = "Nominatim insert more pbf file gives issue"
description = '''hi everyone,  i installed nominatim in my ubuntu machine for India alone, now i wants to add more countries. i know its possible, so i just tried using  ./utils/setup.php --osm-file andorra-latest.osm.pbf --import-data  then it show the below message for long time  Import osm2pgsql SVN version 0.83....'''
date = "2014-01-30T07:31:00Z"
lastmod = "2014-01-30T08:48:00Z"
weight = 30322
keywords = [ "nominatim", "ubuntu" ]
aliases = [ "/questions/30322" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim insert more pbf file gives issue](/questions/30322/nominatim-insert-more-pbf-file-gives-issue)

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
<span id="post-30322-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30322-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30322-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hi everyone, i installed nominatim in my ubuntu machine for India alone, now i wants to add more countries. i know its possible, so i just tried using<br />
</p>
<pre><code>./utils/setup.php --osm-file andorra-latest.osm.pbf --import-data</code></pre>
<p>then it show the below message for long time</p>
<pre><code>Import
osm2pgsql SVN version 0.83.0 (64bit id space)
&#10;Using projection SRS 4326 (Latlong)
&#10;NOTICE:  drop cascades to function get_word_score(wordscore[],text[])
NOTICE:  type &quot;stringlanguagetype&quot; does not exist, skipping
NOTICE:  type &quot;keyvaluetype&quot; does not exist, skipping
Allocating memory for dense node cache
Allocating dense node cache in one big chunk
Allocating memory for sparse node cache
Sharing dense sparse
Node-cache: cache=6123MB, maxblocks=783744*8192, allocation method=11
Mid: pgsql, scale=10000000 cache=6123
Setting up table: planet_osm_nodes
NOTICE:  table &quot;planet_osm_nodes&quot; does not exist, skipping
NOTICE:  CREATE TABLE / PRIMARY KEY will create implicit index &quot;planet_osm_nodes_pkey&quot; for table &quot;planet_osm_nodes&quot;
Setting up table: planet_osm_ways</code></pre>
<p>Can anybody suggest possible way to get out of this and also any easiest steps available to import.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jan '14, 07:31</strong></p>
<img src="https://secure.gravatar.com/avatar/672f9138349e062b5fc0a11d50a9ca6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arun%20kmp&#39;s gravatar image" />
<p><span>Arun kmp</span><br />
<span class="score" title="63 reputation points">63</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arun kmp has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jan '14, 07:40</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-30322" class="comments-container">
&#10;</div>
<div id="comment-tools-30322" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30322-form-container" class="comment-form-container">
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

<span id="30324"></span>

<div id="answer-container-30324" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30324-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30324-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-30324-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The command you used more or less replaces the content of your DB instead of adding to it. See <a href="https://help.openstreetmap.org/questions/15505/import-more-osm-files-in-to-nominatim">this question</a> for instructions on how to add another file to a Nominatim database. Note that it explicitly states that pbf is not supported. You need to convert your osm file to xml first.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jan '14, 08:48</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-30324" class="comments-container">
&#10;</div>
<div id="comment-tools-30324" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30324-form-container" class="comment-form-container">
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

