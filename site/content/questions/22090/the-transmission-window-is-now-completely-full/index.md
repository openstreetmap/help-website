+++
type = "question"
title = "The transmission window is now completely full"
description = '''I&#x27;m having problems with a extremely slow network response from outside websites. In looking at the Wireshark output, I see what seems to be a very large number of &quot;TCP window full&quot; and &quot;Zero window&quot; occurrences. One of the &quot;window full&quot; events shows up as: 15874 141.816990 64.81.159.15 10.138.30.34...'''
date = "2013-06-15T11:29:00Z"
lastmod = "2013-06-15T11:36:00Z"
weight = 22090
keywords = [ "window", "full", "tcp" ]
aliases = [ "/questions/22090" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [The transmission window is now completely full](/questions/22090/the-transmission-window-is-now-completely-full)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22090-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm having problems with a extremely slow network response from outside websites. In looking at the Wireshark output, I see what seems to be a very large number of "TCP window full" and "Zero window" occurrences. One of the "window full" events shows up as:</p><p>15874 141.816990 64.81.159.15 10.138.30.34 TCP 60 http &gt; unet [ACK] Seq=4714197 Ack=17390 Win=17520 Len=0</p><p>15875 141.817027 10.138.30.34 64.81.159.15 TCP 1514 [TCP segment of a reassembled PDU]</p><p>15876 141.817046 10.138.30.34 64.81.159.15 TCP 1514 [TCP segment of a reassembled PDU]</p><p>15877 141.817183 64.81.159.15 10.138.30.34 TCP 60 http &gt; unet [ACK] Seq=4714197 Ack=20310 Win=17520 Len=0</p><p>15878 141.817233 10.138.30.34 64.81.159.15 TCP 1514 [TCP segment of a reassembled PDU]</p><p>15879 141.817261 10.138.30.34 64.81.159.15 TCP 1514 [TCP segment of a reassembled PDU]</p><p>15880 141.817288 10.138.30.34 64.81.159.15 TCP 1514 [TCP Window Full] [TCP segment of a reassembled PDU]</p><p>Could these be contributing to the slow network response and if so, what should be my next step in resolving these issues?</p></div><div id="question-tags" class="tags-container tags">window full tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jun '13, 11:29</strong></p><img src="https://secure.gravatar.com/avatar/21cc833a9ec64197a6a405e174846a54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gvsenterprises&#39;s gravatar image" /><p>gvsenterprises<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gvsenterprises has no accepted answers">0%</span></p></div></div><div id="comments-container-22090" class="comments-container"></div><div id="comment-tools-22090" class="comment-tools"></div><div class="clear"></div><div id="comment-22090-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22092"></span>

<div id="answer-container-22092" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22092-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Window full means that the sender has sent as many bytes as it was allowed to before it has to wait for acknowledgement packets. If the receiver reduces his window size to zero it means "dear sender, STOP sending, I have to process data!", which usually means that it has trouble processing data fast enough. Both Window Full and Window Zero may indicate that you have a problem, usually on the receiving side. It is NOT a network problem, it is a PC/Server problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '13, 11:36</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-22092" class="comments-container"><span id="22093"></span><div id="comment-22093" class="comment"><div id="post-22093-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the information. Now do I understand correctly that, since these exceptions are happening when browsing websites that otherwise work fine from another location (i.e. my house vs. my office), this problem is more likely a client PC issue at the office and not necessarily a problem on the office network?</p></div><div id="comment-22093-info" class="comment-info"><span class="comment-age">(15 Jun '13, 13:56)</span> gvsenterprises</div></div><span id="22094"></span><div id="comment-22094" class="comment"><div id="post-22094-score" class="comment-score"></div><div class="comment-text"><p>It is usually a client PC problem and not a network problem, yes. So e.g. if a web site works fast at home but not at the office the PC at the office seems to have trouble processing incoming data fast enough when you see Window Full and Zero Window issues.</p></div><div id="comment-22094-info" class="comment-info"><span class="comment-age">(15 Jun '13, 14:11)</span> Jasper ♦♦</div></div></div><div id="comment-tools-22092" class="comment-tools"></div><div class="clear"></div><div id="comment-22092-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

