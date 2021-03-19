+++
type = "question"
title = "why do we make use of a tap interface for RTP statistics?"
description = '''Hi, What is the need/advantage of using tap interface for calculating RTP statistics? Why not simply read from a RAW socket which will give entire packet information such as FRAME info etc., i.e., files tap-rtp-common.c that has rtp-stream_packet. I understand that for some statistics such as jitter...'''
date = "2013-03-22T07:38:00Z"
lastmod = "2013-03-22T16:24:00Z"
weight = 19751
keywords = [ "tap", "rtp" ]
aliases = [ "/questions/19751" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [why do we make use of a tap interface for RTP statistics?](/questions/19751/why-do-we-make-use-of-a-tap-interface-for-rtp-statistics)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19751-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>What is the need/advantage of using tap interface for calculating RTP statistics? Why not simply read from a RAW socket which will give entire packet information such as FRAME info etc.,</p><p>i.e., files tap-rtp-common.c that has rtp-stream_packet. I understand that for some statistics such as jitter, we need frame time information etc., So we need entire frame data and not just UDP info.</p><p>But any advantage in using the tap interface instead of simply reading from SOCK_RAW?</p><p>Any info will be very much appreciated.</p><p>Thanks, Badri.</p></div><div id="question-tags" class="tags-container tags">tap rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '13, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/a61a39377187ba85feebe6c0da639b66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="badrigate&#39;s gravatar image" /><p>badrigate<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="badrigate has no accepted answers">0%</span></p></div></div><div id="comments-container-19751" class="comments-container"></div><div id="comment-tools-19751" class="comment-tools"></div><div class="clear"></div><div id="comment-19751-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19761"></span>

<div id="answer-container-19761" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19761-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Do you want to see only live traffic; how about capture files then?</p><p>How do you intent to figure out what the RTP frames are among the frames coming in from the raw socket?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '13, 09:59</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-19761" class="comments-container"></div><div id="comment-tools-19761" class="comment-tools"></div><div class="clear"></div><div id="comment-19761-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19765"></span>

<div id="answer-container-19765" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19765-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>But any advantage in using the tap interface instead of simply reading from SOCK_RAW?</p></blockquote><p>The advantage is that you get to use Wireshark's code for dissecting RTP rather than writing your own program to read from a SOCK_RAW socket and doing whatever parsing of RTP packets you want to do; I know of no OS with an in-kernel RTP implementation such that the SOCK_RAW socket will give you anything more than just packet data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '13, 16:24</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-19765" class="comments-container"><span id="19767"></span><div id="comment-19767" class="comment"><div id="post-19767-score" class="comment-score"></div><div class="comment-text"><p>hi guy,</p><p>My doubt is on wireshark's implementation. I am seeing many RTP stacks that use only udp_recv for their implementations. But wireshark uses a tap interface for calculating rtp statistics. In particular, for jitter calculation, we need frame information. so it makes sense to have entire data packet and not just udp info. But wireshark developers could have read that info from SOCK_RAW instead of using a tap interface.</p><p>Thanks, Badri.</p></div><div id="comment-19767-info" class="comment-info"><span class="comment-age">(23 Mar '13, 01:02)</span> badrigate</div></div><span id="19772"></span><div id="comment-19772" class="comment"><div id="post-19772-score" class="comment-score"></div><div class="comment-text"><p>If I may say so, please read Jaap's answer again. Wireshark can dissect <em>files</em> as well as other sources of input.</p><p>So: that's just one reason while reading from SOCK_RAW isn't going to be relevant.</p><p>By the way: Wireshark's "tap interface" is just an internal mechanism whereby analysis portions of Wireshark can obtain access to specific type of frames.</p></div><div id="comment-19772-info" class="comment-info"><span class="comment-age">(23 Mar '13, 09:22)</span> Bill Meier ♦♦</div></div><span id="19776"></span><div id="comment-19776" class="comment"><div id="post-19776-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I am seeing many RTP stacks that use only udp_recv for their implementations.</p></blockquote><p>Wireshark does not <em>have</em> an "RTP stack". It's a protocol analyzer, not an RTP client or server.</p><blockquote><p>In particular, for jitter calculation, we need frame information. so it makes sense to have entire data packet and not just udp info.</p></blockquote><p>What do you mean by "frame information"? Do you mean the link-layer and IP header? Do you mean the frame time stamp? The frame time stamp <em>is</em> available to the RTP dissector and it can provide that information to a tap.</p></div><div id="comment-19776-info" class="comment-info"><span class="comment-age">(23 Mar '13, 11:37)</span> Guy Harris ♦♦</div></div><span id="19777"></span><div id="comment-19777" class="comment"><div id="post-19777-score" class="comment-score"></div><div class="comment-text"><blockquote><p>But wireshark developers could have read that info from SOCK_RAW</p></blockquote><p>No, we could <em>NOT</em> have done so.</p><p>For one thing, as Jaap and Bill Meier noted, Wireshark reads <em>files</em>.</p><p>For another thing, when doing a live traffic capture, Wireshark uses whatever raw packet capture mechanism is in the OS. That is not necessarily a SOCK_RAW socket.</p></div><div id="comment-19777-info" class="comment-info"><span class="comment-age">(23 Mar '13, 11:39)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-19765" class="comment-tools"></div><div class="clear"></div><div id="comment-19765-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

