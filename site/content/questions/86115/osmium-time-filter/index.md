+++
type = "question"
title = "Osmium time-filter"
description = '''I would like to filter an OSM history file by time first. However, I still need the history of each object. Osmium time-filter is an option. Unfortunately it only works to retrieve the status at a specific datum. The To-Time time does not work osmium timefilter -o europa.osh.pbf /Users/.../.../europ...'''
date = "2022-11-08T10:24:00Z"
lastmod = "2022-11-08T14:57:00Z"
weight = 86115
keywords = [ "osmium", "history", "time" ]
aliases = [ "/questions/86115" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Osmium time-filter](/questions/86115/osmium-time-filter)

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
<span id="post-86115-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86115-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86115-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to filter an OSM history file by time first. However, I still need the history of each object. Osmium time-filter is an option. Unfortunately it only works to retrieve the status at a specific datum. The To-Time time does not work</p>
<p>osmium timefilter -o europa.osh.pbf /Users/.../.../europe-internal.osh.pbf.download 2000-01-01T00:00:00Z 2010-01-01T00:00:00Z</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span> <span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Nov '22, 10:24</strong></p>
<img src="https://secure.gravatar.com/avatar/a44ac9f77b803b607b9ed5268918fe32?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="max92ue&#39;s gravatar image" />
<p><span>max92ue</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="max92ue has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Nov '22, 10:41</strong> </span></p>
</div>
</div>
<div id="comments-container-86115" class="comments-container">
&#10;</div>
<div id="comment-tools-86115" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86115-form-container" class="comment-form-container">
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

<span id="86120"></span>

<div id="answer-container-86120" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86120-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86120-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86120-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The to-time should work fine. The command line you quote has several errors in them, maybe that's the reason it doesn't work for you? The command is "time-filter", not "timefilter", and the filename ending in <code>.download</code> will also not work, because the file type can't be detected, if you rename the file to <code>.osh.pbf</code> it should work.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Nov '22, 14:57</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-86120" class="comments-container">
&#10;</div>
<div id="comment-tools-86120" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86120-form-container" class="comment-form-container">
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

