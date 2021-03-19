+++
type = "question"
title = "Bytes in Flight exceeds window size"
description = '''Hi, I am examining a trace from netscaler.  On statistics -&amp;gt; IO Graphs , I am comparing bytes in flights and window size.  Strangely , my bytes in flight is higher than window size. Only when I supply tcp stream as a display the problem seems to recover.  When there is no input in display filter ...'''
date = "2016-12-21T23:36:00Z"
lastmod = "2016-12-21T23:48:00Z"
weight = 58286
keywords = [ "netscaler", "tcpwindowsize", "tcp", "tcp-bytes-in-flight" ]
aliases = [ "/questions/58286" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Bytes in Flight exceeds window size](/questions/58286/bytes-in-flight-exceeds-window-size)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58286-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am examining a trace from netscaler. On statistics -&gt; IO Graphs , I am comparing bytes in flights and window size. Strangely , my bytes in flight is higher than window size. Only when I supply tcp stream as a display the problem seems to recover. When there is no input in display filter , bif exceeds the window size. Besides , when I enter vlan (nstrace.vlan ) it doesn't have an effect. Still bif is higher.</p><p>Note : I select Y-Field as tcp.analysis.bytes_in_flight and tcp.window_size ; then Y-axis as max(Y-Field).</p><p>Any idea would be appreciated.</p></div><div id="question-tags" class="tags-container tags">netscaler tcpwindowsize tcp tcp-bytes-in-flight</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Dec '16, 23:36</strong></p><img src="https://secure.gravatar.com/avatar/44673984e5e640fa3df7e4ef8b60569c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ozan_Cesur&#39;s gravatar image" /><p>Ozan_Cesur<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ozan_Cesur has no accepted answers">0%</span></p></div></div><div id="comments-container-58286" class="comments-container"></div><div id="comment-tools-58286" class="comment-tools"></div><div class="clear"></div><div id="comment-58286-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58287"></span>

<div id="answer-container-58287" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58287-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Bytes in flight and window size is a session based values. So exactly you need more things in the filter for the two graphs;</p><ol><li>IP_address_Site_A and tcpstream_ID. In the YField max value: calculated_windowsize</li><li>IP_address_Site_B and tcpstream_ID. in the YField max value: bytes_in_flight</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Dec '16, 23:48</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Dec '16, 23:51</p></div></div><div id="comments-container-58287" class="comments-container"><span id="58288"></span><div id="comment-58288" class="comment"><div id="post-58288-score" class="comment-score"></div><div class="comment-text"><p>I thought when I left the display filter empty , wireshark would search for all the sessions. So when it draws bytes_in_flight information for a specific session, it should have found the window size information for that specific session as well.</p><p>As I see it is not how wireshark draws graphs when I left display filter empty. I should look for how it behaves when no filters entered</p><p>Thanks for the response</p></div><div id="comment-58288-info" class="comment-info"><span class="comment-age">(22 Dec '16, 00:00)</span> Ozan_Cesur</div></div><span id="58292"></span><div id="comment-58292" class="comment"><div id="post-58292-score" class="comment-score"></div><div class="comment-text"><p>First I have converted your answer into acomment, as it is more a comment.</p><p>If you leave the filter field empty. Wireshark looks at every packet and if it it contains a the field it draws the value (max, SUM...) But Wireshark does this without any kind of intelligence.</p><p>The intteligence is the display filter in this case, which need to be defined by the user.</p><p>But at least for the window size value there are some intelligent graphs available, as you have expected by the IO graph: Statistics -&gt; TCP Stream Graphs -&gt; Window Scaling</p><p>or</p><p>Statistics -&gt; TCP Stream Graphs -&gt; tcptrace</p></div><div id="comment-58292-info" class="comment-info"><span class="comment-age">(22 Dec '16, 01:05)</span> Christian_R</div></div></div><div id="comment-tools-58287" class="comment-tools"></div><div class="clear"></div><div id="comment-58287-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

