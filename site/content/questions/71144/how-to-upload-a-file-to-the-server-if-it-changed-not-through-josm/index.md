+++
type = "question"
title = "How to upload a file to the server if it changed not through JOSM?"
description = '''I changed the .osm file using a bot (I found and recorded addresses, observing the file structure), but I can’t upload it to the server via JOSM, the program says that there are no changes, and there 95% of the city is marked (it was ~ 5%). How can I update the file on the server?'''
date = "2019-10-13T08:45:00Z"
lastmod = "2019-10-14T00:04:00Z"
weight = 71144
keywords = [ "josm" ]
aliases = [ "/questions/71144" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to upload a file to the server if it changed not through JOSM?](/questions/71144/how-to-upload-a-file-to-the-server-if-it-changed-not-through-josm)

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
<span id="post-71144-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71144-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71144-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I changed the .osm file using a bot (I found and recorded addresses, observing the file structure), but I can’t upload it to the server via JOSM, the program says that there are no changes, and there 95% of the city is marked (it was ~ 5%). How can I update the file on the server?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Oct '19, 08:45</strong></p>
<img src="https://secure.gravatar.com/avatar/e73b2932c544f015401e4cab1267282b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kivdev&#39;s gravatar image" />
<p><span>Kivdev</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kivdev has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71144" class="comments-container">
<span id="71152"></span>
<div id="comment-71152" class="comment">
<div id="post-71152-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Where did you 'find' these addresses?</p>
</div>
<div id="comment-71152-info" class="comment-info">
<span class="comment-age">(14 Oct '19, 00:04)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-71144" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71144-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="71146"></span>

<div id="answer-container-71146" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71146-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-71146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Do <em>not</em> upload an automatically modified file to OSM without following the guidelines for mechanical edits (<a href="https://wiki.openstreetmap.org/wiki/Automated_Edits_code_of_conduct),">https://wiki.openstreetmap.org/wiki/Automated_Edits_code_of_conduct),</a> otherwise your edits will be reverted again.</p>
<p>Most importantly:</p>
<ul>
<li>discuss your changes in the relevant community</li>
<li>double check that the license of any third party data you used is compatible with OSM</li>
<li>double check that the tags and values you are using comply with community standards</li>
</ul>
<p>Technically, if you want JOSM to upload your data, you will probably have to add a "modified=true" XML attribute to the node/way/relation XML nodes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Oct '19, 11:04</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-71146" class="comments-container">
&#10;</div>
<div id="comment-tools-71146" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71146-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71145"></span>

<div id="answer-container-71145" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71145-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71145-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71145-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Osmconvert#Windows">https://wiki.openstreetmap.org/wiki/Osmconvert#Windows</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Oct '19, 10:28</strong></p>
<img src="https://secure.gravatar.com/avatar/e73b2932c544f015401e4cab1267282b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kivdev&#39;s gravatar image" />
<p><span>Kivdev</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kivdev has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71145" class="comments-container">
&#10;</div>
<div id="comment-tools-71145" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71145-form-container" class="comment-form-container">
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

