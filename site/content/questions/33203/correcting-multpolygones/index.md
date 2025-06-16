+++
type = "question"
title = "Correcting multpolygones"
description = '''Is it possible to reuse an old multi relation for a new set of multi relations or is deleting the old multi relation and creating a complete new one the best way ? I hesitate to use the last method because it’s destroying old data.'''
date = "2014-05-15T14:09:00Z"
lastmod = "2014-05-16T12:45:00Z"
weight = 33203
keywords = [ "destroying", "relation", "reuse", "multipolygon" ]
aliases = [ "/questions/33203" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Correcting multpolygones](/questions/33203/correcting-multpolygones)

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
<span id="post-33203-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33203-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33203-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to reuse an old multi relation for a new set of multi relations or is deleting the old multi relation and creating a complete new one the best way ? I hesitate to use the last method because it’s destroying old data.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-destroying" rel="tag" title="see questions tagged &#39;destroying&#39;">destroying</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-reuse" rel="tag" title="see questions tagged &#39;reuse&#39;">reuse</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 May '14, 14:09</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-33203" class="comments-container">
<span id="33204"></span>
<div id="comment-33204" class="comment">
<div id="post-33204-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>An example might help clarify the question here, perhaps?</p>
</div>
<div id="comment-33204-info" class="comment-info">
<span class="comment-age">(15 May '14, 14:37)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="33212"></span>
<div id="comment-33212" class="comment">
<div id="post-33212-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The large white island carries ID 3645243/5 outer, <a href="https://www.openstreetmap.org/#map=17/52.48753/4.77726">https://www.openstreetmap.org/#map=17/52.48753/4.77726</a> I wont to change it into for instance 3645243/0 because its the outer rim. But I did not find a method the change it other then remove the group 3645243.</p>
</div>
<div id="comment-33212-info" class="comment-info">
<span class="comment-age">(15 May '14, 20:47)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="33215"></span>
<div id="comment-33215" class="comment">
<div id="post-33215-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Note that if you're trying to fix why that island isn't rendered with the landuse=grass green, it's because the outer way isn't a closed loop. There's a break at this node: <a href="https://www.openstreetmap.org/node/2784295245">https://www.openstreetmap.org/node/2784295245</a></p>
</div>
<div id="comment-33215-info" class="comment-info">
<span class="comment-age">(16 May '14, 00:21)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="33218"></span>
<div id="comment-33218" class="comment">
<div id="post-33218-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>One of the inner loops is broken too.</p>
</div>
<div id="comment-33218-info" class="comment-info">
<span class="comment-age">(16 May '14, 02:41)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
</div>
<div id="comment-tools-33203" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33203-form-container" class="comment-form-container">
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

<span id="33214"></span>

<div id="answer-container-33214" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33214-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33214-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-33214-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Hendrikklaas has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not exactly sure what you mean with the "/5" and "/0" notation. Are you using that to represent where the way is located in the list of relation members? If so, there's nothing you need to do. For a multipolygon relation, the order of the members has no effect, so don't worry about it. As long as the roles have been set correctly, everything will work just fine.</p>
<p>If you feel you really need to reorder the members, even though it won't have any real effect, you can do it easily in the relation editor in JOSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 May '14, 00:06</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-33214" class="comments-container">
<span id="33231"></span>
<div id="comment-33231" class="comment">
<div id="post-33231-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks guys, The 0 - 5 was ment for the order of the elements of the relation, Ill switch to JOSM to make the adjustments.</p>
</div>
<div id="comment-33231-info" class="comment-info">
<span class="comment-age">(16 May '14, 11:26)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="33233"></span>
<div id="comment-33233" class="comment">
<div id="post-33233-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>But alester already correctly explained that changing the order is unnecessary.</p>
</div>
<div id="comment-33233-info" class="comment-info">
<span class="comment-age">(16 May '14, 12:45)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-33214" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33214-form-container" class="comment-form-container">
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

