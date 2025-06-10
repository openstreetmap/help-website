+++
type = "question"
title = "Switch2osm tile server insert more countries"
description = '''i am successfully installed tile server based on the instruction given in the  http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/ for india and i got the png image too. Then i tried to add for some other countries. when i insert using  &quot;osm2pgsql --slim -d gis -C 16000 --numb...'''
date = "2014-02-13T06:47:00Z"
lastmod = "2014-02-13T09:48:00Z"
weight = 30698
keywords = [ "osm", "tiles", "switch2osm", "postgresql", "tileserver" ]
aliases = [ "/questions/30698" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Switch2osm tile server insert more countries](/questions/30698/switch2osm-tile-server-insert-more-countries)

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
<span id="post-30698-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30698-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30698-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>i am successfully installed tile server based on the instruction given in the</p>
<p><a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/">http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/</a></p>
<p>for india and i got the png image too. Then i tried to add for some other countries. when i insert using</p>
<p>"osm2pgsql --slim -d gis -C 16000 --number-processes 3 new-york-latest.osm.pbf"</p>
<p>it replace india data in postgresql database.</p>
<p>Guide me best option to solve this issue.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Feb '14, 06:47</strong></p>
<img src="https://secure.gravatar.com/avatar/672f9138349e062b5fc0a11d50a9ca6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arun%20kmp&#39;s gravatar image" />
<p><span>Arun kmp</span><br />
<span class="score" title="63 reputation points">63</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arun kmp has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Feb '14, 08:45</strong> </span></p>
</div>
</div>
<div id="comments-container-30698" class="comments-container">
&#10;</div>
<div id="comment-tools-30698" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30698-form-container" class="comment-form-container">
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

<span id="30704"></span>

<div id="answer-container-30704" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30704-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30704-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-30704-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Arun kmp has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://help.openstreetmap.org/questions/5389/merging-2-countries-with-osm2pgsql">This previous question</a> shows how to append files, and the top answer to it describes a problem that you might get if there's shared data between the file that you originally used and the file that you're merging. As <span>@EdLoach</span> says in that answer - merge files together using <a href="http://wiki.openstreetmap.org/wiki/Osmosis">osmosis</a> first and then load.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Feb '14, 09:48</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Feb '14, 09:50</strong> </span></p>
</div>
</div>
<div id="comments-container-30704" class="comments-container">
&#10;</div>
<div id="comment-tools-30704" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30704-form-container" class="comment-form-container">
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

