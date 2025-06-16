+++
type = "question"
title = "How to map &quot;unreal&quot; one way streets?"
description = '''Hi, we have some streets that were previously one way streets, but the one way signs have been removed, so you may drive in both directions. But the signs at the end of the one way street, that interdicts to drive into the street are still there... How to map this scenario? I have now put a tag &quot;one...'''
date = "2012-12-30T14:36:00Z"
lastmod = "2013-01-01T00:35:00Z"
weight = 18778
keywords = [ "oneway" ]
aliases = [ "/questions/18778" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to map "unreal" one way streets?](/questions/18778/how-to-map-unreal-one-way-streets)

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
<span id="post-18778-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18778-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18778-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>we have some streets that were previously one way streets, but the one way signs have been removed, so you may drive in both directions. But the signs at the end of the one way street, that interdicts to drive into the street are still there...</p>
<p>How to map this scenario?</p>
<p>I have now put a tag "oneway=yes" for a little segment at the end of the street. Is this correct?</p>
<p>Regards</p>
<p>Paul</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-oneway" rel="tag" title="see questions tagged &#39;oneway&#39;">oneway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Dec '12, 14:36</strong></p>
<img src="https://secure.gravatar.com/avatar/ab6a61ab061494abf18c7b9848b97ac4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="taunusmapper&#39;s gravatar image" />
<p><span>taunusmapper</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="taunusmapper has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18778" class="comments-container">
&#10;</div>
<div id="comment-tools-18778" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18778-form-container" class="comment-form-container">
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

<span id="18779"></span>

<div id="answer-container-18779" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18779-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18779-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18779-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the end of that street has a no-entry sign on it, then you can make a <a href="https://wiki.openstreetmap.org/wiki/Relation:restriction">turn restriction</a> for it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Dec '12, 15:30</strong></p>
<img src="https://secure.gravatar.com/avatar/f7f8127223bd00c9e8f569ce2e9ddf22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RM87&#39;s gravatar image" />
<p><span>RM87</span><br />
<span class="score" title="3346 reputation points"><span>3.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="37 badges"><span class="silver">●</span><span class="badgecount">37</span></span><span title="53 badges"><span class="bronze">●</span><span class="badgecount">53</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RM87 has 20 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-18779" class="comments-container">
<span id="18781"></span>
<div id="comment-18781" class="comment">
<div id="post-18781-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. I have now added the following tags on the point where the "unreal" oneway street is connected to the other street from where you aren't allowed to drive into:</p>
<p>type=restriction restriction=no_entry from=Main Street to=Unreal Oneway Street</p>
<p>I hope this is ok...</p>
<p>Best regards,</p>
<p>paul</p>
</div>
<div id="comment-18781-info" class="comment-info">
<span class="comment-age">(30 Dec '12, 17:43)</span> <span class="comment-user userinfo">taunusmapper</span>
</div>
</div>
<span id="18783"></span>
<div id="comment-18783" class="comment">
<div id="post-18783-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please take a look at relations <a href="https://www.openstreetmap.org/browse/relation/2669845">2669845</a> and <a href="https://www.openstreetmap.org/browse/relation/2669845">2669845</a> that user <a href="https://www.openstreetmap.org/user/wambacher">wambacher</a> just created. This is one way how a turn restriction can be added to that crossing.</p>
<p>As it seems you are not familiar with relations, you may want to read the <a href="https://wiki.openstreetmap.org/wiki/Relation">relations page</a> on wiki (and pages it links to).</p>
</div>
<div id="comment-18783-info" class="comment-info">
<span class="comment-age">(30 Dec '12, 18:34)</span> <span class="comment-user userinfo">RM87</span>
</div>
</div>
<span id="18784"></span>
<div id="comment-18784" class="comment">
<div id="post-18784-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Ahhh, thanks! With the two linked relations I have understood the way how to map this.</p>
<p>I have found (and read) the Wiki articles about relations and turn restrictions before, but it was not really clear to me, how to tag it...</p>
<p>But with this real example it's clear to me now.</p>
<p>Thanks a lot.</p>
<p>Best regards</p>
<p>paul</p>
</div>
<div id="comment-18784-info" class="comment-info">
<span class="comment-age">(30 Dec '12, 19:20)</span> <span class="comment-user userinfo">taunusmapper</span>
</div>
</div>
</div>
<div id="comment-tools-18779" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18779-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="18799"></span>

<div id="answer-container-18799" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18799-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18799-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18799-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For the opposite situation, where you can only leave the intersection on a particular way, make it one-way from the intersection to the first point that allows two-way movement.</p>
<p><a href="https://www.openstreetmap.org/?lat=44.932969&amp;lon=-123.011902&amp;zoom=18&amp;layers=M">Example in Salem Oregon</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jan '13, 00:35</strong></p>
<img src="https://secure.gravatar.com/avatar/666698a7b13e402aba7e1e0f6de7c1d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baloo%20Uriza&#39;s gravatar image" />
<p><span>Baloo Uriza</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baloo Uriza has 12 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-18799" class="comments-container">
&#10;</div>
<div id="comment-tools-18799" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18799-form-container" class="comment-form-container">
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

