+++
type = "question"
title = "Wireshark won&#x27;t capture packets unless another pcap app is running"
description = '''Hi, Wierd problem. I&#x27;m trying to debug a monitoring app I have written which is capturing a lot of udp traffic. My app is losing 1-2% of the packets I expect to see, so I ran wireshark to identify if the expected number of packets is arriving at the machine. But wireshark doesn&#x27;t see any of the pack...'''
date = "2014-06-02T05:25:00Z"
lastmod = "2014-06-02T06:49:00Z"
weight = 33270
keywords = [ "and", "pcap", "wireshark" ]
aliases = [ "/questions/33270" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark won't capture packets unless another pcap app is running](/questions/33270/wireshark-wont-capture-packets-unless-another-pcap-app-is-running)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33270-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Wierd problem. I'm trying to debug a monitoring app I have written which is capturing a lot of udp traffic. My app is losing 1-2% of the packets I expect to see, so I ran wireshark to identify if the expected number of packets is arriving at the machine. But wireshark doesn't see any of the packets I am expecting until I run my monitoring app at the same time. Debugging my app, wireshark appears to burst into life when my app calls the pcap librarys open function, which is called with pretty standard variables I'm not using any display or capture filters, the lights on the hardware are flashing all the time, I can't understand why wireshark isn't seeing the traffic until another app opens the port.</p><p>TIA</p><p>Paul</p></div><div id="question-tags" class="tags-container tags">and pcap wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jun '14, 05:25</strong></p><img src="https://secure.gravatar.com/avatar/661c1dd7e522fadf3b1c00ae0bf144eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="roccap&#39;s gravatar image" /><p>roccap<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="roccap has no accepted answers">0%</span></p></div></div><div id="comments-container-33270" class="comments-container"><span id="33285"></span><div id="comment-33285" class="comment"><div id="post-33285-score" class="comment-score"></div><div class="comment-text"><p>what is your</p><ul><li>OS and OS version</li><li>Wireshark version</li></ul><p>How did you</p><ul><li>install Wireshark</li><li>install WinPcap, if your OS is Windows</li><li>start Wireshark</li></ul></div><div id="comment-33285-info" class="comment-info"><span class="comment-age">(02 Jun '14, 08:23)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-33270" class="comment-tools"></div><div class="clear"></div><div id="comment-33270-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33276"></span>

<div id="answer-container-33276" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33276-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Is your other app putting the port into promiscuous mode? Have you checked that option in the Wireshark UI?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '14, 06:49</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-33276" class="comments-container"><span id="33281"></span><div id="comment-33281" class="comment"><div id="post-33281-score" class="comment-score"></div><div class="comment-text"><p>The promiscuous option is set in the GUI. Interestingly, running tcpdump will also cause wireshark to start acquiring packets.</p></div><div id="comment-33281-info" class="comment-info"><span class="comment-age">(02 Jun '14, 07:37)</span> roccap</div></div><span id="33284"></span><div id="comment-33284" class="comment"><div id="post-33284-score" class="comment-score"></div><div class="comment-text"><p>Unsetting the option, doing a capture then unsetting and resetting the option appears to do the trick. Thanks Paul</p></div><div id="comment-33284-info" class="comment-info"><span class="comment-age">(02 Jun '14, 08:20)</span> roccap</div></div></div><div id="comment-tools-33276" class="comment-tools"></div><div class="clear"></div><div id="comment-33276-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

