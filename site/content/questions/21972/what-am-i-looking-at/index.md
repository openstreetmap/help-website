+++
type = "question"
title = "What am I looking at?"
description = '''Hello all, We have been having some serious performance problems from one of our applications. One of the suspects is the communication between our apps server and our SQL server. So I got a wireshark capture between the two and there is red everywhere, but I don&#x27;t know what I&#x27;m looking at. I&#x27;m not ...'''
date = "2013-06-12T12:50:00Z"
lastmod = "2013-06-12T13:54:00Z"
weight = 21972
keywords = [ "errors" ]
aliases = [ "/questions/21972" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What am I looking at?](/questions/21972/what-am-i-looking-at)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21972-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21972-score" class="post-score" title="current number of votes">0</div><span id="post-21972-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>We have been having some serious performance problems from one of our applications. One of the suspects is the communication between our apps server and our SQL server. So I got a wireshark capture between the two and there is red everywhere, but I don't know what I'm looking at. I'm not a network guy, but I am digging to see if I can help fix this problem.</p><p>I checked the 'Expert Infos' and it has several errors:</p><p>Checksum IPv4 Bad Checksum 26027 Molformed TDS Malformed Packet(Exception occurred) 763 Checksum Ethernet Bad checksum 1400</p><p>This is a 30 second capture. Can I get some advice on whether this is bad and, if so, where should I look for the problem?</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-errors" rel="tag" title="see questions tagged &#39;errors&#39;">errors</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jun '13, 12:50</strong></p><img src="https://secure.gravatar.com/avatar/021f86739cdc63adfeb07c9ed73cf727?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rwigs&#39;s gravatar image" /><p><span>rwigs</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rwigs has no accepted answers">0%</span></p></div></div><div id="comments-container-21972" class="comments-container"></div><div id="comment-tools-21972" class="comment-tools"></div><div class="clear"></div><div id="comment-21972-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21973"></span>

<div id="answer-container-21973" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21973-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21973-score" class="post-score" title="current number of votes">1</div><span id="post-21973-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It depends on where you captured - if you did the capture on one of the devices that are part of the problem you probably "created" the CRC errors by the way you recorded the packets. But you also said you captured "between the two" which would usually mean that you had a third, passive device doing the capture, in which case the CRC errors would be a bad thing.</p><p>You can probably ignore the TDS messages, since this one just means that the TDS dissector in Wireshark had problems dissecting the payload. This is not a network error, it's a decoding problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '13, 12:56</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-21973" class="comments-container"><span id="21977"></span><div id="comment-21977" class="comment"><div id="post-21977-score" class="comment-score"></div><div class="comment-text"><p>The capture was run on the APPS server, but I did uncheck 'Validate the TCP checksum if possible" option (I read that can cause these errors). There is also:</p><p>1 Warning: Acknowledgement number: Broken TCP. The acknowledge field is nonzero</p><p>12 Notes: "Time To Live" != 255 for a packet sent to the Local Network Control Block 1 No bind info for interface Context ID:0 375 Keep-Alive 131 Keep-Alive ACK 131 Retransmission(suspected) 11 Duplicate ACK(#1) 5 Duplicate ACK(#2) 2 Duplicate ACK(#3) 1 Fast Retransmission(suspected) 1 Duplicate ACK(#4) 1 Duplicate ACK(#5) 1 Duplicate ACK(#6) 1</p><p>6 Chats: Connection finish(FIN) 25 Connection reset(RST) 3 Connection establish request(SYS):server port microsoft-ds 1 Connection establish acknowledge(SYN+ACK)server port microsoft-ds 1 Connection establish request(SYS):server port netbios-ssn 1 Connection establish acknowledge(SYN+ACK)server port netbios-ssn 1</p><p>Does any of this provide more information?</p></div><div id="comment-21977-info" class="comment-info"><span class="comment-age">(12 Jun '13, 13:34)</span> <span class="comment-user userinfo">rwigs</span></div></div><span id="21979"></span><div id="comment-21979" class="comment"><div id="post-21979-score" class="comment-score"></div><div class="comment-text"><p>"Validate the TCP checksum if possible" is a <strong>display</strong> setting, not a recording setting, so it will tell Wireshark to not mark bad CRCs in the display, but it will still record bad CRCs when capturing.</p><p>The Time to live message is interesting but in most cases it is just a device not following RFC completely. It would require more investigation, especially into the source it is coming from.</p><p>The Keep alives are usually irrelevant, while Duplicate ACKs and Retransmissions can hint towards connection problems, but still need more investigation. For that a look into the capture file is necessary, because just reading the expert messages is not nearly providing enough details.</p><p>Forget the chats.</p></div><div id="comment-21979-info" class="comment-info"><span class="comment-age">(12 Jun '13, 13:54)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-21973" class="comment-tools"></div><div class="clear"></div><div id="comment-21973-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

