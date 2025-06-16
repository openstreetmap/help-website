+++
type = "question"
title = "How to tag ways inside administrative boundary relations?"
description = '''I have started to update the province and county boundaries of our country. I don&#x27;t know what is the standard approach for tagging the way segments which are used in different relations. I have read in this page we have to tag the ways with only boundary=administrative and admin_level=* tags without...'''
date = "2016-08-07T07:31:00Z"
lastmod = "2016-08-08T09:46:00Z"
weight = 51291
keywords = [ "admin_level", "boundary", "relation", "administrative" ]
aliases = [ "/questions/51291" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to tag ways inside administrative boundary relations?](/questions/51291/how-to-tag-ways-inside-administrative-boundary-relations)

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
<span id="post-51291-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51291-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51291-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have started to update the province and county boundaries of our country. I don't know what is the standard approach for tagging the way segments which are used in different relations. I have read in <a href="/questions/4658/tagging-areas-as-place-vs-boundaryadministrative">this page</a> we have to tag the ways with only boundary=administrative and admin_level=* tags without any name tags.</p>
<p>If a way is part of different boundary relations with different admin_level tag in each one, which level should be chosen for the way itself?</p>
<p>In my case I have a way segment which is used in admin_level=2 (for country border relation) , used in another relation with admin_level=4 (for province relation) and also used in a county relation which is admin_level=6. now how should I tag the way?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-admin_level" rel="tag" title="see questions tagged &#39;admin_level&#39;">admin_level</span> <span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-administrative" rel="tag" title="see questions tagged &#39;administrative&#39;">administrative</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Aug '16, 07:31</strong></p>
<img src="https://secure.gravatar.com/avatar/f7da215f2999ecac8d169e32e2c3502e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Adib%20Yz&#39;s gravatar image" />
<p><span>Adib Yz</span><br />
<span class="score" title="291 reputation points">291</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Adib Yz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Aug '16, 09:10</strong> </span></p>
</div>
</div>
<div id="comments-container-51291" class="comments-container">
&#10;</div>
<div id="comment-tools-51291" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51291-form-container" class="comment-form-container">
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

<span id="51294"></span>

<div id="answer-container-51294" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51294-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51294-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-51294-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Adib Yz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Generally if the boundaries are mapped by relations then there is no need for boundary=administrative or admin_level tags on the individual ways. In many cases such tags have been left from a legacy of earlier tagging approaches.</p>
<p>It is useful to have some sort of tag on the ways to help other people who might be editing in their vicinity. Not everyone notices that untagged ways are part of boundary relations. Options might be a note, description or source tag; or possibly boundary=administrative without associated admin_level tags (although this will probably generate validation errors, and thus may be counter-productive).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Aug '16, 11:25</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-51294" class="comments-container">
<span id="51301"></span>
<div id="comment-51301" class="comment">
<div id="post-51301-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh, I've always been adding boundary=administrative + admin_level=* , where * = the highest level of boundary using the line (so the lowest number). The French rendering style does take this tag on a way in account: see e.g. 14/-10.8555/-75.2220 . It's probably redundant as you say.</p>
</div>
<div id="comment-51301-info" class="comment-info">
<span class="comment-age">(08 Aug '16, 09:20)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
<span id="51302"></span>
<div id="comment-51302" class="comment">
<div id="post-51302-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Highest level boundary admin_level is still in the wiki as recommended practice, then is followed by a paragraph saying they are optional. Tagging the ways is a historical leftover to get them to render but is no longer required, if I remember correctly. <a href="https://wiki.openstreetmap.org/wiki/Relation:boundary#Way_tags">https://wiki.openstreetmap.org/wiki/Relation:boundary#Way_tags</a></p>
</div>
<div id="comment-51302-info" class="comment-info">
<span class="comment-age">(08 Aug '16, 09:46)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-51294" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51294-form-container" class="comment-form-container">
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

