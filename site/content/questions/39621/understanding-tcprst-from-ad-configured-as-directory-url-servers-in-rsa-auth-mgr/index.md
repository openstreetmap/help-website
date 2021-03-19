+++
type = "question"
title = "Understanding TCP/RST from AD - configured as Directory URL servers in RSA Auth Mgr"
description = '''Hi there. Am looking to see if the community has had this experience, and if not, maybe some feedback or suggestions: Environment: RSA Auth Manager 8.1, (1) Primary, (3) Replicas The Primary has (2) Directory URL servers configured - both Windows 2008 AD VM&#x27;s Issue:   Whenever the Primary Directory ...'''
date = "2015-02-03T16:49:00Z"
lastmod = "2015-02-04T01:27:00Z"
weight = 39621
keywords = [ "tcpflags", "tcpdump", "rsa" ]
aliases = [ "/questions/39621" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Understanding TCP/RST from AD - configured as Directory URL servers in RSA Auth Mgr](/questions/39621/understanding-tcprst-from-ad-configured-as-directory-url-servers-in-rsa-auth-mgr)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39621-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39621-score" class="post-score" title="current number of votes">0</div><span id="post-39621-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there. Am looking to see if the community has had this experience, and if not, maybe some feedback or suggestions:</p><p><strong>Environment</strong>: RSA Auth Manager 8.1, (1) Primary, (3) Replicas</p><p>The Primary has (2) Directory URL servers configured - both Windows 2008 AD VM's</p><p><strong>Issue:</strong> Whenever the Primary Directory URL server is offline, the Primary RSA instance cannot successfully connect to the 2nd AD/DC. I've also tried using the IP address instead of FQDN, that makes no difference. I've also tried swapping the order of the Directory URL servers, that makes no difference either.</p><p>The same results occur, A.M. can always talk to the Primary Directory URL server, no matter which one is configured, as soon as the Primary is turned off, A.M. cant establish successful connection with the Failover URL server, demonstrated by what looks like TCP/RST coming from the AD/DC</p><p>Additionally, the FQDN in use is not configured as a DNS Round Robin. Windows Firewall is turned off on both AD/DC's.. and these are vSphere VM's by the way.</p><p>from the A.M. Primary I can successfully run "openssl s_client -connect 10.100.0.91:389" to that Failover Directory URL server, and the connection succeeds</p><p>I'm providing 4 lines of packet analysis from TCPDump from the A.M. primary..<br />
</p><p>the A.M. Primary is 10.100.2.167 the Failover URL server is 10.100.0.91</p><pre><code>1778 17:17:11.289622    10.100.0.91 10.100.2.167    TCP 74  389→56923 [SYN, ACK] Seq=0 Ack=1 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1 TSval=664262070 TSecr=64906072

1779  17:17:11.289669   10.100.2.167    10.100.0.91 TCP 66  56923→389 [ACK] Seq=1 Ack=1 Win=14720 Len=0 TSval=64906072 TSecr=664262070

1780 17:17:11.290053    10.100.2.167    10.100.0.91 TCP 205 56923→389 [PSH, ACK] Seq=1 Ack=1 Win=14720 Len=139 TSval=64906072 TSecr=664262070

1781 17:17:11.290351    10.100.0.91 10.100.2.167    TCP 60  389→56923 [RST, ACK] Seq=1 Ack=140 Win=0 Len=0</code></pre><p>the sample above will also occur if I move 10.100.0.91 to be the Primary Directory URL server, and then when the same tests are ran, the exact same behavior occurs on the other AD/DC, which was previously able to connect when it was configured as the Primary Directory URL server</p><p>If anyone has any ideas, it would be much appreciated. Have spent a LOT of time on this so far, and am running out of ideas. Was thinking next approach is to run Wireshark on the AD/DC side and compare, perhaps something else is happening that we're missing from the TCPdump on the A.M. appliance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcpflags" rel="tag" title="see questions tagged &#39;tcpflags&#39;">tcpflags</span> <span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-rsa" rel="tag" title="see questions tagged &#39;rsa&#39;">rsa</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Feb '15, 16:49</strong></p><img src="https://secure.gravatar.com/avatar/bf1ee11f03a2ccc8257376adb3543740?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kapshure&#39;s gravatar image" /><p><span>kapshure</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kapshure has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Feb '15, 01:16</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-39621" class="comments-container"></div><div id="comment-tools-39621" class="comment-tools"></div><div class="clear"></div><div id="comment-39621-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39627"></span>

<div id="answer-container-39627" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39627-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39627-score" class="post-score" title="current number of votes">0</div><span id="post-39627-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From these 4 packets, one can only assume the following:</p><ul><li>The AD server is somehow not happy with the way the LDAP session is being set up. What is the difference in the SSL ClientHello when it is configured as a primary and when it is configured as a secondary? Are you using SNI?</li><li>Some device in between the MA and the Primary AD is not happy with the way the LDAP session is being set up. If so, you might see a different IP.TTL for the RST packet.</li></ul><p>BTW, why are you using LDAP over SSL on port 389 and not on 636?</p><p>Are you able to share the faulty and good session setup on www.cloudshark.org so that we can have a look at the difference? Only the first 6 packets of each stream will suffice for now.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '15, 01:27</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-39627" class="comments-container"></div><div id="comment-tools-39627" class="comment-tools"></div><div class="clear"></div><div id="comment-39627-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

