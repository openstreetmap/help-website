+++
type = "question"
title = "Find relation by number of members"
description = '''In an own map I have a special relation type which only makes sense with at least two members, one in the role left and one in the role right. So to find critical relations it would be a good first approach to filter all relations with only one member. Is this possible, like tags:5-10? A little bit ...'''
date = "2013-04-29T09:10:00Z"
lastmod = "2013-04-29T09:10:00Z"
weight = 21962
keywords = [ "josm", "find" ]
aliases = [ "/questions/21962" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Find relation by number of members](/questions/21962/find-relation-by-number-of-members)

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
<span id="post-21962-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21962-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21962-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In an own map I have a special relation type which only makes sense with at least two members, one in the role <code>left</code> and one in the role <code>right</code>. So to find critical relations it would be a good first approach to filter all relations with only one member. Is this possible, like <code>tags:5-10</code>?</p>
<p>A little bit more advanced was my approach was to select all relations, and then remove the ones with this kind of member configuration:</p>
<p><code>parent role:left child role:right parent</code>, but this expression seems to be odd (at least after the <code>parent role:left</code> part.</p>
<p>Basic idea:</p>
<ul>
<li>select all members in the role <code>right</code></li>
<li>select their parents (=relations)</li>
<li>from those relations, select all children <code>role=left</code></li>
<li>again, select their parents.</li>
</ul>
<p>Can someone there give me a hint?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-find" rel="tag" title="see questions tagged &#39;find&#39;">find</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Apr '13, 09:10</strong></p>
<img src="https://secure.gravatar.com/avatar/62ad8307fa020dc2edf77a6c64066eee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="philipp&#39;s gravatar image" />
<p><span>philipp</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="philipp has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Apr '13, 09:13</strong> </span></p>
</div>
</div>
<div id="comments-container-21962" class="comments-container">
&#10;</div>
<div id="comment-tools-21962" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21962-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

