+++
type = "question"
title = "Window size value in the ACK packet of a SYN-SYN/ACK-ACK handshake"
description = '''Hi, Can somebody explain me why the initial WS value in the SYN packet differs from the WS value of the ACK packet and whether there is a way to calculate it ? Example : SYN : Win=65535 MS=1460 WS=4 SYN/ACK : Win=65535 MS=1460 WS=1 ACK : Win=256960  I know 256960 comes from the following calculation...'''
date = "2016-04-01T11:15:00Z"
lastmod = "2016-04-02T06:20:00Z"
weight = 51352
keywords = [ "windowscale" ]
aliases = [ "/questions/51352" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Window size value in the ACK packet of a SYN-SYN/ACK-ACK handshake](/questions/51352/window-size-value-in-the-ack-packet-of-a-syn-synack-ack-handshake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51352-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Can somebody explain me why the initial WS value in the SYN packet differs from the WS value of the ACK packet and whether there is a way to calculate it ?</p><p>Example :</p><pre><code>SYN : Win=65535 MS=1460 WS=4
SYN/ACK : Win=65535 MS=1460 WS=1
ACK : Win=256960</code></pre>I know 256960 comes from the following calculation but this is apparently not always the case for other PCAPs I've analyzed.<p>65535/1460 = 44.89 So 44 full size frame max x 1460 x 4 = 256960.</p><p>Thanks, Thierry</p></div><div id="question-tags" class="tags-container tags">windowscale</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '16, 11:15</strong></p><img src="https://secure.gravatar.com/avatar/eac75eef24254c1c9ee690951f6c4006?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thierryn&#39;s gravatar image" /><p>thierryn<br />
<span class="score" title="21 reputation points">21</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thierryn has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Apr '16, 12:45</p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-51352" class="comments-container"></div><div id="comment-tools-51352" class="comment-tools"></div><div class="clear"></div><div id="comment-51352-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="51353"></span>

<div id="answer-container-51353" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51353-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>in a scenario like this...:</p><pre><code>(1)Client -&gt; Server: SYN     Win=65535 WS=4
(2)Server -&gt; Client: SYN,ACK Win=65535 WS=1
(3)Client -&gt; Server: ACK     Win=256960</code></pre><p>Wireshark shows us in the Info column of the Frames (1) and (2) not the calculated Window Size, like we can see it in Frame (3), because....<br />
</p><ul><li>The window size in the SYN Packets is never scaled</li><li>The Window Scale Option(WS) may only be activated if both partners advertises these option</li><li>The SYN packets are the only location where the WS option may appear</li></ul><p>And the formula for the window size in the ack segment is for Wireshark info column displays <code> calculated window size = window size * window scale factor ( 262140 = 65535 *4 )</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Apr '16, 11:55</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Apr '16, 13:25</p></div></div><div id="comments-container-51353" class="comments-container"><span id="51356"></span><div id="comment-51356" class="comment"><div id="post-51356-score" class="comment-score"></div><div class="comment-text"><p>Sorry Christian, but it's not clear for me. Your calculation is wrong : 65535 * 4 is not 256960 but 262140. That's why it's not clear to me...</p></div><div id="comment-51356-info" class="comment-info"><span class="comment-age">(01 Apr '16, 12:28)</span> thierryn</div></div><span id="51357"></span><div id="comment-51357" class="comment"><div id="post-51357-score" class="comment-score"></div><div class="comment-text"><p>Ok sorry haven't calculated it, And I edited the answer. So what is the value of window size field in the packet detail pane of the ACK segment? The value should be 64.240 for 256960. Please see that there will be 2 values <code>window size</code> and <code>calculated window size</code>. As shown in my answer.</p></div><div id="comment-51357-info" class="comment-info"><span class="comment-age">(01 Apr '16, 12:34)</span> Christian_R</div></div></div><div id="comment-tools-51353" class="comment-tools"></div><div class="clear"></div><div id="comment-51353-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="51358"></span>

