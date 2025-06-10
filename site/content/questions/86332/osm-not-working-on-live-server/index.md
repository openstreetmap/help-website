+++
type = "question"
title = "OSM not working on live server"
description = '''My site uses OSM to display a town border with layers to represent differing entities on the map. Everything work great on my local WAMP system but not on the main server. This is the URL for the problem page... MSHolmes Town Article. There are no errors thrown in the console. Any clues as to the so...'''
date = "2022-12-11T02:30:00Z"
lastmod = "2022-12-12T17:02:00Z"
weight = 86332
keywords = [ "maps", "display" ]
aliases = [ "/questions/86332" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM not working on live server](/questions/86332/osm-not-working-on-live-server)

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
<span id="post-86332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86332-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My site uses OSM to display a town border with layers to represent differing entities on the map. Everything work great on my local WAMP system but not on the main server. This is the URL for the problem page... <a href="https://www.msholmes.org/article/1101/htm/lexington-town-map">MSHolmes Town Article</a>.</p>
<p>There are no errors thrown in the console. Any clues as to the solution of the problem are greatly appreciated.</p>
<p>jdadwilson</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-maps" rel="tag" title="see questions tagged &#39;maps&#39;">maps</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Dec '22, 02:30</strong></p>
<img src="https://secure.gravatar.com/avatar/47cd782879a08989369c25cac6004ec2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jdadwilson&#39;s gravatar image" />
<p><span>jdadwilson</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jdadwilson has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86332" class="comments-container">
<span id="86333"></span>
<div id="comment-86333" class="comment">
<div id="post-86333-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Without the source code of the site I suspect that anyone would be guessing.</p>
<p>This seems to be related to <a href="https://community.openstreetmap.org/t/border-for-city-not-found-on-nominatim/6281/19">this forum thread</a>.</p>
</div>
<div id="comment-86333-info" class="comment-info">
<span class="comment-age">(11 Dec '22, 03:32)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-86332" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86332-form-container" class="comment-form-container">
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

<span id="86336"></span>

<div id="answer-container-86336" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86336-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to give your Leaflet (map) div a height.</p>
<p>This is the <code>map_canvas_xl</code> element. At present it doesn't have a height set on it so the map won't display.</p>
<p>If you use CSS to assign it (for example) <code>height: 500px</code> then the map shows up.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Dec '22, 08:59</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-86336" class="comments-container">
<span id="86341"></span>
<div id="comment-86341" class="comment">
<div id="post-86341-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks... now working.</p>
</div>
<div id="comment-86341-info" class="comment-info">
<span class="comment-age">(12 Dec '22, 17:02)</span> <span class="comment-user userinfo">jdadwilson</span>
</div>
</div>
</div>
<div id="comment-tools-86336" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86336-form-container" class="comment-form-container">
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

