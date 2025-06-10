+++
type = "question"
title = "Merge generated JOSM with OSM data conflicts"
description = '''I have some official building plans that were converted to OSM format for a certain building complex. I wanted to have them replace the current buildings in OSM (and also add ones that weren&#x27;t there yet) because they are more accurate. I wrote a short script that compares the buildings as shapes and...'''
date = "2013-11-14T17:09:00Z"
lastmod = "2013-11-14T19:46:00Z"
weight = 28109
keywords = [ "josm", "merge", "diff" ]
aliases = [ "/questions/28109" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Merge generated JOSM with OSM data conflicts](/questions/28109/merge-generated-josm-with-osm-data-conflicts)

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
<span id="post-28109-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28109-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28109-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have some official building plans that were converted to OSM format for a certain building complex. I wanted to have them replace the current buildings in OSM (and also add ones that weren't there yet) because they are more accurate. I wrote a short script that compares the buildings as shapes and then creates a JOSM file that replaces certain buildings that were deemed to be matches with my data. I then plan to manually clean it up and make sure it is fit for submission.</p>
<p>I want to be able to apply these this generated file to OSM. The file has additions modifications and deletions. If I open the generated file, then download the OSM data, it seems to merge them, but there's conflicts. If I try to resolve the conflicts, only the way is deleted, not the nodes. Any way I can have everything deleted (I have the nodes marked as "delete" in the JOSM file).</p>
<p>EDIT: Here's some screenshots documenting what's going on. <a href="http://imgur.com/a/yAYyo">http://imgur.com/a/yAYyo</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span> <span class="post-tag tag-link-diff" rel="tag" title="see questions tagged &#39;diff&#39;">diff</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Nov '13, 17:09</strong></p>
<img src="https://secure.gravatar.com/avatar/82ca299d632dcf182650afd85a20474a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mwr54&#39;s gravatar image" />
<p><span>mwr54</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mwr54 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Nov '13, 17:40</strong> </span></p>
</div>
</div>
<div id="comments-container-28109" class="comments-container">
&#10;</div>
<div id="comment-tools-28109" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28109-form-container" class="comment-form-container">
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

<span id="28113"></span>

<div id="answer-container-28113" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28113-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28113-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28113-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I fixed my own problem after tinkering with it for awhile. You have to include all the attributes for the element you want to delete. I just had the id and version initially.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Nov '13, 19:46</strong></p>
<img src="https://secure.gravatar.com/avatar/82ca299d632dcf182650afd85a20474a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mwr54&#39;s gravatar image" />
<p><span>mwr54</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mwr54 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-28113" class="comments-container">
&#10;</div>
<div id="comment-tools-28113" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28113-form-container" class="comment-form-container">
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

