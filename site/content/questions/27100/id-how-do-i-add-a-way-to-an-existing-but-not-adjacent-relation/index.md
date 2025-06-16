+++
type = "question"
title = "iD: How do I add a way to an existing, but not adjacent, relation?"
description = '''Imagine that I&#x27;m here and am trying to add Road C to this existing relation. If I edit the area in iD, and select the &quot;+&quot; below &quot;all relations&quot; I get this box appear:  I don&#x27;t want to create a new releation, because it already exists just to the west. Am I supposed to type something into the text bo...'''
date = "2013-10-12T10:37:00Z"
lastmod = "2013-10-20T11:06:00Z"
weight = 27100
keywords = [ "ideditor", "relation" ]
aliases = [ "/questions/27100" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [iD: How do I add a way to an existing, but not adjacent, relation?](/questions/27100/id-how-do-i-add-a-way-to-an-existing-but-not-adjacent-relation)

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
<span id="post-27100-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27100-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-27100-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Imagine that I'm <a href="http://api06.dev.openstreetmap.org/#map=17/53.12991/-0.48733&amp;layers=D">here</a> and am trying to add <a href="http://api06.dev.openstreetmap.org/browse/way/4295042642">Road C</a> to <a href="http://api06.dev.openstreetmap.org/browse/relation/4294969114">this</a> existing relation.</p>
<p>If I edit the area in iD, and select the "+" below "all relations" I get this box appear:</p>
<p><img src="/upfiles/iD_01.png" alt="iD Add relation box" /></p>
<p>I don't want to create a new releation, because it already exists just to the west. Am I supposed to type something into the text box to search? There are no clues on screen. Is there any iD documentation somewhere that explains how to do this?</p>
<p>(note all these links are on the api06 dev server - I'm not sure that they'll all work if you're not signed up there)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Oct '13, 10:37</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Oct '13, 10:46</strong> </span></p>
</div>
</div>
<div id="comments-container-27100" class="comments-container">
<span id="27102"></span>
<div id="comment-27102" class="comment">
<div id="post-27102-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Seems like the relation to which you want to add the way must be in your current view in order to be able to select it. Is that what your are asking?</p>
</div>
<div id="comment-27102-info" class="comment-info">
<span class="comment-age">(12 Oct '13, 12:28)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="27103"></span>
<div id="comment-27103" class="comment">
<div id="post-27103-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>With P2 I'd search for the relation number. I can understand why iD would try to protect new mappers from that - but wondered what the intended workflow is?</p>
</div>
<div id="comment-27103-info" class="comment-info">
<span class="comment-age">(12 Oct '13, 12:54)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="27104"></span>
<div id="comment-27104" class="comment">
<div id="post-27104-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I have no idea. The regular search mechanism in iD is capable of doing world-wide searches but there is no such option for relations.</p>
</div>
<div id="comment-27104-info" class="comment-info">
<span class="comment-age">(12 Oct '13, 14:02)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="27350"></span>
<div id="comment-27350" class="comment">
<div id="post-27350-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>For info I've created an issue <a href="https://github.com/systemed/iD/issues/1906">here</a>.</p>
</div>
<div id="comment-27350-info" class="comment-info">
<span class="comment-age">(20 Oct '13, 11:06)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-27100" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27100-form-container" class="comment-form-container">
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

<span id="27114"></span>

<div id="answer-container-27114" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27114-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27114-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-27114-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There were several discussions about relations in iD. I think the outcome was that it cannot be done, although they do show these options. Potlatch is very simple to use, there are even videos on the net how to do relations. If you have the time, add the relations in Potlatch and then play with iD, it will probably take lot of experimenting. If you find how to do it, the iD community would welcome it. I occasionally come across a need to use relations and I solely use Potlatch. It's very simple and reliable. Martin</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Oct '13, 18:46</strong></p>
<img src="https://secure.gravatar.com/avatar/06b9779157ed5d9958611cdc3b6aa4a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="slover98&#39;s gravatar image" />
<p><span>slover98</span><br />
<span class="score" title="567 reputation points">567</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="slover98 has one accepted answer">5%</span></p>
</div>
</div>
<div id="comments-container-27114" class="comments-container">
<span id="27347"></span>
<div id="comment-27347" class="comment">
<div id="post-27347-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for the reply. I was looking for information about iD because a new mapper has added new bits of a walking route in iD by naming them "blah trail" instead of adding to the existing "blah trail" relation. Whilst it may be easier to add to relations currently in Potlatch (or JOSM) I was wondering whether I could suggest something that didn't involve learning a different editor.</p>
</div>
<div id="comment-27347-info" class="comment-info">
<span class="comment-age">(20 Oct '13, 10:19)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-27114" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27114-form-container" class="comment-form-container">
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

