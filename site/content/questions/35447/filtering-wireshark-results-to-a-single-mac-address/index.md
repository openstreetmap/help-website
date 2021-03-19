+++
type = "question"
title = "Filtering Wireshark Results to a single MAC Address"
description = '''Ok, So let me explain the reason, I am using Wireshark. I am currently running CentOS 6.5 64-bit in Virtualbox with a Bridge Connection to my external WLAN USB Adapter. As of now, The only way I can get an IP is by having a wired connect, but that is kinda a pain when I am using a laptop. I&#x27;ve alrea...'''
date = "2014-08-12T20:52:00Z"
lastmod = "2014-08-13T01:00:00Z"
weight = 35447
keywords = [ "filter", "mac", "centos", "virtualbox" ]
aliases = [ "/questions/35447" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Filtering Wireshark Results to a single MAC Address](/questions/35447/filtering-wireshark-results-to-a-single-mac-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35447-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Ok, So let me explain the reason, I am using Wireshark.</p><p>I am currently running CentOS 6.5 64-bit in Virtualbox with a Bridge Connection to my external WLAN USB Adapter.</p><p>As of now, The only way I can get an IP is by having a wired connect, but that is kinda a pain when I am using a laptop.</p><p>I've already asked on Virtualbox Forum and they can see nothing wrong with the configuration.</p><p>I am wanting to use Wireshark to see how far the CentOS is "supposedly reaching" before failing to retrieve an IP.</p><p>I have Wireshark open and running but I need to filter the results by the MAC Address of the CentOS Guest Operating System. I've searched through the Internet, and the help pages, but cannot find the proper command.</p><p>Can someone explain how I could filter please?</p><p>If this is already posted, I was not able to find said article and would appreciate it if someone would let me know.</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">filter mac centos virtualbox</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Aug '14, 20:52</strong></p><img src="https://secure.gravatar.com/avatar/4259fa14f327d7f7a6198d16555aae1f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="countryboy01&#39;s gravatar image" /><p>countryboy01<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="countryboy01 has no accepted answers">0%</span></p></div></div><div id="comments-container-35447" class="comments-container"></div><div id="comment-tools-35447" class="comment-tools"></div><div class="clear"></div><div id="comment-35447-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35449"></span>

<div id="answer-container-35449" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35449-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Capturing on the bridged interface of Virtualbox does not work properly. We have had several reports in the past.</p><p>Please run tcpdump in the virtual machine (CentOS) and only use Wireshark to analyze the traffic.</p><blockquote><p>tcpdump -ni eth0 -s 0 -w /var/tmp/dhcp.pcap</p></blockquote><p>Then run the command <strong>dhclient</strong> in CentOS. After a few seconds stop the tcpdump and check what you've got.</p><p>If that does not work, try to capture on the ethernet/wireless interface of your Virtualbox host, <strong>not</strong> the bridged interface!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '14, 01:00</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-35449" class="comments-container"></div><div id="comment-tools-35449" class="comment-tools"></div><div class="clear"></div><div id="comment-35449-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

