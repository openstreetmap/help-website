+++
type = "question"
title = "What is the best practice for house names?"
description = '''I&#x27;m new to OpenStreetMap and I&#x27;m trying to work out what the best practice is for adding addresses to the map. I know several houses in my area have a name instead of a house number (this is quite common in some areas of the UK), I would like the house name to appear on the map like house numbers do...'''
date = "2022-06-24T23:57:00Z"
lastmod = "2022-06-30T07:25:00Z"
weight = 84879
keywords = [ "address", "tagging", "addrhousename" ]
aliases = [ "/questions/84879" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [What is the best practice for house names?](/questions/84879/what-is-the-best-practice-for-house-names)

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
<span id="post-84879-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84879-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84879-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm new to OpenStreetMap and I'm trying to work out what the best practice is for adding addresses to the map. I know several houses in my area have a name instead of a house number (this is quite common in some areas of the UK), I would like the house name to appear on the map like house numbers do. I assumed that you would do this by using "addr:housename" tag but thought I'd take a look at what others have done first. Looking at the map it seems some people use only the "name" tag for house names, while others use only the "addr:housename" tag, and some people put the same information in both the "name" and "addr:housename" tags.</p>
<p>Is either of these three options considered the best practice, or is it down to personal preference / the situation?</p>
<p>Thanks for any help anyone can offer.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-addrhousename" rel="tag" title="see questions tagged &#39;addrhousename&#39;">addrhousename</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jun '22, 23:57</strong></p>
<img src="https://secure.gravatar.com/avatar/a1507269d010fc0edfd76ff5728f60fb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Al3x25&#39;s gravatar image" />
<p><span>Al3x25</span><br />
<span class="score" title="36 reputation points">36</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Al3x25 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84879" class="comments-container">
&#10;</div>
<div id="comment-tools-84879" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84879-form-container" class="comment-form-container">
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

<span id="84882"></span>

<div id="answer-container-84882" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84882-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84882-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84882-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Al3x25 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please use <code>addr:housename</code> not <code>name</code>. Name can be used if the building is occupied by a named business where the building name may be different: Acme Ltd in Acme House would be <code>name=Acme[ Ltd]</code>, <code>addr:housename=Acme House</code>. Hotels, pubs, schools and similar amenities in single buildings may lack <code>addr:housename</code> when it would be the same as <code>name=*</code>, but this should probably be explicit. For instance a <a href="https://envelopes.osmuk.org/#18/58.46122/-5.05037">tool to show UK addresses</a> as they might appear on an envelope will not show this part of the address.Pubs converted to residential use are fairly <a href="https://www.openstreetmap.org/node/3375692552">good examples</a> of how the <code>name=*</code> disappears but the <code>addr:housename</code> stays.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jun '22, 16:49</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-84882" class="comments-container">
<span id="84918"></span>
<div id="comment-84918" class="comment">
<div id="post-84918-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just to follow up on this. If I see residential houses using the "name" tag should I replace it with the "addr:housename" tag?</p>
</div>
<div id="comment-84918-info" class="comment-info">
<span class="comment-age">(30 Jun '22, 07:25)</span> <span class="comment-user userinfo">Al3x25</span>
</div>
</div>
</div>
<div id="comment-tools-84882" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84882-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="84880"></span>

<div id="answer-container-84880" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84880-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84880-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84880-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am probably not a good person to answer as house names are not used where I am. That said, my reading of the wiki would lead me to use the addr:housename tag for house names.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jun '22, 04:02</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-84880" class="comments-container">
&#10;</div>
<div id="comment-tools-84880" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84880-form-container" class="comment-form-container">
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

