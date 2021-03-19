+++
type = "question"
title = "packets shown by tcpdump and wireshark"
description = '''Hi I wanted to check if the sniffer application I&#x27;m using has zero packet loss. For that I have used tcpreplay to send a specific number of packets into the capture port. The number of packets shown by wireshark or tcpdump -r while opening the pcap file does not seem to be the same as the one shown ...'''
date = "2015-07-27T00:07:00Z"
lastmod = "2015-07-27T15:46:00Z"
weight = 44514
keywords = [ "tcpdump", "pcap", "tcpreplay" ]
aliases = [ "/questions/44514" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [packets shown by tcpdump and wireshark](/questions/44514/packets-shown-by-tcpdump-and-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44514-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I wanted to check if the sniffer application I'm using has zero packet loss. For that I have used tcpreplay to send a specific number of packets into the capture port. The number of packets shown by wireshark or tcpdump -r while opening the pcap file does not seem to be the same as the one shown by tcpreplay. Why is that?</p></div><div id="question-tags" class="tags-container tags">tcpdump pcap tcpreplay</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '15, 00:07</strong></p><img src="https://secure.gravatar.com/avatar/5bf5e940f9cb50a96c3ee06e808e5eb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jichu&#39;s gravatar image" /><p>jichu<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jichu has no accepted answers">0%</span></p></div></div><div id="comments-container-44514" class="comments-container"></div><div id="comment-tools-44514" class="comment-tools"></div><div class="clear"></div><div id="comment-44514-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44549"></span>

<div id="answer-container-44549" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44549-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Why is that?</p></blockquote><p>There are many possible reasons:</p><ul><li>packet loss on the network</li><li>packet loss on the switch mirror port (if you were using that)</li><li>packet loss on the sniffer system (high CPU/IO load, etc.)</li><li>bug in tcpreplay and/or Wireshark with the result that one of these shows wrong numbers</li><li>rather unlikely: TCP segment offloading on the sender</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '15, 15:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-44549" class="comments-container"><span id="44551"></span><div id="comment-44551" class="comment"><div id="post-44551-score" class="comment-score"></div><div class="comment-text"><p>Hi, thanks for the reply.. I checked with "iperf" there is no loss in network, and I use ESXi Virtual switch for the system, I don't think packet loss happens there. The sniffer software I use (netsniff-ng) shows no packet loss, so only option left is a bug and/or TCP segmentation offloading</p></div><div id="comment-44551-info" class="comment-info"><span class="comment-age">(28 Jul '15, 00:04)</span> jichu</div></div><span id="44552"></span><div id="comment-44552" class="comment"><div id="post-44552-score" class="comment-score"></div><div class="comment-text"><p>So what Guest OS are you using where you run tcpreplay?</p></div><div id="comment-44552-info" class="comment-info"><span class="comment-age">(28 Jul '15, 00:20)</span> Christian_R</div></div><span id="44553"></span><div id="comment-44553" class="comment"><div id="post-44553-score" class="comment-score"></div><div class="comment-text"><p>I use Ubuntu Server 14.04 LTS for both sniffer and for tcpreplay</p></div><div id="comment-44553-info" class="comment-info"><span class="comment-age">(28 Jul '15, 00:50)</span> jichu</div></div><span id="44554"></span><div id="comment-44554" class="comment"><div id="post-44554-score" class="comment-score"></div><div class="comment-text"><p>Have you checked the counters with ifcongig or ethtool -S?</p></div><div id="comment-44554-info" class="comment-info"><span class="comment-age">(28 Jul '15, 01:00)</span> Christian_R</div></div><span id="44555"></span><div id="comment-44555" class="comment"><div id="post-44555-score" class="comment-score"></div><div class="comment-text"><p>Yes, no packet drops shown in ifconfig eth1 and ethtool -s eth1 command</p></div><div id="comment-44555-info" class="comment-info"><span class="comment-age">(28 Jul '15, 01:13)</span> jichu</div></div><span id="44556"></span><div id="comment-44556" class="comment not_top_scorer"><div id="post-44556-score" class="comment-score"></div><div class="comment-text"><p>And tcpreplay shows more packets transmitted correctly then the tcpdump output? Is it still reproduceable?</p></div><div id="comment-44556-info" class="comment-info"><span class="comment-age">(28 Jul '15, 01:16)</span> Christian_R</div></div><span id="44557"></span><div id="comment-44557" class="comment not_top_scorer"><div id="post-44557-score" class="comment-score"></div><div class="comment-text"><p>Yes thats correct. I'm running one now, when its completed I can post the output</p></div><div id="comment-44557-info" class="comment-info"><span class="comment-age">(28 Jul '15, 01:39)</span> jichu</div></div><span id="44559"></span><div id="comment-44559" class="comment not_top_scorer"><div id="post-44559-score" class="comment-score"></div><div class="comment-text"><p>Hi</p><p>TCP replay output:</p><p>Actual: 612469500 packets (305393106000 bytes) sent in 10685.58 seconds. Rated: 28579928.0 bps, 218.05 Mbps, 57317.38 pps Statistics for network device: eth1 Attempted packets: 612469500 Successful packets: 612469500 Failed packets: 0 Retried packets (ENOBUFS): 0 Retried packets (EAGAIN): 0</p><p>Sum of all tcpdump -r output (using a script): 48861713</p><p>The script is used is :</p><p>#!/bin/bash<br />
files=(/share/capture/job2/*.pcap) sum=0 for f in "${files[@]}" do output=<code>sudo tcpdump -r $f 2&gt; /dev/null | wc -l</code> sum=$((output + sum)) done echo $sum</p></div><div id="comment-44559-info" class="comment-info"><span class="comment-age">(28 Jul '15, 04:00)</span> jichu</div></div><span id="44560"></span><div id="comment-44560" class="comment not_top_scorer"><div id="post-44560-score" class="comment-score"></div><div class="comment-text"><p>And what does capinfo tell you?</p></div><div id="comment-44560-info" class="comment-info"><span class="comment-age">(28 Jul '15, 04:35)</span> Christian_R</div></div><span id="44561"></span><div id="comment-44561" class="comment not_top_scorer"><div id="post-44561-score" class="comment-score"></div><div class="comment-text"><p>Same as tcpdump -r</p></div><div id="comment-44561-info" class="comment-info"><span class="comment-age">(28 Jul '15, 04:45)</span> jichu</div></div><span id="44575"></span><div id="comment-44575" class="comment not_top_scorer"><div id="post-44575-score" class="comment-score"></div><div class="comment-text"><p>Maybe it is something like that (as Kurt already noticed): <strong>packet loss on the sniffer system (high CPU/IO load, etc.)</strong></p><p>And the difference is that Iperf and tcpreplay sends out the packets in different wave forms.</p></div><div id="comment-44575-info" class="comment-info"><span class="comment-age">(28 Jul '15, 13:05)</span> Christian_R</div></div></div><div id="comment-tools-44549" class="comment-tools"><span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a></div><div class="clear"></div><div id="comment-44549-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

