+++
type = "question"
title = "Wireshark Packet Forwarding"
description = '''Will Wireshark enable packet forwarding to tcp socket instead of file ? (e.g. Resend captured packets to ip:port using &quot;some&quot; protocol) ?'''
date = "2013-02-01T13:22:00Z"
lastmod = "2013-02-01T14:10:00Z"
weight = 18239
keywords = [ "forwarding", "feature-request", "packet", "wireshark" ]
aliases = [ "/questions/18239" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark Packet Forwarding](/questions/18239/wireshark-packet-forwarding)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18239-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Will Wireshark enable packet forwarding to tcp socket instead of file ? (e.g. Resend captured packets to ip:port using "some" protocol) ?</p></div><div id="question-tags" class="tags-container tags">forwarding feature-request packet wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Feb '13, 13:22</strong></p><img src="https://secure.gravatar.com/avatar/049954c19a42f88823709640897cb958?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ahmediukas&#39;s gravatar image" /><p>ahmediukas<br />
<span class="score" title="21 reputation points">21</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ahmediukas has no accepted answers">0%</span></p></div></div><div id="comments-container-18239" class="comments-container"></div><div id="comment-tools-18239" class="comment-tools"></div><div class="clear"></div><div id="comment-18239-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18240"></span>

<div id="answer-container-18240" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18240-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>No. Wireshark always writes captured packets to file. In some cases you can also direct the incoming packets to a pipe IIRC, but that will not resend them anywhere else. You need a packet replay / packet generator tool for that, for example bittwist, tcpreplay or ostinato.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '13, 13:58</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-18240" class="comments-container"><span id="18244"></span><div id="comment-18244" class="comment"><div id="post-18244-score" class="comment-score"></div><div class="comment-text"><p>Jasper thx, tcpreplay i need for something else (almost did it myself today, so woohoo :)</p></div><div id="comment-18244-info" class="comment-info"><span class="comment-age">(01 Feb '13, 14:39)</span> ahmediukas</div></div></div><div id="comment-tools-18240" class="comment-tools"></div><div class="clear"></div><div id="comment-18240-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18242"></span>

<div id="answer-container-18242" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18242-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, it won't.</p><p>If all you want to do is send raw packets over the wire, Wireshark is overkill. What you might want is, for example, a combination of a program that can capture traffic and write it to a pipe and a program that can read the pipe and send it over the wire, such as <a href="http://d0pefishsec.blogspot.com/2010/04/monitoring-remote-traffic-with-tcpdump.html">tcpdump and netcat</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '13, 14:10</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-18242" class="comments-container"><span id="18243"></span><div id="comment-18243" class="comment"><div id="post-18243-score" class="comment-score"></div><div class="comment-text"><p>Actually I need to get packets into some LEA applications, (which can't handle libpcap directly), not putting them back on a wire. Will do for myself, just asked not to make something which will be soon available :)</p></div><div id="comment-18243-info" class="comment-info"><span class="comment-age">(01 Feb '13, 14:33)</span> ahmediukas</div></div><span id="18245"></span><div id="comment-18245" class="comment"><div id="post-18245-score" class="comment-score">1</div><div class="comment-text"><p>By "which can't handle libpcap directly" do you mean the applications can't directly capture network traffic (which doesn't <em>have</em> to be done with libpcap - libpcap just sits atop already-existing OS-dependent capture mechanisms on UN*X, and, on Windows, the apps could have their own driver rather than using WinPcap's driver), that they don't understand pcap file format, or both?</p><p>If the apps can't handle pcap format, then your biggest problem isn't getting packets written to a socket, it's writing packets in a format that the apps <em>can</em> handle.</p></div><div id="comment-18245-info" class="comment-info"><span class="comment-age">(01 Feb '13, 14:40)</span> Guy Harris ♦♦</div></div><span id="18246"></span><div id="comment-18246" class="comment"><div id="post-18246-score" class="comment-score"></div><div class="comment-text"><p>I have my own dissectors/decoders, i just need raw traffic interecepting. That's why I will reroute them using libpcap for which i already have library written.</p></div><div id="comment-18246-info" class="comment-info"><span class="comment-age">(01 Feb '13, 15:17)</span> ahmediukas</div></div></div><div id="comment-tools-18242" class="comment-tools"></div><div class="clear"></div><div id="comment-18242-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

