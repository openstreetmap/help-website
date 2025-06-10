+++
type = "question"
title = "Nominatim wont compile 64-bit osm2pgsql on Rhel 6.4 64 bit"
description = '''Nominatim wont compile 64-bit osm2pgsql on Rhel 6.4 64 bit i install like this, without errors: ./autogen.sh ./configure --enable-64bit-ids make after install, it works, but when running a planet update, i get &quot;duplicate key violates unique constraint&quot;. I realize its likely caused because my osm2pgs...'''
date = "2013-09-11T20:00:00Z"
lastmod = "2013-10-01T18:07:00Z"
weight = 26296
keywords = [ "osmosis", "6.4", "rhel", "osm2pgsql", "nominatim" ]
aliases = [ "/questions/26296" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim wont compile 64-bit osm2pgsql on Rhel 6.4 64 bit](/questions/26296/nominatim-wont-compile-64-bit-osm2pgsql-on-rhel-64-64-bit)

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
<span id="post-26296-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26296-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26296-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Nominatim wont compile 64-bit osm2pgsql on Rhel 6.4 64 bit</p>
<p>i install like this, without errors: ./autogen.sh ./configure --enable-64bit-ids make</p>
<p>after install, it works, but when running a planet update, i get "duplicate key violates unique constraint".</p>
<p>I realize its likely caused because my osm2pgsql is 32-bit for some reason: [root@blade10 Nominatim-2.0.1]# osm2pgsql/osm2pgsql osm2pgsql SVN version 0.81.0 (32bit id space)</p>
<p>im running rhel 6.4 64 bit</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-6.4" rel="tag" title="see questions tagged &#39;6.4&#39;">6.4</span> <span class="post-tag tag-link-rhel" rel="tag" title="see questions tagged &#39;rhel&#39;">rhel</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Sep '13, 20:00</strong></p>
<img src="https://secure.gravatar.com/avatar/f606a0be81931b140017947c63373bba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmelo&#39;s gravatar image" />
<p><span>mmelo</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmelo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26296" class="comments-container">
&#10;</div>
<div id="comment-tools-26296" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26296-form-container" class="comment-form-container">
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

<span id="26300"></span>

<div id="answer-container-26300" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26300-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26300-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-26300-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mmelo has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try running configure without the <code>--enable-64bit-ids</code> switch. The 2.0.1 release has a bug where using the switch actually results in a 32-bit version being built.</p>
<p>At the moment, it is also strongly recommended to use the development version from github instead of the 2.0.1 version. A new release should follow soon.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Sep '13, 08:27</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-26300" class="comments-container">
<span id="26896"></span>
<div id="comment-26896" class="comment">
<div id="post-26896-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>the new 2.1 release is out and works normally. thanks</p>
</div>
<div id="comment-26896-info" class="comment-info">
<span class="comment-age">(01 Oct '13, 18:07)</span> <span class="comment-user userinfo">mmelo</span>
</div>
</div>
</div>
<div id="comment-tools-26300" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26300-form-container" class="comment-form-container">
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

