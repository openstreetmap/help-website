+++
type = "question"
title = "iD editor: Copy a line in place"
description = '''Let&#x27;s say there is a twisty trail, miles and miles long, along a continental divide. Let&#x27;s also say a new country is born, Bogusania, whose boundary happens to coincide with this trail. Alas, I cannot just do CTRL+C CTRL+V to get a copy of this trail(&#x27;s nodes) right in the same place, for my new bou...'''
date = "2019-12-12T22:29:00Z"
lastmod = "2019-12-14T01:33:00Z"
weight = 72089
keywords = [ "ideditor", "copy-paste", "lines" ]
aliases = [ "/questions/72089" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [iD editor: Copy a line in place](/questions/72089/id-editor-copy-a-line-in-place)

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
<span id="post-72089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72089-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Let's say there is a twisty trail, miles and miles long, along a continental divide.</p>
<p>Let's also say a new country is born, Bogusania, whose boundary happens to coincide with this trail.</p>
<p>Alas, I <a href="https://github.com/openstreetmap/iD/issues/7114">cannot</a> just do CTRL+C CTRL+V to get a copy of this trail('s nodes) right in the same place, for my new boundary. Should I give up? Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-copy-paste" rel="tag" title="see questions tagged &#39;copy-paste&#39;">copy-paste</span> <span class="post-tag tag-link-lines" rel="tag" title="see questions tagged &#39;lines&#39;">lines</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Dec '19, 22:29</strong></p>
<img src="https://secure.gravatar.com/avatar/47edd1ee4d973c50bbe7991bb063d09d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jidanni&#39;s gravatar image" />
<p><span>jidanni</span><br />
<span class="score" title="339 reputation points">339</span><span title="32 badges"><span class="badge1">●</span><span class="badgecount">32</span></span><span title="36 badges"><span class="silver">●</span><span class="badgecount">36</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jidanni has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72089" class="comments-container">
<span id="72090"></span>
<div id="comment-72090" class="comment">
<div id="post-72090-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>What you probably want to do is use the trail itself as the boundary of the country, rather than duplicate the data. How you specifically do that in iD, though, I'm not familiar with. I'll let someone else answer that part.</p>
</div>
<div id="comment-72090-info" class="comment-info">
<span class="comment-age">(12 Dec '19, 23:42)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-72089" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72089-form-container" class="comment-form-container">
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

<span id="72094"></span>

<div id="answer-container-72094" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72094-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72094-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-72094-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jidanni has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>whose boundary happens to coincide with this trail.</p>
</blockquote>
<p>If it happens to coincide with the trail (rather than is defined as being the trail) I'd agree that you'd want to define the boundary and the trail separately, as you are trying to do. If you can't do that in the editor that you are currently using (perhaps for very good reasons, to do with who that editor is targeted at and causing the least surprise), use a different editor.</p>
<p>However, if it is actually defined as being the trail then at the very least you should be using the trail nodes in the boundary, and I'd actually suggest splitting the trail so that the part that forms the boundary actually forms part of the boundary relation, as alester suggests in the comment on the question. This latter approach is more prone to "newbie breakage" but is arguably the best way to model the real-life situation. If you want to see how it works long-term look at townlands (low-level admin areas) in Ireland, where boundaries often follow roads.</p>
<p>With regard to the "use a different editor" suggestion, I'm not assuming that you <em>can't</em> do this in iD (there are lots of things that people assume that you can't do that you can), only mentioning that there are multiple editors available for OSM, with different strengths and weaknesses. I regularly use four of them, depending on the job in hand. If you find that you can't do what you want to do in one editor, try a different one.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Dec '19, 14:47</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-72094" class="comments-container">
<span id="72104"></span>
<div id="comment-72104" class="comment">
<div id="post-72104-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(Indeed, in iD one can simply add things one wants to reuse to relations. And indeed, best to not reuse e.g., river centerlines for boundaries, but make a copy, as rivers change, but treaties don't.) (I am allergic to some editors, due to their hardwired partial left-handed mouse mappings (JOSM).) OK, I made a rough copy of the continental divide (one node per about five trail nodes) by hand.</p>
</div>
<div id="comment-72104-info" class="comment-info">
<span class="comment-age">(14 Dec '19, 01:33)</span> <span class="comment-user userinfo">jidanni</span>
</div>
</div>
</div>
<div id="comment-tools-72094" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72094-form-container" class="comment-form-container">
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

