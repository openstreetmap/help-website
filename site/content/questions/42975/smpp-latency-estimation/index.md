+++
type = "question"
title = "smpp latency estimation"
description = '''I would like to use &quot;Wireshark&quot; for the estimation of the average time between the submission of &quot;sumbit_sm&quot; smpp PDUs and the reception of the corresponding &quot;submit_sm-resp&quot; smpp PDUs, i.e. the average latency (round trip-delay) between &quot;smpp&quot; requests and responses generally.  If i am not mistaken...'''
date = "2015-06-08T08:29:00Z"
lastmod = "2015-06-09T05:39:00Z"
weight = 42975
keywords = [ "smpp", "latency" ]
aliases = [ "/questions/42975" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [smpp latency estimation](/questions/42975/smpp-latency-estimation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42975-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to use "Wireshark" for the estimation of the average time between the submission of "sumbit_sm" smpp PDUs and the reception of the corresponding "submit_sm-resp" smpp PDUs, i.e. the average latency (round trip-delay) between "smpp" requests and responses generally.</p><p>If i am not mistaken Wireshark can display a "time since request" column but it displays the "http.time" value. Also, I cannot find a graph displaying the round-trip time (delay) for smpp traffic specifically or something related in the "statistics" menu.</p><p>So, is there any way of estimating "latency" using "Wireshark" (web or "command line" tool like "tshark", etc) ?</p></div><div id="question-tags" class="tags-container tags">smpp latency</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '15, 08:29</strong></p><img src="https://secure.gravatar.com/avatar/442070793088ed8c41e42c6b8c16932c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aristotelis&#39;s gravatar image" /><p>Aristotelis<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aristotelis has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jun '15, 08:35</p></div></div><div id="comments-container-42975" class="comments-container"></div><div id="comment-tools-42975" class="comment-tools"></div><div class="clear"></div><div id="comment-42975-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43012"></span>

<div id="answer-container-43012" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43012-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, of course you can do it for individual messages by comparing the timestamp of the request and the response. But I suppose you want to do this for many requests.</p><p>To do that without updating Wireshark's C code to include SMPP response times you'd probably have to use <a href="https://wiki.wireshark.org/Mate">MATE</a>. The biggest problem with MATE is that the documentation is woefully out of date and often inaccurate, but it would allow you to do what you want: get a field attached to SMPP response packets that lists the response time since the request.</p><p>Just to give you a start, you'd want to create a GOP (Group Of Pdus) that includes both the request and the response. MATE automatically calculates the necessary timestamps.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jun '15, 05:39</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-43012" class="comments-container"><span id="43030"></span><div id="comment-43030" class="comment"><div id="post-43030-score" class="comment-score"></div><div class="comment-text"><p>Great thanks... this is something to start with...</p><p>actually i created a short script that calculates the time between (submit-sm) request and (submit-sm-resp) response.</p><hr /><pre><code>Pdu smpp_pdu Proto smpp Transport tcp/ip {
        Extract cmd From smpp.command_id;
        Extract seq From smpp.sequence_number ;      

        Extract stream From tcp.stream;
        Extract time From tcp.time_relative;
};
Gop smpp_session On smpp_pdu Match (seq, stream) {
    // Start with &quot;smpp.command_id == 0x00000004&quot; (submit_sm)
    Start (cmd=4);
    // Stop with &quot;smpp.command_id == 0x80000004&quot; (submit_sm-resp)
    Stop (cmd=2147483652);

};
Done;</code></pre><hr /><p>However (until now) it does not work (exactly) in the way i like.</p><p>For example (among other things): a single tcp frame may contain more than one (submit-sm) requests. It seems that the above script computes correctly the time between the request/response of one of them but it also displays the same time for the rest of those requests (as in the following screen-shot) although times should be different (e.g. in the case presented below it should something like: 0.002462, 0.003943, 0.005487, 0.006817, 0.047319 - it seems the displays the first computed time as many times as the "requests" found in this frame.</p><p>Anyway, thanks again... i will keep trying...</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Clipboard02.new.jpg" alt="alt text" /></p></div><div id="comment-43030-info" class="comment-info"><span class="comment-age">(10 Jun '15, 03:04)</span> Aristotelis</div></div><span id="43053"></span><div id="comment-43053" class="comment"><div id="post-43053-score" class="comment-score"></div><div class="comment-text"><p>Ok, i have revised (a bit) my script to the following version. In this way, the "latency" between request/response is being calculated correctly even in the case where there are multiple requests/responses in a single (tcp) frame. However, it should be worth mentioning that the original "tcp trace" file must be filtered based upon the "tcp stream" index, then create a new "pcap" file (containing frames of that single "tcp stream" only) and finally evaluate the "latency" making use of this "MATE" script. In this way, we will avoid a case where the same "seq-id" is being reused over different "tcp streams" (in that case this script has no "steam-index" reference and it may compute the "latency" between a request and a response "belonging" to different "tcp streams".</p><hr /><p>Pdu smpp_pdu Proto smpp Transport mate { Extract cmd From smpp.command_id; Extract seq From smpp.sequence_number;<br />
};</p><p>Gop smpp_session On smpp_pdu Match (seq){ // Start with "smpp.command_id == 0x00000004" (submit_sm) Start (cmd=4); // Stop with "smpp.command_id == 0x80000004" (submit_sm-resp) Stop (cmd=2147483652);<br />
};</p><p>Done;</p><hr /></div><div id="comment-43053-info" class="comment-info"><span class="comment-age">(10 Jun '15, 10:20)</span> Aristotelis</div></div></div><div id="comment-tools-43012" class="comment-tools"></div><div class="clear"></div><div id="comment-43012-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

