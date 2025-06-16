+++
type = "question"
title = "Subdivided buildings"
description = '''Fareham (UK) Shopping Centre is a large building. One wing of it contains Fareham Health Centre and the Job Centre. Would it be permissible to divide the building on the map, so that those two parts could be named separately, even though the entire building is physically connected? If not, is there ...'''
date = "2012-01-25T20:06:00Z"
lastmod = "2012-02-12T23:03:00Z"
weight = 10216
keywords = [ "building", "divided" ]
aliases = [ "/questions/10216" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Subdivided buildings](/questions/10216/subdivided-buildings)

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
<span id="post-10216-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10216-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10216-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Fareham (UK) Shopping Centre is a large building. One wing of it contains Fareham Health Centre and the Job Centre. Would it be permissible to divide the building on the map, so that those two parts could be named separately, even though the entire building is physically connected? If not, is there another way to get the rendered map to show which parts of the building contain the Health Centre and the Job Centre?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-divided" rel="tag" title="see questions tagged &#39;divided&#39;">divided</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jan '12, 20:06</strong></p>
<img src="https://secure.gravatar.com/avatar/c81fd17cde8b2747629b78bdef81a202?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Madryn&#39;s gravatar image" />
<p><span>Madryn</span><br />
<span class="score" title="2241 reputation points"><span>2.2k</span></span><span title="36 badges"><span class="badge1">●</span><span class="badgecount">36</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Madryn has 5 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-10216" class="comments-container">
&#10;</div>
<div id="comment-tools-10216" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10216-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="10221"></span>

<div id="answer-container-10221" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10221-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10221-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-10221-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The answer to this depends on the situation. Are there <em>parts of the building</em> that have different names, or are there different <em>facilities within the building</em> that have their own names?</p>
<p>Both approaches avoid splitting the building outline.</p>
<p><strong>Facilities within the building</strong></p>
<p>If facilities within the building have their own name, then the usual solution for mapping is:</p>
<ul>
<li>Draw the building outline as <code>building=yes</code> with the <code>name</code> of the building as a whole.</li>
<li>Place the facilities as nodes or smaller areas within the building outline, add the appropriate tag (such as <code>office=employment_agency</code> for a job centre and their respective <code>name</code> tags.</li>
</ul>
<p><strong>Building parts</strong></p>
<p>If it is actually the <em>building parts</em> that have names - say, one wing of the building is known as "Foobar wing" -, then the situation would need to be tagged differently.</p>
<p>One possible solution is the <code>building:part=yes</code> tag (not yet properly documented, unfortunately). It can be used to map areas within a larger <code>building=yes</code> outline as a building part. That building part can then have tags that are different from the tags of the building as a whole.</p>
<p>That tag has been discussed originally in the context of building mapping for 3D visualization, where one building part might e.g. have a different number of levels than other parts of the same building. But there is no reason why it couldn't be applied to other situations where tags, such as <code>name</code>, only apply to one part of the building.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jan '12, 21:23</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jan '12, 00:38</strong> </span></p>
</div>
</div>
<div id="comments-container-10221" class="comments-container">
&#10;</div>
<div id="comment-tools-10221" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10221-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="10218"></span>

<div id="answer-container-10218" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10218-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10218-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10218-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no problems in drawing two building on the map where the buildings are connected structuraly. It does not matte wether it is one or two buildings, and there can be cases where it is hard to distinguish how many building there actualy are. Just have two ways that share a set of nodes where the buildings connect.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jan '12, 21:12</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jan '12, 22:46</strong> </span></p>
</div>
</div>
<div id="comments-container-10218" class="comments-container">
<span id="10222"></span>
<div id="comment-10222" class="comment">
<div id="post-10222-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The question asks about "a large building", not about two buildings that are connected.</p>
</div>
<div id="comment-10222-info" class="comment-info">
<span class="comment-age">(25 Jan '12, 21:25)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-10218" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10218-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="10538"></span>

<div id="answer-container-10538" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10538-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10538-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10538-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The answer the the question called 'One building, two tenants' seems relevant to this question as well. I have decided to map the Health Centre and Job Centre as nodes at their respective entrances, which is what people really want to know about. I need to visit the site again to find the exact location of the Job Centre entrance - won't be long.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '12, 11:51</strong></p>
<img src="https://secure.gravatar.com/avatar/c81fd17cde8b2747629b78bdef81a202?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Madryn&#39;s gravatar image" />
<p><span>Madryn</span><br />
<span class="score" title="2241 reputation points"><span>2.2k</span></span><span title="36 badges"><span class="badge1">●</span><span class="badgecount">36</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Madryn has 5 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-10538" class="comments-container">
<span id="10539"></span>
<div id="comment-10539" class="comment">
<div id="post-10539-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes - both approaches are used and both are "correct" - it's down the person actually mapping the building to decide what fits best for a particular location.</p>
</div>
<div id="comment-10539-info" class="comment-info">
<span class="comment-age">(11 Feb '12, 12:28)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-10538" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10538-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="10564"></span>

<div id="answer-container-10564" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10564-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10564-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-10564-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is what I did recently as the three companies have various percentages of the overall building <a href="https://www.openstreetmap.org/?lat=52.336068&amp;lon=-0.205438&amp;zoom=18&amp;layers=M">https://www.openstreetmap.org/?lat=52.336068&amp;lon=-0.205438&amp;zoom=18&amp;layers=M</a><br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Feb '12, 23:03</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span> </br></p>
</div>
</div>
<div id="comments-container-10564" class="comments-container">
&#10;</div>
<div id="comment-tools-10564" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10564-form-container" class="comment-form-container">
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

