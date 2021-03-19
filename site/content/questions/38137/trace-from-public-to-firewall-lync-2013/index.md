+++
type = "question"
title = "Trace from Public to Firewall - Lync 2013"
description = '''Hi- New to wireshark. Troubleshooting access to a Reverse Proxy server through firewall. This is for a Lync 2013 deployment. My Reverse Proxy is sitting in my DMZ. I am using NAT on a Cisco ASA 5510. The public IP is 67.136.135.233. I can access the RP from within the DMZ and all Lync functions appe...'''
date = "2014-11-25T11:22:00Z"
lastmod = "2014-12-02T11:14:00Z"
weight = 38137
keywords = [ "lync" ]
aliases = [ "/questions/38137" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Trace from Public to Firewall - Lync 2013](/questions/38137/trace-from-public-to-firewall-lync-2013)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38137-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38137-score" class="post-score" title="current number of votes">0</div><span id="post-38137-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi- New to wireshark. Troubleshooting access to a Reverse Proxy server through firewall. This is for a Lync 2013 deployment. My Reverse Proxy is sitting in my DMZ. I am using NAT on a Cisco ASA 5510. The public IP is 67.136.135.233. I can access the RP from within the DMZ and all Lync functions appear to work as expected. I CANNOT access this server from outside the firewall. All Lync-related objects/rules appear to be set up correctly on the ASA...</p><p>PLEASE... Can you read my log and tell me what's going on? [I'm using a laptop connected through a mobile hotspot to run Wireshark]</p><pre><code>No. Time    Source  Destination Protocol    Length  Info
41  39.929778   IntelCor_53:69:b6   Broadcast   ARP 42  Who has 192.168.43.1?  Tell 192.168.43.154

42  39.974162   SamsungE_0a:f5:a4   IntelCor_53:69:b6   ARP 42  192.168.43.1 is at 34:23:ba:0a:f5:a4

43  39.974474   192.168.43.154  67.136.135.233  TCP 66  49557 &gt; 443 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1

44  40.18278    192.168.43.154  67.136.135.233  TCP 66  49558 &gt; 443 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1

45  42.922161   192.168.43.154  67.136.135.233  TCP 66  [TCP Retransmission] 49557 &gt; 443 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1

46  43.182483   192.168.43.154  67.136.135.233  TCP 66  [TCP Retransmission] 49558 &gt; 443 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1

47  47.750547   IntelCor_53:69:b6   SamsungE_0a:f5:a4   ARP 42  Who has 192.168.43.1?  Tell 192.168.43.154

48  47.807485   SamsungE_0a:f5:a4   IntelCor_53:69:b6   ARP 42  192.168.43.1 is at 34:23:ba:0a:f5:a4

49  48.923489   192.168.43.154  67.136.135.233  TCP 62  [TCP Retransmission] 49557 &gt; 443 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 SACK_PERM=1

50  49.188817   192.168.43.154  67.136.135.233  TCP 62  [TCP Retransmission] 49558 &gt; 443 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 SACK_PERM=1

51  61.181722   192.168.43.154  67.136.135.233  TCP 66  49559 &gt; 443 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1

52  64.183307   192.168.43.154  67.136.135.233  TCP 66  [TCP Retransmission] 49559 &gt; 443 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1

53  64.37699    192.168.43.154  192.168.43.1    DNS 76  Standard query 0x0238  A dns.msftncsi.com

54  64.430653   192.168.43.1    192.168.43.154  DNS 92  Standard query response 0x0238  A 131.107.255.255

55  69.249998   IntelCor_53:69:b6   SamsungE_0a:f5:a4   ARP 42  Who has 192.168.43.1?  Tell 192.168.43.154

56  69.291325   SamsungE_0a:f5:a4   IntelCor_53:69:b6   ARP 42  192.168.43.1 is at 34:23:ba:0a:f5:a4

57  70.183769   192.168.43.154  67.136.135.233  TCP 62  [TCP Retransmission] 49559 &gt; 443 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 SACK_PERM=1

