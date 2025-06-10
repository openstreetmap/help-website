+++
type = "question"
title = "How check a tile server is working right??"
description = '''I have a server configurated and running. If I try http://server/mod_tile NoResp200: 0 NoResp304: 0 NoResp404: 0 NoResp503: 0 NoResp5XX: 0 NoRespOther: 0 NoFreshCache: 0 NoOldCache: 0 NoVeryOldCache: 0 NoFreshRender: 0 NoOldRender: 0 NoVeryOldRender: 0 NoRespZoom00: 0 NoRespZoom01: 0 NoRespZoom02: 0...'''
date = "2015-02-17T14:03:00Z"
lastmod = "2017-09-30T11:27:00Z"
weight = 41075
keywords = [ "tile_server", "marble", "mapnik", "mod_tile" ]
aliases = [ "/questions/41075" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How check a tile server is working right??](/questions/41075/how-check-a-tile-server-is-working-right)

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
<span id="post-41075-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41075-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41075-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a server configurated and running. If I try <a href="http://server/mod_tile">http://server/mod_tile</a></p>
<pre><code>NoResp200: 0
NoResp304: 0
NoResp404: 0
NoResp503: 0
NoResp5XX: 0
NoRespOther: 0
NoFreshCache: 0
NoOldCache: 0
NoVeryOldCache: 0
NoFreshRender: 0
NoOldRender: 0
NoVeryOldRender: 0
NoRespZoom00: 0
NoRespZoom01: 0
NoRespZoom02: 0
NoRespZoom03: 0
NoRespZoom04: 0
NoRespZoom05: 0
NoRespZoom06: 0
NoRespZoom07: 0
NoRespZoom08: 0
NoRespZoom09: 0
NoRespZoom10: 0
NoRespZoom11: 0
NoRespZoom12: 0
NoRespZoom13: 0
NoRespZoom14: 0
NoRespZoom15: 0
NoRespZoom16: 0
NoRespZoom17: 0
NoRespZoom18: 0
NoTileBufferReads: 0
DurationTileBufferReads: 0
NoTileBufferReadZoom00: 0
DurationTileBufferReadZoom00: 0
NoTileBufferReadZoom01: 0
DurationTileBufferReadZoom01: 0
NoTileBufferReadZoom02: 0
DurationTileBufferReadZoom02: 0
NoTileBufferReadZoom03: 0
DurationTileBufferReadZoom03: 0
NoTileBufferReadZoom04: 0
DurationTileBufferReadZoom04: 0
NoTileBufferReadZoom05: 0
DurationTileBufferReadZoom05: 0
NoTileBufferReadZoom06: 0
DurationTileBufferReadZoom06: 0
NoTileBufferReadZoom07: 0
DurationTileBufferReadZoom07: 0
NoTileBufferReadZoom08: 0
DurationTileBufferReadZoom08: 0
NoTileBufferReadZoom09: 0
DurationTileBufferReadZoom09: 0
NoTileBufferReadZoom10: 0
DurationTileBufferReadZoom10: 0
NoTileBufferReadZoom11: 0
DurationTileBufferReadZoom11: 0
NoTileBufferReadZoom12: 0
DurationTileBufferReadZoom12: 0
NoTileBufferReadZoom13: 0
DurationTileBufferReadZoom13: 0
NoTileBufferReadZoom14: 0
DurationTileBufferReadZoom14: 0
NoTileBufferReadZoom15: 0
DurationTileBufferReadZoom15: 0
NoTileBufferReadZoom16: 0
DurationTileBufferReadZoom16: 0
NoTileBufferReadZoom17: 0
DurationTileBufferReadZoom17: 0
NoTileBufferReadZoom18: 0
DurationTileBufferReadZoom18: 0
NoRes200Layer/osm_tiles/: 0
NoRes404Layer/osm_tiles/: 0</code></pre>
<p>If I try <a href="http://localhost/osm_tiles/0/0/0.png">http://localhost/osm_tiles/0/0/0.png</a></p>
<p>I get a world map image. What I really want is to integrate this tile server with Marble widget, but before doing that I would like to check the renderd and tile_mod are working fine, and they supplay the tiles I need. How can I check this feature?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tile_server" rel="tag" title="see questions tagged &#39;tile_server&#39;">tile_server</span> <span class="post-tag tag-link-marble" rel="tag" title="see questions tagged &#39;marble&#39;">marble</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Feb '15, 14:03</strong></p>
<img src="https://secure.gravatar.com/avatar/b15a888ad4460eeaf0e285c2beaf1dd3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="acerezo&#39;s gravatar image" />
<p><span>acerezo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="acerezo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Feb '15, 14:15</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-41075" class="comments-container">
&#10;</div>
<div id="comment-tools-41075" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41075-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="59895"></span>

<div id="answer-container-59895" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59895-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59895-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59895-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi</p>
<p>I also get the same results as you but the way i test as im still learning is that i built an android app and can zoom in on that to confirm its working, also looking at the task manager shows how busy the computer is</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Sep '17, 11:22</strong></p>
<img src="https://secure.gravatar.com/avatar/bf2467b1454ef10dcb8ab27c0588fca4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jason1975&#39;s gravatar image" />
<p><span>jason1975</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jason1975 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-59895" class="comments-container">
&#10;</div>
<div id="comment-tools-59895" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59895-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="59896"></span>

<div id="answer-container-59896" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59896-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59896-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59896-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>"mod_tile" will normally write tile details to syslog, so something like</p>
<pre><code>tail -f /var/log/syslog | grep &quot; TILE &quot;</code></pre>
<p>should show lots if "START TILE" and "END TILE" (see <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">here</a> for a bit more info).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Sep '17, 11:27</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-59896" class="comments-container">
&#10;</div>
<div id="comment-tools-59896" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59896-form-container" class="comment-form-container">
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

