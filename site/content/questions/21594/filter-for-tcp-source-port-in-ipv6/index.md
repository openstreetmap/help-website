+++
type = "question"
title = "Filter for TCP source port in IPv6"
description = '''Hello,  I&#x27;m trying to create a capture filter for my TCP packets. I want to filter for packets with a specific source port, lets say port 1.  My filter is &quot;tcp src port 1&quot;, and I also tried &quot;tcp and src port 1&quot;.  However, this works perfectly when I use IPv4. But when I use IPv6, it doesn&#x27;t. I don&#x27;t...'''
date = "2013-05-30T05:57:00Z"
lastmod = "2013-05-30T09:05:00Z"
weight = 21594
keywords = [ "source", "port", "libpcap", "ipv6" ]
aliases = [ "/questions/21594" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Filter for TCP source port in IPv6](/questions/21594/filter-for-tcp-source-port-in-ipv6)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21594-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21594-score" class="post-score" title="current number of votes">0</div><span id="post-21594-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm trying to create a capture filter for my TCP packets. I want to filter for packets with a specific source port, lets say port 1.</p><p>My filter is "tcp src port 1", and I also tried "tcp and src port 1".</p><p>However, this works perfectly when I use IPv4. But when I use IPv6, it doesn't. I don't capture any packets, although the TCP header is exactly the same, I just exchanged the IP-layer. When I filter for "tcp port 1" or "tcp and port 1", I get all packets which have 1 as destination port, but none of the packets which have 1 as source port.</p><p>Could this be a bug in the pcap library? The fact that it fully works with IPv4, but only with the destination port in IPv6 and not with the source port makes me think that way....</p><p>Oh yeah, also, when I try to make a display filter, everything works if I set it for example to "tcp.srcport==1", in both IPv4 and IPv6.</p><p>I'm running libpcap0.8 version 1.4.0-1, my wireshark version is 1.8.7-1.</p><p>Thanks for your help!</p><p>Regards, Moe</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-source" rel="tag" title="see questions tagged &#39;source&#39;">source</span> <span class="post-tag tag-link-port" rel="tag" title="see questions tagged &#39;port&#39;">port</span> <span class="post-tag tag-link-libpcap" rel="tag" title="see questions tagged &#39;libpcap&#39;">libpcap</span> <span class="post-tag tag-link-ipv6" rel="tag" title="see questions tagged &#39;ipv6&#39;">ipv6</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 May '13, 05:57</strong></p><img src="https://secure.gravatar.com/avatar/6c33bb9edee5bd585393bbd6a8b83b26?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="moe&#39;s gravatar image" /><p><span>moe</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="moe has no accepted answers">0%</span></p></div></div><div id="comments-container-21594" class="comments-container"><span id="21598"></span><div id="comment-21598" class="comment"><div id="post-21598-score" class="comment-score"></div><div class="comment-text"><p>Just changed the virtual network card, did not make a difference</p></div><div id="comment-21598-info" class="comment-info"><span class="comment-age">(30 May '13, 07:05)</span> <span class="comment-user userinfo">moe</span></div></div></div><div id="comment-tools-21594" class="comment-tools"></div><div class="clear"></div><div id="comment-21594-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21595"></span>

<div id="answer-container-21595" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21595-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21595-score" class="post-score" title="current number of votes">3</div><span id="post-21595-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="moe has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Works for me (libpcap version 1.3.0 on OSX):</p><pre><code>$ tshark -i en1 &quot;tcp src port 80&quot;
Capturing on en1
  0.000000 2001:898:2000:1::244 -&gt; 2001:980:5354:3:fa1e:dfff:fed8:8748 TCP 94 http &gt; 53101 [SYN, ACK] Seq=0 Ack=1 Win=5712 Len=0 MSS=1440 SACK_PERM=1 TSval=1714395974 TSecr=394066808 WS=128
  0.027056 2001:898:2000:1::244 -&gt; 2001:980:5354:3:fa1e:dfff:fed8:8748 TCP 86 http &gt; 53101 [ACK] Seq=1 Ack=784 Win=7296 Len=0 TSval=1714396004 TSecr=394066809
  0.046179 2001:898:2000:1::244 -&gt; 2001:980:5354:3:fa1e:dfff:fed8:8748 TCP 1410 [TCP segment of a reassembled PDU]
  0.051261 2001:898:2000:1::244 -&gt; 2001:980:5354:3:fa1e:dfff:fed8:8748 HTTP 91 HTTP/1.1 200 OK  (text/html)</code></pre><p>Could you show the output of "compile BPF filter" (or run 'tcpdump -d "&lt;filter&gt;"' on the CLI). It should show something like this:</p><pre><code>(000) ldh      [12]
