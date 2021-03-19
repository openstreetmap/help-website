+++
type = "question"
title = "wireshark see packets which should be dropped by iptables"
description = '''hello,  using iptables root@net06:~# iptables -A INPUT -s 192.168.1.5 -p udp -j DROP  i wanted do drop all incoming udp packets, but i don&#x27;t know why wireshark see all this packets.  Moreover  iptables -L -n -v  says that packets were droped.'''
date = "2011-06-11T16:03:00Z"
lastmod = "2011-06-11T23:12:00Z"
weight = 4521
keywords = [ "iptables" ]
aliases = [ "/questions/4521" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark see packets which should be dropped by iptables](/questions/4521/wireshark-see-packets-which-should-be-dropped-by-iptables)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4521-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4521-score" class="post-score" title="current number of votes">0</div><span id="post-4521-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello, using iptables</p><pre><code>[email protected]:~# iptables -A INPUT -s 192.168.1.5 -p udp -j DROP</code></pre><p>i wanted do drop all incoming udp packets, but i don't know why wireshark see all this packets. Moreover</p><pre><code>iptables -L -n -v</code></pre><p>says that packets were droped.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-iptables" rel="tag" title="see questions tagged &#39;iptables&#39;">iptables</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jun '11, 16:03</strong></p><img src="https://secure.gravatar.com/avatar/25703ef912a06ab6a5c6793426eeaec2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="azazzel01&#39;s gravatar image" /><p><span>azazzel01</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="azazzel01 has no accepted answers">0%</span></p></div></div><div id="comments-container-4521" class="comments-container"></div><div id="comment-tools-4521" class="comment-tools"></div><div class="clear"></div><div id="comment-4521-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4524"></span>

<div id="answer-container-4524" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4524-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4524-score" class="post-score" title="current number of votes">1</div><span id="post-4524-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>One basic rule of network analysis is that you never run the analysis tool on the same system as the device under test (or device under suspicion) as that might nog give you the right picture (as you are experiencing).</p><p>What you would want to do is run wireshark twice on systems on span/mirror ports that span/mirror the traffic on the outside and inside interfaces of the system running iptables. Then you can see the effect and effectiveness of the iptables rules in place.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '11, 22:04</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4524" class="comments-container"><span id="4525"></span><div id="comment-4525" class="comment"><div id="post-4525-score" class="comment-score"></div><div class="comment-text"><p>ok, thanks for help. I have just did it using ulogd and plugin to id ulogd-pcap. In this way iptables creates a pcap file with packets which were not dropped and it can be easiy open by wireshark.</p></div><div id="comment-4525-info" class="comment-info"><span class="comment-age">(11 Jun '11, 23:12)</span> <span class="comment-user userinfo">azazzel01</span></div></div></div><div id="comment-tools-4524" class="comment-tools"></div><div class="clear"></div><div id="comment-4524-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4522"></span>

<div id="answer-container-4522" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4522-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4522-score" class="post-score" title="current number of votes">0</div><span id="post-4522-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>My guess is that libpcap captures the packets just before they get processed (and blocked if UDP) by your iptables engine.</p><p>If your iptables machine is routing the packets you might wanna check on the other side if they exit as well (in which case your iptables has a problem). If it is an endpoint you should check if any UDP packet ever gets answered - either by an UDP packet if there is a service on that port, or an ICMP port unreachable packet if there is not. If you see none of these reply packets dropping the UDP packets obviously works.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '11, 16:21</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-4522" class="comments-container"><span id="4523"></span><div id="comment-4523" class="comment"><div id="post-4523-score" class="comment-score"></div><div class="comment-text"><p>yes, You are right i have found some information, that libpcap works just before netfilter and that's why wireshark see all the packets. I have chaced it using:</p><pre><code>[email protected]:~# iptables -L INPUT -n -v</code></pre><p>and iptables shows that the packets were dropped but it doesn't solve my problem. I wrote simple C program which sends udp packets to some other computer (with iptables dropping) and i need to know exactly which packets were dropped. Because wireshark shows all packets and iptables shows only number of dropped packets is it possible to check it ?</p><p>Thank You for help and sorry for my english, i am not native english speaker.</p></div><div id="comment-4523-info" class="comment-info"><span class="comment-age">(11 Jun '11, 17:09)</span> <span class="comment-user userinfo">azazzel01</span></div></div></div><div id="comment-tools-4522" class="comment-tools"></div><div class="clear"></div><div id="comment-4522-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

