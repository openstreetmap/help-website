+++
type = "question"
title = "TCP Retransmission is detected instead of a duplicate ip packet"
description = '''Hi, I expect that there is a wrong TCP-retransmission detected where wireshark should detect a duplicate ip packet. We would like a possibility to filter out any duplicate ip packets (means same IP-Identification in a flow) caused by mirroring multiple interfaces on a switch at the same time (eg. be...'''
date = "2012-01-19T21:59:00Z"
lastmod = "2012-08-05T17:04:00Z"
weight = 8490
keywords = [ "duplicate", "retransmission" ]
aliases = [ "/questions/8490" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Retransmission is detected instead of a duplicate ip packet](/questions/8490/tcp-retransmission-is-detected-instead-of-a-duplicate-ip-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8490-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I expect that there is a wrong TCP-retransmission detected where wireshark should detect a duplicate ip packet. We would like a possibility to filter out any duplicate ip packets (means same IP-Identification in a flow) caused by mirroring multiple interfaces on a switch at the same time (eg. before and after a firewall). The packets are different on L2 but are the same on Layer3 except TTL,.. To filter TCP-Retransmission could change the real traffic as it could be a normal tcp-retransmission.</p><p>Does anybody how to filter out any duplicated ip packets?</p><p>Regards C</p></div><div id="question-tags" class="tags-container tags">duplicate retransmission</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jan '12, 21:59</strong></p><img src="https://secure.gravatar.com/avatar/03d97d33d584fedf21acf795dc41258a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chris2012&#39;s gravatar image" /><p>chris2012<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chris2012 has no accepted answers">0%</span></p></div></div><div id="comments-container-8490" class="comments-container"></div><div id="comment-tools-8490" class="comment-tools"></div><div class="clear"></div><div id="comment-8490-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="13375"></span>

<div id="answer-container-13375" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13375-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is a bug-report open for this, but no one has found the time and/or interest to solve this. Please have a look at <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=4561">Bug 4561</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '12, 17:04</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-13375" class="comments-container"></div><div id="comment-tools-13375" class="comment-tools"></div><div class="clear"></div><div id="comment-13375-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8501"></span>

<div id="answer-container-8501" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8501-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Wireshark installation comes with a command line tool called <strong>editcap</strong>, which has a parameter set to remove duplicate packets, usually like this:</p><p><strong>editcap -d infile.pcap outfile.pcap</strong></p><p>You might need to adjust the additional -D and -w parameters to tell editcap how many packets to consider and what maximum time distance between duplicates you want to allow. The default parameters sometimes do no remove all duplicates, so if that happens, work with -D and -w.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '12, 03:38</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Jan '12, 03:39</p></div></div><div id="comments-container-8501" class="comments-container"><span id="8508"></span><div id="comment-8508" class="comment"><div id="post-8508-score" class="comment-score"></div><div class="comment-text"><p>I have also tried editcap but it has not worked for my traces (maybe because of different vlan tags or the offset caused by vlan-tagging). I do not really know but I could send you a short trace which should show the problem.</p><p>I tried many different editcap-combinations, but editcap is doing no deduplication at all: editcap.exe -d trace1.pcap trace1_filtered.pcap -w 1 -D 100 4780 packets seen, 0 packets skipped with duplicate window of 100 packets.</p><p>Regards, Chris</p></div><div id="comment-8508-info" class="comment-info"><span class="comment-age">(20 Jan '12, 04:39)</span> chris2012</div></div><span id="8509"></span><div id="comment-8509" class="comment"><div id="post-8509-score" class="comment-score"></div><div class="comment-text"><p>The vlan tagging should not be a problem since the same packet in a different vlan means that it must have been routed - and if it has been routed, MAC addresses, TTL etc. are modified, which means it's not a real duplicate (so editcap won't remove it).</p><p>You can send me a short trace if you want, but keep in mind that it should not contain any sensitive data. I created a temporary email alias for this, so send your file to: [email protected]</p></div><div id="comment-8509-info" class="comment-info"><span class="comment-age">(20 Jan '12, 04:51)</span> Jasper ♦♦</div></div><span id="13368"></span><div id="comment-13368" class="comment"><div id="post-13368-score" class="comment-score"></div><div class="comment-text"><p>I have the condition described by Jasper: Different MACs, different TTLs (off by 1), BUT... SAME IP ID. Almost certainly packets that are being routed between VLANs.</p><p>My confusion is... <em>Why does Wireshark note the 2nd of these packets as a Retransmission?</em> Doesn't the condition of identical IP IDs rule out a retransmitted packet?</p><p>(FWIW, I'm running Version 1.6.5 (SVN Rev 40429 from /trunk-1.6) )</p><p>Thanx for any enlightenment :-)</p><p>feenyman99</p></div><div id="comment-13368-info" class="comment-info"><span class="comment-age">(05 Aug '12, 06:05)</span> feenyman99</div></div><span id="13369"></span><div id="comment-13369" class="comment"><div id="post-13369-score" class="comment-score"></div><div class="comment-text"><p>I haven't looked at the tcp expert analysis code, but I guess it just does not check any layer other than the tcp layer for it's analysis results... so even if the ip id indicates a duplicate the tcp expert ignores it.</p></div><div id="comment-13369-info" class="comment-info"><span class="comment-age">(05 Aug '12, 08:03)</span> Jasper ♦♦</div></div><span id="13374"></span><div id="comment-13374" class="comment"><div id="post-13374-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Why does Wireshark note the 2nd of these packets as a Retransmission? Doesn't the condition of identical IP IDs rule out a retransmitted packet?</p></blockquote><p>Maybe it should, but the code that creates a conversation (which is the base for TCP analysis), does not care about the IP ID, which is O.K. for IP conversations, as IP IDs will change during a conversation.</p><blockquote><p><code>epan\conversation.c:find_or_create_conversation()</code><br />
</p></blockquote><p>for TCP retransmit analysis, the IP ID 'should' be checked, to detect only real retransmits.</p><p>However, it would be some overhead to do that. SRC/DST IP and SRC/DST port will be constant for a TCP conversation, but the IP IDs will change with every packet, so it would cost memory to record all IP IDs of a conversation and it would cost time to check for duplicates. Please bear in mind, that there might be many conversations in a capture file.</p><p>If you think this is a bug, please file a bug report at <a href="http://bugs.wireshark.org">bugs.wireshark.org</a>.</p><p>Regards<br />
Kurt</p></div><div id="comment-13374-info" class="comment-info"><span class="comment-age">(05 Aug '12, 13:58)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-8501" class="comment-tools"></div><div class="clear"></div><div id="comment-8501-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

