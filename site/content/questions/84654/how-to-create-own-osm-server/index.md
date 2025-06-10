+++
type = "question"
title = "How to create own OSM Server"
description = '''I want to create own osm server for non commercial/ Internal use only with routing machine/ Geo Coding Please help me with the easiest way Step By Step'''
date = "2022-06-01T13:36:00Z"
lastmod = "2022-06-01T14:17:00Z"
weight = 84654
keywords = [ "osm", "routing", "tileserver" ]
aliases = [ "/questions/84654" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to create own OSM Server](/questions/84654/how-to-create-own-osm-server)

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
<span id="post-84654-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84654-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84654-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to create own osm server for non commercial/ Internal use only with routing machine/ Geo Coding Please help me with the easiest way Step By Step</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jun '22, 13:36</strong></p>
<img src="https://secure.gravatar.com/avatar/baf99cff3be491e336d62ef49cc43698?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Abhishek991990&#39;s gravatar image" />
<p><span>Abhishek991990</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Abhishek991990 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84654" class="comments-container">
&#10;</div>
<div id="comment-tools-84654" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84654-form-container" class="comment-form-container">
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

<span id="84655"></span>

<div id="answer-container-84655" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84655-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84655-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84655-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For tiles: switch2osm.org</p>
<p>For geocoding (Nominatim): <a href="https://nominatim.org/release-docs/develop/admin/Installation/">https://nominatim.org/release-docs/develop/admin/Installation/</a> although you might find "Photon" easier to install since you can download a pre-computed data set: <a href="https://github.com/komoot/photon">https://github.com/komoot/photon</a></p>
<p>For routing: Graphhopper is probably easiest <a href="https://github.com/graphhopper/graphhopper/blob/master/docs/web/quickstart.md">https://github.com/graphhopper/graphhopper/blob/master/docs/web/quickstart.md</a></p>
<p>Note that if you want to do this with world-wide data you will need a big server (around 2 TB fast hard disk, 128 GB RAM).</p>
<p>If you are familiar with Docker then you might also find ready-made Docker containers for these services.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jun '22, 13:53</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Jun '22, 13:54</strong> </span></p>
</div>
</div>
<div id="comments-container-84655" class="comments-container">
<span id="84656"></span>
<div id="comment-84656" class="comment">
<div id="post-84656-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Any Other way to do all of this via Windows Server or Windows System With GUI</p>
</div>
<div id="comment-84656-info" class="comment-info">
<span class="comment-age">(01 Jun '22, 14:08)</span> <span class="comment-user userinfo">Abhishek991990</span>
</div>
</div>
<span id="84657"></span>
<div id="comment-84657" class="comment">
<div id="post-84657-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Use <a href="https://www.openstreetmap.org/user/SomeoneElse/diary/42617">Windows Subsystem for Linux</a> or <a href="https://switch2osm.org/serving-tiles/using-a-docker-container/">Docker</a>.</p>
</div>
<div id="comment-84657-info" class="comment-info">
<span class="comment-age">(01 Jun '22, 14:17)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-84655" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84655-form-container" class="comment-form-container">
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

