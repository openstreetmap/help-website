+++
type = "question"
title = "MATE display filter for SIP calls"
description = '''Hi, I&#x27;ve deployed a MATE configuration file to filter SIP signalling + media. Using the filter: mate.session.callid == &quot;mycallid&quot; I only get SIP signalling but no media. I can get SIP+media with the following filter only: mate.session.media_port == &quot;myport&quot;. Is it possible to fix the configuration f...'''
date = "2012-11-23T00:26:00Z"
lastmod = "2012-11-23T00:26:00Z"
weight = 16235
keywords = [ "media", "mate", "sip" ]
aliases = [ "/questions/16235" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [MATE display filter for SIP calls](/questions/16235/mate-display-filter-for-sip-calls)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16235-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I've deployed a MATE configuration file to filter SIP signalling + media. Using the filter: mate.session.callid == "mycallid" I only get SIP signalling but no media. I can get SIP+media with the following filter only: mate.session.media_port == "myport". Is it possible to fix the configuration file to get media filtering by call-id?</p><pre><code>Pdu sip_pdu Proto sip Transport udp/ip {
Extract callid From sip.Call-ID;
Extract from From sip.from.user;
Extract to From sip.to.user;
Extract method From sip.Method;
Extract cseq_method From sip.CSeq.method;
Extract media_addr From sdp.connection_info.address;
Extract media_port From sdp.media.port;
};
Gop sip_ses On sip_pdu Match (callid) {
Start(method=&quot;INVITE&quot;);
Stop(cseq_method=&quot;BYE&quot;);
Extra (callid, from, to, media_port);
};

Pdu udp_pdu Proto udp Transport ip {
Extract media_addr From ip.addr;
Extract media_port From udp.port;
};
Gop udp_ses On udp_pdu Match (media_port, media_port) {
Extra (media_port);
};

Pdu tcp_pdu Proto tcp Transport ip {
Extract media_addr From ip.addr;
Extract media_port From tcp.port;
Extract tcp_start From tcp.flags.syn;
Extract tcp_stop From tcp.flags.fin;
};
Gop tcp_ses On tcp_pdu Match (media_port, media_port) {
Start (tcp_start=1);
Stop (tcp_stop=1);
Extra (media_port);
};

Gog session {
Member sip_ses (media_port);
Member udp_ses (media_port);
Member tcp_ses (media_port);
Extra (callid, from, to);
};
Done;</code></pre><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">media mate sip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '12, 00:26</strong></p><img src="https://secure.gravatar.com/avatar/5aa3e602fe20c86ecbe0c2bf2353efef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Robin&#39;s gravatar image" /><p>Robin<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Robin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Nov '12, 04:32</p></div></div><div id="comments-container-16235" class="comments-container"><span id="45823"></span><div id="comment-45823" class="comment"><div id="post-45823-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Did you manage to resolve this issue ?</p><p>Thanks in anticipation</p></div><div id="comment-45823-info" class="comment-info"><span class="comment-age">(13 Sep '15, 20:07)</span> sshark</div></div></div><div id="comment-tools-16235" class="comment-tools"></div><div class="clear"></div><div id="comment-16235-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

