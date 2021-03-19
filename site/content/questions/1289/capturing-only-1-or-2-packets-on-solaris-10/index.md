+++
type = "question"
title = "Capturing only 1 or 2 packets on Solaris 10"
description = '''Hello, I have a Solaris 10 machine with a 4-port ethernet card on which I just installed Wireshark. The problem I&#x27;m having is kind of weird. Basically, I&#x27;m not capturing any packets on the network interface which I&#x27;m testing by just pinging another machine on the network. But if I leave the capture ...'''
date = "2010-12-08T13:02:00Z"
lastmod = "2010-12-08T13:02:00Z"
weight = 1289
keywords = [ "packets", "solaris", "wireshark" ]
aliases = [ "/questions/1289" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing only 1 or 2 packets on Solaris 10](/questions/1289/capturing-only-1-or-2-packets-on-solaris-10)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1289-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have a Solaris 10 machine with a 4-port ethernet card on which I just installed Wireshark. The problem I'm having is kind of weird. Basically, I'm not capturing any packets on the network interface which I'm testing by just pinging another machine on the network. But if I leave the capture running and I start an extended ping it will capture 1 of 2 packets (the request, the reply, or both) and that is all. The ping is works correctly as I can see in the terminal window but Wireshark just stops capturing. Any ideas?</p><p>I'll just throw this out there if why I'm trying to capture packets. Maybe someone has a inkling to what is going on. From the Solaris box I'm trying to ping a device with 9216 byte packets. The ping is not successful. I can ping the device with packets up to 1470 bytes and after that, the ping doesn't work anymore. I've then added my windows laptop to the network and have tried to ping the device with 9216 byte packets and it works fine. I can also ping the Solaris box with 9216 byte packets. Then I have another device that requires 9216 byte packets which I can successfully ping from the Solaris box.</p><p>Any help would be appreciated. Thank you.</p></div><div id="question-tags" class="tags-container tags">packets solaris wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Dec '10, 13:02</strong></p><img src="https://secure.gravatar.com/avatar/b9243ba350d9aa5abf33b60340cdfc87?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gregory%20Berry&#39;s gravatar image" /><p>Gregory Berry<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gregory Berry has no accepted answers">0%</span></p></div></div><div id="comments-container-1289" class="comments-container"><span id="3184"></span><div id="comment-3184" class="comment"><div id="post-3184-score" class="comment-score"></div><div class="comment-text"><p>What is the MTU of the interface that the Solaris box is connected to?</p></div><div id="comment-3184-info" class="comment-info"><span class="comment-age">(28 Mar '11, 14:19)</span> cmaynard ♦♦</div></div><span id="3191"></span><div id="comment-3191" class="comment"><div id="post-3191-score" class="comment-score"></div><div class="comment-text"><p>Which int are you capturing on? Is there LACP or some bonding going on? Is the default GW changing somehow (like you're running RIP with a router?)? Is your subnet mask set correctly? Perhaps the interfaces are getting confused because the router is proxy arp'ing for you? Finally, jumbo frames must be supported end to end. So first troubleshoot with 1400 byte packets and mix in the jumbo frames after you're successful with 1400 byte frames. I know I asked a bunch of questions, but I think you're missing something in your description of the problem...so I wanted to cover all bases.</p></div><div id="comment-3191-info" class="comment-info"><span class="comment-age">(28 Mar '11, 18:39)</span> hansangb</div></div></div><div id="comment-tools-1289" class="comment-tools"></div><div class="clear"></div><div id="comment-1289-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

