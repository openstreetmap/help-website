+++
type = "question"
title = "Problem with VLAN filtering, live vs. recorded"
description = '''We have a Linux box connected to a mirror port on a Juniper router. If I use tcpdump or tethereal to view packets live, I cannot filter by VLAN, but I can by host, e.g.  tethereal -i eth2 -n host www.example.com works, while tethereal -i eth2 -n vlan 123 and host www.example.com does not. If I recor...'''
date = "2014-10-17T16:15:00Z"
lastmod = "2014-11-04T14:02:00Z"
weight = 37143
keywords = [ "capture-filter", "vlan" ]
aliases = [ "/questions/37143" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Problem with VLAN filtering, live vs. recorded](/questions/37143/problem-with-vlan-filtering-live-vs-recorded)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37143-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have a Linux box connected to a mirror port on a Juniper router. If I use tcpdump or tethereal to view packets live, I cannot filter by VLAN, but I can by host, e.g.<br />
<code>tethereal -i eth2 -n host www.example.com</code> works, while<br />
<code>tethereal -i eth2 -n vlan 123 and host www.example.com</code> does not.<br />
If I record a pcap file, e.g.<br />
<code>tethereal -i eth2 -w my.cap -c 400</code><br />
then I can replay it with e.g.<br />
<code>tcpdump -r my.cap -n vlan and host www.example.com</code><br />
or<br />
<code>tcpdump -r my.cap -n vlan 123 host www.example.com</code><br />
but not<br />
<code>tcpdump -r my.cap -n host www.example.com</code><br />
</p><p>It is particularly annoying that we cannot filter live by VLAN, e.g.<br />
<code>tethereal -i eth2 -n vlan 123</code><br />
On an older router (Nortel Passport), this worked.</p><p>We have libpcap-1.4.0 on CentOS 6 with a Mellanox driver v2.0 and a MT26448 card, connected to a Juniper EX9008 router.</p><p>I want to be able to filter live by VLAN number. Is this something I can do with the right syntax, or is it an issue with the driver or OS or hardware ?</p></div><div id="question-tags" class="tags-container tags">capture-filter vlan</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Oct '14, 16:15</strong></p><img src="https://secure.gravatar.com/avatar/15e8cc4271eec8d4c25ac13dfd5192db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adaviel&#39;s gravatar image" /><p>adaviel<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adaviel has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-37143" class="comments-container"><span id="37240"></span><div id="comment-37240" class="comment"><div id="post-37240-score" class="comment-score"></div><div class="comment-text"><p>could you please post the output of the following commands on your system?</p><blockquote><p>tcpdump -d vlan 123 and host www.example.com<br />
tcpdump -d host www.example.com</p><p>tcpdump -ni eth2 -w - | od -x</p></blockquote><p>please add the expected VLAN and traffic (IPs, protocol, ports, etc.)</p><p>HINT: the last command could produce a lot of output, depending on the traffic!</p></div><div id="comment-37240-info" class="comment-info"><span class="comment-age">(21 Oct '14, 07:39)</span> Kurt Knochner ♦</div></div><span id="37297"></span><div id="comment-37297" class="comment"><div id="post-37297-score" class="comment-score"></div><div class="comment-text"><p>The web form won't let me add that much text. See <a href="http://andrew.triumf.ca/tcpdump_vlan.txt">http://andrew.triumf.ca/tcpdump_vlan.txt</a></p><p>I tried building the latest tarballs from tcpdump.org but they have the same issue.</p></div><div id="comment-37297-info" class="comment-info"><span class="comment-age">(22 Oct '14, 17:16)</span> adaviel</div></div><span id="37316"></span><div id="comment-37316" class="comment"><div id="post-37316-score" class="comment-score"></div><div class="comment-text"><p>can you please add the output of the following command:</p><blockquote><p>tcpdump -ni eth2 -w - | od -x</p></blockquote><p>this is <strong>without</strong> writing a capture file to disk.</p></div><div id="comment-37316-info" class="comment-info"><span class="comment-age">(23 Oct '14, 12:04)</span> Kurt Knochner ♦</div></div><span id="37320"></span><div id="comment-37320" class="comment"><div id="post-37320-score" class="comment-score"></div><div class="comment-text"><p>OK, I've updated the link. How exactly is that different ? Is tcpdump -w x.cap different from tcpdump -w - &gt; x.cap ? Reading from a file or stdin, they seem identical</p></div><div id="comment-37320-info" class="comment-info"><span class="comment-age">(23 Oct '14, 14:26)</span> adaviel</div></div></div><div id="comment-tools-37143" class="comment-tools"></div><div class="clear"></div><div id="comment-37143-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="37147"></span>

<div id="answer-container-37147" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37147-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Linux does annoying things to VLAN tags in packets received on PF_PACKET sockets (libpcap uses PF_PACKET sockets on Linux), and libpcap doesn't yet compensate for that in the code that compiles filters. It does attempt to undo the things Linux does to the tags, so you see the packets complete with VLAN tags, so filters on a file containing those reconstructed packets works.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '14, 01:02</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></br></p></div></div><div id="comments-container-37147" class="comments-container"><span id="37213"></span><div id="comment-37213" class="comment"><div id="post-37213-score" class="comment-score"></div><div class="comment-text"><p>Do you have any details ? Is it possible to patch libpcap or the network driver so that it will work ?</p></div><div id="comment-37213-info" class="comment-info"><span class="comment-age">(20 Oct '14, 17:26)</span> adaviel</div></div><span id="37234"></span><div id="comment-37234" class="comment"><div id="post-37234-score" class="comment-score"></div><div class="comment-text"><p><a href="http://lists.openwall.net/netdev/2008/07/08/31">http://lists.openwall.net/netdev/2008/07/08/31</a> talks about some of the problems. There was a blog entry on it as well, can't find that anymore.</p></div><div id="comment-37234-info" class="comment-info"><span class="comment-age">(21 Oct '14, 05:45)</span> Jaap ♦</div></div><span id="37298"></span><div id="comment-37298" class="comment"><div id="post-37298-score" class="comment-score"></div><div class="comment-text"><p>That's talking about kernel patches added in 2008. I believe that the one to linux/if_vlan.h is included in 2.6.32. I don't understand whether the patch is supposed to fix my problem, or whether it causes my problem.</p></div><div id="comment-37298-info" class="comment-info"><span class="comment-age">(22 Oct '14, 17:30)</span> adaviel</div></div><span id="37302"></span><div id="comment-37302" class="comment"><div id="post-37302-score" class="comment-score"></div><div class="comment-text"><p>Take note of this part: "There are mainly two remaining problems with this approach:" which suggests to me that there are residual problems even after these patches applied.</p></div><div id="comment-37302-info" class="comment-info"><span class="comment-age">(23 Oct '14, 02:01)</span> Jaap ♦</div></div></div><div id="comment-tools-37147" class="comment-tools"></div><div class="clear"></div><div id="comment-37147-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="37573"></span>

<div id="answer-container-37573" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37573-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This may be fixed in libpcap 1.7.x See <a href="https://github.com/the-tcpdump-group/libpcap/issues/390">issue 390</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Nov '14, 14:02</strong></p><img src="https://secure.gravatar.com/avatar/15e8cc4271eec8d4c25ac13dfd5192db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adaviel&#39;s gravatar image" /><p>adaviel<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adaviel has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-37573" class="comments-container"></div><div id="comment-tools-37573" class="comment-tools"></div><div class="clear"></div><div id="comment-37573-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

