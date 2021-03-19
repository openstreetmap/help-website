+++
type = "question"
title = "Wireshark not recognizing skinny"
description = ''' Wireshark not recognized new SCCP protocol . You can found messages only if you will do filter by SCCP port 2000 . Is any plan to support it ? Thank you'''
date = "2011-01-31T08:07:00Z"
lastmod = "2011-04-28T07:24:00Z"
weight = 2040
keywords = [ "2000", "skinny", "sccp", "cisco", "port" ]
aliases = [ "/questions/2040" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark not recognizing skinny](/questions/2040/wireshark-not-recognizing-skinny)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2040-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2040-score" class="post-score" title="current number of votes">0</div><span id="post-2040-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="http://img401.imageshack.us/img401/4337/skinnyy.jpg" alt="alt text" /></p><p>Wireshark not recognized new SCCP protocol . You can found messages only if you will do filter by SCCP port 2000 .</p><p>Is any plan to support it ?</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-2000" rel="tag" title="see questions tagged &#39;2000&#39;">2000</span> <span class="post-tag tag-link-skinny" rel="tag" title="see questions tagged &#39;skinny&#39;">skinny</span> <span class="post-tag tag-link-sccp" rel="tag" title="see questions tagged &#39;sccp&#39;">sccp</span> <span class="post-tag tag-link-cisco" rel="tag" title="see questions tagged &#39;cisco&#39;">cisco</span> <span class="post-tag tag-link-port" rel="tag" title="see questions tagged &#39;port&#39;">port</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jan '11, 08:07</strong></p><img src="https://secure.gravatar.com/avatar/7b65f55f5ce6c32034c26aadeb551748?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dan_D&#39;s gravatar image" /><p><span>Dan_D</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dan_D has no accepted answers">0%</span></p></img></div></div><div id="comments-container-2040" class="comments-container"></div><div id="comment-tools-2040" class="comment-tools"></div><div class="clear"></div><div id="comment-2040-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="2142"></span>

<div id="answer-container-2142" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2142-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2142-score" class="post-score" title="current number of votes">1</div><span id="post-2142-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As with any protocol, I guess it will be updated if it is scratching someone's itch.</p><p>The best way to get it in the face of developers, file a bug at bugs.wireshark.org with as much information as you can.</p><p>And as grossman correctly pointed out the packet you have expanded above (frame 12) isn't anything other than a TCP ACK (it has length 0)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '11, 17:32</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p><span>martyvis</span><br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-2142" class="comments-container"></div><div id="comment-tools-2142" class="comment-tools"></div><div class="clear"></div><div id="comment-2142-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2043"></span>

<div id="answer-container-2043" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2043-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2043-score" class="post-score" title="current number of votes">0</div><span id="post-2043-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>While there are some SKINNY messages that the dissector doesn't recognize, it looks like this is a pure TCP ACK, judging by the LEN=0 in the screen-shot.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jan '11, 10:35</strong></p><img src="https://secure.gravatar.com/avatar/e458b44fd60b4064eb73fc42e67b3897?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grossman&#39;s gravatar image" /><p><span>grossman</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grossman has no accepted answers">0%</span></p></div></div><div id="comments-container-2043" class="comments-container"></div><div id="comment-tools-2043" class="comment-tools"></div><div class="clear"></div><div id="comment-2043-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2108"></span>

<div id="answer-container-2108" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2108-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2108-score" class="post-score" title="current number of votes">0</div><span id="post-2108-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It is a updated skinny protocol which available in CM 7 and firmware 903 .before this firmaware wireshark can recognize all message with small issue which I discrabe in</p><p>http://ask.wireshark.org/questions/558/skinny-protocol-problem</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Feb '11, 10:00</strong></p><img src="https://secure.gravatar.com/avatar/7b65f55f5ce6c32034c26aadeb551748?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dan_D&#39;s gravatar image" /><p><span>Dan_D</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dan_D has no accepted answers">0%</span></p></div></div><div id="comments-container-2108" class="comments-container"></div><div id="comment-tools-2108" class="comment-tools"></div><div class="clear"></div><div id="comment-2108-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3786"></span>

<div id="answer-container-3786" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3786-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3786-score" class="post-score" title="current number of votes">0</div><span id="post-3786-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I know I'm a little late to this post, but I have seen the same thing, where wireshark doesn't recognize the skinny packet in the new firmware and CM 7 as anything other than generic SCCP.</p><p>From what I have seen the issue is that the reserved portion of the SCCP packet is no longer all zeros. Cisco is now populating these bits, so Wireshark and other tools don't recognize them anymore. I have just recently gotten confirmation from a Cisco TAC engineer that this is a permanent change to the protocol, so hopefully Wireshark will be able to recognize these packets eventually.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '11, 07:24</strong></p><img src="https://secure.gravatar.com/avatar/c00d4aa6f5e6d9e1f12a144135a67d84?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robrien&#39;s gravatar image" /><p><span>robrien</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robrien has no accepted answers">0%</span></p></div></div><div id="comments-container-3786" class="comments-container"></div><div id="comment-tools-3786" class="comment-tools"></div><div class="clear"></div><div id="comment-3786-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

