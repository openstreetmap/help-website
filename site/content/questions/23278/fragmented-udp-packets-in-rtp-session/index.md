+++
type = "question"
title = "Fragmented UDP Packets in RTP Session"
description = '''Hello, I have a problem on a video conference system over wan with fragmented udp packets. In a video session are a lot of stops on the screen. I have created a wireshark dump where I have found a lot of the following messages &quot;Fragmented IP protocol (proto=UDP 17, off=0, ID=39a4) [Reassembled in #1...'''
date = "2013-07-23T00:04:00Z"
lastmod = "2013-07-23T00:04:00Z"
weight = 23278
keywords = [ "fragment", "udp", "rtp" ]
aliases = [ "/questions/23278" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Fragmented UDP Packets in RTP Session](/questions/23278/fragmented-udp-packets-in-rtp-session)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23278-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have a problem on a video conference system over wan with fragmented udp packets. In a video session are a lot of stops on the screen. I have created a wireshark dump where I have found a lot of the following messages "Fragmented IP protocol (proto=UDP 17, off=0, ID=39a4) [Reassembled in #15794]</p><p>The first to solve this problem for me is, to configure qos between both sites. The other one is, the check the mtu size on the systems. What else can I do to solve the problem?</p><p>THANKS</p></div><div id="question-tags" class="tags-container tags">fragment udp rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jul '13, 00:04</strong></p><img src="https://secure.gravatar.com/avatar/2d3344dc2a69d0ad82d625b75f46640e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flugfaust&#39;s gravatar image" /><p>flugfaust<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flugfaust has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Jul '13, 02:23</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-23278" class="comments-container"><span id="23344"></span><div id="comment-23344" class="comment"><div id="post-23344-score" class="comment-score"></div><div class="comment-text"><p>Does nobody have a solution for me?</p></div><div id="comment-23344-info" class="comment-info"><span class="comment-age">(24 Jul '13, 13:50)</span> flugfaust</div></div><span id="23357"></span><div id="comment-23357" class="comment"><div id="post-23357-score" class="comment-score"></div><div class="comment-text"><p>Not really an "Ask Wireshark" question, more a "Fix my Network Request", hence the lack of replies.</p></div><div id="comment-23357-info" class="comment-info"><span class="comment-age">(25 Jul '13, 02:39)</span> grahamb ♦</div></div><span id="23358"></span><div id="comment-23358" class="comment"><div id="post-23358-score" class="comment-score"></div><div class="comment-text"><p>I wonder if the conference system should be making RTP packets so large that they have to be fragmented or do you have a smaller MTU than expected(by the application)? How large are the fragments? Freeze might be caused by packet loss have you checked for that?</p></div><div id="comment-23358-info" class="comment-info"><span class="comment-age">(25 Jul '13, 04:22)</span> Anders ♦</div></div></div><div id="comment-tools-23278" class="comment-tools"></div><div class="clear"></div><div id="comment-23278-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

