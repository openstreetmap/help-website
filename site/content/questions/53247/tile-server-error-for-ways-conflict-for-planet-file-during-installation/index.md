+++
type = "question"
title = "Tile server error for ways conflict for planet file during installation"
description = '''Now I started configuring tile server for planet on a new machine using the link  &quot;https://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/&quot; instructions, so while I executed the following command : osm2pgsql --slim -C 32000 --number-processes 4 /home/osm/planet-latest.osm.pbf  Now...'''
date = "2016-12-05T10:23:00Z"
lastmod = "2016-12-05T12:44:00Z"
weight = 53247
keywords = [ "openstreetmap", "osm2pgsql", "planet_osm", "tileserver" ]
aliases = [ "/questions/53247" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tile server error for ways conflict for planet file during installation](/questions/53247/tile-server-error-for-ways-conflict-for-planet-file-during-installation)

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
<span id="post-53247-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53247-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53247-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Now I started configuring tile server for planet on a new machine using the link</p>
<p>"https://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/"</p>
<p>instructions, so while I executed the following command :</p>
<pre><code>osm2pgsql --slim -C 32000 --number-processes 4 /home/osm/planet-latest.osm.pbf</code></pre>
<p>Now while osm2pgsql is processing it gave following error and is still continuing to process further as:</p>
<pre><code>Processing: Node(3571919k 181.5k/s) Way(373048k 9.58k/s) Relation(166890 6.83/s)
Standard exception processing way_id 255785: topologyException:side location conflict at 2.13239e+06 6.90709e+06
Processing: Node(3571919k 181.5k/s) Way(373048k 9.58k/s) Relation(1485570 11.86/s)
Standard exception processing way_id 2563291: topologyException:side location conflict at 2.0772e+06 5.55411e+06
Processing: Node(3571919k 181.5k/s) Way(373048k 9.58k/s) Relation(3404650 15.65/s)</code></pre>
<p>So are these errors fine while configuring a new tile server for planet?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-planet_osm" rel="tag" title="see questions tagged &#39;planet_osm&#39;">planet_osm</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Dec '16, 10:23</strong></p>
<img src="https://secure.gravatar.com/avatar/78879ca1108e4678322460c818621e39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasonwhite1091&#39;s gravatar image" />
<p><span>Jasonwhite1091</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasonwhite1091 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53247" class="comments-container">
&#10;</div>
<div id="comment-tools-53247" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53247-form-container" class="comment-form-container">
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

<span id="53249"></span>

<div id="answer-container-53249" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53249-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53249-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-53249-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, these messages are not an issue for your import.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Dec '16, 12:44</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-53249" class="comments-container">
&#10;</div>
<div id="comment-tools-53249" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53249-form-container" class="comment-form-container">
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

