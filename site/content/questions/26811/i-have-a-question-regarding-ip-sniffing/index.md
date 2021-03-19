+++
type = "question"
title = "I have a question regarding ip sniffing"
description = '''When trying to sniff ips on my network, I am not displayed with their ips, but the names of the network instead. Here is a picture --&amp;gt; http://tinypic.com/r/5ww2n9/5 if anyone can help me make it so that i can see the different ips, that would be awesome. Im sniffing through En1 (wirelessly) i had...'''
date = "2013-11-09T21:54:00Z"
lastmod = "2013-11-09T22:48:00Z"
weight = 26811
keywords = [ "sniffing", "ip", "wireshark", "port", "network" ]
aliases = [ "/questions/26811" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [I have a question regarding ip sniffing](/questions/26811/i-have-a-question-regarding-ip-sniffing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26811-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When trying to sniff ips on my network, I am not displayed with their ips, but the names of the network instead. Here is a picture --&gt; <a href="http://tinypic.com/r/5ww2n9/5">http://tinypic.com/r/5ww2n9/5</a> if anyone can help me make it so that i can see the different ips, that would be awesome. Im sniffing through En1 (wirelessly) i had it working a while back, but i assume i accidentally did something to screw it up. Thanks a ton</p></div><div id="question-tags" class="tags-container tags">sniffing ip wireshark port network</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Nov '13, 21:54</strong></p><img src="https://secure.gravatar.com/avatar/cf1e3b412882ac3a1ae0b980b65cf128?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spinz&#39;s gravatar image" /><p>spinz<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spinz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Nov '13, 21:55</p></div></div><div id="comments-container-26811" class="comments-container"></div><div id="comment-tools-26811" class="comment-tools"></div><div class="clear"></div><div id="comment-26811-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26812"></span>

<div id="answer-container-26812" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26812-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>When trying to sniff ips on my network</p></blockquote><p>Is your network [an Ethernet segment plugged into a Cisco Cable Modem Termination System in order to snoop DOCSIS (networking over cable TV) traffic]?</p><p>If not, then turn off the "Treat all frames as DOCSIS frames" preference for the Ethernet dissector, and don't select DOCSIS as a link-layer header type when capturing on Ethernet.</p><blockquote><p>i assume i accidentally did something to screw it up</p></blockquote><p>You probably either turned "Treat all frames as DOCSIS frames" on or captured with DOCSIS specified as the link-layer header type.</p><p>If you did the first of those, turning the option off should be sufficient.</p><p>If you did the latter, the capture file has the wrong link-layer header type, but you could fix it by running the command</p><pre><code>editcap -T ether {the bad file&#39;s path name} {a file name to write to}</code></pre><p>and then renaming the output file on top of the input file. (You <em>did</em> install the command-line tools when installing Wireshark, right? If not, do so.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '13, 22:48</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-26812" class="comments-container"><span id="26898"></span><div id="comment-26898" class="comment"><div id="post-26898-score" class="comment-score"></div><div class="comment-text"><p>hi thank you so much for your reply. I turned off "treat all frames as docsis frames," but I am still not seeing the ips. here is a picture of my capture.... <a href="http://tinypic.com/r/126fais/5">http://tinypic.com/r/126fais/5</a></p></div><div id="comment-26898-info" class="comment-info"><span class="comment-age">(12 Nov '13, 07:11)</span> spinz</div></div><span id="26903"></span><div id="comment-26903" class="comment"><div id="post-26903-score" class="comment-score"></div><div class="comment-text"><p>OK, you're now capturing in monitor mode, so you're seeing raw 802.11 frames as they appear on the air (and you see non-data frames, such as beacons, which don't <em>have</em> IP addresses), and you're probably capturing on a protected network (using WEP or WPA/WPA2), which means the frames you capture are <em>encrypted</em>, and to see their contents - including the IP headers! - you'd need to give Wireshark enough information to decrypt them.</p><p>Either don't check the "Monitor mode" box for the interface, in which case you'll only capture traffic to and from your machine but you'll get decrypted data, or follow the <a href="http://wiki.wireshark.org/HowToDecrypt802.11">"how to decrypt 802.11"</a> instructions, in which case you'll see other traffic on your network (although, if you're on a WPA/WPA2 network, you might have to disconnect and reconnect other machines after you start capturing if you want to decrypt their traffic, as you'd need to force them to do the initial "EAPOL handshake").</p></div><div id="comment-26903-info" class="comment-info"><span class="comment-age">(12 Nov '13, 13:23)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-26812" class="comment-tools"></div><div class="clear"></div><div id="comment-26812-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

