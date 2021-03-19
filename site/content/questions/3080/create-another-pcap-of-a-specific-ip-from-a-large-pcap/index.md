+++
type = "question"
title = "Create another PCAP of a specific IP from a large PCAP"
description = '''Hi, Actually, am caught up in a flux and was looking for some help.  I have a 1 GB file with data from multiple IP&#x27;s. I use ngrp to find a particular keyword in the file and then find the source IP and destination IP of that packet where the keyword was present. I then used tshark and the found IP&#x27;s...'''
date = "2011-03-24T07:28:00Z"
lastmod = "2011-03-27T03:43:00Z"
weight = 3080
keywords = [ "python", "packets", "pcap", "tshark", "dump" ]
aliases = [ "/questions/3080" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Create another PCAP of a specific IP from a large PCAP](/questions/3080/create-another-pcap-of-a-specific-ip-from-a-large-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3080-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Actually, am caught up in a flux and was looking for some help.</p><p>I have a 1 GB file with data from multiple IP's. I use ngrp to find a particular keyword in the file and then find the source IP and destination IP of that packet where the keyword was present. I then used tshark and the found IP's to create another PCAP from the large PCAP of packets of only the communication between those two IP's. However, when I run my Python script to decode the created PCAP file, it does not give any results. While the same script on the original PCAP gives results. I have tried multiple options but nothing seems to give me the right results. Can you suggest a method to help me with this problem? Would be really grateful</p><p>Best regards,</p></div><div id="question-tags" class="tags-container tags">python packets pcap tshark dump</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Mar '11, 07:28</strong></p><img src="https://secure.gravatar.com/avatar/b6ced69daaca6b894f8fad8179b8ac48?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John%20Major&#39;s gravatar image" /><p>John Major<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John Major has no accepted answers">0%</span></p></div></div><div id="comments-container-3080" class="comments-container"><span id="3084"></span><div id="comment-3084" class="comment"><div id="post-3084-score" class="comment-score"></div><div class="comment-text"><p>I guess you used tshark like this:</p><p>tshark -r 1gb-file.pcap -R "ip.addr == 1.2.3.4 and ip.addr == 2.3.4.5" -w just-2-stations.pcap</p></div><div id="comment-3084-info" class="comment-info"><span class="comment-age">(24 Mar '11, 09:50)</span> packethunter</div></div></div><div id="comment-tools-3080" class="comment-tools"></div><div class="clear"></div><div id="comment-3080-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3149"></span>

<div id="answer-container-3149" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3149-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>I guess your filter is the problem:</p><blockquote><p><em>Actually I used a little different version of this. I user "ip.src == 1.2.3.4 and ip.dest == 2.3.4.5" or "ip.src == 2.3.4.5" and "ip.dest == 1.2.3.4"</em></p></blockquote><p>If you do it like that you will probably get zero packets, resulting in an empty file (well, it'll have 24 bytes for pcap file headers, but not a single frame). The reason for it is in the way Wireshark prefers "and" and "or" statements when there are no brackets to prioritize - I'm not 100% sure but I think the way Wireshark parsed your statement is like this:</p><pre><code>ip.src == 1.2.3.4 and (ip.dest == 2.3.4.5 or ip.src == 2.3.4.5) and ip.dest == 1.2.3.4</code></pre><p>That way you ended up with the filter requesting both IP source and destination to be the same IP, which of course never matched. You need to either use packethunter's syntax for filtering, or put brackets around the "and" blocks like this:</p><pre><code>(ip.src == 1.2.3.4 and ip.dest == 2.3.4.5) or (ip.src == 2.3.4.5 and ip.dest == 1.2.3.4)</code></pre><p>Things for you to do:</p><ol><li>load your 1GB with Wireshark, stop the loading process when you're pretty sure there is at least one packet of the communication loaded <strong>but before</strong> Wireshark runs into an out of memory situation.</li><li>If you can't do that build your filter with existing, substituted IP addresses and change them back for the real filtering later.</li><li>Test your display filter to give you the results you want for the complete file. If you <strong>know</strong> that there is at least one packet that should be displayed but isn't you got your display filter syntax wrong.</li><li>Use tshark with the working filter</li><li>Check the file size: if it is only 24 bytes you created another "empty" pcap file with zero packets, meaning your filter didn't match anything (and your python script won't find anything)</li><li>Run your python script.</li></ol><p>P.S: next time just comment your question again to bring it back up to anyone's attention if you're wondering why there is no further answer. Trying to email me for private help isn't the exact idea of this Q&amp;A forum - others might be interested in the answers, too ;-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '11, 03:43</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-3149" class="comments-container"></div><div id="comment-tools-3149" class="comment-tools"></div><div class="clear"></div><div id="comment-3149-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3099"></span>

<div id="answer-container-3099" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3099-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Actually I used a little different version of this. I user "ip.src == 1.2.3.4 and ip.dest == 2.3.4.5" or "ip.src == 2.3.4.5" and "ip.dest == 1.2.3.4"</p><p>This way I was trying to capture the entire communication between only two IP's from a host of IP's. Yet, the formed PCAP has some segmentation fault or tcp pur of sequence or malformed packet error. As a result I cant decode it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Mar '11, 23:45</strong></p><img src="https://secure.gravatar.com/avatar/b6ced69daaca6b894f8fad8179b8ac48?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John%20Major&#39;s gravatar image" /><p>John Major<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John Major has no accepted answers">0%</span></p></div></div><div id="comments-container-3099" class="comments-container"></div><div id="comment-tools-3099" class="comment-tools"></div><div class="clear"></div><div id="comment-3099-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

