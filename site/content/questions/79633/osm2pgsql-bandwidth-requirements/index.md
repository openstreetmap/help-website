+++
type = "question"
title = "osm2pgsql bandwidth requirements?"
description = '''Hi there! I&#x27;ve been mapping for a few years and now i would like to try rendering my own tiles, since none of the tiles out there really satisfy me; i will of course release the style as open source and make the tiles publicly accessible when done (i doubt anybody will ever be interested, but that&#x27;s...'''
date = "2021-04-12T22:14:00Z"
lastmod = "2021-04-13T11:38:00Z"
weight = 79633
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/79633" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql bandwidth requirements?](/questions/79633/osm2pgsql-bandwidth-requirements)

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
<span id="post-79633-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79633-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79633-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there!</p>
<p>I've been mapping for a few years and now i would like to try rendering my own tiles, since none of the tiles out there really satisfy me; i will of course release the style as open source and make the tiles publicly accessible when done (i doubt anybody will ever be interested, but that's not the point).</p>
<p>By looking at osm2pgsql manual and documentation, looks like anyone is assuming that osm2pgsql and postgresql will be living in the same server. In my case, i need two separate servers because of hardware limitations.</p>
<p>Does anybody know how much bandwith will i need between osm2pgsql and postgresql?</p>
<p>Thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Apr '21, 22:14</strong></p>
<img src="https://secure.gravatar.com/avatar/5e2d16c25d614101fc8a31ce4868ea8f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaRkBoDoM&#39;s gravatar image" />
<p><span>DaRkBoDoM</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaRkBoDoM has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79633" class="comments-container">
<span id="79634"></span>
<div id="comment-79634" class="comment">
<div id="post-79634-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Your question is a bit "how long is a piece of string", because without know what data you're loading, what tile style you're using and what usage of osm2pgsql you're actually asking about (Initial data load? Database updates?).</p>
</div>
<div id="comment-79634-info" class="comment-info">
<span class="comment-age">(12 Apr '21, 22:20)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="79635"></span>
<div id="comment-79635" class="comment">
<div id="post-79635-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>At the moment, i am loading only a 1Gb test pbf file; i would like to be able to load the whole world someday, but it depends on system requirements in the end.</p>
<p>So, let's assume a 1Gb initial data load with default (carto) stylesheet as my "standard" example. How much bandwidth will it need approximately?</p>
</div>
<div id="comment-79635-info" class="comment-info">
<span class="comment-age">(12 Apr '21, 22:28)</span> <span class="comment-user userinfo">DaRkBoDoM</span>
</div>
</div>
</div>
<div id="comment-tools-79633" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79633-form-container" class="comment-form-container">
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

<span id="79636"></span>

<div id="answer-container-79636" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79636-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79636-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-79636-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I cannot give you concrete numbers but it is usually not the bandwidth but the latency that will kill you. Nowadays you cannot even run a world-wide tile server on a server that has spinning hard disks, it is just too slow - you need SSD/NVMe disks and ideally local disks, not network drives. Running postgres on a separate physical machine with anything less than 10 GBit ethernet will certainly be painfully slow. Maybe if you can give us more information about the available hardware we can make a recommendation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '21, 23:19</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-79636" class="comments-container">
<span id="79639"></span>
<div id="comment-79639" class="comment">
<div id="post-79639-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! That's a close enough call. I had no idea on how many query and how intensive osm2pgsql is. My plan was to run the dbms through a 10Mbit internet link… looks like it is definitely not doable, even if i will be the only user.</p>
</div>
<div id="comment-79639-info" class="comment-info">
<span class="comment-age">(13 Apr '21, 11:05)</span> <span class="comment-user userinfo">DaRkBoDoM</span>
</div>
</div>
<span id="79640"></span>
<div id="comment-79640" class="comment">
<div id="post-79640-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It would "work" of course but you'd probably be sat there waiting 20 seconds for a tile to appear. Can you not install rendering software on the same machine that runs the DB?</p>
</div>
<div id="comment-79640-info" class="comment-info">
<span class="comment-age">(13 Apr '21, 11:38)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-79636" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79636-form-container" class="comment-form-container">
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

