+++
type = "question"
title = "JOSM Purge downloaded area"
description = '''I accidentally downloaded a region separate from the area I want to edit in the current file. I was able to purge the objects using the &quot;Purge&quot; action, but it still tries to re-download the area when I use &quot;Update data&quot;. Can I somehow mark the area un-downloaded? See the black rectangle in the top r...'''
date = "2022-11-19T12:27:00Z"
lastmod = "2022-11-21T22:55:00Z"
weight = 86188
keywords = [ "download", "josm", "purge" ]
aliases = [ "/questions/86188" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM Purge downloaded area](/questions/86188/josm-purge-downloaded-area)

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
<span id="post-86188-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86188-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86188-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I accidentally downloaded a region separate from the area I want to edit in the current file.</p>
<p>I was able to purge the objects using the "Purge" action, but it still tries to re-download the area when I use "Update data". Can I somehow mark the area un-downloaded?</p>
<p>See the black rectangle in the top right of the screenshot:</p>
<p><img src="https://help.openstreetmap.org/upfiles/Screenshot_20221119_132153.png" alt="screenshot" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-purge" rel="tag" title="see questions tagged &#39;purge&#39;">purge</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Nov '22, 12:27</strong></p>
<img src="https://secure.gravatar.com/avatar/09f491ff872d3ed578d7e246d1bf30cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xerusf&#39;s gravatar image" />
<p><span>xerusf</span><br />
<span class="score" title="76 reputation points">76</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xerusf has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-86188" class="comments-container">
&#10;</div>
<div id="comment-tools-86188" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86188-form-container" class="comment-form-container">
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

<span id="86196"></span>

<div id="answer-container-86196" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86196-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86196-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86196-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/JOSM_file_format">JOSM stores</a> the download area in a <code>bounds</code> tag within the *.OSM file on save. I don't know of a way to remove one of these without saving the file to desktop, finding the offending bounding box in a text editor, deleting it and then saving and reopening the file in JOSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Nov '22, 22:55</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Nov '22, 22:56</strong> </span></p>
</div>
</div>
<div id="comments-container-86196" class="comments-container">
&#10;</div>
<div id="comment-tools-86196" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86196-form-container" class="comment-form-container">
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

