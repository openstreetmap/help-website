+++
type = "question"
title = "Find the sip.call-id of a RTN event ?"
description = '''Hi everybody, I have a 50 MB pcap file with 80 VoIP captured calls. Only 2 of this VoIP sessions has a RTN (Retrain Negative) response inside, founded using the display filter: t30.FacsimileControl == 50 The question is how can I found automatically the 2 caller IDs of the SIP sessions that contain ...'''
date = "2016-05-26T07:13:00Z"
lastmod = "2016-05-26T09:56:00Z"
weight = 52962
keywords = [ "retrain", "rtn", "parser", "negative" ]
aliases = [ "/questions/52962" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Find the sip.call-id of a RTN event ?](/questions/52962/find-the-sipcall-id-of-a-rtn-event)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52962-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52962-score" class="post-score" title="current number of votes">0</div><span id="post-52962-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everybody,</p><p>I have a 50 MB pcap file with 80 VoIP captured calls. Only 2 of this VoIP sessions has a RTN (Retrain Negative) response inside, founded using the display filter: t30.FacsimileControl == 50</p><p>The question is how can I found automatically the 2 caller IDs of the SIP sessions that contain RTN ? I can found it manualy, opening one by one all the 80 Flow sequences, but I need to automatically analise hundreds of pcap file with thousands of VoIP calls.</p><p>Thank you for your precious support,</p><p>Serban</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-retrain" rel="tag" title="see questions tagged &#39;retrain&#39;">retrain</span> <span class="post-tag tag-link-rtn" rel="tag" title="see questions tagged &#39;rtn&#39;">rtn</span> <span class="post-tag tag-link-parser" rel="tag" title="see questions tagged &#39;parser&#39;">parser</span> <span class="post-tag tag-link-negative" rel="tag" title="see questions tagged &#39;negative&#39;">negative</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 May '16, 07:13</strong></p><img src="https://secure.gravatar.com/avatar/7cc0965a77db91a7b64ca5bf88811404?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Serban&#39;s gravatar image" /><p><span>Serban</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Serban has no accepted answers">0%</span></p></div></div><div id="comments-container-52962" class="comments-container"></div><div id="comment-tools-52962" class="comment-tools"></div><div class="clear"></div><div id="comment-52962-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52963"></span>

<div id="answer-container-52963" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52963-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52963-score" class="post-score" title="current number of votes">0</div><span id="post-52963-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><a href="https://wiki.wireshark.org/Mate/Manual">MATE</a> is the answer. It allows you to extract some information from both the SIP packets and the RTP (well, udptl as we talk about T.38 here) packets into generated protocol fields added to their dissection trees, and use these generated protocol fields to link together the packets of different protocols which belong to the same VoIP call (and eventually filter on them).</p><p>In particular, you would use the connection information (IP address and port) from the SDPs to identify the RTP flow established using those SDPs, and augment each RTP packet with contents of From and To headers (and/or, if you insist, the Call-ID) of the establishing SIP INVITE. So you would again use your display filter <code>t30.FacsimileControl == 50</code> to show only the udptl packets matching that expression, but the MATE fields added to the dissection tree of these packets would show the contents of the SIP headers as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 May '16, 07:36</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 May '16, 04:36</strong> </span></p></div></div><div id="comments-container-52963" class="comments-container"><span id="52964"></span><div id="comment-52964" class="comment"><div id="post-52964-score" class="comment-score"></div><div class="comment-text"><p>Hi Sindy,</p><p>thank you for your fast and accurate answer. I'll start to learn MATE and hope to solve this problem. Kepp you upated. Serban</p></div><div id="comment-52964-info" class="comment-info"><span class="comment-age">(26 May '16, 08:54)</span> <span class="comment-user userinfo">Serban</span></div></div><span id="52965"></span><div id="comment-52965" class="comment"><div id="post-52965-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@Serban</span>, glad to help. Now something about the house rules (see site FAQ for details):</p><ul><li><p>at this site, Answers are only posts which answer the original Question. All the rest are Comments. So I've converted your post accordingly.</p></li><li><p>the idea of this site is to build a Q&amp;A knowledge base. So if you find an Answer helpful, mark it as such ("accept" it) by clicking the checkmark (not "thumbs up") icon next to it. This changes the colour in the list of questions to green, indicating to other people asking the same or similar question that the Question has ever got a useful Answer. So as soon as you solve your task using MATE, please come back and Accept the answer.</p></li></ul></div><div id="comment-52965-info" class="comment-info"><span class="comment-age">(26 May '16, 09:06)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="52966"></span><div id="comment-52966" class="comment"><div id="post-52966-score" class="comment-score"></div><div class="comment-text"><p>ok Sindy. I'll be back on the topic as soon as I'll do progress on MATE. Thank you</p></div><div id="comment-52966-info" class="comment-info"><span class="comment-age">(26 May '16, 09:56)</span> <span class="comment-user userinfo">Serban</span></div></div></div><div id="comment-tools-52963" class="comment-tools"></div><div class="clear"></div><div id="comment-52963-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

