+++
type = "question"
title = "Gate that is locked to vehicles but occasionally lets walkers and cyclists out."
description = '''The gate here https://www.openstreetmap.org/#map=19/52.33809/-0.17666 has been closed to vehicles for a several years. It had a small hand gate for walkers and cyclists which saved a detour of one K or so. The College has some young students now so the small gate can&#x27;t be opened from Coxons Close eit...'''
date = "2017-01-06T14:20:00Z"
lastmod = "2017-01-11T19:00:00Z"
weight = 53896
keywords = [ "access", "conditional", "routing", "barrier", "tags" ]
aliases = [ "/questions/53896" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Gate that is locked to vehicles but occasionally lets walkers and cyclists out.](/questions/53896/gate-that-is-locked-to-vehicles-but-occasionally-lets-walkers-and-cyclists-out)

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
<span id="post-53896-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53896-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53896-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The gate here <a href="https://www.openstreetmap.org/#map=19/52.33809/-0.17666">https://www.openstreetmap.org/#map=19/52.33809/-0.17666</a> has been closed to vehicles for a several years. It had a small hand gate for walkers and cyclists which saved a detour of one K or so. The College has some young students now so the small gate can't be opened from Coxons Close either since 2015. I'm told it is exit only at some times, A young woman I asked said "I have to take the long way around but a can get out after work by pressing a button on the inside to get out". I mapped it as barrier=gate, how do i add these conditional tags. I tried out the routers on the main map page. Car, cycle and foot all route through it. Should I just break the way to stop incorrect routing?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-conditional" rel="tag" title="see questions tagged &#39;conditional&#39;">conditional</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-barrier" rel="tag" title="see questions tagged &#39;barrier&#39;">barrier</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jan '17, 14:20</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Jan '17, 14:21</strong> </span></p>
</div>
</div>
<div id="comments-container-53896" class="comments-container">
&#10;</div>
<div id="comment-tools-53896" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53896-form-container" class="comment-form-container">
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

<span id="53897"></span>

<div id="answer-container-53897" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53897-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53897-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-53897-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="andy mackey has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Don't break the way, use <a href="https://wiki.openstreetmap.org/wiki/Key:access">access</a> tags instead.</p>
<p>According to your description it sounds like a private gate to me. In this case I would just add <code>access=private</code> to the gate. This should be enough for routers to avoid the gate, otherwise they are broken (or use old data).</p>
<p>Alternatively you could try to use <a href="https://wiki.openstreetmap.org/wiki/Conditional_restrictions">conditional restrictions</a> if you know the exact times the gate is open. However in your case I wouldn't bother to map them. If you insist to map them nevertheless then use the most restrictive value as default. Example: <code>access=private</code> + <code>foot:conditional=yes @ Mo-Fr 08:00-16:00</code> + <code>bicycle:conditional=yes @ Mo-Fr 08:00-16:00</code>. However this still doesn't include the <em>direction</em> which seems to be important according to your description.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jan '17, 14:52</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Jan '17, 14:57</strong> </span></p>
</div>
</div>
<div id="comments-container-53897" class="comments-container">
<span id="53899"></span>
<div id="comment-53899" class="comment">
<div id="post-53899-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks Alex</p>
</div>
<div id="comment-53899-info" class="comment-info">
<span class="comment-age">(06 Jan '17, 16:43)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="53988"></span>
<div id="comment-53988" class="comment">
<div id="post-53988-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I added access=private as scai suggested and now walkers and drivers don't get sent through there by the routers.</p>
</div>
<div id="comment-53988-info" class="comment-info">
<span class="comment-age">(11 Jan '17, 19:00)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-53897" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53897-form-container" class="comment-form-container">
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

