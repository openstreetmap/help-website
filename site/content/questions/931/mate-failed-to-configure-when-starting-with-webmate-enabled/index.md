+++
type = "question"
title = "&#x27;mate failed to configure&#x27; when starting with web.mate enabled"
description = '''Has anyone run into any problems with web.mate? I&#x27;m running Windows 7 64 bit with the 64 bit Wireshark v1.4.1. The mate plugin is loading fine. I have loaded up tcp.mate without any errors. When I start up Wireshark with web.mate enabled I get this error: c:usersMEwireshark_mateweb.mate at line 1: S...'''
date = "2010-11-12T10:08:00Z"
lastmod = "2011-01-06T12:53:00Z"
weight = 931
keywords = [ "web", "mate", "tcp", "wireshark" ]
aliases = [ "/questions/931" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# ['mate failed to configure' when starting with web.mate enabled](/questions/931/mate-failed-to-configure-when-starting-with-webmate-enabled)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-931-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Has anyone run into any problems with web.mate? I'm running Windows 7 64 bit with the 64 bit Wireshark v1.4.1. The mate plugin is loading fine. I have loaded up tcp.mate without any errors. When I start up Wireshark with web.mate enabled I get this error:</p><p>c:usersMEwireshark_mateweb.mate at line 1: Syntax Error before web.mate</p><p>The permissions, directory path and attributes of the web.mate file are identical to those of tcp.mate which loads without any problems. I downloaded both files at the same time, using the same browser. I downloaded web.mate a couple of times to be sure something didn't get corrupted in the download and the file is identical each time.</p><p>I downloaded the web.mate file from the wireshark wiki so it isn't that I have some one-off version with some random edits. <a href="http://wiki.wireshark.org/Mate/Tutorial?action=AttachFile&amp;do=view&amp;target=web.mate">http://wiki.wireshark.org/Mate/Tutorial?action=AttachFile&amp;do=view&amp;target=web.mate</a></p></div><div id="question-tags" class="tags-container tags">web mate tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Nov '10, 10:08</strong></p><img src="https://secure.gravatar.com/avatar/c72ae7a46acbddf07e3c2ba755b19a4c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="devrick0&#39;s gravatar image" /><p>devrick0<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="devrick0 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Nov '10, 05:24</p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-931" class="comments-container"></div><div id="comment-tools-931" class="comment-tools"></div><div class="clear"></div><div id="comment-931-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1653"></span>

<div id="answer-container-1653" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1653-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like the format of these files have changed, so the example given does not work. <a href="http://www.wireshark.org/lists/wireshark-users/200708/msg00071.html">http://www.wireshark.org/lists/wireshark-users/200708/msg00071.html</a></p><p>After a lot of trial and error, I came up with one that seems to work. I was looking for the ability to add a column that has the full time for each web page request, and it looks like it works. Here's what I came up with:</p><pre><code>Pdu tcp_pdu Proto tcp Transport ip {
    Extract addr From ip.addr;
    Extract port From tcp.port;
    Extract tcp_start From tcp.flags.syn;
    Extract tcp_stop From tcp.flags.reset;
    Extract tcp_stop From tcp.flags.fin;
};

Gop tcp_ses On tcp_pdu Match (addr, addr, port, port) {
    Start (tcp_start=1);
    Stop (tcp_stop=1);
};

Transform rm_client_from_dns_resp {
    Match (dns_resp=1, client) Insert (dns_resp=1); 
};

Pdu dns_pdu Proto dns Transport ip {
    Extract addr From ip.addr;
    Extract dns_resp From dns.flags.response;
    Extract host From dns.qry.name;
    Extract client From ip.src;
    Extract dns_id From dns.id;
    Transform rm_client_from_dns_resp;

};

Transform rm_client_from_http_resp1 {
    Match (http_rq);
    Match (addr) Insert (not_rq);
    Match (not_rq,client);
};

Transform rm_client_from_http_resp2 {
    Match (not_rq,client);
};

Pdu http_pdu Proto http Transport tcp/ip {
    Extract addr From ip.addr;
    Extract port From tcp.port;
    Extract http_rq From http.request.method;
    Extract http_rs From http.response;
    Extract host From http.host;
    Extract client From ip.src;
    Transform rm_client_from_http_resp1;
//  Transform rm_client_from_http_resp2;

};

Gop dns_req On dns_pdu Match (addr, addr, dns_id) {
    Start (dns_resp=0);
    Stop (dns_resp=1);
    Extra (host, client);
};

Gop http_req On http_pdu Match (addr, addr, port, port) {
    Start (http_rq);
    Stop (http_rq);
    Extra (host, client);
};

//Transform start_cond {
//       Match (attr1=aaa, attr2=bbb) Insert (msg_type=start);
//       Match (attr3=www; attr2=bbb) Insert (msg_type=start);
//       Match (attr5^a ) Insert (msg_type=stop);
//       Match (attr6$z ) Insert (msg_type=start);
//};

//Pdu pdu ...  {
//     ...;

Done;</code></pre><p>Good luck,</p><p>Brian</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jan '11, 12:53</strong></p><img src="https://secure.gravatar.com/avatar/9776b01972dc1286f9cb2cd433065141?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lanlord&#39;s gravatar image" /><p>lanlord<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lanlord has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Feb '16, 09:28</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-1653" class="comments-container"></div><div id="comment-tools-1653" class="comment-tools"></div><div class="clear"></div><div id="comment-1653-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