(001) jeq      #0x86dd          jt 2    jf 6
(002) ldb      [20]
(003) jeq      #0x6             jt 4    jf 15
(004) ldh      [54]
(005) jeq      #0x50            jt 14   jf 15
(006) jeq      #0x800           jt 7    jf 15
(007) ldb      [23]
(008) jeq      #0x6             jt 9    jf 15
(009) ldh      [20]
(010) jset     #0x1fff          jt 15   jf 11
(011) ldxb     4*([14]&amp;0xf)
(012) ldh      [x + 14]
(013) jeq      #0x50            jt 14   jf 15
(014) ret      #65535
(015) ret      #0</code></pre><p>Maybe there is a bug in your version of libpcap indeed. Also, are you sure your frames are not vlan tagged (or encapsulated in pppoe or something else)?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 May '13, 06:27</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-21595" class="comments-container"><span id="21596"></span><div id="comment-21596" class="comment"><div id="post-21596-score" class="comment-score"></div><div class="comment-text"><p>Thats my output from "compile BF filter":</p><pre><code>(000) ldh      [12]
(001) jeq      #0x86dd          jt 2    jf 6
(002) ldb      [20]
(003) jeq      #0x6             jt 4    jf 15
(004) ldh      [54]
(005) jeq      #0x1             jt 14   jf 15
(006) jeq      #0x800           jt 7    jf 15
(007) ldb      [23]
(008) jeq      #0x6             jt 9    jf 15
(009) ldh      [20]
(010) jset     #0x1fff          jt 15   jf 11
(011) ldxb     4*([14]&amp;0xf)
(012) ldh      [x + 14]
(013) jeq      #0x1             jt 14   jf 15
(014) ret      #65535
(015) ret      #0</code></pre><p>Its the same output as you have, except that I specified port 1 in line 6.</p><p>The communication I'm capturing is between two Virtual machines on the same physical PC. Wireshark runs on one of the virtual machines. So, yes, I'm sure that there's no VLAN or other things.</p><p>Here is (part of) the output of tshark when I do not filter for ports:</p><pre><code>$ sudo tshark -i eth0 &quot;tcp&quot;
Capturing on eth0
  0.000000          ::a -&gt; ::c          TCP 54425 &gt; tcpmux [SYN, ACK] Seq=500048637 Ack=3996483048 Win=1024 Len=0 MSS=1460
  0.000253          ::c -&gt; ::a          TCP tcpmux &gt; 54425 [RST] Seq=3996483048 Win=0 Len=0</code></pre><p>Now with the filter applied:</p><pre><code>$ sudo tshark -i eth0 &quot;tcp port 1&quot;
Capturing on eth0
  0.000000          ::a -&gt; ::c          TCP 35982 &gt; tcpmux [SYN, ACK] Seq=4190420215 Ack=4138811225 Win=1024 Len=0 MSS=1460</code></pre><p>The RST packet does not appear.</p><p>Any clues how to debug this further? I will try to change the virtual network cards of the machines, maybe this helps... I also already tried a different libpcap version (1.3.0-1), but that also did not help.</p></div><div id="comment-21596-info" class="comment-info"><span class="comment-age">(30 May '13, 06:50)</span> <span class="comment-user userinfo">moe</span></div></div><span id="21597"></span><div id="comment-21597" class="comment"><div id="post-21597-score" class="comment-score"></div><div class="comment-text"><p>Are you able to share the capture files on www.cloudshark.org? One taken with just "tcp" as filter and the other one taken with "tcp port 1" as filter (preferably made at the same time)?</p></div><div id="comment-21597-info" class="comment-info"><span class="comment-age">(30 May '13, 07:04)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="21601"></span><div id="comment-21601" class="comment"><div id="post-21601-score" class="comment-score"></div><div class="comment-text"><p>here you go! the first pcap with the filter "tcp": <a href="http://cloudshark.org/captures/7c257d3b1532">http://cloudshark.org/captures/7c257d3b1532</a></p><p>the second pcap with the filter "tcp port 1": <a href="http://cloudshark.org/captures/5c6adae06fa1">http://cloudshark.org/captures/5c6adae06fa1</a></p><p>both taken at the same time</p></div><div id="comment-21601-info" class="comment-info"><span class="comment-age">(30 May '13, 07:21)</span> <span class="comment-user userinfo">moe</span></div></div><span id="21602"></span><div id="comment-21602" class="comment"><div id="post-21602-score" class="comment-score"></div><div class="comment-text"><p>The return traffic is having an IPv6 fragmentation header. This changes the offset of the TCP within the packet. Since there are no loops allowed in BPF filtering, it is not possible for BPF to dynamically hop over all the possible IPv6 headers to adjust the offset for the tcp header.</p><p>The strange part is that when using only "tcp" as filter, the fragmentation header is accounted for (see line 4 of the BPF code):</p><pre><code>$ tcpdump -d &quot;tcp&quot;
