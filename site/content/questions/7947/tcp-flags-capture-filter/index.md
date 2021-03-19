+++
type = "question"
title = "TCP flags capture filter"
description = '''With the &quot;Wireshark: Capture Options&quot; dialog, I&#x27;m trying to use a custom &quot;Capture Filter&quot; I want to capture reset packets only (display filter equivalent: tcp.flags.reset ==1)'''
date = "2011-12-13T09:18:00Z"
lastmod = "2011-12-13T10:40:00Z"
weight = 7947
keywords = [ "filter", "capture", "flags", "tcp", "reset" ]
aliases = [ "/questions/7947" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP flags capture filter](/questions/7947/tcp-flags-capture-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7947-score" class="post-score" title="current number of votes">1</div><span id="post-7947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>With the "Wireshark: Capture Options" dialog, I'm trying to use a custom "Capture Filter"</p><p>I want to capture reset packets only (display filter equivalent: tcp.flags.reset ==1)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-flags" rel="tag" title="see questions tagged &#39;flags&#39;">flags</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-reset" rel="tag" title="see questions tagged &#39;reset&#39;">reset</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Dec '11, 09:18</strong></p><img src="https://secure.gravatar.com/avatar/30f87f92e01c6cd2f41ba32751d2334b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peter_Clark&#39;s gravatar image" /><p><span>Peter_Clark</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peter_Clark has no accepted answers">0%</span></p></div></div><div id="comments-container-7947" class="comments-container"></div><div id="comment-tools-7947" class="comment-tools"></div><div class="clear"></div><div id="comment-7947-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7949"></span>

<div id="answer-container-7949" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7949-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7949-score" class="post-score" title="current number of votes">2</div><span id="post-7949-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>On older versions of UN*X, the command <code>man tcpdump</code> will give, among other things, documentation about capture filters; on newer versions, <code>man pcap-filter</code> will give that documentation.</p><p>The key part is</p><pre><code>   expr relop expr
          True  if the relation holds, where relop is one of &gt;, &lt;, &gt;=, &lt;=,
          =, !=, and expr is an arithmetic expression composed of  integer
          constants  (expressed  in  standard C syntax), the normal binary
          operators [+, -, *, /, &amp;, |, &lt;&lt;, &gt;&gt;],  a  length  operator,  and
          special  packet  data  accessors.  Note that all comparisons are
          unsigned, so that, for example, 0x80000000 and 0xffffffff are  &gt;
          0.  To access data inside the packet, use the following syntax:
               proto [ expr : size ]
          Proto is one of ether, fddi, tr, wlan, ppp, slip, link, ip, arp,
          rarp, tcp, udp, icmp, ip6 or radio, and indicates  the  protocol
          layer  for  the  index  operation.  (ether, fddi, wlan, tr, ppp,
          slip and link all refer to the link layer. radio refers  to  the
          &quot;radio  header&quot;  added to some 802.11 captures.)  Note that tcp,
          udp and other upper-layer protocol types only apply to IPv4, not
          IPv6 (this will be fixed in the future).  The byte offset, rela-
          tive to the indicated protocol layer, is given by expr.  Size is
          optional  and  indicates  the  number  of  bytes in the field of
          interest; it can be either one, two, or four,  and  defaults  to
          one.   The  length operator, indicated by the keyword len, gives
          the length of the packet.

          For example, `ether[0] &amp; 1 != 0&#39; catches all multicast  traffic.
          The  expression `ip[0] &amp; 0xf != 5&#39; catches all IPv4 packets with
          options.  The expression `ip[6:2] &amp; 0x1fff  =  0&#39;  catches  only
          unfragmented  IPv4  datagrams  and  frag zero of fragmented IPv4
          datagrams.  This check is implicitly applied to the tcp and  udp
          index  operations.   For instance, tcp[0] always means the first
          byte of the TCP header, and never means the  first  byte  of  an
          intervening fragment.

          Some  offsets  and field values may be expressed as names rather
          than as numeric values.  The  following  protocol  header  field
          offsets  are  available:  icmptype  (ICMP  type field), icmpcode
          (ICMP code field), and tcpflags (TCP flags field).

          The following ICMP type field values are available: icmp-echore-
          ply,  icmp-unreach, icmp-sourcequench, icmp-redirect, icmp-echo,
          icmp-routeradvert,  icmp-routersolicit,   icmp-timxceed,   icmp-
          paramprob,  icmp-tstamp,  icmp-tstampreply, icmp-ireq, icmp-ire-
          qreply, icmp-maskreq, icmp-maskreply.

          The following TCP flags field  values  are  available:  tcp-fin,
          tcp-syn, tcp-rst, tcp-push, tcp-ack, tcp-urg.</code></pre><p>In particular, unless Wireshark is using an older version of libpcap/WinPcap, as per the "Some offsets and field values may be expressed as names..." section, filtering for RST packets can be done with <code>tcp[tcpflags] &amp; tcp-rst != 0</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Dec '11, 10:40</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-7949" class="comments-container"></div><div id="comment-tools-7949" class="comment-tools"></div><div class="clear"></div><div id="comment-7949-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

