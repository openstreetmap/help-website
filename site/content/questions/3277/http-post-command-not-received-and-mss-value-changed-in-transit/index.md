+++
type = "question"
title = "HTTP POST command not received and MSS value changed in transit"
description = '''Hello, I am debugging a connection reset issue with the following symptoms. The network admins say all firewalls and routers are wide-open between the IP&#x27;s, no blocking of any sort. I&#x27;m running tcpdump on two systems while they attempt to communicate with each other and using wireshark to look at th...'''
date = "2011-04-01T16:49:00Z"
lastmod = "2011-04-01T23:17:00Z"
weight = 3277
keywords = [ "rst", "mss", "post", "http", "firewall" ]
aliases = [ "/questions/3277" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [HTTP POST command not received and MSS value changed in transit](/questions/3277/http-post-command-not-received-and-mss-value-changed-in-transit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3277-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3277-score" class="post-score" title="current number of votes">0</div><span id="post-3277-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am debugging a connection reset issue with the following symptoms. The network admins say all firewalls and routers are wide-open between the IP's, no blocking of any sort. I'm running tcpdump on two systems while they attempt to communicate with each other and using wireshark to look at the traces.</p><p>Setup:</p><p>SYS1: Private IP NAT'd to public IP, one-to one. SYS2: Public IP. Idea is SYS1 will communicate with SYS2 over the internet. Here is the problem.</p><p>SYS1 sends ping, SYS2 replies</p><p>SYS1 sends SYN, SYS2 sees SYN, replies with SYN, ACK</p><p>SYS1 sees ACK, replies with ACK which SYS2 sees.</p><p>SYS1 sends HTTP POST command and SYS2 never sees it, it is not in the SYS2 trace.</p><p>Both systems then log a RST from the other: Acknowledgement number: Broken TCP. The acknowledge field is nonzero while the ACK flag is not set</p><p>The only odd thing I see in the traces is that both systems send an MSS of 1460 with the SYN frame and both receive an MSS of 1380 when they get those SYN frames, so something in the path is changing that. I don't think that should cause the problem above but it does point to some sort of frame manipulation going on somewhere. I am trying to utilize other setups to eliminate parts of the picture but if this sounds familiar to anyone I'd be interested in your thoughts.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span> <span class="post-tag tag-link-mss" rel="tag" title="see questions tagged &#39;mss&#39;">mss</span> <span class="post-tag tag-link-post" rel="tag" title="see questions tagged &#39;post&#39;">post</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-firewall" rel="tag" title="see questions tagged &#39;firewall&#39;">firewall</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '11, 16:49</strong></p><img src="https://secure.gravatar.com/avatar/13b4c45fe297fb884712b3af91c5749d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jgg&#39;s gravatar image" /><p><span>jgg</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jgg has no accepted answers">0%</span></p></div></div><div id="comments-container-3277" class="comments-container"></div><div id="comment-tools-3277" class="comment-tools"></div><div class="clear"></div><div id="comment-3277-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3285"></span>

<div id="answer-container-3285" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3285-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3285-score" class="post-score" title="current number of votes">1</div><span id="post-3285-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The TCP MSS value stands for Maximum Segment Size, the maximum amount of TCP payload accepted in each TCP segment (and thus packet). The TCP MSS value is changed by intermediate devices when they know there will be some tunneling (IPsec, MPLS, PPPoE, etc) that will add a header to each packet. That way, they prevent IP fragmentation when full-sizes frames are sent later on.</p><p>Some devices do even change the MSS any way, just to be sure. I know the Cisco FWSM (firewall module in a 65XX) changes the MSS to 1380 by default.</p><p>That said, this is not a problem if both systems adhere to the lower MSS value. It would be useful to know the size of the HTTP POST packet, including the sizes of the IP header, the TCP header and the TCP length.</p><p>If both systems see a TCP RST from the other, without them sending them to each other, this means there is some device in between that is causing them. The most logical conclusion would be that there is some device having IDP (Intrusion Detection and Prevention) functionality, maybe the FW, maybe a separate device, that is not liking the HTTP POST and is rejecting it with the TCP RST packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Apr '11, 23:17</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3285" class="comments-container"></div><div id="comment-tools-3285" class="comment-tools"></div><div class="clear"></div><div id="comment-3285-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3278"></span>

<div id="answer-container-3278" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3278-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3278-score" class="post-score" title="current number of votes">0</div><span id="post-3278-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Check to see IP ID's are the same. It's possible that only TCP's MSS is being adjusted (Cisco routers, for example can do this). Also, I think you meant "SYS1 sees SYN+ACK and replies with ACK" You didn't mention what your packet size was for the HTTP POST. Is it 1380? You can also use ping packets with "do not fragment" bits set (-f for Windows, or using advanced options for cisco routers). If using windows, don't forget that Windows doesn't account for 8 byte ICMP header. So "ping -f 1472..." will really send 1480 byte IP packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Apr '11, 17:17</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p><span>hansangb</span><br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span></p></div></div><div id="comments-container-3278" class="comments-container"></div><div id="comment-tools-3278" class="comment-tools"></div><div class="clear"></div><div id="comment-3278-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

