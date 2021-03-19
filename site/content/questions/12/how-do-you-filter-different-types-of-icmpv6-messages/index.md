+++
type = "question"
title = "How do you filter different types of ICMPv6 messages?"
description = '''Libpcap lets you filter ICMP messages with named field values, e.g. icmp[icmptype] = icmp-echo  What is the ICMPv6 equivalent?'''
date = "2010-09-08T11:46:00Z"
lastmod = "2010-09-15T22:45:00Z"
weight = 12
keywords = [ "icmpv6", "capture-filter", "ipv6" ]
aliases = [ "/questions/12" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How do you filter different types of ICMPv6 messages?](/questions/12/how-do-you-filter-different-types-of-icmpv6-messages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12-score" class="post-score" title="current number of votes">1</div><span id="post-12-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Libpcap lets you filter ICMP messages with named field values, e.g.</p><pre><code>icmp[icmptype] = icmp-echo</code></pre><p>What is the ICMPv6 equivalent?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-icmpv6" rel="tag" title="see questions tagged &#39;icmpv6&#39;">icmpv6</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-ipv6" rel="tag" title="see questions tagged &#39;ipv6&#39;">ipv6</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Sep '10, 11:46</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Sep '10, 11:47</strong> </span></p></div></div><div id="comments-container-12" class="comments-container"></div><div id="comment-tools-12" class="comment-tools"></div><div class="clear"></div><div id="comment-12-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="136"></span>

<div id="answer-container-136" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-136-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-136-score" class="post-score" title="current number of votes">2</div><span id="post-136-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Gerald Combs has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like looking into icmp6 messages has not yet been implemented. However, you can use the IPv6 layer with an index (as long as there are no extra IPv6 headers):</p><pre><code>[email protected]:~$ tcpdump -nli en1 icmp6
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on en1, link-type EN10MB (Ethernet), capture size 65535 bytes
07:39:03.127714 IP6 2001:888:1cb7:1a:fa1e:dfff:fed8:8748 &gt; 2001:888:0:1::666: ICMP6, echo request, seq 486, length 16
07:39:03.144453 IP6 2001:888:0:1::666 &gt; 2001:888:1cb7:1a:fa1e:dfff:fed8:8748: ICMP6, echo reply, seq 486, length 16
07:39:04.127686 IP6 2001:888:1cb7:1a:fa1e:dfff:fed8:8748 &gt; 2001:888:0:1::666: ICMP6, echo request, seq 487, length 16
07:39:04.144941 IP6 2001:888:0:1::666 &gt; 2001:888:1cb7:1a:fa1e:dfff:fed8:8748: ICMP6, echo reply, seq 487, length 16
^C
4 packets captured
8 packets received by filter
0 packets dropped by kernel
[email protected]:~$ tcpdump -nli en1 icmp6[0]=128
tcpdump: IPv6 upper-layer protocol is not supported by proto[x]
[email protected]:~$ tcpdump -nli en1 icmp6 and ip6[40]=128
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on en1, link-type EN10MB (Ethernet), capture size 65535 bytes
07:39:22.127170 IP6 2001:888:1cb7:1a:fa1e:dfff:fed8:8748 &gt; 2001:888:0:1::666: ICMP6, echo request, seq 505, length 16
07:39:23.127169 IP6 2001:888:1cb7:1a:fa1e:dfff:fed8:8748 &gt; 2001:888:0:1::666: ICMP6, echo request, seq 506, length 16
^C
2 packets captured
8 packets received by filter
0 packets dropped by kernel
[email protected]:~$ tcpdump -nli en1 icmp6 and ip6[40]=129
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on en1, link-type EN10MB (Ethernet), capture size 65535 bytes
07:39:51.144359 IP6 2001:888:0:1::666 &gt; 2001:888:1cb7:1a:fa1e:dfff:fed8:8748: ICMP6, echo reply, seq 534, length 16
07:39:52.219218 IP6 2001:888:0:1::666 &gt; 2001:888:1cb7:1a:fa1e:dfff:fed8:8748: ICMP6, echo reply, seq 535, length 16
07:39:53.143163 IP6 2001:888:0:1::666 &gt; 2001:888:1cb7:1a:fa1e:dfff:fed8:8748: ICMP6, echo reply, seq 536, length 16
07:39:54.148842 IP6 2001:888:0:1::666 &gt; 2001:888:1cb7:1a:fa1e:dfff:fed8:8748: ICMP6, echo reply, seq 537, length 16
^C
4 packets captured
20 packets received by filter
0 packets dropped by kernel
[email protected]:~$ tcpdump --version
tcpdump version 4.0.0
libpcap version 1.0.0
Usage: tcpdump [-aAdDefgIKlLnNOpqRStuUvxX] [ -B size ] [ -c count ]
        [ -C file_size ] [ -E algo:secret ] [ -F file ] [ -G seconds ]
        [ -i interface ] [ -M secret ] [ -r file ]
        [ -s snaplen ] [ -T type ] [ -w file ] [ -W filecount ]
        [ -y datalinktype ] [ -z command ] [ -Z user ]
        [ expression ]
[email protected]:~$</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '10, 22:45</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-136" class="comments-container"></div><div id="comment-tools-136" class="comment-tools"></div><div class="clear"></div><div id="comment-136-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

