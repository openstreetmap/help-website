+++
type = "question"
title = "DT1 ranap message not decoding"
description = '''I have found lot of ranap messages are not decoded by wireshark. These messages are decoded up to sccp. -------------------------------------------- No. Time Source Destination Protocol Length Info  21781 18.879876 201 7 SCCP (Int. ITU) 122 DT1  Frame 21781: 122 bytes on wire (976 bits), 122 bytes c...'''
date = "2012-09-09T22:11:00Z"
lastmod = "2012-09-10T07:40:00Z"
weight = 14152
keywords = [ "ranap" ]
aliases = [ "/questions/14152" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [DT1 ranap message not decoding](/questions/14152/dt1-ranap-message-not-decoding)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14152-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14152-score" class="post-score" title="current number of votes">0</div><span id="post-14152-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have found lot of ranap messages are not decoded by wireshark. These messages are decoded up to sccp.</p><pre><code>--------------------------------------------
No.     Time        Source                Destination           Protocol Length Info
  21781 18.879876   201                   7                     SCCP (Int. ITU) 122    DT1

Frame 21781: 122 bytes on wire (976 bits), 122 bytes captured (976 bits)
Ethernet II, Src: AlcatelL_14:c5:44 (0c:a4:02:14:c5:44), Dst: AlcatelD_cd:c1:0c (00:11:3f:cd:c1:0c)
802.1Q Virtual LAN, PRI: 0, CFI: 0, ID: 1490
Internet Protocol Version 4, Src: 10.50.0.115 (10.50.0.115), Dst: 10.24.16.2 (10.24.16.2)
Stream Control Transmission Protocol, Src Port: m3ua (2905), Dst Port: m3ua (2905)
MTP 3 User Adaptation Layer
Signalling Connection Control Part
    Message Type: Data Form 1 (0x06)
    Destination Local Reference: 0x0d97d8
    .... ...0 = More data: No more data (0x00)
    Pointer to first Mandatory Variable parameter: 1
Data (23 bytes)

0000  d8 76 e8 00 14 c6 cd 00 40 52 00 01 40 02 40 03   .v......@R[email protected]@.
0010  00 00 00 03 40 01 00                              [email protected]
    Data: d876e80014c6cd00405200014002400300000003400100
    [Length: 23]
    -------------------------------------------------</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ranap" rel="tag" title="see questions tagged &#39;ranap&#39;">ranap</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Sep '12, 22:11</strong></p><img src="https://secure.gravatar.com/avatar/ff63d6abbb91e67370ca72fa125b2cae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="isarana&#39;s gravatar image" /><p><span>isarana</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="isarana has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Sep '12, 22:47</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-14152" class="comments-container"><span id="14155"></span><div id="comment-14155" class="comment"><div id="post-14155-score" class="comment-score"></div><div class="comment-text"><p>shall i open a bug report for this ?</p></div><div id="comment-14155-info" class="comment-info"><span class="comment-age">(10 Sep '12, 01:37)</span> <span class="comment-user userinfo">isarana</span></div></div></div><div id="comment-tools-14152" class="comment-tools"></div><div class="clear"></div><div id="comment-14152-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14160"></span>

<div id="answer-container-14160" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14160-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14160-score" class="post-score" title="current number of votes">2</div><span id="post-14160-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, I think the problem might bee that you don't have the connection request in the trace and Wireshark can't figure out the next protocol after SCCP as there is no connection information. You might want to play around with the SCCP preferences it might wotk to set the default payload to ranap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '12, 03:51</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-14160" class="comments-container"><span id="14164"></span><div id="comment-14164" class="comment"><div id="post-14164-score" class="comment-score"></div><div class="comment-text"><p>I have set the preferences to ranap. Still its not decoding correctly. <img src="https://osqa-ask.wireshark.org/upfiles/wireshark_pkt.PNG" alt="alt text" /></p></div><div id="comment-14164-info" class="comment-info"><span class="comment-age">(10 Sep '12, 07:40)</span> <span class="comment-user userinfo">isarana</span></div></div></div><div id="comment-tools-14160" class="comment-tools"></div><div class="clear"></div><div id="comment-14160-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

