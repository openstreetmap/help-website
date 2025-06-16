+++
type = "question"
title = "Repairing a relation I accidentally cut?"
description = '''Hi, I just noticed a minor change in a road layout - 10 metres before joining a main street, a smaller street used to branch into two separate parts - one each for turning left/right. The lane for turning right no longer exists so I removed it (and also the &quot;one way&quot; in the other branch) - and only ...'''
date = "2016-07-26T00:09:00Z"
lastmod = "2016-07-27T10:37:00Z"
weight = 51096
keywords = [ "relation", "newbie", "broken" ]
aliases = [ "/questions/51096" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Repairing a relation I accidentally cut?](/questions/51096/repairing-a-relation-i-accidentally-cut)

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
<span id="post-51096-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51096-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51096-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I just noticed a minor change in a road layout - 10 metres before joining a main street, a smaller street used to branch into two separate parts - one each for turning left/right.</p>
<p>The lane for turning right no longer exists so I removed it (and also the "one way" in the other branch) - and only realised that someone had drawn an administrative border going down one branch, up again the other, when I had saved the change.</p>
<p>Now, obviously, there is a gap in that relation</p>
<p><a href="https://www.openstreetmap.org/relation/6362783">https://www.openstreetmap.org/relation/6362783</a></p>
<p>Is there a way to patch it up again using Potlatch 2? I have no experience of either JOSM or xml.</p>
<p>(Alternatively, could one of the experts do the fix?)</p>
<p>Regards, Jochen</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-broken" rel="tag" title="see questions tagged &#39;broken&#39;">broken</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jul '16, 00:09</strong></p>
<img src="https://secure.gravatar.com/avatar/06b2f5d4fa9884ae47333da22b6f2662?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marabu_Too&#39;s gravatar image" />
<p><span>Marabu_Too</span><br />
<span class="score" title="210 reputation points">210</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marabu_Too has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jul '16, 00:14</strong> </span></p>
</div>
</div>
<div id="comments-container-51096" class="comments-container">
&#10;</div>
<div id="comment-tools-51096" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51096-form-container" class="comment-form-container">
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

<span id="51126"></span>

<div id="answer-container-51126" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51126-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51126-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-51126-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Marabu_Too has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can in fact do this with Potlatch, I do it all the time. Choose the way you want to use for the relation, click "Advanced" in the lower left of the screen. You now get an overview of the relations the way is part of. You can click "Add to" to pick a relation from a list of local relations (this can be quite long). If you know which relation you've broken, you can also use "Load relation" and insert the number of the broken relation.</p>
<p>Some relations (eg hiking trails or bus routes) need their members to be in "chronological" order. You can access the list of members in Potlatch (doubleclick the relation as it appears when you select a member, then choose "Members" from the tab that opens) and change the order. But this is MUCH more practical in JOSM. See <a href="/questions/8197/re-ordering-sorting-ways-in-a-relation">this answer</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jul '16, 08:38</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-51126" class="comments-container">
<span id="51128"></span>
<div id="comment-51128" class="comment">
<div id="post-51128-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah - thanks a lot for that explanation... which leaves me in a quandary:</p>
<p>the spot where I cut that relation has changed massively - the big traffic island which divided the main street has gone, and there is now a normal intersection at the point where the big parking lot has its exit. For more than a year no one has bothered to correct this.</p>
<p>The only risk free thing I could do so far was change the northern end of High Street from one way to two way traffic.</p>
<p>There are seven or eight relations involved.</p>
<p>Dare I try to fix this?</p>
<p>I'll have to think about this until tonight.</p>
</div>
<div id="comment-51128-info" class="comment-info">
<span class="comment-age">(27 Jul '16, 09:23)</span> <span class="comment-user userinfo">Marabu_Too</span>
</div>
</div>
<span id="51129"></span>
<div id="comment-51129" class="comment">
<div id="post-51129-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think you could get it right if you first merge all the roads around the traffic island together (hence all the relations applying to all the little segments now). Then split it again, and keep the part which retains one of the old way IDs. Delete the other part, and change the geometry of the bit you kept. Also, you might need a turn restriction for the traffic with High Street.</p>
</div>
<div id="comment-51129-info" class="comment-info">
<span class="comment-age">(27 Jul '16, 09:36)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
<span id="51130"></span>
<div id="comment-51130" class="comment">
<div id="post-51130-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It seems to me that this is (tonight - I'm about to leave now) where I finally get acquainted with JOSM, where I can experiment until I get it right.</p>
<p>Potlatch 2 has one feature which, in these particular circumstances, can be quite nasty: occasionally I am too hasty when typing something into Advanced, and don't check if the text field is actually highlighted; typing "s" then will Save.</p>
<p>I'll see if I can follow your advice in JOSM; thanks again!</p>
</div>
<div id="comment-51130-info" class="comment-info">
<span class="comment-age">(27 Jul '16, 10:37)</span> <span class="comment-user userinfo">Marabu_Too</span>
</div>
</div>
</div>
<div id="comment-tools-51126" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51126-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="51102"></span>

<div id="answer-container-51102" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51102-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-51102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Repaired using JOSM in <a href="https://www.openstreetmap.org/changeset/41034901">https://www.openstreetmap.org/changeset/41034901</a> - there were actually <em>two</em> relations that needed fixing, as three boundaries meet at the intersection (the third one wasn't damaged).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jul '16, 12:38</strong></p>
<img src="https://secure.gravatar.com/avatar/8200fa5c0cc8feb096558c5972a6191c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Piskvor&#39;s gravatar image" />
<p><span>Piskvor</span><br />
<span class="score" title="1266 reputation points"><span>1.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Piskvor has 9 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-51102" class="comments-container">
<span id="51116"></span>
<div id="comment-51116" class="comment">
<div id="post-51116-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks a million - great relief!</p>
</div>
<div id="comment-51116-info" class="comment-info">
<span class="comment-age">(26 Jul '16, 21:26)</span> <span class="comment-user userinfo">Marabu_Too</span>
</div>
</div>
</div>
<div id="comment-tools-51102" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51102-form-container" class="comment-form-container">
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

