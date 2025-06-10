+++
type = "question"
title = "Cannot load the local map tiles from the DB in my slippy map – using the Switch2OSM package"
description = '''I have currently loaded the &quot;Switch2OSM&quot; package on to my server from &quot;http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/.&quot; It is a Ubuntu 12.04 server.  When I view the &quot;slippymap.html&quot; in the browser, Only the Mapnik source works, when I view the Local tiles, all I get are p...'''
date = "2013-01-17T11:46:00Z"
lastmod = "2013-11-13T22:17:00Z"
weight = 19156
keywords = [ "switch2osm", "slippymap", "tileserver" ]
aliases = [ "/questions/19156" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot load the local map tiles from the DB in my slippy map – using the Switch2OSM package](/questions/19156/cannot-load-the-local-map-tiles-from-the-db-in-my-slippy-map-using-the-switch2osm-package)

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
<span id="post-19156-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19156-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-19156-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have currently loaded the "Switch2OSM" package on to my server from "http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/." It is a Ubuntu 12.04 server.</p>
<p>When I view the "slippymap.html" in the browser, Only the Mapnik source works, when I view the Local tiles, all I get are pink tiles with broken image icons. But I show no errors in the server system or no errors during installation.</p>
<p>I had loaded "Canada.osm.bz2" into the database with no issues at all. Could some one help give me some direction on what I need to look at to fix this.</p>
<p>Thank you for your time.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span> <span class="post-tag tag-link-slippymap" rel="tag" title="see questions tagged &#39;slippymap&#39;">slippymap</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jan '13, 11:46</strong></p>
<img src="https://secure.gravatar.com/avatar/f3bdc751fabba825386b4e995ed504ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Orbitaltwist&#39;s gravatar image" />
<p><span>Orbitaltwist</span><br />
<span class="score" title="30 reputation points">30</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Orbitaltwist has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Nov '13, 16:37</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-19156" class="comments-container">
&#10;</div>
<div id="comment-tools-19156" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19156-form-container" class="comment-form-container">
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

<span id="28067"></span>

<div id="answer-container-28067" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28067-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28067-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-28067-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When you say "no errors in the server system" do you mean no errors in your web server's error.log? Because that would be the first point to check. If you get pink tiles but no entries in the error log, then the frontend isn't requesting files from localhost, or the server is misconfigured. If you <em>do</em> get entries in the error log, they will indicate what the problem is.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Nov '13, 22:03</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-28067" class="comments-container">
<span id="28069"></span>
<div id="comment-28069" class="comment">
<div id="post-28069-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>meta: (converted from comment to answer) this is an answer to this question, isn't it? :-) Any further details would be another (more detailed) question.</p>
</div>
<div id="comment-28069-info" class="comment-info">
<span class="comment-age">(13 Nov '13, 22:17)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-28067" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28067-form-container" class="comment-form-container">
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

