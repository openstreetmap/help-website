+++
type = "question"
title = "TCP-flag SYN"
description = '''After taking a capture and going back to my wireshark class notes - I know TCP header size should be between 20 and 32 bytes. Within my environment i am seeing a variation of TCP SYN flag header length with 40 bytes. we are starting to block it but wanted to get more info on this&amp;gt; If somebody can...'''
date = "2015-12-23T04:24:00Z"
lastmod = "2015-12-23T09:59:00Z"
weight = 48682
keywords = [ "tcpflags", "syn" ]
aliases = [ "/questions/48682" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP-flag SYN](/questions/48682/tcp-flag-syn)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48682-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>After taking a capture and going back to my wireshark class notes - I know TCP header size should be between 20 and 32 bytes. Within my environment i am seeing a variation of TCP SYN flag header length with 40 bytes. we are starting to block it but wanted to get more info on this&gt; If somebody can share somelight. s<img src="https://osqa-ask.wireshark.org/upfiles/tcp_40bytes.PNG" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/tcp_40bytes.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">tcpflags syn</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Dec '15, 04:24</strong></p><img src="https://secure.gravatar.com/avatar/5902c771c9609c2fa34087def265627e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dgo%20Vrgs&#39;s gravatar image" /><p>Dgo Vrgs<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dgo Vrgs has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 23 Dec '15, 07:01</p></div></div><div id="comments-container-48682" class="comments-container"><span id="48683"></span><div id="comment-48683" class="comment"><div id="post-48683-score" class="comment-score"></div><div class="comment-text"><p>You're mistaken, TCP header maximum size is not 32 bytes. Valid TCP header sizes are between 20 and 60 bytes, so 40 bytes is okay. What options do you see in the header? And why do you block headers with 40 bytes?</p></div><div id="comment-48683-info" class="comment-info"><span class="comment-age">(23 Dec '15, 05:28)</span> Jasper ♦♦</div></div><span id="48687"></span><div id="comment-48687" class="comment"><div id="post-48687-score" class="comment-score"></div><div class="comment-text"><p>Jasper, thank you for the response - im still trying to figure out as there is one specific customer that complains when we see not sure if it's the packet length total of 40 bytes or the segment header length of 40 bytes. Gonna do some digging and get an example posted. In either case a packet with length 40 should still be good even if the segment is only 40 bytes.</p><p>The actual segment length is 40Bytes - I personally dont see anything wrong with it.</p></div><div id="comment-48687-info" class="comment-info"><span class="comment-age">(23 Dec '15, 06:26)</span> Dgo Vrgs</div></div><span id="48794"></span><div id="comment-48794" class="comment"><div id="post-48794-score" class="comment-score"></div><div class="comment-text"><p>To add to Jasper reply, here is a possible reason why you are seeing 4NOP in a row or more. A known thread that I've seen that potentially a Cisco device modifying the TCP options in the past. <a href="https://supportforums.cisco.com/discussion/11035321/cisco-asa-831-rtmp-content-fails-play#3218614">https://supportforums.cisco.com/discussion/11035321/cisco-asa-831-rtmp-content-fails-play#3218614</a></p></div><div id="comment-48794-info" class="comment-info"><span class="comment-age">(02 Jan '16, 11:32)</span> hunghoong</div></div></div><div id="comment-tools-48682" class="comment-tools"></div><div class="clear"></div><div id="comment-48682-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48688"></span>

<div id="answer-container-48688" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48688-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>That screenshot lists TCP options that are most certainly bogus. NOPs in TCP options are used for 32 bit alignment, so you never need more than 3 in a row; often you only see one. There's two possibilities here:</p><ol><li>an attacker is trying to fool around with your systems, generating weird TCP option sets. In which case it would make sense to block them if you can. Keep in mind that the length of 40 bytes is not a good filter indicator as there may be valid TCP headers with that size.</li><li>you have a device in your network that removes valid TCP options and replaces them with NOPs. Some Cisco devices have been known to do this in the past, which is why you see the "Expert Info 4 NOP in a row" warning.</li></ol><p>If I were you I'd try to capture the same packets directly at the WAN interface of the router to your internet uplink (the interface closest to the internet which is still under your control), and check if the packets look strange there, too. If so, you've probably got an attacker, but you should still talk to your ISP about it, maybe they know what's happening. If not (and you see correct options instead of the NOPs) you have a device in your network that is misbehaving.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Dec '15, 09:59</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></img></div></div><div id="comments-container-48688" class="comments-container"><span id="48786"></span><div id="comment-48786" class="comment"><div id="post-48786-score" class="comment-score"></div><div class="comment-text"><p>Jasper, thank you so much for the info. i bit late but this makes sense</p></div><div id="comment-48786-info" class="comment-info"><span class="comment-age">(01 Jan '16, 10:56)</span> Dgo Vrgs</div></div><span id="48787"></span><div id="comment-48787" class="comment"><div id="post-48787-score" class="comment-score"></div><div class="comment-text"><p>@Dgo Vrgs</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-48787-info" class="comment-info"><span class="comment-age">(01 Jan '16, 11:48)</span> grahamb ♦</div></div></div><div id="comment-tools-48688" class="comment-tools"></div><div class="clear"></div><div id="comment-48688-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

