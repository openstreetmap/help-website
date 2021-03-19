+++
type = "question"
title = "Gratuitous ARP with Multiple Zero Fields"
description = '''We had an event in our network that generated an ARP storm. There were two contributors to this: 1) Gratuitous ARP Requests from VMware: at 09:35:02, we started seeing Gratuitous ARP&#x27;s with Sending Eth MAC of particular VMGuest,  Destination Eth MAC = broadcast (ff&#x27;s) In ARP:  Sender MAC all zeros, ...'''
date = "2016-05-07T09:39:00Z"
lastmod = "2016-05-09T11:24:00Z"
weight = 52295
keywords = [ "arp", "zeros", "vmware", "gratuitous" ]
aliases = [ "/questions/52295" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Gratuitous ARP with Multiple Zero Fields](/questions/52295/gratuitous-arp-with-multiple-zero-fields)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52295-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52295-score" class="post-score" title="current number of votes">0</div><span id="post-52295-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We had an event in our network that generated an ARP storm. There were two contributors to this: 1) Gratuitous ARP Requests from VMware: at 09:35:02, we started seeing Gratuitous ARP's with Sending Eth MAC of particular VMGuest, Destination Eth MAC = broadcast (ff's) In ARP:</p><ul><li>Sender MAC all zeros,</li><li>Sender IP all zeros,</li><li>Target MAC All FF's,</li><li>Target IP all Zeros</li></ul><p>This gradually increased to a very high level from multiple VM Guests across every VLAN that the ESX host has on its trunk. Trying to understand:</p><ul><li>Has anyone seen this before?</li><li>Why are there All zeros in those ARP fields?</li><li>What could generate this traffic?</li></ul><p>2) Once this hit one of our VLAN's, I had GARP Replies from 5 different hosts with his own MAC in Sender MAC but all zeros in the other Sender/Target fields. This huge storm led to a collapse of our older core switches because the ARP storm reached &gt;2GBps. Question on this traffic is: - Why would a host reply to the GARP in this way?</p><p>Packet dissection below for request and reply.<br />
</p><p>Thanks in advance for help.</p><p>-Tim</p><pre><code>GARP Request:
 No.     RelativeTime   Delta Display  Time                          Source                Src Port Destination           vlan_id    Length Info 
2715936 96.183749      0.001018       2016-05-06 09:36:06.341627    Vmware_ac:00:57                Broadcast             2081,127   68     Gratuitous ARP for 0.0.0.0 (Request)
Frame 2715936: 68 bytes on wire (544 bits), 68 bytes captured (544 bits)
    Encapsulation type: Ethernet (1)
    Arrival Time: May  6, 2016 09:36:06.341627000 Eastern Daylight Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1462541766.341627000 seconds
    [Time delta from previous captured frame: 0.000000000 seconds]
    [Time delta from previous displayed frame: 0.001018000 seconds]
    [Time since reference or first frame: 96.183749000 seconds]
    Frame Number: 2715936
    Frame Length: 68 bytes (544 bits)
    Capture Length: 68 bytes (544 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:ethertype:vlan:ethertype:vlan:ethertype:arp]
    [Coloring Rule Name: ARP]
    [Coloring Rule String: arp]
Ethernet II, Src: Vmware_ac:00:57 (00:50:56:ac:00:57), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
    Destination: Broadcast (ff:ff:ff:ff:ff:ff)
        Address: Broadcast (ff:ff:ff:ff:ff:ff)
        .... ..1. .... .... .... .... = LG bit: Locally administered address (this is NOT the factory default)
        .... ...1 .... .... .... .... = IG bit: Group address (multicast/broadcast)
    Source: Vmware_ac:00:57 (00:50:56:ac:00:57)
        Address: Vmware_ac:00:57 (00:50:56:ac:00:57)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Type: 802.1Q Virtual LAN (0x8100)
802.1Q Virtual LAN, PRI: 1, CFI: 0, ID: 2081
    001. .... .... .... = Priority: Background (1)
    ...0 .... .... .... = CFI: Canonical (0)
    .... 1000 0010 0001 = ID: 2081
    Type: 802.1Q Virtual LAN (0x8100)
802.1Q Virtual LAN, PRI: 0, CFI: 0, ID: 127
    000. .... .... .... = Priority: Best Effort (default) (0)
    ...0 .... .... .... = CFI: Canonical (0)
    .... 0000 0111 1111 = ID: 127
    Type: ARP (0x0806)
    Padding: 00000000000000000000
    Trailer: 0000000000000000
