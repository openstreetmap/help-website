+++
type = "question"
title = "Decoding NAS-EPS"
description = '''Dear All, I would like to know the prodedure to decode the NAS-EPS messages.  Thanks.'''
date = "2015-11-03T02:32:00Z"
lastmod = "2015-11-14T14:16:00Z"
weight = 47179
keywords = [ "nas", "eps" ]
aliases = [ "/questions/47179" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decoding NAS-EPS](/questions/47179/decoding-nas-eps)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47179-score" class="post-score" title="current number of votes">0</div><span id="post-47179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear All,</p><p>I would like to know the prodedure to decode the NAS-EPS messages. Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nas" rel="tag" title="see questions tagged &#39;nas&#39;">nas</span> <span class="post-tag tag-link-eps" rel="tag" title="see questions tagged &#39;eps&#39;">eps</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Nov '15, 02:32</strong></p><img src="https://secure.gravatar.com/avatar/f8d6ab7c5eee7672554abadaa8adb9c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smehra24&#39;s gravatar image" /><p><span>smehra24</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smehra24 has no accepted answers">0%</span></p></div></div><div id="comments-container-47179" class="comments-container"><span id="47189"></span><div id="comment-47189" class="comment"><div id="post-47189-score" class="comment-score"></div><div class="comment-text"><p>What's the format of your input file? Are you having a pcap file? A text file with the hex dump of the message? Without this basic information it's not possible to answer you. Could you post an example of your NAS EPS message format?</p></div><div id="comment-47189-info" class="comment-info"><span class="comment-age">(03 Nov '15, 10:59)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-47179" class="comment-tools"></div><div class="clear"></div><div id="comment-47179-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47585"></span>

<div id="answer-container-47585" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47585-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47585-score" class="post-score" title="current number of votes">0</div><span id="post-47585-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi! Can wireshark decrypt NAS-EPS messages (encrypted with either AES128 or SNOW3G) if K and OP are provided? Thanks</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Nov '15, 13:20</strong></p><img src="https://secure.gravatar.com/avatar/925fdcfe4e352fb79e10fa50bab50e1c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="savannah&#39;s gravatar image" /><p><span>savannah</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="savannah has no accepted answers">0%</span></p></div></div><div id="comments-container-47585" class="comments-container"><span id="47587"></span><div id="comment-47587" class="comment"><div id="post-47587-score" class="comment-score"></div><div class="comment-text"><p>No this is not implemented. SNOW3G will most probably not happen due to the patents associated. EEA2 (AES256) could eventually be implemented if someone feels motivated enough (not many people have access to the K and OP keys though, so it limits its usage).</p></div><div id="comment-47587-info" class="comment-info"><span class="comment-age">(13 Nov '15, 13:35)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="47609"></span><div id="comment-47609" class="comment"><div id="post-47609-score" class="comment-score"></div><div class="comment-text"><p>NAS decryption is a somewhat popular feature for telecom-tailored probe systems, and really one of the main things I'd use them for (ie: one of the main things I can't do with just Wireshark).</p><p>For NAS-EPS, if you're a network operator most MME platforms I know of support the ability to selectively negotiate down to null encryption for a given SIM through configuration if you want to do an ad-hoc trace of the NAS signalling also.</p></div><div id="comment-47609-info" class="comment-info"><span class="comment-age">(14 Nov '15, 14:16)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-47585" class="comment-tools"></div><div class="clear"></div><div id="comment-47585-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

