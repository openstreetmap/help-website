+++
type = "question"
title = "TCP ACKed unseen segment - wireshark bug?"
description = '''This is a screenshot of a complete &#x27;echo&#x27; conversation between a PC and an embedded device with a small 64 byte window size. It looks like wireshark loses track of the conversation when the embedded device ACKs the zero window probe and opens its window on #136. Is this the same bug as reported here...'''
date = "2013-05-17T10:03:00Z"
lastmod = "2014-01-29T08:53:00Z"
weight = 21230
keywords = [ "unseen_segment", "zerowindowprobe" ]
aliases = [ "/questions/21230" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TCP ACKed unseen segment - wireshark bug?](/questions/21230/tcp-acked-unseen-segment-wireshark-bug)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21230-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This is a screenshot of a complete 'echo' conversation between a PC and an embedded device with a small 64 byte window size. It looks like wireshark loses track of the conversation when the embedded device ACKs the zero window probe and opens its window on #136. Is this the same bug as reported here?</p><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8404">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8404</a></p><p><img src="http://i98.photobucket.com/albums/l264/foxbat_gb/forums/wireshark-zerowin.png" alt="screenshot" /></p><p><a href="http://i98.photobucket.com/albums/l264/foxbat_gb/forums/wireshark-zerowin.png">Larger image link</a></p></div><div id="question-tags" class="tags-container tags">unseen_segment zerowindowprobe</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '13, 10:03</strong></p><img src="https://secure.gravatar.com/avatar/b85143343d6fdeb8d22b8aa2c5a6fe64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Brown&#39;s gravatar image" /><p>Andy Brown<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Brown has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 17 May '13, 10:05</p></div></div><div id="comments-container-21230" class="comments-container"></div><div id="comment-tools-21230" class="comment-tools"></div><div class="clear"></div><div id="comment-21230-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21237"></span>

<div id="answer-container-21237" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21237-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not sure if it is the exact same problem, but in your case the TCP expert seems to get into trouble when seeing a window probe that doesn't send the last already ACKed byte but the next byte to come. The TCP expert calls packet 135 a ZeroWindowProbe because</p><ol><li>the sequence number is the next expected one</li><li>the window in the other direction is zero</li><li>and the segment holds just 1 byte</li></ol><p>The conditions for a ZeroWindowProbeACK are:</p><ol><li>the previous ACK is repeated</li><li>the last segment in the other direction was a ZeroWindowProbe</li></ol><p>Obviously, the first condition is not met here, because the ACK no. is 66, not 65. Instead, now the "ACKed lost segment" diagnostic code seems to kick in, and marking the previous segment lost, which is clearly not true. I guess the TCP expert code needs to be changed to consider ZeroWindowProbe packets like the one in your trace and not diagnose a "lost segment". So you could attach your problem to the bug you mention, because it is probably caused by a similar part of the TCP expert code.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '13, 13:06</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-21237" class="comments-container"></div><div id="comment-tools-21237" class="comment-tools"></div><div class="clear"></div><div id="comment-21237-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="29273"></span>

<div id="answer-container-29273" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29273-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>frame 136 : this is a ack of the tcpzerowindowprobe segment ( frame 135 ) but as ack=66 means that the byte from the probe segment is consumed by TCP_192.168.1.3 ( we also see that window=63 and 63=64-1 )</p><p>for me , I think the correct name for frame 136 is TCP_ZeroWindowProbeAck and not TCP_ACKed unseen segment. May be a bug.</p><p>I have the same behaviour with the following trace <img src="https://osqa-ask.wireshark.org/upfiles/Capture_17.PNG" alt="alt text" /></p><p>frame 4 to 10, 10.0.3.68 get 4 segments of 128 bytes, then last received segment is acked with a window of 0 ( frame 11 ). As the window of 10.0.3.68 is closed , 10.0.3.70 send window probe segments wich are allway acked from 10.0.2.68 : frame 13 to 19. we see also that the probe byte is not consumed because seq equal ack for each probing EXCEPT the last probe : frame22 when 10.0.3.68 get frame 22, it TCP application has consumed data and the window can be re-opened. So the frame 22 ( window probe ) is acked but the probe byte is consumed ack = seq + 1 = 108420 win different of 0</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '14, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/a3431aa0c6ff3eafc02d7a08b91524af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gibu&#39;s gravatar image" /><p>gibu<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gibu has no accepted answers">0%</span></p></img></div></div><div id="comments-container-29273" class="comments-container"></div><div id="comment-tools-29273" class="comment-tools"></div><div class="clear"></div><div id="comment-29273-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