(000) ldh      [12]
(001) jeq      #0x86dd          jt 2    jf 7
(002) ldb      [20]
(003) jeq      #0x6             jt 10   jf 4
(004) jeq      #0x2c            jt 5    jf 11
(005) ldb      [54]
(006) jeq      #0x6             jt 10   jf 11
(007) jeq      #0x800           jt 8    jf 11
(008) ldb      [23]
(009) jeq      #0x6             jt 10   jf 11
(010) ret      #65535
(011) ret      #0
$</code></pre><p>This might be considered a bug in libpcap or if looked at differently, it would be an enhancement request in libpcap :-)</p></div><div id="comment-21602-info" class="comment-info"><span class="comment-age">(30 May '13, 07:41)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="21603"></span><div id="comment-21603" class="comment"><div id="post-21603-score" class="comment-score"></div><div class="comment-text"><p>As for now, you can manually do the skipping of the extra header as follows:</p><pre><code>$ tcpdump -nnlr tcp.pcap &quot;(ip6[6]=6 and ip6[40:2]=1) or (ip6[6]=44 and ip6[40]=6 and ip6[48:2]=1)&quot;
reading from file tcp.pcap, link-type EN10MB (Ethernet)
16:14:23.515746 IP6 ::0.0.0.12 &gt; ::0.0.0.10: frag (0|20) 1 &gt; 63034: Flags [R], seq 1099986487, win 0, length 0
16:14:23.547560 IP6 ::0.0.0.12 &gt; ::0.0.0.10: frag (0|20) 1 &gt; 63035: Flags [R], seq 1099986487, win 0, length 0
16:14:23.579576 IP6 ::0.0.0.12 &gt; ::0.0.0.10: frag (0|20) 1 &gt; 63036: Flags [R], seq 1099986487, win 0, length 0
16:14:23.611582 IP6 ::0.0.0.12 &gt; ::0.0.0.10: frag (0|20) 1 &gt; 63037: Flags [R], seq 1099986487, win 0, length 0
16:14:23.644003 IP6 ::0.0.0.12 &gt; ::0.0.0.10: frag (0|20) 1 &gt; 63038: Flags [R], seq 1099986487, win 0, length 0
16:14:23.676372 IP6 ::0.0.0.12 &gt; ::0.0.0.10: frag (0|20) 1 &gt; 63039: Flags [R], seq 1099986487, win 0, length 0
$</code></pre></div><div id="comment-21603-info" class="comment-info"><span class="comment-age">(30 May '13, 07:50)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="21608"></span><div id="comment-21608" class="comment not_top_scorer"><div id="post-21608-score" class="comment-score"></div><div class="comment-text"><p>You are the man! I would have never found that issue on my own!</p><p>I guess changing this in libpcap would be desirable, especially because there might be also extension headers before the fragmentation header.</p><p>Thanks! If I managed to get my code published in Nmap, I will give you the credits for this one :)</p></div><div id="comment-21608-info" class="comment-info"><span class="comment-age">(30 May '13, 09:05)</span> <span class="comment-user userinfo">moe</span></div></div></div><div id="comment-tools-21595" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-21595-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

