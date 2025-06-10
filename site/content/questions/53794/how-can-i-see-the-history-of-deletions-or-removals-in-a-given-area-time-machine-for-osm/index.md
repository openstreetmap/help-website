+++
type = "question"
title = "How can I see the history of deletions or removals in a given area?  Time Machine for OSM?"
description = '''I&#x27;m looking at an area where a few prominent trails are missing from the OSM data set. I think they must have been there in the past. I know how to look at given changesets and history of any current way.... but this is different. How can I see and track objects in an area that are now gone? The ans...'''
date = "2017-01-02T06:06:00Z"
lastmod = "2017-01-02T16:38:00Z"
weight = 53794
keywords = [ "changeset", "history" ]
aliases = [ "/questions/53794" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I see the history of deletions or removals in a given area? Time Machine for OSM?](/questions/53794/how-can-i-see-the-history-of-deletions-or-removals-in-a-given-area-time-machine-for-osm)

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
<span id="post-53794-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53794-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53794-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm looking at an area where a few prominent trails are missing from the OSM data set. I think they must have been there in the past.</p>
<p>I know how to look at given changesets and history of any current way.... but this is different. How can I see and track objects in an area that are now gone?</p>
<p>The answers at <a href="https://help.openstreetmap.org/questions/7/how-do-i-see-the-history-for-my-area">https://help.openstreetmap.org/questions/7/how-do-i-see-the-history-for-my-area</a> are focused on a different type of deletion. Some answers refer to a potlatch feature that's no longer current.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jan '17, 06:06</strong></p>
<img src="https://secure.gravatar.com/avatar/372fabe5d3962d54b0c9474e35a05359?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bryce%20C%20Nesbitt&#39;s gravatar image" />
<p><span>Bryce C Nesbitt</span><br />
<span class="score" title="345 reputation points">345</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bryce C Nesbitt has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53794" class="comments-container">
<span id="53800"></span>
<div id="comment-53800" class="comment">
<div id="post-53800-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The "potlatch feature that's no longer current" still works for me, BTW.</p>
</div>
<div id="comment-53800-info" class="comment-info">
<span class="comment-age">(02 Jan '17, 16:38)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-53794" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53794-form-container" class="comment-form-container">
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

<span id="53795"></span>

<div id="answer-container-53795" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53795-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53795-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-53795-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The standard tools for this sort of thing are <a href="http://wiki.openstreetmap.org/wiki/Achavi">Achavi</a> and <a href="http://wiki.openstreetmap.org/wiki/OSM_History_Viewer">Open Histoy Viewer</a>. People who use them regularly get good results with them.</p>
<p>A slightly simpler approach is to use <a href="http://wiki.openstreetmap.org/wiki/Attic_Data">Attic data</a> queries with <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Attic_data_.28.22date.22.29">Overpass</a>, possibly combined with a binary chop over time. In practice if I'm looking for a removed element I can usually remember a time when it was present so dont need to run multiple queries. Once you have the object id it is easy to find when it was deleted.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jan '17, 09:19</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-53795" class="comments-container">
<span id="53798"></span>
<div id="comment-53798" class="comment">
<div id="post-53798-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can also show all GPX traces with potlatch2 and probably JOSM which may help if public traces have been uploaded.</p>
</div>
<div id="comment-53798-info" class="comment-info">
<span class="comment-age">(02 Jan '17, 15:56)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-53795" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53795-form-container" class="comment-form-container">
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

