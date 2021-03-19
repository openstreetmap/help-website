+++
type = "question"
title = "How to determine which NIC is being used ?"
description = '''I have 3 NICs in a windows box. NIC1 local network. NIC2 slow ISP. NIC3 fast ISP. What I am trying to do: Capture a couple of thousand packets from all 3 NICs. Then look at a packet that I am interested in and see which NIC is being used. Example I see a packet with the source address of a pc on my ...'''
date = "2013-07-23T07:52:00Z"
lastmod = "2013-07-23T08:35:00Z"
weight = 23287
keywords = [ "dual-nic" ]
aliases = [ "/questions/23287" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to determine which NIC is being used ?](/questions/23287/how-to-determine-which-nic-is-being-used)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23287-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have 3 NICs in a windows box. NIC1 local network. NIC2 slow ISP. NIC3 fast ISP.</p><p>What I am trying to do: Capture a couple of thousand packets from all 3 NICs. Then look at a packet that I am interested in and see which NIC is being used.</p><p>Example I see a packet with the source address of a pc on my lan. Which NIC is it using to connect to the internet?</p><p>Reason for this: 1 I want to make some of the lan use the slow NIC and the rest to use the fast NIC. 2 Geeky frustration, I believe I should be able to use wireshark to find out the information I want but I am unable to work out how.</p><p>To solve my some lan to slow NIC problem I think I need to use a static route but AFAIK that relies on destination IP not source IP? If any one can help me out with either of these points, it would save me from continuing to have a headache :)</p></div><div id="question-tags" class="tags-container tags">dual-nic</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jul '13, 07:52</strong></p><img src="https://secure.gravatar.com/avatar/49d81170eb8d1b6646f6c3197a94b1f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="apaseall&#39;s gravatar image" /><p>apaseall<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="apaseall has no accepted answers">0%</span></p></div></div><div id="comments-container-23287" class="comments-container"></div><div id="comment-tools-23287" class="comment-tools"></div><div class="clear"></div><div id="comment-23287-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23290"></span>

<div id="answer-container-23290" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23290-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you're capturing on the PC on all three interfaces with a single Wireshark instance at the same time, <strong>and</strong> using PCAPng as capture file format, Wireshark (actually, dumpcap) will keep the interface index used to capture each frame as an integer in the header of each frame. Which you can filter on, or create a column for. Just take a look at the first layer of your packets, and you'll see a line telling you the interface index. On that you can use the popup menu to filter on the number, or also to apply it as a column.</p><p>If you're not capturing at the same time, or not on the PC itself, or not using PCAPng, you can try to determine the NIC by looking at the MAC the frame was send with. Using IP addresses of the cards will very often not help because Windows is notorious for sending packets on NICs other than the one holding a specific IP in case the NICs are all in the same subnet. Going by MAC should work though.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '13, 08:35</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-23290" class="comments-container"><span id="23291"></span><div id="comment-23291" class="comment"><div id="post-23291-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper for the reply. I am indeed using wireshark on the pc with all three cards. I captured a couple of thousand packets from all three interfaces at once.</p><p>I am not sure what PCAPng is.</p><p>I saw the interface index but that is just a number. I tried to find another part of wireshark that would let me know which NIC that number corresponded to failed :(</p><p>As for the MAC addresses, I tried looking for them but could not find any that corresponded to any of the known MACs I have. ie not for the 3 NICs in the box, or the switch (connected to NIC1 to get lan) nor the client PC.</p></div><div id="comment-23291-info" class="comment-info"><span class="comment-age">(23 Jul '13, 08:45)</span> apaseall</div></div><span id="23292"></span><div id="comment-23292" class="comment"><div id="post-23292-score" class="comment-score"></div><div class="comment-text"><p>I converted your comment to a comment.</p><p>I see. "PCAPng" is a file format, which is automatically used since Wireshark 1.8 or later. You can usually tell by the file extension ".pcapng", or by just using the "File Open" dialog which will show you the format in the lower right pane.</p><p>Regarding the interface indexes - try opening the "Summary" in the statistics menu. It will list all capture interfaces that were captured on in the current trace. Usually the first line is interface id 0, the second is id 1 and so on. Note the GUID of the interface (the number in the curly brackets), which is the unique identifier the OS uses to identify the card.</p><p>Run a command prompt, and type "getmac". It should give you a list of MAC addresses and transport names, with the same GUIDs as you saw in the summary statistics. With that you can map the capture cards to the MACs. With "ipconfig /all" you can map the MACs to the IPs.</p><p>Let me know if I'm going to fast and I'll explain the steps in greater detail.</p></div><div id="comment-23292-info" class="comment-info"><span class="comment-age">(23 Jul '13, 09:04)</span> Jasper ♦♦</div></div><span id="23301"></span><div id="comment-23301" class="comment"><div id="post-23301-score" class="comment-score"></div><div class="comment-text"><p>New to this forum so thanks for converting to a comment.</p><p>I had not saved the capture. Now I see what the PCAPng is :)</p><p>I try and stay away from GUIDs, which I guess is the reason they are so long.</p><p>Getmac is a new one for me :) I now have a pile of numbers associated with each NIC (MAC, GUID, IPV4 address, IPV6 address plus the ISP boxes IPV4 address and IPV6 address). Think that should give me something to use whilst looking at the capture.</p><p>I'm keeping up so far, going to take a while away from looking into this. Might even be tomorrow before I can sit down with a clear head. I'll let you know how I go on, once I have another bash at it.</p></div><div id="comment-23301-info" class="comment-info"><span class="comment-age">(23 Jul '13, 10:18)</span> apaseall</div></div><span id="23303"></span><div id="comment-23303" class="comment"><div id="post-23303-score" class="comment-score"></div><div class="comment-text"><p>Sure, take your time ;-)</p></div><div id="comment-23303-info" class="comment-info"><span class="comment-age">(23 Jul '13, 11:02)</span> Jasper ♦♦</div></div><span id="23335"></span><div id="comment-23335" class="comment"><div id="post-23335-score" class="comment-score"></div><div class="comment-text"><p>I have side stepped the issue for now. I think I understand now how to solve the issue if I need to go back to it.</p><p>My solution: NIC3 has the lowest automatic metric. Use NAT with NIC1 internal with NIC2 and NIC3 public. Enter static route to NIC2 for known destination. Basically I went and found out the IP range of the destination I wanted the client to use NIC2 with.</p><p>Ugly solution in my mind as what I really want is to split NIC2 and NIC3 usage on LAN IP not destination addresses.</p></div><div id="comment-23335-info" class="comment-info"><span class="comment-age">(24 Jul '13, 10:23)</span> apaseall</div></div></div><div id="comment-tools-23290" class="comment-tools"></div><div class="clear"></div><div id="comment-23290-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

