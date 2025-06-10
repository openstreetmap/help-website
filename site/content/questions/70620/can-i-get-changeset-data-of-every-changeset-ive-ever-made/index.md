+++
type = "question"
title = "Can I get changeset data of every changeset I&#x27;ve ever made?"
description = '''Hi everyone, I don&#x27;t know how it&#x27;s called exactly but I want, for every changeset my OSM account has uploaded:  the changeset ID the changeset date the number of changes in the changeset the changeset comment the source and if possible, the changeset bounding box  Is it possible to get these? Thanks...'''
date = "2019-09-04T07:13:00Z"
lastmod = "2019-09-04T09:13:00Z"
weight = 70620
keywords = [ "changeset", "metadata" ]
aliases = [ "/questions/70620" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can I get changeset data of every changeset I've ever made?](/questions/70620/can-i-get-changeset-data-of-every-changeset-ive-ever-made)

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
<span id="post-70620-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70620-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70620-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone, I don't know how it's called exactly but I want, for every changeset my OSM account has uploaded:</p>
<ul>
<li>the changeset ID</li>
<li>the changeset date</li>
<li>the number of changes in the changeset</li>
<li>the changeset comment</li>
<li>the source</li>
<li>and if possible, the changeset bounding box</li>
</ul>
<p>Is it possible to get these?</p>
<p>Thanks for your help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-metadata" rel="tag" title="see questions tagged &#39;metadata&#39;">metadata</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Sep '19, 07:13</strong></p>
<img src="https://secure.gravatar.com/avatar/15d45a99f101e06c9e79916af33f8336?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Privatemajory&#39;s gravatar image" />
<p><span>Privatemajory</span><br />
<span class="score" title="1125 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Privatemajory has 4 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-70620" class="comments-container">
&#10;</div>
<div id="comment-tools-70620" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70620-form-container" class="comment-form-container">
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

<span id="70622"></span>

<div id="answer-container-70622" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70622-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70622-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-70622-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Privatemajory has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can download all changesets from planet.osm.org. The file <a href="https://planet.openstreetmap.org/planet/changesets-latest.osm.bz2">https://planet.openstreetmap.org/planet/changesets-latest.osm.bz2</a> is updated once a week. It currently has 2.8 GByte!</p>
<p>Then you can filter this file using <a href="https://osmcode.org/osmium-tool/">osmium-tool</a>. The <a href="https://docs.osmcode.org/osmium/latest/osmium-changeset-filter.html">changeset-filter</a> command can filter by user id or user name.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Sep '19, 08:22</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-70622" class="comments-container">
<span id="70623"></span>
<div id="comment-70623" class="comment">
<div id="post-70623-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. I'll see if I'll be able to download then mess with that gigantic file.</p>
</div>
<div id="comment-70623-info" class="comment-info">
<span class="comment-age">(04 Sep '19, 09:13)</span> <span class="comment-user userinfo">Privatemajory</span>
</div>
</div>
</div>
<div id="comment-tools-70622" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70622-form-container" class="comment-form-container">
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

