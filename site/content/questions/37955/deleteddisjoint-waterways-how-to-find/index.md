+++
type = "question"
title = "Deleted/disjoint waterways - how to find?"
description = '''Is there a way of finding waterways which have been deleted during the redaction process? (usually waterway=stream) I have been checking waterways using OSMi, and have found a lot of them deleted by the redaction bot during the license change in 2012. Now, this means that the water network is disjoi...'''
date = "2014-10-25T21:41:00Z"
lastmod = "2015-12-07T11:51:00Z"
weight = 37955
keywords = [ "waterway", "redaction" ]
aliases = [ "/questions/37955" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Deleted/disjoint waterways - how to find?](/questions/37955/deleteddisjoint-waterways-how-to-find)

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
<span id="post-37955-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37955-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37955-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way of finding <em>waterways</em> which have been deleted during the redaction process? (usually waterway=stream)</p>
<p>I have been checking waterways using OSMi, and have found a lot of them deleted by the redaction bot during the license change in 2012. Now, this means that the water network is disjointed in the map; unlike highways, this has gone unnoticed for so long that I can't find any post-redaction QA tools.</p>
<p>An example to clarify:</p>
<ul>
<li>2012: situation out in the terrain: Stream A flows into Stream B; Stream B flows into River C.</li>
<li>situation in OSM: everything mapped, but the mapper of Stream B did not agree with the new license.</li>
<li><p>the redaction bot cometh, and deletes Stream B (this is expected behavior, and I'm not asking about this)</p></li>
<li><p>2014: in the terrain, Stream A still flows into Stream B, which flows into River C</p></li>
<li>in the map, Stream A now does not flow into anything, it just ends; it is not connected in any way with River C</li>
<li>I want to find these situations and resurvey, so that OSM mirrors reality again :)</li>
<li>This seems to be a very common occurence around [50N,15E], so I'm looking for something more robust than "just look at the map and see if it seems weird"</li>
<li>(Some sort of graph traversal comes to mind?)</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-waterway" rel="tag" title="see questions tagged &#39;waterway&#39;">waterway</span> <span class="post-tag tag-link-redaction" rel="tag" title="see questions tagged &#39;redaction&#39;">redaction</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Oct '14, 21:41</strong></p>
<img src="https://secure.gravatar.com/avatar/8200fa5c0cc8feb096558c5972a6191c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Piskvor&#39;s gravatar image" />
<p><span>Piskvor</span><br />
<span class="score" title="1266 reputation points"><span>1.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Piskvor has 9 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Oct '14, 10:33</strong> </span></p>
</div>
</div>
<div id="comments-container-37955" class="comments-container">
&#10;</div>
<div id="comment-tools-37955" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37955-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="37959"></span>

<div id="answer-container-37959" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37959-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37959-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-37959-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Piskvor has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As far as I know we had post-redaction tools which showed where the bot was active, but I currently do not remember them, and I guess they may be shut down already (redaction is quite some time ago).</p>
<p>These <em>general</em> QA tools may help: (the one which you already used …) <a href="http://tools.geofabrik.de/osmi/?view=water&amp;lon=90.84424&amp;lat=15.65447&amp;zoom=1&amp;overlays=bodies_of_water,broken_bow,vmap0_rivers,long_rivers,waterways_river,waterways_stream,waterways_drain,waterways_canal,waterways_riverbank,waterways_other,waterways_width,waterways_in_tunnels,waterways_on_bridges,waterways_without_names,waterway_nodes,coastline,simple_islands,coastline_nodes,rivermouths,coastline_not_simple,coastline_unconnected">OSMI for waterways</a> (makes it much easier to see and follow the waterways) and (for central/eastern Europe around Germany) <a href="http://www.kompf.de/gps/rivermap.html">Martin Kompf's rivermap</a> (disjoint rivers are grey) may help.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '14, 23:21</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Oct '14, 13:00</strong> </span></p>
</div>
</div>
<div id="comments-container-37959" class="comments-container">
<span id="37994"></span>
<div id="comment-37994" class="comment">
<div id="post-37994-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I have initially discovered the issue while using OSMi; the rivermap seems to be the tool I'm looking for. Thank you!</p>
</div>
<div id="comment-37994-info" class="comment-info">
<span class="comment-age">(27 Oct '14, 10:22)</span> <span class="comment-user userinfo">Piskvor</span>
</div>
</div>
</div>
<div id="comment-tools-37959" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37959-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47029"></span>

<div id="answer-container-47029" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47029-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47029-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47029-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A new set of inspections is now available in the OSMi Water layer, which also addresses this type of error: <a href="http://tools.geofabrik.de/osmi/?view=water">http://tools.geofabrik.de/osmi/?view=water</a></p>
<p>( See also the blog post: <a href="http://blog.geofabrik.de/en/?p=323">http://blog.geofabrik.de/en/?p=323</a> )</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Dec '15, 11:51</strong></p>
<img src="https://secure.gravatar.com/avatar/8200fa5c0cc8feb096558c5972a6191c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Piskvor&#39;s gravatar image" />
<p><span>Piskvor</span><br />
<span class="score" title="1266 reputation points"><span>1.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Piskvor has 9 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-47029" class="comments-container">
&#10;</div>
<div id="comment-tools-47029" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47029-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="37957"></span>

<div id="answer-container-37957" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37957-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37957-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-37957-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Piskvor, if the rivers or streams are removed by the BOT it has to be. The mappers who made them in OSM failed to subscribe to the new rules so the DATA could not be continued. I dont expect them to get a restoration. It would create the unlicensed import of DATA. Could you still provide a link to the region ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '14, 23:01</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Oct '14, 23:02</strong> </span></p>
</div>
</div>
<div id="comments-container-37957" class="comments-container">
<span id="37958"></span>
<div id="comment-37958" class="comment">
<div id="post-37958-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>as I understand it, the question is not about the undeletion/reverting of the bot but to just know where approximately the bot edited waterways and to re-map the waterways then from scratch (with own survey or bing). This may be okay, even without a agreement of the original mappers.</p>
</div>
<div id="comment-37958-info" class="comment-info">
<span class="comment-age">(25 Oct '14, 23:11)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="37993"></span>
<div id="comment-37993" class="comment">
<div id="post-37993-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, I may have been unclear: I'm not trying to restore the deleted <em>data</em>; I'm quite aware they were deleted for a reason. I'm trying to find what <em>really existing</em> features were deleted, so I can resurvey them.</p>
</div>
<div id="comment-37993-info" class="comment-info">
<span class="comment-age">(27 Oct '14, 10:21)</span> <span class="comment-user userinfo">Piskvor</span>
</div>
</div>
</div>
<div id="comment-tools-37957" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37957-form-container" class="comment-form-container">
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

