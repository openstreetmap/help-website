+++
type = "question"
title = "TCP REST after SYNC-ACK from Server"
description = '''In my linux host, I noticed that linux is sending RESET just after it receives SYNC-ACK. Note that there is no active firewall in the box. If I reboot linux box, issue disappears, but same doesn&#x27;t work after &quot;service networking restart&quot;. Here is capture screenshoot. https://s27.postimg.org/45fuwmz43...'''
date = "2017-01-20T06:54:00Z"
lastmod = "2017-01-20T07:00:00Z"
weight = 58909
keywords = [ "tcpdump", "tcp" ]
aliases = [ "/questions/58909" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [TCP REST after SYNC-ACK from Server](/questions/58909/tcp-rest-after-sync-ack-from-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58909-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In my linux host, I noticed that linux is sending RESET just after it receives SYNC-ACK. Note that there is no active firewall in the box. If I reboot linux box, issue disappears, but same doesn't work after "service networking restart".</p><p>Here is capture screenshoot. <a href="https://s27.postimg.org/45fuwmz43/Capture.png">https://s27.postimg.org/45fuwmz43/Capture.png</a></p><p>May I know no. of reasons for this scenario ?</p><p>As per @Jasper answer, here are more details. 1) I am using <strong>telnet host 80</strong> to validate things 2) linux date command results seems right without any issue.</p></div><div id="question-tags" class="tags-container tags">tcpdump tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jan '17, 06:54</strong></p><img src="https://secure.gravatar.com/avatar/524e64ae12c365f81728baf697d32f0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rajdip&#39;s gravatar image" /><p>rajdip<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rajdip has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Jan '17, 07:13</p></div></div><div id="comments-container-58909" class="comments-container"></div><div id="comment-tools-58909" class="comment-tools"></div><div class="clear"></div><div id="comment-58909-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58910"></span>

<div id="answer-container-58910" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58910-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Either the client socket is closed already when the SYN/ACK arrives, or you've got timestamp problems, which is hard to tell because you posted an incomplete screenshot.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '17, 07:00</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-58910" class="comments-container"><span id="58915"></span><div id="comment-58915" class="comment"><div id="post-58915-score" class="comment-score"></div><div class="comment-text"><p>Since I am using telnet to validate things, I keep open telnet until it says "Connection failed...."</p></div><div id="comment-58915-info" class="comment-info"><span class="comment-age">(20 Jan '17, 07:15)</span> rajdip</div></div><span id="58917"></span><div id="comment-58917" class="comment"><div id="post-58917-score" class="comment-score"></div><div class="comment-text"><p>Here is pcap file. <a href="http://wikisend.com/download/586222/capture.pcap">http://wikisend.com/download/586222/capture.pcap</a></p></div><div id="comment-58917-info" class="comment-info"><span class="comment-age">(20 Jan '17, 07:26)</span> rajdip</div></div><span id="58919"></span><div id="comment-58919" class="comment"><div id="post-58919-score" class="comment-score"></div><div class="comment-text"><p>Looks like its the timestamp value that does this. Check Christians answer in this question: <a href="https://ask.wireshark.org/questions/57774/syn-synack-rst-reason">https://ask.wireshark.org/questions/57774/syn-synack-rst-reason</a></p></div><div id="comment-58919-info" class="comment-info"><span class="comment-age">(20 Jan '17, 07:28)</span> Jasper ♦♦</div></div><span id="58921"></span><div id="comment-58921" class="comment"><div id="post-58921-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot. It was tcp timestamps issue. It worked successfully after echo 0 &gt; /proc/sys/net/ipv4/tcp_timestamps. I will make permanent changes in /etc/sysctl.conf</p></div><div id="comment-58921-info" class="comment-info"><span class="comment-age">(20 Jan '17, 07:59)</span> rajdip</div></div><span id="58922"></span><div id="comment-58922" class="comment"><div id="post-58922-score" class="comment-score"></div><div class="comment-text"><p>Just out of curiosity: What OS do you exactly?</p></div><div id="comment-58922-info" class="comment-info"><span class="comment-age">(20 Jan '17, 08:54)</span> Christian_R</div></div><span id="58928"></span><div id="comment-58928" class="comment not_top_scorer"><div id="post-58928-score" class="comment-score"></div><div class="comment-text"><p>It's debian, running on ARM SBC.</p></div><div id="comment-58928-info" class="comment-info"><span class="comment-age">(20 Jan '17, 22:10)</span> rajdip</div></div></div><div id="comment-tools-58910" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-58910-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

