+++
type = "question"
title = "export osm2pgsql to osm"
description = '''Hello i use osm2pgsql to import data into the tile server database,such as &quot;osm2pgsql --slim -d gis -C 1600 --number-processes 3 mymap.osm.pbf. Now i want export data to osm or bpf file. Any ideas? Thanks a lot!'''
date = "2017-07-22T17:28:00Z"
lastmod = "2017-07-22T19:19:00Z"
weight = 57235
keywords = [ "osm2pgsql", "osmosis" ]
aliases = [ "/questions/57235" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [export osm2pgsql to osm](/questions/57235/export-osm2pgsql-to-osm)

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
<span id="post-57235-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57235-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57235-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello i use osm2pgsql to import data into the tile server database,such as "osm2pgsql --slim -d gis -C 1600 --number-processes 3 mymap.osm.pbf. Now i want export data to osm or bpf file.</p>
<p>Any ideas?</p>
<p>Thanks a lot!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jul '17, 17:28</strong></p>
<img src="https://secure.gravatar.com/avatar/30dd275524fc5278a2a16b18168745cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bz3616&#39;s gravatar image" />
<p><span>bz3616</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bz3616 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57235" class="comments-container">
&#10;</div>
<div id="comment-tools-57235" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57235-form-container" class="comment-form-container">
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

<span id="57236"></span>

<div id="answer-container-57236" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57236-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57236-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-57236-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The osm2pgsql schema is not really suitable for a re-export to OSM format (xml or pbf) as depending on how you set things up (essentially you would have had to thought about this before the import and if you had, you wouldn't have used osm2pgsql) you will have lost the necessary information to recreate all objects as they where before the import.</p>
<p>In any case you WILL need to roll your own exporter for this (if you can actually live with the information loss).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jul '17, 19:19</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jul '17, 20:01</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-57236" class="comments-container">
&#10;</div>
<div id="comment-tools-57236" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57236-form-container" class="comment-form-container">
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

