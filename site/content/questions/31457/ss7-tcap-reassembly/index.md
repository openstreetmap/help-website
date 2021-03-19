+++
type = "question"
title = "SS7 TCAP Reassembly"
description = '''Hi, We are familiar with SCCP Reassembly layer in SS7 world (for XUDT/ XUDTS/ LUDT/ LUDTS etc).  But, is there such a thing called TCAP Reassembly that is done within TCAP layer itself? We&#x27;ve encountered an example in which the SCCP layer type is UDTS with length &amp;lt; 254 and the length inside TCAP ...'''
date = "2014-04-03T00:55:00Z"
lastmod = "2014-04-03T01:38:00Z"
weight = 31457
keywords = [ "tcap", "reassembly", "ss7" ]
aliases = [ "/questions/31457" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SS7 TCAP Reassembly](/questions/31457/ss7-tcap-reassembly)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31457-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31457-score" class="post-score" title="current number of votes">0</div><span id="post-31457-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>We are familiar with SCCP Reassembly layer in SS7 world (for XUDT/ XUDTS/ LUDT/ LUDTS etc). But, is there such a thing called TCAP Reassembly that is done within TCAP layer itself? We've encountered an example in which the SCCP layer type is UDTS with length &lt; 254 and the length inside TCAP layer (ITU) is ~400 bytes.</p><p>Can anyone advice?</p><p>Hemda &amp; Diana</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcap" rel="tag" title="see questions tagged &#39;tcap&#39;">tcap</span> <span class="post-tag tag-link-reassembly" rel="tag" title="see questions tagged &#39;reassembly&#39;">reassembly</span> <span class="post-tag tag-link-ss7" rel="tag" title="see questions tagged &#39;ss7&#39;">ss7</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Apr '14, 00:55</strong></p><img src="https://secure.gravatar.com/avatar/900044aef60dc6223168781e5d576bfb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dianalab9&#39;s gravatar image" /><p><span>Dianalab9</span><br />
<span class="score" title="26 reputation points">26</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dianalab9 has no accepted answers">0%</span></p></div></div><div id="comments-container-31457" class="comments-container"></div><div id="comment-tools-31457" class="comment-tools"></div><div class="clear"></div><div id="comment-31457-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31459"></span>

<div id="answer-container-31459" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31459-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31459-score" class="post-score" title="current number of votes">1</div><span id="post-31459-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>UDT is conection less -right? TCAP standard Q.773 has this comment The user should be aware of total message length limitations when using TCAP in the SS No. 7 connectionless environment.</p><p>A take this to mean that you can't send a TCAP message bigger than the max number of data in a UDT message, in an UDT message. I think segmentation has to take place in the transport layer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Apr '14, 01:18</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-31459" class="comments-container"><span id="31461"></span><div id="comment-31461" class="comment"><div id="post-31461-score" class="comment-score"></div><div class="comment-text"><p>ok, great, thank you!</p></div><div id="comment-31461-info" class="comment-info"><span class="comment-age">(03 Apr '14, 01:38)</span> <span class="comment-user userinfo">Dianalab9</span></div></div></div><div id="comment-tools-31459" class="comment-tools"></div><div class="clear"></div><div id="comment-31459-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

