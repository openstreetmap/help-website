+++
type = "question"
title = "How do I periodically update my tile server and keep it up to date"
description = '''I have successfully built my tile server by following this link (https://switch2osm.org/manually-building-a-tile-server-18-04-lts/ ) and open layers for viewing the tiles. How do I keep automate the process of updating my tile server periodically from OpenStreetMap server? I couldn&#x27;t find any tutori...'''
date = "2018-10-08T16:50:00Z"
lastmod = "2018-10-09T20:41:00Z"
weight = 66220
keywords = [ "tileserver", "osm2pgsql", "mapnik", "update" ]
aliases = [ "/questions/66220" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How do I periodically update my tile server and keep it up to date](/questions/66220/how-do-i-periodically-update-my-tile-server-and-keep-it-up-to-date)

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
<span id="post-66220-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66220-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-66220-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have successfully built my tile server by following this link (<a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/manually-building-a-tile-server-18-04-lts/</a> ) and open layers for viewing the tiles. How do I keep automate the process of updating my tile server periodically from OpenStreetMap server? I couldn't find any tutorial related to the same.</p>
<p>P.s. I read that Mapnik has tools that pulls data from the OpenStreetMap periodically but could not figure out how to get it up and running. I also tried to do it using the updating section of (<a href="https://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">https://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/</a> ) but it wasn't helpful too.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Oct '18, 16:50</strong></p>
<img src="https://secure.gravatar.com/avatar/153d30d9d12370c8532371eaaa3593b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vishy91&#39;s gravatar image" />
<p><span>vishy91</span><br />
<span class="score" title="66 reputation points">66</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vishy91 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Oct '18, 19:22</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-66220" class="comments-container">
&#10;</div>
<div id="comment-tools-66220" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66220-form-container" class="comment-form-container">
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

<span id="66221"></span>

<div id="answer-container-66221" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66221-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66221-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-66221-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="vishy91 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are some instructions <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1804_tileserver_load#Updating_your_database_as_people_edit_OpenStreetMap">here</a>. One of these days I'll actually update the switch2osm site with those as well :)</p>
<p>The map style used higher up that wiki page is different to OSM's standard style, but updating the database should work fine.</p>
<p><strong>A couple of notes on the process:</strong></p>
<p>The "regional" stuff is needed if you only want to apply updates to OSM within the area that you first imported data. You'll want to edit the lat and long values within openstreetmap-tiles-update-expire to reflect your area of interest (the example file has an area for Britain and Ireland in it).</p>
<p>If you get any other errors add a comment back here (perhaps create a gist and link to it if there's lots of error log), or contact someone on #OSM on IRC - the chances are that there will be someone familiar with the process in that channel.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Oct '18, 17:00</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-66221" class="comments-container">
<span id="66259"></span>
<div id="comment-66259" class="comment">
<div id="post-66259-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This worked. Thank You</p>
</div>
<div id="comment-66259-info" class="comment-info">
<span class="comment-age">(09 Oct '18, 20:41)</span> <span class="comment-user userinfo">vishy91</span>
</div>
</div>
</div>
<div id="comment-tools-66221" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66221-form-container" class="comment-form-container">
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

