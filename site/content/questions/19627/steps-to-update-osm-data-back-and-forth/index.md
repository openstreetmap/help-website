+++
type = "question"
title = "Steps to update osm data back and forth?"
description = '''I have both a PostGIS database with OSM data imported, and the same data in a SHP folder. By adding missing information to the downloaded OSM data, both in SHP and PostGIS, I&#x27;d be able to contribute with the project. If I need to also update my server from an OSM periodical diff, which would be the ...'''
date = "2013-02-06T18:38:00Z"
lastmod = "2013-02-06T20:48:00Z"
weight = 19627
keywords = [ "osm", "update" ]
aliases = [ "/questions/19627" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Steps to update osm data back and forth?](/questions/19627/steps-to-update-osm-data-back-and-forth)

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
<span id="post-19627-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19627-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19627-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have both a PostGIS database with OSM data imported, and the same data in a SHP folder.</p>
<p>By adding missing information to the downloaded OSM data, both in SHP and PostGIS, I'd be able to contribute with the project.</p>
<p>If I need to also update my server from an OSM periodical diff, which would be the correct sequence of tasks? (I'm assuming that there is new info in OSM to download and new info on my server to upload, and that would be happening regularly).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Feb '13, 18:38</strong></p>
<img src="https://secure.gravatar.com/avatar/52b57b1070fcc5139ba97f14c70a8bc5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Martin0x777&#39;s gravatar image" />
<p><span>Martin0x777</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Martin0x777 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19627" class="comments-container">
&#10;</div>
<div id="comment-tools-19627" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19627-form-container" class="comment-form-container">
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

<span id="19637"></span>

<div id="answer-container-19637" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19637-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19637-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-19637-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Martin0x777 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Both the Shape Files and the PostGIS database - assuming you're using an osm2pgsql or Imposm import - are data reduced; you cannot extract the orginal OSM data from it any more. Therefore, if you add data to your shape file or PostGIS, it will be very difficult to upload that enhancement in OSM. You would need a program that does roughly this:</p>
<ol>
<li>user has updated an object in the shape file</li>
<li>find out which OSM object(s) have been used to create that shape object</li>
<li>find out what changes have to be made to these object to reflect the update</li>
<li>download latest version of the object and make sure we're not accidentally overwriting someone else's change</li>
<li>upload a changeset that reflects the update</li>
</ol>
<p>Some people who want to run continuous imports have done some work in that direction but there's no plug and play solution for your problem.</p>
<p>The best way to edit OSM is via one of the major editors, JOSM or Potlatch.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Feb '13, 20:48</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Feb '13, 20:48</strong> </span></p>
</div>
</div>
<div id="comments-container-19637" class="comments-container">
&#10;</div>
<div id="comment-tools-19637" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19637-form-container" class="comment-form-container">
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