Address Resolution Protocol (request/gratuitous ARP)
    Hardware type: Ethernet (1)
    Protocol type: IPv4 (0x0800)
    Hardware size: 6
    Protocol size: 4
    Opcode: request (1)
    [Is gratuitous: True]
    Sender MAC address: 00:00:00_00:00:00 (00:00:00:00:00:00)
    Sender IP address: 0.0.0.0
    Target MAC address: Broadcast (ff:ff:ff:ff:ff:ff)
    Target IP address: 0.0.0.0
GARP Reply:
No.     RelativeTime   Delta Display  Time                          Source                Src Port Destination           Dst Port vlan_id    Length

1571028 0.984442       0.000000       2016-05-06 09:37:23.970442    Netscout_02:ce:e2              00:00:00_00:00:00              2340,228   68     Gratuitous ARP for 0.0.0.0 (Reply)
Frame 1571028: 68 bytes on wire (544 bits), 68 bytes captured (544 bits)
    Encapsulation type: Ethernet (1)
    Arrival Time: May  6, 2016 09:37:23.970442000 Eastern Daylight Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1462541843.970442000 seconds
    [Time delta from previous captured frame: 0.000000000 seconds]
    [Time delta from previous displayed frame: 0.000000000 seconds]
    [Time since reference or first frame: 0.984442000 seconds]
    Frame Number: 1571028
    Frame Length: 68 bytes (544 bits)
    Capture Length: 68 bytes (544 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:ethertype:vlan:ethertype:vlan:ethertype:arp]
    [Coloring Rule Name: ARP]
    [Coloring Rule String: arp]
Ethernet II, Src: Netscout_02:ce:e2 (00:80:8c:02:ce:e2), Dst: 00:00:00_00:00:00 (00:00:00:00:00:00)
    Destination: 00:00:00_00:00:00 (00:00:00:00:00:00)
        Address: 00:00:00_00:00:00 (00:00:00:00:00:00)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Source: Netscout_02:ce:e2 (00:80:8c:02:ce:e2)
        Address: Netscout_02:ce:e2 (00:80:8c:02:ce:e2)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Type: 802.1Q Virtual LAN (0x8100)
802.1Q Virtual LAN, PRI: 1, CFI: 0, ID: 2340
    001. .... .... .... = Priority: Background (1)
    ...0 .... .... .... = CFI: Canonical (0)
    .... 1001 0010 0100 = ID: 2340
    Type: 802.1Q Virtual LAN (0x8100)
802.1Q Virtual LAN, PRI: 0, CFI: 0, ID: 228
    000. .... .... .... = Priority: Best Effort (default) (0)
    ...0 .... .... .... = CFI: Canonical (0)
    .... 0000 1110 0100 = ID: 228
    Type: ARP (0x0806)
    Padding: 00000000000000000000
    Trailer: 0000000000000000
Address Resolution Protocol (reply/gratuitous ARP)
    Hardware type: Ethernet (1)
    Protocol type: IPv4 (0x0800)
    Hardware size: 6
    Protocol size: 4
    Opcode: reply (2)
    [Is gratuitous: True]
    Sender MAC address: Netscout_02:ce:e2 (00:80:8c:02:ce:e2)
    Sender IP address: 0.0.0.0
    Target MAC address: 00:00:00_00:00:00 (00:00:00:00:00:00)
    Target IP address: 0.0.0.0</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-arp" rel="tag" title="see questions tagged &#39;arp&#39;">arp</span> <span class="post-tag tag-link-zeros" rel="tag" title="see questions tagged &#39;zeros&#39;">zeros</span> <span class="post-tag tag-link-vmware" rel="tag" title="see questions tagged &#39;vmware&#39;">vmware</span> <span class="post-tag tag-link-gratuitous" rel="tag" title="see questions tagged &#39;gratuitous&#39;">gratuitous</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '16, 09:39</strong></p><img src="https://secure.gravatar.com/avatar/3f2f87a6a68e4c51c3851c20b6c56a1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CMH_Tim&#39;s gravatar image" /><p><span>CMH_Tim</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CMH_Tim has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 May '16, 19:53</strong> </span></p></div></div><div id="comments-container-52295" class="comments-container"><span id="52296"></span><div id="comment-52296" class="comment"><div id="post-52296-score" class="comment-score"></div><div class="comment-text"><p>Apologize for poor formatting...first time posting - wasn't sure how to maintain clean view.</p><p>PLease advise if repost is needed.</p></div><div id="comment-52296-info" class="comment-info"><span class="comment-age">(07 May '16, 09:40)</span> <span class="comment-user userinfo">CMH_Tim</span></div></div><span id="52302"></span><div id="comment-52302" class="comment"><div id="post-52302-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Jasper for the formatting assist! What button should I have hit?</p></div><div id="comment-52302-info" class="comment-info"><span class="comment-age">(07 May '16, 19:51)</span> <span class="comment-user userinfo">CMH_Tim</span></div></div><span id="52304"></span><div id="comment-52304" class="comment"><div id="post-52304-score" class="comment-score"></div><div class="comment-text"><p>Forget about the buttons as many of the necessary ones are missing. Press "edit" under the Question or Answer post (the page layout is different when editing comments); to the right from the text entry pane with the buttons above, there is another (read-only) one, called "Markdown Basics", with a link to "learn more about Markdown". And look for "code" there.</p><p>Or edit your own Question and see what formatting characters Jasper had to add so that the text would look that way.</p></div><div id="comment-52304-info" class="comment-info"><span class="comment-age">(08 May '16, 01:25)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-52295" class="comment-tools"></div><div class="clear"></div><div id="comment-52295-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52298"></span>

