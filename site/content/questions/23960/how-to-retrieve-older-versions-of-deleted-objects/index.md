+++
type = "question"
title = "How to retrieve older versions of deleted objects?"
description = '''http://www.openstreetmap.org/browse/way/211750802 this way was deleted. i want to see the first version of this but http://www.openstreetmap.org/browse/way/211750802/1 gives file not found.'''
date = "2013-07-04T10:13:00Z"
lastmod = "2013-07-04T10:26:00Z"
weight = 23960
keywords = [ "deleted", "version", "old" ]
aliases = [ "/questions/23960" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to retrieve older versions of deleted objects?](/questions/23960/how-to-retrieve-older-versions-of-deleted-objects)

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
<span id="post-23960-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23960-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23960-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><a href="http://www.openstreetmap.org/browse/way/211750802">http://www.openstreetmap.org/browse/way/211750802</a> this way was deleted.</p>
<p>i want to see the first version of this but <a href="http://www.openstreetmap.org/browse/way/211750802/1">http://www.openstreetmap.org/browse/way/211750802/1</a> gives file not found.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-deleted" rel="tag" title="see questions tagged &#39;deleted&#39;">deleted</span> <span class="post-tag tag-link-version" rel="tag" title="see questions tagged &#39;version&#39;">version</span> <span class="post-tag tag-link-old" rel="tag" title="see questions tagged &#39;old&#39;">old</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jul '13, 10:13</strong></p>
<img src="https://secure.gravatar.com/avatar/651103e616e49724bb139f1a3e0a1a39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amritkarma&#39;s gravatar image" />
<p><span>amritkarma</span><br />
<span class="score" title="684 reputation points">684</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amritkarma has one accepted answer">11%</span></p>
</div>
</div>
<div id="comments-container-23960" class="comments-container">
&#10;</div>
<div id="comment-tools-23960" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23960-form-container" class="comment-form-container">
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

<span id="23962"></span>

<div id="answer-container-23962" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23962-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23962-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-23962-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The browse pages on openstreetmap.org don't allow you to see individual versions of objects like the API does. You can view the entire history of an object by appending <code>/history</code> to its URI, like this: <a href="http://www.openstreetmap.org/browse/way/211750802/history">http://www.openstreetmap.org/browse/way/211750802/history</a>.</p>
<p>If you accidentally delete data like this, you have <a href="http://wiki.openstreetmap.org/wiki/Change_rollback">a number of options available</a>:</p>
<ul>
<li>If you haven't closed your editor (JOSM in your case) you may be able to use its Undo function to restore the deleted data, then re-upload</li>
<li>If you realise you've accidentally deleted data after closing JOSM, you can use the <a href="http://wiki.openstreetmap.org/wiki/JOSM/Plugins/Reverter">Reverter plug-in</a> to restore it</li>
<li>If you're not comfortable doing this, or can't get it working, ask on the <a href="http://lists.openstreetmap.org/listinfo/talk">Talk mailing list</a> or the <a href="http://irc.openstreetmap.org/">IRC channel</a> where an experienced mapper may be able to help you revert your mistakes.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jul '13, 10:26</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonathan Bennett has 21 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-23962" class="comments-container">
&#10;</div>
<div id="comment-tools-23962" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23962-form-container" class="comment-form-container">
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

