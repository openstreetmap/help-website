+++
type = "question"
title = "JOSM Changefile Backup"
description = '''I did a lot of work today in JOSM and I was regularly uploading my changes to OSM (or so I thought). After every upload JOSM would notify me that there was something not synchronised with my local data, it would ask me to synchronise, I would click yes, it would do stuff and I thought everything had...'''
date = "2020-05-14T22:19:00Z"
lastmod = "2020-05-15T14:38:00Z"
weight = 74819
keywords = [ "josm" ]
aliases = [ "/questions/74819" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM Changefile Backup](/questions/74819/josm-changefile-backup)

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
<span id="post-74819-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74819-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74819-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I did a lot of work today in JOSM and I was regularly uploading my changes to OSM (or so I thought). After every upload JOSM would notify me that there was something not synchronised with my local data, it would ask me to synchronise, I would click yes, it would do stuff and I thought everything had been taken care of.</p>
<p>At the end of the day I closed JOSM after uploading my final changes and was met with a surprising 'do you want to save your changes?' screen. I thought... well no because I've uploaded them all. However checking OSM, none of today's changes have been made. (Probably eight hours of work).</p>
<p>Is there any way I could recover the data? I'm thinking something along the lines of a changeset being stored somewhere or other when it met its errors with synchronisation.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 May '20, 22:19</strong></p>
<img src="https://secure.gravatar.com/avatar/19d95386711430cdb0d54618ebaeb54a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="owenward&#39;s gravatar image" />
<p><span>owenward</span><br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="owenward has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74819" class="comments-container">
<span id="74827"></span>
<div id="comment-74827" class="comment">
<div id="post-74827-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If JOSM complains about unsynchronized data on upload you need to synchronize it and then upload your changes again. The upload can't succeed if the data is not synchronized.</p>
</div>
<div id="comment-74827-info" class="comment-info">
<span class="comment-age">(15 May '20, 10:12)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="74830"></span>
<div id="comment-74830" class="comment">
<div id="post-74830-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's best to manually save a local copy to be extra safe. The text content gets compressed efficiently. The file size doesn't pile up.</p>
</div>
<div id="comment-74830-info" class="comment-info">
<span class="comment-age">(15 May '20, 12:46)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-74819" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74819-form-container" class="comment-form-container">
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

<span id="74824"></span>

<div id="answer-container-74824" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74824-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74824-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-74824-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can check if there is an autosaved file in the autosave subdirectory of the JOSM preferences folder:</p>
<p><a href="https://josm.openstreetmap.de/wiki/Help/Preferences#JOSMpreferencedatacachedirectories">https://josm.openstreetmap.de/wiki/Help/Preferences#JOSMpreferencedatacachedirectories</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 May '20, 23:57</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-74824" class="comments-container">
<span id="74834"></span>
<div id="comment-74834" class="comment">
<div id="post-74834-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I checked... nothing there unfortunately.</p>
</div>
<div id="comment-74834-info" class="comment-info">
<span class="comment-age">(15 May '20, 14:38)</span> <span class="comment-user userinfo">owenward</span>
</div>
</div>
</div>
<div id="comment-tools-74824" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74824-form-container" class="comment-form-container">
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