<div id="answer-container-51358" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51358-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The scale factor is only specified in packets with a SYN flag, so the client tells it scale factor in the SYN packet, the server in the SYN/ACK packet. Scaling is only used if both offer a scale factor, otherwise it can't be used by either node. A node offering a scale factor of 1 basically says "I know how it works, but I'm not going to use it myself". A Scale factor is then used for all other packets coming from the same node.</p><p>What you need to do is look at the "Window Size Value" field in the TCP layer, and multiply that with the Window Scale Multiplier in the SYN packet TCP options, in your case 4. And do that for all following packets from the client to get the actual window size.</p><p>The value 256960 equals 64240*4, so I guess your ACK packet had a "Window Size Value" of 64240.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Apr '16, 12:52</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Apr '16, 13:10</p></div></div><div id="comments-container-51358" class="comments-container"><span id="51359"></span><div id="comment-51359" class="comment"><div id="post-51359-score" class="comment-score"></div><div class="comment-text"><p>Agree: The scale factor like 2^4 = 16 is the correct interpretation for the WS scale field in the header and the packet detail pane, if the value is 4.<br />
</p><p>But Wireshark shows us the calculated decimal value, in this case the 16 in the info column. So nobody should be wondering...</p></div><div id="comment-51359-info" class="comment-info"><span class="comment-age">(01 Apr '16, 13:00)</span> Christian_R</div></div><span id="51360"></span><div id="comment-51360" class="comment"><div id="post-51360-score" class="comment-score"></div><div class="comment-text"><p>Uh oh I think I mixed your example with the one in the question... I think I'll have to rewrite my answer</p></div><div id="comment-51360-info" class="comment-info"><span class="comment-age">(01 Apr '16, 13:03)</span> Jasper ♦♦</div></div><span id="51362"></span><div id="comment-51362" class="comment"><div id="post-51362-score" class="comment-score"></div><div class="comment-text"><p>Yeah it was cheeky, from me to use my own values at the first part of the answer and using the values of the question in the second the part ;) I will correct my answer, too.</p></div><div id="comment-51362-info" class="comment-info"><span class="comment-age">(01 Apr '16, 13:21)</span> Christian_R</div></div></div><div id="comment-tools-51358" class="comment-tools"></div><div class="clear"></div><div id="comment-51358-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="51367"></span>

<div id="answer-container-51367" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51367-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hey guys,</p><p>These are the three-way handshake packets :</p><p><img src="https://osqa-ask.wireshark.org/upfiles/2016-04-02_13-42-00_Rst3AtY.gif" alt="alt text" /></p><p>So Why is Win=65535 with WS=4 at the SYN packet and Win=256960 (and not 65535x4) at the ACK packet ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '16, 04:46</strong></p><img src="https://secure.gravatar.com/avatar/eac75eef24254c1c9ee690951f6c4006?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thierryn&#39;s gravatar image" /><p>thierryn<br />
<span class="score" title="21 reputation points">21</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thierryn has no accepted answers">0%</span> </br></p></img></div></div><div id="comments-container-51367" class="comments-container"><span id="51368"></span><div id="comment-51368" class="comment"><div id="post-51368-score" class="comment-score"></div><div class="comment-text"><p>The window size is unique for every segment but the scale factor is advertised only in the syn segments. So for the ack you have 256960 which equals the window size of 64240 multiplied by the Ws of 4. Which we both told you.</p></div><div id="comment-51368-info" class="comment-info"><span class="comment-age">(02 Apr '16, 05:53)</span> Christian_R</div></div></div><div id="comment-tools-51367" class="comment-tools"></div><div class="clear"></div><div id="comment-51367-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="51369"></span>

<div id="answer-container-51369" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51369-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is the point : why 64240 x 4 and not 65535 x 4 as 65535 was initially mentioned in the SYN packet ??</p><p>Another example hereunder. There is not WS, so easier... Why a window size of 16384 in the SYN packet and then a window size of 17520 in the ACK packet ??</p><p><img src="https://osqa-ask.wireshark.org/upfiles/2016-04-02_13-42-00_0pBKDmn.gif" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '16, 06:20</strong></p><img src="https://secure.gravatar.com/avatar/eac75eef24254c1c9ee690951f6c4006?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thierryn&#39;s gravatar image" /><p>thierryn<br />
<span class="score" title="21 reputation points">21</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thierryn has no accepted answers">0%</span></p></img></div></div><div id="comments-container-51369" class="comments-container"><span id="51370"></span><div id="comment-51370" class="comment"><div id="post-51370-score" class="comment-score"></div><div class="comment-text"><p>Because it defined so in the RFCs. Please read this <a href="http://packetbomb.com/understanding-throughput-and-tcp-windows/">http://packetbomb.com/understanding-throughput-and-tcp-windows/</a></p></div><div id="comment-51370-info" class="comment-info"><span class="comment-age">(02 Apr '16, 06:34)</span> Christian_R</div></div></div><div id="comment-tools-51369" class="comment-tools"></div><div class="clear"></div><div id="comment-51369-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

