+++
type = "question"
title = "How to best tag a permit parking lane which has opening hours?"
description = '''Hi there I have been mapping at my university recently, and even after spending some time on the Key:parking:lane page on the OSM wiki, I am not exactly sure how to tag a lane that:  has marked parking spaces; is open Monday to Friday from 7:00 to 21:00; is only for people having a permit delivered ...'''
date = "2013-08-31T06:31:00Z"
lastmod = "2013-09-01T02:19:00Z"
weight = 25993
keywords = [ "tagging", "parking" ]
aliases = [ "/questions/25993" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to best tag a permit parking lane which has opening hours?](/questions/25993/how-to-best-tag-a-permit-parking-lane-which-has-opening-hours)

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
<span id="post-25993-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25993-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-25993-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there</p>
<p>I have been mapping at my university recently, and even after spending some time on the <a href="https://wiki.openstreetmap.org/wiki/Key:parking:lane">Key:parking:lane page</a> on the OSM wiki, I am not exactly sure how to tag a lane that:</p>
<ul>
<li>has marked parking spaces;</li>
<li>is open Monday to Friday from 7:00 to 21:00;</li>
<li>is only for people having a permit delivered by the university.</li>
</ul>
<p>For a parking lot, it is fairly easy using <code>amenity=parking</code>, <code>parking=surface</code>, <code>access=private</code> and <code>opening_hours=Mo-Fr 07:00-21:00</code>. However, with lanes, the system is different and according to the wiki page, using the key <code>parking:condition:both:time_interval=*</code> will make it necessary to use <code>parking:condition:both:default=*</code> for outside the opening hours, for which I am not sure what value to use (maybe "no"?).</p>
<p>Using the key <code>opening_hours=*</code> for the lane would be a problem as the street is still accessible out of those parking hours.</p>
<p>The way I am talking about is <a href="https://www.openstreetmap.org/browse/way/24297653">this one</a>, so you can see my attempt at it.</p>
<p>Cheers!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-parking" rel="tag" title="see questions tagged &#39;parking&#39;">parking</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Aug '13, 06:31</strong></p>
<img src="https://secure.gravatar.com/avatar/19c111f5c672fdb25353073c835f6a38?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephane-guillou&#39;s gravatar image" />
<p><span>stephane-gui...</span><br />
<span class="score" title="585 reputation points">585</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephane-guillou has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-25993" class="comments-container">
&#10;</div>
<div id="comment-tools-25993" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25993-form-container" class="comment-form-container">
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

<span id="25997"></span>

<div id="answer-container-25997" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25997-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25997-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-25997-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="stephane-guillou has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not an expert at the parking:lane tag but the <a href="https://wiki.openstreetmap.org/wiki/Key:parking:lane/Examples">example page</a> has various cases where a <em>time_interval</em> is specified without a <em>default</em> key. So I guess it is correct to specify no default at all. Yet there is no clear definition what this means. The <a href="https://wiki.openstreetmap.org/wiki/Talk:Proposed_features/parking:lane">proposals talk page</a> has some sections about the <em>default</em> condition but they are either just the same examples as already mentioned or just wild guesses but nothing specific. <a href="http://taginfo.openstreetmap.org/keys/parking%3Acondition%3Adefault#values">Taginfo</a> just shows two values for the default key, <em>free</em> and <em>disc</em>. I guess the best option is to ask on a tagging mailing list or at the wiki talk page.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Aug '13, 07:45</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-25997" class="comments-container">
<span id="26026"></span>
<div id="comment-26026" class="comment">
<div id="post-26026-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Ok, I did not see that there was an example page. This does help a bit, and <a href="https://wiki.openstreetmap.org/wiki/Talk:Proposed_features/parking:lane#Default">this conversation</a> does explain why the default is no parking. I will then delete the default I used in this particular case as it is "no parking". Cheers!</p>
</div>
<div id="comment-26026-info" class="comment-info">
<span class="comment-age">(01 Sep '13, 02:19)</span> <span class="comment-user userinfo">stephane-gui...</span>
</div>
</div>
</div>
<div id="comment-tools-25997" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25997-form-container" class="comment-form-container">
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

