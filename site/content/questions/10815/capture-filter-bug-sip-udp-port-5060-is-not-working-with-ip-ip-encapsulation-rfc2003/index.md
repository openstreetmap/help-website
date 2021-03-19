+++
type = "question"
title = "Capture filter bug? - SIP &quot;udp port 5060&quot; is not working with IP-IP-Encapsulation RFC2003"
description = '''I have an Session Border Controller which can use IP-in-IP encapsulation (RFC 2003) to send all sip data for example to a capture machine.  On that machine I have a wireshark to make SIP traces. It seems capture filter &quot;udp port 5060&quot; is not working. Could it cause by IP-IP encapsulation?  These pac...'''
date = "2012-05-09T01:54:00Z"
lastmod = "2012-05-09T05:42:00Z"
weight = 10815
keywords = [ "filter", "capture", "sip", "rfc2003", "encapsulation" ]
aliases = [ "/questions/10815" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capture filter bug? - SIP "udp port 5060" is not working with IP-IP-Encapsulation RFC2003](/questions/10815/capture-filter-bug-sip-udp-port-5060-is-not-working-with-ip-ip-encapsulation-rfc2003)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10815-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an Session Border Controller which can use IP-in-IP encapsulation (RFC 2003) to send all sip data for example to a capture machine.</p><p>On that machine I have a wireshark to make SIP traces. It seems capture filter "udp port 5060" is not working. Could it cause by IP-IP encapsulation?</p><p>These packets contians the following headers: -Ethernet -IP -IP -UDP -SIP</p><p>Is this a bug? I tried 1.6.5 and 1.6.7 too.</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">filter capture sip rfc2003 encapsulation</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '12, 01:54</strong></p><img src="https://secure.gravatar.com/avatar/d3c47e6a43b283cee6a2cc63ea50a501?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hrex&#39;s gravatar image" /><p>hrex<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hrex has no accepted answers">0%</span></p></div></div><div id="comments-container-10815" class="comments-container"></div><div id="comment-tools-10815" class="comment-tools"></div><div class="clear"></div><div id="comment-10815-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10826"></span>

<div id="answer-container-10826" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10826-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, the IP-in-IP encapsulation is messing up your capture filter. BPF (the engine responsible for filtering) uses fixed offsets to look for things. You can see the way the filter works by using "tcpdump -d &lt;filter&gt;". When I do this for "udp port 5060", I get:</p><pre><code>(000) ldh      [12]
(001) jeq      #0x800           jt 2    jf 12
(002) ldb      [23]
(003) jeq      #0x11            jt 4    jf 12
(004) ldh      [20]
(005) jset     #0x1fff          jt 12   jf 6
(006) ldxb     4*([14]&amp;0xf)
(007) ldh      [x + 14]
(008) jeq      #0x13c4          jt 11   jf 9
(009) ldh      [x + 16]
(010) jeq      #0x13c4          jt 11   jf 12
(011) ret      #65535
(012) ret      #0</code></pre><p>As BPF is not aware of IP-in-IP encapsulation, it will check for the value of 5060 (0x13c4) in the wrong place. This also happens when there is vlan tagging, but for vlan tagging, you can add the word "vlan" to your filter to make it correct the offsets. I don't think there is a similar keyword for IP-in-IP.</p><p>You can manually account for variable IP header lengths or you can make life easy and test for specific offsets (counting from 0 from the start of the outer IP header) by using:</p><pre><code>ip[&lt;offset&gt;:2]==0x13c4 or ip[&lt;offset+2&gt;:2==0x13c4</code></pre><p>Could you upload a small example capture file on <a href="http://www.cloudshark.org"></a><a href="http://www.cloudshark.org">www.cloudshark.org</a> and post the link here, then we can assist you in building a proper capture filter.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '12, 05:42</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-10826" class="comments-container"></div><div id="comment-tools-10826" class="comment-tools"></div><div class="clear"></div><div id="comment-10826-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10817"></span>

<div id="answer-container-10817" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10817-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>1.) SIP is defined for UDP and <strong>TCP</strong> 5060. Maybe the clients use TCP in your case.</p><p>2.) Maybe they use SIP on a non-standard port</p><p>3.) Maybe SIP is encrypted, then it's port 5061</p><p>4.) Regarding IP-IP encapsulation, you need to give us a little bit more information (e.g. how do you send the data to a capture machine).</p><p>I suggest to check 1. - 3. first.</p><p>EDIT: If your sniffer really sees IP-in-IP packets, the answer of the following question might help you:</p><p><strong><a href="http://ask.wireshark.org/questions/9723/capture-an-ip-inside-a-gre-packet">http://ask.wireshark.org/questions/9723/capture-an-ip-inside-a-gre-packet</a></strong></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '12, 02:15</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 May '12, 03:13</p></div></div><div id="comments-container-10817" class="comments-container"><span id="10819"></span><div id="comment-10819" class="comment"><div id="post-10819-score" class="comment-score"></div><div class="comment-text"><p>1-3 is OK. It is UDP, 5060 and not encrypted. I can see it if I don't want to use capture filter or I using "host x.y.z.v"</p><p>There are some machines like this SBC which can mirror traffic to specified IP destination. Normally that machine is not in the SIP flow. To do this they are using RFC2003 IP-IP Encapsulation within IP.</p><p>So for example capture filter: "udp port 53" is working fine. "udp port 5060" is not working when packets arriving in RFC2003 IP-IP tunneling. I think because packets build up from L2-L3-L3-L4 headers.</p></div><div id="comment-10819-info" class="comment-info"><span class="comment-age">(09 May '12, 03:19)</span> hrex</div></div><span id="10824"></span><div id="comment-10824" class="comment"><div id="post-10824-score" class="comment-score"></div><div class="comment-text"><p>O.K. did you check <a href="http://ask.wireshark.org/questions/9723/capture-an-ip-inside-a-gre-packet">http://ask.wireshark.org/questions/9723/capture-an-ip-inside-a-gre-packet</a> ?</p></div><div id="comment-10824-info" class="comment-info"><span class="comment-age">(09 May '12, 05:35)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-10817" class="comment-tools"></div><div class="clear"></div><div id="comment-10817-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

