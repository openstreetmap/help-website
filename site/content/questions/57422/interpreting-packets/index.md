+++
type = "question"
title = "Interpreting Packets"
description = '''Thanks in advance for the help! I am new to using wireshark and am struggling to use it in my particular application. I have a desktop PC that communicates to a controller, which sends commands to a robot. I&#x27;m trying to understand the communication between the PC and the controller. I&#x27;m attempting t...'''
date = "2016-11-16T09:58:00Z"
lastmod = "2016-11-17T00:31:00Z"
weight = 57422
keywords = [ "beginner" ]
aliases = [ "/questions/57422" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Interpreting Packets](/questions/57422/interpreting-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57422-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57422-score" class="post-score" title="current number of votes">0</div><span id="post-57422-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Thanks in advance for the help! I am new to using wireshark and am struggling to use it in my particular application.</p><p>I have a desktop PC that communicates to a controller, which sends commands to a robot. I'm trying to understand the communication between the PC and the controller. I'm attempting to use the setup below to monitor the communications. I'm capturing the packets on my laptop using USBPcap and viewing them using Wireshark.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/setup.png" alt="alt text" /></p><p>When I capture while sending a few commands from the PC to the controller to move the robot, I recieve packets like in the image below. Numbers 1-618 occur every time the USB is plugged in, so numbers 619-621 contain the communication between the PC and the controller. And this is where I am stuck. Is the process I am using to monitor communication correct? How do I interpret this information? I'm concerned something is wrong with my process since I received the message "Malformed Packet".</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Packets.png" alt="alt text" /></p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-beginner" rel="tag" title="see questions tagged &#39;beginner&#39;">beginner</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Nov '16, 09:58</strong></p><img src="https://secure.gravatar.com/avatar/bd9d80ea9664b787bdf6fd6234987bf1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="moelleea&#39;s gravatar image" /><p><span>moelleea</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="moelleea has no accepted answers">0%</span></p></img></div></div><div id="comments-container-57422" class="comments-container"><span id="57423"></span><div id="comment-57423" class="comment"><div id="post-57423-score" class="comment-score"></div><div class="comment-text"><p>Assuming that the communication from the PC to the Controller is RS232, why don't you capture the comms traffic on the PC?</p><p>And what is the OS on the PC?</p></div><div id="comment-57423-info" class="comment-info"><span class="comment-age">(16 Nov '16, 10:32)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-57422" class="comment-tools"></div><div class="clear"></div><div id="comment-57422-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57431"></span>

<div id="answer-container-57431" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57431-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57431-score" class="post-score" title="current number of votes">1</div><span id="post-57431-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming that, for whatever reason, you cannot capture the serial traffic using a software running on the desktop PC as <span>@grahamb</span> suggests, the way you took is still quite complex.</p><p>Whatever method you use to capture the data, the first thing to do when analysing serial communication is to identify the data speed and format on the wire. Of course it is best if you know them in advance, but if you don't, an oscilloscope is your best friend, as it can show you whether the communication is "asynchronous" (most likely if one of the ends is a standard serial port of a standard PC) or "synchronous" if some kind of specialized adaptor is used, what is the duration of a single bit on the line (which is the inverse of the transmission speed, 10 bits per second mean that a single bit is present on the line for 0.1 second).</p><p>For standard serial adaptors, possible speeds are 50, 100, 150, 300, 600, 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200, or even faster with newer hardware. So the inverse value of the bit duration measured (quite inaccurately) using the oscilloscope should be close to one of these. If asynchronous mode is used and the signal is not modulated onto any carrier, the line is at the same voltage level (stop bit, i.e. logical 1) if no transmission is ongoing, so you need a memorizing oscilloscope.</p><p>Next, for an asynchronous communication, you have to determine</p><ul><li>how many data bits are used (5 to 8 are typical values),</li><li>whether a parity bit is used, and if it is, whether it is odd or even,</li><li>how many stop bits are used (1, 1.5 and 2 are typical values).</li></ul><p>For synchronous communication, the task would be more complex as in such case, the boundaries of individual bytes are not marked as clearly as in the asynchronous case (using start bit and stop bit(s)) but either some kind of bit oriented protocol like HDLC is used or some multi-byte synchronisation pattern is occasionally present in the data stream.</p><p>Knowing all the above, you can set the serial adaptor you use to monitor accordingly. Then, you can use some own software to read the incoming data from that port and dump them in hex and ASCII for further analysis. If there is a gap longer than one byte time, this may indicate a message boundary, so you may want to print a newline and a timestamp before printing the first byte after the gap, so you'd get something like</p><pre><code>10:00:03.20 41=A 62=b 63=c
10:00:04.15 43=C 30=0 35=5 FE=.
10:00:07.11 41=A 63=c 65=e</code></pre><p>If you want to use Wireshark's ability to dump USB communication, you have to understand how the serial to USB adaptor packs the data into the bulk transfer. I'm afraid that no dissector capable of extracting the serial data from communication of the serial-to-USB adaptor with its driver exists so you would have to write it yourself.</p><p>If you insist on going that way, I'd recommend you to do the following:</p><ul><li>disconnect the RS-232 side of the USB to serial adaptor from the monitored cable and the USB side of it from the PC</li><li>connect pins 2 and 3 on the RS-232 connector of the adaptor</li><li>start capturing</li><li>insert the USB end of the USB to serial adaptor back to the PC</li><li>configure the serial port representing the adaptor for "no handshake" and for some speed, parity, number of stop bits etc.</li><li>connect a text terminal software to the serial port and type some string like "hello world", you should see it echoed</li><li>stop the capture.</li></ul><p>In the capture, you should see the enumeration phase, including the vendor and product id, which you would later use to tell Wireshark to use your dissector to dissect USB bulk transfers of this vendor and product. You should also see in the bulk transfers' payload substrings of what you typed on the terminal. The substrings may be as small as a single character or they may be longer; they may be even encoded in some unexpected way so you won't be able to match the bulk transfer payload to what you wrote at all.</p><p>Your own dissector, if properly registered for the vendor and product id, would then receive the bulk data from Wireshark for analysis, and it would be up to you how you would reassemble them into some logical units. A typical behaviour of Wireshark dissectors is that if a protocol data unit (PDU) is spread across several frames of a transport protocol, the complete reassembled PDU is added to the dissection tree of the last one of the transport frames carrying it.</p><p>So after writing your dissector, Wireshark would show you about the same as suggested above - chunks of bytes with timestamps.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '16, 00:31</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></img></div></div><div id="comments-container-57431" class="comments-container"></div><div id="comment-tools-57431" class="comment-tools"></div><div class="clear"></div><div id="comment-57431-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

