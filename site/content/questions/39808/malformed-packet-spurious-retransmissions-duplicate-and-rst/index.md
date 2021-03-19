+++
type = "question"
title = "Malformed Packet, Spurious Retransmissions, Duplicate and RST"
description = '''I am analyzing LAN network traffic. While capturing traffic i found some problems given below. 1. Malformed Packet (Exception occurred) 2.Connection Reset RST. 3. Retransmission (suspected) 4. Spurious Retransmissions 5.. Duplicate Acknowledgement ACK. Can anyone tell me what is the actual reason be...'''
date = "2015-02-11T13:37:00Z"
lastmod = "2015-02-11T14:22:00Z"
weight = 39808
keywords = [ "tcp" ]
aliases = [ "/questions/39808" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Malformed Packet, Spurious Retransmissions, Duplicate and RST](/questions/39808/malformed-packet-spurious-retransmissions-duplicate-and-rst)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39808-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am analyzing LAN network traffic. While capturing traffic i found some problems given below. 1. Malformed Packet (Exception occurred) 2.Connection Reset RST. 3. Retransmission (suspected) 4. Spurious Retransmissions 5.. Duplicate Acknowledgement ACK. Can anyone tell me what is the actual reason behind this problem. Here is a link of capture file. <a href="https://drive.google.com/file/d/0B8asXfpLSWu5WXk2TmJNX0pWakE/view?usp=sharing">https://drive.google.com/file/d/0B8asXfpLSWu5WXk2TmJNX0pWakE/view?usp=sharing</a></p></div><div id="question-tags" class="tags-container tags">tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '15, 13:37</strong></p><img src="https://secure.gravatar.com/avatar/26db4cdccaf9209d05b0c74fff16b967?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mohdaftab93&#39;s gravatar image" /><p>mohdaftab93<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mohdaftab93 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Feb '15, 14:35</p></div></div><div id="comments-container-39808" class="comments-container"></div><div id="comment-tools-39808" class="comment-tools"></div><div class="clear"></div><div id="comment-39808-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="39811"></span>

<div id="answer-container-39811" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39811-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Can anyone tell me <strong>what is the actual reason behind this problem</strong>.</p></blockquote><p>Unfortunately nobody will be able to tell you <strong>the reason</strong> for those messages in Wireshark, because it could be caused by:</p><ul><li>a problem with your client, like driver problem, hardware defect, etc.</li><li>a problem with the server (same as client)</li><li>a problem in your network, which is causing packet loss, like overloaded switches,router, firewalls, etc. or even broken devices</li><li>a problem with you capturing setup and thus you were unable to capture all frames that have been on the link, like oversubscribing the port mirroring, a defect of you capturing nic, etc., etc.</li></ul><p>What we can do is to take a look at the capture file. Maybe there are other signs in that file. If you like to do that, please post the capture file somewhere (google drive, dropbox, cloudshark.org) and post the link here.</p><p><strong>++ UPDATE ++</strong></p><p>The capture file you posted looks totally normal. Occasional loss of packets is absolutely normal in any network, which will cause the messages in Wireshark you mentioned. So, no reason to worry.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '15, 14:21</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Feb '15, 14:45</p></div></div><div id="comments-container-39811" class="comments-container"><span id="39817"></span><div id="comment-39817" class="comment"><div id="post-39817-score" class="comment-score"></div><div class="comment-text"><p>Here is the link of capture file. <a href="https://drive.google.com/file/d/0B8asXfpLSWu5WXk2TmJNX0pWakE/view?usp=sharing">https://drive.google.com/file/d/0B8asXfpLSWu5WXk2TmJNX0pWakE/view?usp=sharing</a></p></div><div id="comment-39817-info" class="comment-info"><span class="comment-age">(11 Feb '15, 15:05)</span> mohdaftab93</div></div><span id="39818"></span><div id="comment-39818" class="comment"><div id="post-39818-score" class="comment-score"></div><div class="comment-text"><p>I already looked at the file. See my <strong>++UPDATE++</strong></p></div><div id="comment-39818-info" class="comment-info"><span class="comment-age">(11 Feb '15, 15:07)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-39811" class="comment-tools"></div><div class="clear"></div><div id="comment-39811-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39812"></span>

<div id="answer-container-39812" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39812-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><ol><li>Malformed packet means that the packet cannot be successfully dissected by Wireshark. It can be a code issue, or that the packet holds unexpected bytes, or is too short, or is damaged</li><li>Connection Reset is a packet that ends a TCP connection. Either after it was successful, or when there is a fatal problem. In most situations, it's just the end of a successful connection these days</li><li>Retransmission is TCP segment data that is sent again as a replacement for a lost segment</li><li>Spurious retransmission -&gt; see <a href="https://blog.packet-foo.com/2013/06/spurious-retransmissions/">https://blog.packet-foo.com/2013/06/spurious-retransmissions/</a></li><li>Duplicate ACKs occur when segments are lost. It is an indicator with which the receiver tells the sender that something is missing</li></ol><p>Without the packets it's hard to say if you have a problem, or just normal or noncritical behavior.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '15, 14:22</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-39812" class="comments-container"><span id="39816"></span><div id="comment-39816" class="comment"><div id="post-39816-score" class="comment-score"></div><div class="comment-text"><p>Here is the link of capture file. <a href="https://drive.google.com/file/d/0B8asXfpLSWu5WXk2TmJNX0pWakE/view?usp=sharing">https://drive.google.com/file/d/0B8asXfpLSWu5WXk2TmJNX0pWakE/view?usp=sharing</a></p></div><div id="comment-39816-info" class="comment-info"><span class="comment-age">(11 Feb '15, 15:03)</span> mohdaftab93</div></div></div><div id="comment-tools-39812" class="comment-tools"></div><div class="clear"></div><div id="comment-39812-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