58  82.186157   192.168.43.154  67.136.135.233  TCP 66  49560 &gt; 443 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1

59  82.4369 192.168.43.154  67.136.135.233  TCP 66  49561 &gt; 443 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1

60  82.522134   192.168.43.154  192.168.43.255  NBNS    92  Name query NB WPAD&lt;00&gt;

61  82.522697   192.168.43.154  224.0.0.252 LLMNR   64  Standard query 0x80b0  A wpad

62  82.523107   192.168.43.154  224.0.0.252 LLMNR   64  Standard query 0x914f  AAAA 
wpad
63  82.933491   192.168.43.154  224.0.0.252 LLMNR   64  Standard query 0x80b0  A wpad

64  82.933502   192.168.43.154  224.0.0.252 LLMNR   64  Standard query 0x914f  AAAA wpad

65  83.272728   192.168.43.154  192.168.43.255  NBNS    92  Name query NB WPAD&lt;00&gt;

66  84.02534    192.168.43.154  192.168.43.255  NBNS    92  Name query NB WPAD&lt;00&gt;

67  85.188314   192.168.43.154  67.136.135.233  TCP 66  [TCP Retransmission] 49560 &gt; 443 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1

68  85.437492   192.168.43.154  67.136.135.233  TCP 66  [TCP Retransmission] 49561 &gt; 443 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1

69  90.249988   IntelCor_53:69:b6   SamsungE_0a:f5:a4   ARP 42  Who has 192.168.43.1?  Tell 192.168.43.154

70  90.30039    SamsungE_0a:f5:a4   IntelCor_53:69:b6   ARP 42  192.168.43.1 is at 34:23:ba:0a:f5:a4

71  91.183634   192.168.43.154  67.136.135.233  TCP 62  [TCP Retransmission] 49560 &gt; 443 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 SACK_PERM=1

72  91.437979   192.168.43.154  67.136.135.233  TCP 62  [TCP Retransmission] 49561 &gt; 443 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 SACK_PERM=1

73  94.376815   192.168.43.154  192.168.43.1    DNS 76  Standard query 0x19c9  A dns.msftncsi.com

74  94.532964   192.168.43.154  192.168.43.1    DNS 76  Standard query 0x19c9  A dns.msftncsi.com

75  94.612641   192.168.43.1    192.168.43.154  DNS 92  Standard query response 0x19c9  A 131.107.255.255</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lync" rel="tag" title="see questions tagged &#39;lync&#39;">lync</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '14, 11:22</strong></p><img src="https://secure.gravatar.com/avatar/fd9cf4dab107c4336dcebe25ac625c91?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SteveSmo&#39;s gravatar image" /><p><span>SteveSmo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SteveSmo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Nov '14, 15:25</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-38137" class="comments-container"></div><div id="comment-tools-38137" class="comment-tools"></div><div class="clear"></div><div id="comment-38137-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38217"></span>

<div id="answer-container-38217" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38217-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38217-score" class="post-score" title="current number of votes">0</div><span id="post-38217-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As you can see, there are multiple attempts to connect to port 443 (SYN frames), but there is no SYN-ACK. As you mentioned the ASA firewall, there is either no rule that allows the traffic or nor NAT (DNAT) that translates the traffic for 67.136.135.233:443 to the internal address. Please check the firewall log.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '14, 15:30</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-38217" class="comments-container"><span id="38282"></span><div id="comment-38282" class="comment"><div id="post-38282-score" class="comment-score"></div><div class="comment-text"><p>Doh!!! Everything on the firewall was set up correctly. ISSUE was that the interface for the external NIC on the VM server was incorrect. Changed to correct interface resolved issue. Thanks to all for your input.</p></div><div id="comment-38282-info" class="comment-info"><span class="comment-age">(02 Dec '14, 11:14)</span> <span class="comment-user userinfo">SteveSmo</span></div></div></div><div id="comment-tools-38217" class="comment-tools"></div><div class="clear"></div><div id="comment-38217-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

