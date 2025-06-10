+++
type = "question"
title = "error while opening file 2048"
description = '''Hi, I am trying to append a dataset to existing map data using below mentioned command. But I am getting an error. San somebody help me to resolve this? Command: sudo -u www-data osm2pgsql -a 2048 --slim --number-processes 4 gcc-states-latest.osm.pbf --cache-strategy sparse Error: Reading in file: 2...'''
date = "2016-02-10T06:20:00Z"
lastmod = "2016-02-10T08:31:00Z"
weight = 48031
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/48031" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [error while opening file 2048](/questions/48031/error-while-opening-file-2048)

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
<span id="post-48031-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48031-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48031-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am trying to append a dataset to existing map data using below mentioned command. But I am getting an error. San somebody help me to resolve this?</p>
<p>Command: sudo -u www-data osm2pgsql -a 2048 --slim --number-processes 4 gcc-states-latest.osm.pbf --cache-strategy sparse</p>
<p>Error: Reading in file: 2048 error while opening file 2048</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Feb '16, 06:20</strong></p>
<img src="https://secure.gravatar.com/avatar/1a9eea008bc0c9a26985aa042d9b8ac2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Reshma%20Maner&#39;s gravatar image" />
<p><span>Reshma Maner</span><br />
<span class="score" title="235 reputation points">235</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Reshma Maner has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Feb '16, 08:15</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-48031" class="comments-container">
&#10;</div>
<div id="comment-tools-48031" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48031-form-container" class="comment-form-container">
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

<span id="48032"></span>

<div id="answer-container-48032" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48032-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48032-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-48032-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SimonPoole has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You seem to have your command line mixed up see <a href="https://github.com/openstreetmap/osm2pgsql/blob/master/docs/usage.md">https://github.com/openstreetmap/osm2pgsql/blob/master/docs/usage.md</a> in particular the append option simply uses the normal input file that you have already specified (gcc-states-latest.osm.pbf).</p>
<p>Note: appending to an existing osm2pgsql schema database will only work if their are no common elements in the data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Feb '16, 08:13</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-48032" class="comments-container">
<span id="48033"></span>
<div id="comment-48033" class="comment">
<div id="post-48033-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes. Thanks. Issue is resolved now.</p>
</div>
<div id="comment-48033-info" class="comment-info">
<span class="comment-age">(10 Feb '16, 08:31)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
</div>
<div id="comment-tools-48032" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48032-form-container" class="comment-form-container">
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

