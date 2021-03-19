+++
type = "question"
title = "packet misses at high incoming packet rates"
description = '''Hi, I am testing our own Ethernet Controller board. We have support for RGMII 1000Mbps and I am  generating Etherent packets at a high rate of 850Mbps. The set-up I use to test is the following. I have my board connected to Windows PC running Wireshark. It is a direct link through an Ethernet cable,...'''
date = "2016-03-02T22:29:00Z"
lastmod = "2016-03-03T00:19:00Z"
weight = 50696
keywords = [ "high", "rate", "1000mbps", "packet" ]
aliases = [ "/questions/50696" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [packet misses at high incoming packet rates](/questions/50696/packet-misses-at-high-incoming-packet-rates)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50696-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50696-score" class="post-score" title="current number of votes">0</div><span id="post-50696-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am testing our own Ethernet Controller board. We have support for RGMII 1000Mbps and I am generating Etherent packets at a high rate of 850Mbps.</p><p>The set-up I use to test is the following. I have my board connected to Windows PC running Wireshark. It is a direct link through an Ethernet cable, with no switch/router in between.</p><p>Our board generates Etherent packets at the high rate of 850Mbps, however, at the Wrireshark end, I see that all the packets are not received. When I send around 100 packets at 850Mbps - all packets are received at Wireshrk and displayed in the Wireshark window. However, if I send around 10,000 packets at 850Mbps - only around 8000 packets are received and displayed by Wireshark.</p><p>Is there any known restriction for Wireshrk at this high rate of packets? Has anybody faced similar issues?</p><p>I have tested transmission-reception between two of our boards, and all the packets are received. Hence this rules out any issues related to our boards.</p><p>Regards, Vineetha</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-high" rel="tag" title="see questions tagged &#39;high&#39;">high</span> <span class="post-tag tag-link-rate" rel="tag" title="see questions tagged &#39;rate&#39;">rate</span> <span class="post-tag tag-link-1000mbps" rel="tag" title="see questions tagged &#39;1000mbps&#39;">1000mbps</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Mar '16, 22:29</strong></p><img src="https://secure.gravatar.com/avatar/f8f902d061b471173765fe5dfa1e8b52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vineetha&#39;s gravatar image" /><p><span>Vineetha</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vineetha has no accepted answers">0%</span></p></div></div><div id="comments-container-50696" class="comments-container"></div><div id="comment-tools-50696" class="comment-tools"></div><div class="clear"></div><div id="comment-50696-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50698"></span>

<div id="answer-container-50698" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50698-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50698-score" class="post-score" title="current number of votes">0</div><span id="post-50698-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The issue isn't just with Wireshark, it's the capture mechanism (probably WinPcap as you're running Windows) and the I/O capabilities of your PC (disk, memory, NIC).</p><p>Wireshark does dissection as well as capture (and updates a GUI as well), so isn't the best choice for high speed captures, dumpcap, part of the Wireshark suite, is the actual capturing process so using that may help.</p><p>Even if you use dumpcap, I don't think standard commodity PC hardware and software can reliably capture at those rates. To do that you're probably looking at specialised capture hardware, e.g <a href="http://gb.riverbed.com/products/performance-management-control/network-performance-management/network-troubleshooting.html">SteelCentral Netshark</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Mar '16, 00:19</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-50698" class="comments-container"></div><div id="comment-tools-50698" class="comment-tools"></div><div class="clear"></div><div id="comment-50698-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

