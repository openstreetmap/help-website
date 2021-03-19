+++
type = "question"
title = "data length"
description = '''![alt text][1] Hi all, I&#x27;m trying to understand the data length and segment length calculation. I tried to take the IP total length and subtract the Ip Header length and the Tcp Header length but there seem to a difference for some frames. What is the reason? Cheers, A'''
date = "2015-07-26T21:00:00Z"
lastmod = "2015-08-03T00:26:00Z"
weight = 44512
keywords = [ "tcppackets" ]
aliases = [ "/questions/44512" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [data length](/questions/44512/data-length)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44512-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44512-score" class="post-score" title="current number of votes">0</div><span id="post-44512-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>![alt text][1]</p><p>Hi all,</p><p>I'm trying to understand the data length and segment length calculation. I tried to take the IP total length and subtract the Ip Header length and the Tcp Header length but there seem to a difference for some frames. What is the reason?</p><p>Cheers, A</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcppackets" rel="tag" title="see questions tagged &#39;tcppackets&#39;">tcppackets</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jul '15, 21:00</strong></p><img src="https://secure.gravatar.com/avatar/4c677562260c945708be7ab99ca96a1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adriannuix&#39;s gravatar image" /><p><span>adriannuix</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adriannuix has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Jul '15, 18:11</strong> </span></p></div></div><div id="comments-container-44512" class="comments-container"><span id="44570"></span><div id="comment-44570" class="comment"><div id="post-44570-score" class="comment-score"></div><div class="comment-text"><p>Could you post the packet on cloudshark or google drive so that it can be examined?</p><p>It is difficult to analyze with a screen shot.</p></div><div id="comment-44570-info" class="comment-info"><span class="comment-age">(28 Jul '15, 10:21)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="44613"></span><div id="comment-44613" class="comment"><div id="post-44613-score" class="comment-score"></div><div class="comment-text"><p><a href="https://drive.google.com/file/d/0B2E18hcsiwRnZ1U3UjFXSzVtcnM/view?usp=sharing">https://drive.google.com/file/d/0B2E18hcsiwRnZ1U3UjFXSzVtcnM/view?usp=sharing</a></p></div><div id="comment-44613-info" class="comment-info"><span class="comment-age">(29 Jul '15, 18:08)</span> <span class="comment-user userinfo">adriannuix</span></div></div></div><div id="comment-tools-44512" class="comment-tools"></div><div class="clear"></div><div id="comment-44512-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="44583"></span>

<div id="answer-container-44583" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44583-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44583-score" class="post-score" title="current number of votes">0</div><span id="post-44583-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There the follwing length now:<br />
<strong>Frame length:</strong> Total length of the Frame, including the Padding Fields (if present and needed) of the Ethernet Layer<br />
<strong>Captured Length:</strong> Frame Length which is captured (Interresting if a filter has been used)<br />
<strong>IP.TotalLength:</strong> Total Packet Length. from IP-Header until Layer 7 payload ends<br />
<strong>TCP.SegmentLegth:</strong> Resulting TCP Payload and only calculated by Wireshark<br />
<strong>TCP.HeaderLength:</strong> Is the length of the TCP Header, because header size is variabel</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jul '15, 23:59</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Aug '15, 13:29</strong> </span></p></div></div><div id="comments-container-44583" class="comments-container"><span id="44614"></span><div id="comment-44614" class="comment"><div id="post-44614-score" class="comment-score"></div><div class="comment-text"><p>I updated the link for a full file.</p><p>Thank you</p></div><div id="comment-44614-info" class="comment-info"><span class="comment-age">(29 Jul '15, 18:12)</span> <span class="comment-user userinfo">adriannuix</span></div></div><span id="44617"></span><div id="comment-44617" class="comment"><div id="post-44617-score" class="comment-score"></div><div class="comment-text"><p>In the new trace I can´t see any uncommon length like at the old trace?!</p></div><div id="comment-44617-info" class="comment-info"><span class="comment-age">(29 Jul '15, 20:43)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="44745"></span><div id="comment-44745" class="comment"><div id="post-44745-score" class="comment-score"></div><div class="comment-text"><pre><code>In the new trace I can´t see any uncommon length like at the old trace?!</code></pre><p>I have spotted some, for example Frame 51 and Frame 52.</p></div><div id="comment-44745-info" class="comment-info"><span class="comment-age">(02 Aug '15, 16:09)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-44583" class="comment-tools"></div><div class="clear"></div><div id="comment-44583-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="44742"></span>

<div id="answer-container-44742" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44742-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44742-score" class="post-score" title="current number of votes">0</div><span id="post-44742-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The problem is that the packet was written to the trace file with an incorrect frame.len of 66 bytes. If the original ip.len was 58 bytes and it is traveling over ethernet (which adds 14 bytes to the frame.len) wireshark thinks that the packet is only containing ip header plus tcp header plus 12 bytes tcp timestamp options in total 52 bytes.)<br />
This happens for more outbound packets.<br />
The filter to find those is <code>(frame.len==66 and ip.len gt 52) or frame.number ==51 or frame.number==17 or frame.number==31 or frame.number==69 or frame.number==77</code><br />
. <img src="https://osqa-ask.wireshark.org/upfiles/wireshark_NB5yZOx.png" alt="alt text" /> This seems to be a problem with the packet capturing tool (tcpdump on linux?).<br />
Given that the trace file is dated 28 Nov 1999 I believe the problem should have been fixed by now</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Aug '15, 13:13</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Aug '15, 00:38</strong> </span></p></div></div><div id="comments-container-44742" class="comments-container"><span id="44744"></span><div id="comment-44744" class="comment"><div id="post-44744-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@mrEEde</span>: Just out of curiosity. What do you think about Frame51 and Frame52 in the trace? Look at the IP.ID and the TCP Checksum.</p><p>I think the Frame 52 is a corrupted version of Frame 51. Perhaps only in the capture file not really on the wire. (Because the corrupted Frame is always behind the original Frame).</p></div><div id="comment-44744-info" class="comment-info"><span class="comment-age">(02 Aug '15, 16:06)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="44751"></span><div id="comment-44751" class="comment"><div id="post-44751-score" class="comment-score"></div><div class="comment-text"><p>Christian, frame 52 is not corrupted, it is an incomplete copy of frame 51 with no payload. As the tcp.checksum is calculated including the payload and the payload is missing, wireshark detects it as incorrect.<br />
So the trace tool was trying to trace headers only but not only reduced the frame.cap_len to 66 bytes but also the frame.len which is incorrect.</p></div><div id="comment-44751-info" class="comment-info"><span class="comment-age">(02 Aug '15, 23:34)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="44754"></span><div id="comment-44754" class="comment"><div id="post-44754-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@mrEEde</span>: Thank you. So you think the same as I, that the strange frames only appear in the trace file. And the frames you posted in the picture of your updated answr are exactly the frames I have meant.</p></div><div id="comment-44754-info" class="comment-info"><span class="comment-age">(03 Aug '15, 00:26)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-44742" class="comment-tools"></div><div class="clear"></div><div id="comment-44742-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