<div id="answer-container-52298" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52298-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52298-score" class="post-score" title="current number of votes">1</div><span id="post-52298-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think that the ARP where the root cause.<br />
I think the broadcast storm is more a follow up. I think you had got a looping network. But some info about that kind of ARP packets can be found here:</p><p><a href="https://crnetpackets.com/2015/08/28/special-type-of-arp-packets/">https://crnetpackets.com/2015/08/28/special-type-of-arp-packets/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '16, 14:10</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span> </br></p></div></div><div id="comments-container-52298" class="comments-container"><span id="52301"></span><div id="comment-52301" class="comment"><div id="post-52301-score" class="comment-score"></div><div class="comment-text"><p>Thanks Christian for the response and the link. My response below:</p><p>1) I believe a loop is a possibility, but we've not found proof of it. I'm scrubbing packets to see if there are any spanning tree changes noted. Nothing in our logs so far indicates any network change that would have suddenly caused us to have a loop and triggered this. Regardless of that outcome, I do still believe that VMWare's packets are not properly formatted.</p><p>2) Maybe I missed it, but that link doesn't show any packet with an all-zeros sender MAC or all-zeros on sender and target IP address. My understanding is that the sender should always put there own MAC at the very least.</p><p>Since posting, I've also confirmed that these packets are NOT actually originating from the guest but are generated by the ESX host (had a local packet capture agent running on some guests during the start of this event that didn't show the GARP packets when my network taps did show them).</p><p>I've done some more research and it appears that this behavior may be related to VMWare's "Notify Switch" setting where it sends a RARP packet when a VMGuest joins the network. This RARP has both sender and target MAC set to the Guest MAC. Here's a reference: <a href="http://rickardnobel.se/vswitch-notify-switches-setting/">http://rickardnobel.se/vswitch-notify-switches-setting/</a> Since original post, I've confirmed the RARP's are there and look correct (also not seen on guest VM capture), but the GARP's are not mentioned in that reference and look wrong to me.</p><p>So I'm working with our design engineers to figure out how a loop could have occurred, but still need answers to my original questions about why the GARP requests and subsequent GARP replies were generated.</p><p>Thanks, Tim</p></div><div id="comment-52301-info" class="comment-info"><span class="comment-age">(07 May '16, 19:51)</span> <span class="comment-user userinfo">CMH_Tim</span></div></div><span id="52305"></span><div id="comment-52305" class="comment"><div id="post-52305-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>still need answers to my original questions about why the GARP requests and subsequent GARP replies were generated</p></blockquote><p>While it is hard to say why the original GARP <strong>requests</strong> have been generated (most likely candidates are mere bug and some malware), I'm afraid that many (if not all) implementations would respond to an ARP request containing</p><pre><code>Target MAC address: Broadcast (ff:ff:ff:ff:ff:ff)
Target IP address: 0.0.0.0</code></pre><p>regardless whether such request has been sent as gratuitous or not. The reason is that 0.0.0.0 normally means "any of my local IPs" in local context (see section 3.2.1.3 of <a href="https://tools.ietf.org/html/rfc1122">RFC 1122</a>, especially the point "must not be sent except as source under specific circumstances").</p><p>So you don't even need a loop, it is enough that all machines on the LAN segment respond to a single broadcast ARP request to have a kind of LAN Smurf Attack.</p></div><div id="comment-52305-info" class="comment-info"><span class="comment-age">(08 May '16, 01:49)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="52320"></span><div id="comment-52320" class="comment"><div id="post-52320-score" class="comment-score"></div><div class="comment-text"><p>Well if I were you, I would go with my findings into the lab and try to get a better understanding of this ARPs and their interaction with the network devices.</p><p>There are so much ARP implementation out there and everyone is a little bit different.</p><p>Let´s assume this is the root cause of your problem! How often can you see these Requests? And does it always tear down the network? And how many hosts will answer? And how long (time) can you see this high BC rate?</p><p>Also a loop could occur without some log entrys. Your link was filled up with &gt;2GBit/s Broadcast -&gt; this is normally done by a loop. How have you stoped this incident?</p><p>But I agree with you and <span></span><span>@sindy</span> this ARP packets looks different to the normal GARPs.</p></div><div id="comment-52320-info" class="comment-info"><span class="comment-age">(08 May '16, 12:12)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="52346"></span><div id="comment-52346" class="comment"><div id="post-52346-score" class="comment-score"></div><div class="comment-text"><p><span>@sindy</span> - Thanks about the replies. That makes sense, although not every device replies like that, of course so I think a lot of implementations are interpreting those as incorrect/not relevant and not responding.<br />
</p><p><span>@Christian_R</span> - We are working with the vendor but not had much luck getting them to figure out why they generate these packets. We do have a low volume still going on without noticeable impact, but I'm concerned that if we hit the VLAN where devices actually respond, we could see minor issues again.</p><p>That being said, I'm fairly certain now that those are a symptom - no matter how strange - but not root cause. As noted below, I'm pretty sure that you were right that the root cause was a loop.</p><p>I did go back into our logs from Friday's event and found a 3750 switch stack that logged MAC flapping shortly <em>after</em> the GARP storm started. The flaps were on its two uplinks to our core switches and contained the MACs of the core switches, so there was some type of loop at that time, just no logs of it before the GARP's. Switch/router engineers took a look but couldn't find any evidence of a loop so Saturday night, we proceeded to bring redundancy back by restarting and reconnecting all links to the 2nd core switch.</p><p>When we brought the 2nd core switch back into the network late Saturday night and began reconnecting the redundant links between the core and edges, all went well until that 3750 stack was connected. Once that happened, we had another GARP storm and same impact as before.</p><p>We have no changes made by anyone on Friday when this happened, but my guess is that something happened that started the loop but nothing got logged. On Saturday's reconnect, we're certain there was no storm before the MAC flaps started again.<br />
</p><p>Thanks again for the help. Would love to hear from someone who could explain those GARP requests.</p></div><div id="comment-52346-info" class="comment-info"><span class="comment-age">(09 May '16, 06:57)</span> <span class="comment-user userinfo">CMH_Tim</span></div></div><span id="52355"></span><div id="comment-52355" class="comment"><div id="post-52355-score" class="comment-score"></div><div class="comment-text"><p>Well here could be found more info for the ARPs:<br />
<a href="https://ask.wireshark.org/questions/5178/why-gratuitous-arps-for-0000">https://ask.wireshark.org/questions/5178/why-gratuitous-arps-for-0000</a><br />
<a href="http://www.cisco.com/c/en/us/support/docs/ios-nx-os-software/8021x/116529-problemsolution-product-00.html">http://www.cisco.com/c/en/us/support/docs/ios-nx-os-software/8021x/116529-problemsolution-product-00.html</a><br />
<a href="https://kb.vmware.com/selfservice/microsites/search.do?language=en_US&amp;cmd=displayKC&amp;externalId=1028373">https://kb.vmware.com/selfservice/microsites/search.do?language=en_US&amp;cmd=displayKC&amp;externalId=1028373</a><br />
But I have not read them all. And I have no real world experience with those special type of ARPs.</p><p>Back to your loop: - Sometimes high CPU Load could cause a loop. - Sometimnes this load could be caused by ARP Storms, when you use managed switches. - Some Spanning Tree configurations might end in high CPU load, too.</p></div><div id="comment-52355-info" class="comment-info"><span class="comment-age">(09 May '16, 11:24)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-52298" class="comment-tools"></div><div class="clear"></div><div id="comment-52298-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

