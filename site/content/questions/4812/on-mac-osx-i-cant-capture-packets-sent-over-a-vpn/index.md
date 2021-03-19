+++
type = "question"
title = "on Mac OSX, I can&#x27;t capture packets sent over a VPN"
description = '''TIA - I&#x27;m trying to troubleshoot some problems I&#x27;m having accessing a particular host over a VPN. I&#x27;m running Mac OS/X 10.6.7, and the VPN is a Cisco IPSec VPN. I&#x27;ve verified that the host is routing correctly over the VPN interface (which Mac OS/X calls &quot;utun0&quot;): dhcp-10-0-0-1:~ joshuadavies$ route...'''
date = "2011-06-29T08:30:00Z"
lastmod = "2015-10-22T15:22:00Z"
weight = 4812
keywords = [ "osx", "mac", "vpn", "utun0" ]
aliases = [ "/questions/4812" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [on Mac OSX, I can't capture packets sent over a VPN](/questions/4812/on-mac-osx-i-cant-capture-packets-sent-over-a-vpn)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4812-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>TIA - I'm trying to troubleshoot some problems I'm having accessing a particular host over a VPN. I'm running Mac OS/X 10.6.7, and the VPN is a Cisco IPSec VPN. I've verified that the host is routing correctly over the VPN interface (which Mac OS/X calls "utun0"):</p><p>dhcp-10-0-0-1:~ joshuadavies$ route get -host host.domain.com route to: host.domain.com destination: host.domain.com gateway: 1.2.3.4 interface: utun0 flags: &lt;up,gateway,host,done,wascloned,proto3,ifscope&gt; recvpipe sendpipe ssthresh rtt,msec rttvar hopcount mtu expire 0 0 0 0 0 0 1280 3179</p><p>(obviously I've changed the hostname &amp; gateway above).</p><p>However, when I fire up Wireshark and listen on interface utun0, even when I connect to a host in the remote network, I don't see anything in the capture list. Is there something special I need to do so that packets sent over a VPN link show up in Wireshark 1.4.6 under Mac OS/X?</p></div><div id="question-tags" class="tags-container tags">osx mac vpn utun0</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jun '11, 08:30</strong></p><img src="https://secure.gravatar.com/avatar/225ac437c123dafa9fa55c17b0488773?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joshua%20Davies&#39;s gravatar image" /><p>Joshua Davies<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joshua Davies has no accepted answers">0%</span></p></div></div><div id="comments-container-4812" class="comments-container"><span id="4818"></span><div id="comment-4818" class="comment"><div id="post-4818-score" class="comment-score">1</div><div class="comment-text"><p>A quick look at xnu/bsd/net/if_utun.c in 10.6.7 indicates that it does include BPF tap code, so it should, in theory, be possible to capture on it with libpcap, so, in theory, both tcpdump and Wireshark should work.</p><p>However <a href="http://osdir.com/ml/macnetworkprog/2010-06/msg00006.html">this mail message</a> indicates that, even if it does support BPF, it might not be getting the traffic you want to see. Is there also, for example, a ppp0 interface that's up? If so, what happens if you try capturing on it?</p></div><div id="comment-4818-info" class="comment-info"><span class="comment-age">(29 Jun '11, 12:07)</span> Guy Harris ♦♦</div></div><span id="4823"></span><div id="comment-4823" class="comment"><div id="post-4823-score" class="comment-score"></div><div class="comment-text"><p>The best thing to do is to report this to http://bugreport.apple.com. The more reports, the more likely it will see attention. I filed 9699332.</p></div><div id="comment-4823-info" class="comment-info"><span class="comment-age">(29 Jun '11, 14:19)</span> chrisvire</div></div></div><div id="comment-tools-4812" class="comment-tools"></div><div class="clear"></div><div id="comment-4812-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46861"></span>

<div id="answer-container-46861" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46861-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>From Apple,</p><pre><code>This is a courtesy email regarding Bug ID# 17265290. 
Engineering has provided the following feedback regarding this issue: 
On OS X, using the tcpdump -i option, you can specify pktap or/and iptap.</code></pre><p>I haven't tested this myself, but perhaps that is the solution...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '15, 15:22</strong></p><img src="https://secure.gravatar.com/avatar/d94484ade46426d97ae7e30156aa24ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nigel%20Sheridan-Smith&#39;s gravatar image" /><p>Nigel Sherid...<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nigel Sheridan-Smith has no accepted answers">0%</span></p></div></div><div id="comments-container-46861" class="comments-container"><span id="49840"></span><div id="comment-49840" class="comment"><div id="post-49840-score" class="comment-score"></div><div class="comment-text"><p>I tired this but it still doesn't seem to capture packet via tunneling interface (utun0). Did you find any other way around?</p></div><div id="comment-49840-info" class="comment-info"><span class="comment-age">(04 Feb '16, 10:23)</span> Kjee</div></div></div><div id="comment-tools-46861" class="comment-tools"></div><div class="clear"></div><div id="comment-46861-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

