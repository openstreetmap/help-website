+++
type = "question"
title = "Capturing Bluetooth Profiles - is encryption a problem?"
description = '''Hi, I&#x27;m interested in using Wireshark for sniffing Bluetooth profiles (Bluetooth application data). This data is almost always transferred on an encrypted link setup by default, between two end devices. When the two devices know the BT channel is for a particular profile, they want it encrypted. E.g...'''
date = "2016-03-02T01:08:00Z"
lastmod = "2016-03-02T10:58:00Z"
weight = 50642
keywords = [ "profile", "encryption", "encrypted", "profiles", "bluetooth" ]
aliases = [ "/questions/50642" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing Bluetooth Profiles - is encryption a problem?](/questions/50642/capturing-bluetooth-profiles-is-encryption-a-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50642-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm interested in using Wireshark for sniffing Bluetooth profiles (Bluetooth application data).</p><p>This data is almost always transferred on an encrypted link setup by default, between two end devices. When the two devices know the BT channel is for a particular profile, they want it encrypted. E.g. setting up an AVDTP channel for A2DP. I was wandering if this would be an issue for Wireshark? I know that it has support for a ton of Bluetooth profiles now, but what if the BT link is encrypted? If one is developing on a Bluetooth stack, they can pull the link key information, or even set the device in SSP debug mode prior to pairing/connecting? Does this help?</p><p>Many thanks, Dan</p></div><div id="question-tags" class="tags-container tags">profile encryption encrypted profiles bluetooth</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Mar '16, 01:08</strong></p><img src="https://secure.gravatar.com/avatar/75980d2d29dfec3d2dc59a0cdd507550?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DanRalley&#39;s gravatar image" /><p>DanRalley<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DanRalley has no accepted answers">0%</span></p></div></div><div id="comments-container-50642" class="comments-container"></div><div id="comment-tools-50642" class="comment-tools"></div><div class="clear"></div><div id="comment-50642-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50685"></span>

<div id="answer-container-50685" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50685-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hello,</p><p>Wireshark use libpcap or androiddump to capturing from Bluetooth interfaces what are in real implemented on host side (after processing by controller [Bluetooth chip]), so payload is decrypted in all cases (and often saved in BTSNOOP format).</p><p>But if you have logs from Bluetooth sniffer (from the air), then answer is: there is no decrypting on Wireshark side (but if you need that feature you can fill the bug/enhancement on Wireshark Bugzilla, upload two or more capture files and information needed to decryption [keys, etc.], then it will be implemented). However, in most cases Bluetooth sniffer also decrypting payload so maybe there is nothing to do. As I remember Ubertooth do not decrypt payload right now.</p><p>Summary: If you have Bluetooth USB dongle and capturing from local host interfaces (or USB), then encryption is not a problem (decrypted by controller or host)</p><p>If you have a logs from air sniffer - if sniffer does not decrypt it, then Wireshark does not help you (right now) and you will see "some bytes".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Mar '16, 10:58</strong></p><img src="https://secure.gravatar.com/avatar/6eabf35b1168a8242bb2d69db18a8a7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Micha%C5%82%20%C5%81ab%C4%99dzki&#39;s gravatar image" /><p>Michał Łabędzki<br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michał Łabędzki has one accepted answer">8%</span></p></div></div><div id="comments-container-50685" class="comments-container"><span id="50686"></span><div id="comment-50686" class="comment"><div id="post-50686-score" class="comment-score"></div><div class="comment-text"><p>Hi Michal,</p><p>Thanks for your reply, this has clarified things greatly. If you have dump files from a host stack (libpcap, hcidump etc), as that is already decrypted, Wireshark can abstract the relevant protocol data.</p><p>For me, the greatest use of sniffer traces are from over the air or promiscuous sniffing.</p><p>Out of interest, do you know of any sniffers/plug-ins that have decrypting capabilities? One's that are affordable and not from Frontline/Ellysis?</p><p>This would be a really powerful enhancement, if wireshark could decrypt pcap files generated from open source sniffers like ubertooth. Like I said, giving wireshark the link key or have one device in SSP debug mode, enabling wireshark to decrypt all of the useful profile data.</p><p>At the present time, I want an ubertooth but don't have one. For the Wireshark enhancement to be considered, do you have to have sniffer traces from me, or is there another option for this enhancement to be considered? It will take a while for me to get a working setup and perform some encrypted OTA sniffs.</p><p>Best, Dan</p></div><div id="comment-50686-info" class="comment-info"><span class="comment-age">(02 Mar '16, 11:24)</span> DanRalley</div></div><span id="50687"></span><div id="comment-50687" class="comment"><div id="post-50687-score" class="comment-score"></div><div class="comment-text"><p>Apologies Michal, should have replied here.</p></div><div id="comment-50687-info" class="comment-info"><span class="comment-age">(02 Mar '16, 11:24)</span> DanRalley</div></div><span id="50697"></span><div id="comment-50697" class="comment"><div id="post-50697-score" class="comment-score"></div><div class="comment-text"><p>The problem with Ubertooth is that cannot capture EDR packets, so in most cases there is nothing interesting to decrypt... (for example A2DP). However capture encrypted LE payload is quite easy.</p><p>It is not trivial enhancement so please fill the bug/enhancement on Bugzilla: <a href="https://bugs.wireshark.org/bugzilla/buglist.cgi?limit=0&amp;list_id=23965&amp;order=bug_id%20DESC&amp;query_format=advanced&amp;resolution=---">https://bugs.wireshark.org/bugzilla/buglist.cgi?limit=0&amp;list_id=23965&amp;order=bug_id%20DESC&amp;query_format=advanced&amp;resolution=---</a> And upload capture file, so I can start working on it, because currently I do not have capture files to test, so this enhancement is on my TODO list with low prio. If someone else want to implement it - you are welcome too :)</p><blockquote><p>Out of interest, do you know of any sniffers/plug-ins that have decrypting capabilities? One's that are affordable and not from Frontline/Ellysis?</p></blockquote><p>Nop, as I remember there is no more sniffer then Frontline/Ellysis/Ubertooth/nRF sniffer (LE only). [However tools like HackRF/GNU Radio can be also use to sniffing Bluetooth, but decrypting must be done on userspace]</p></div><div id="comment-50697-info" class="comment-info"><span class="comment-age">(02 Mar '16, 23:20)</span> Michał Łabędzki</div></div><span id="50880"></span><div id="comment-50880" class="comment"><div id="post-50880-score" class="comment-score"></div><div class="comment-text"><p>Thanks Michal,</p><p>Since any BLE connection that doesnt use LE Secure Connections can easily be broken anyway, i'll put this lower on the priority list for now. But i'll put some sniffs together for you to work with shortly.</p><p>I would be happy to provide some BR/EDR decrypted sniffs containing profile data (with link key information provided externally) and try to provide a sniff with one device in SSP debug mode so that you can implement two possible methods of link decryption. However, It sounds like Ubertooth isn't going to help us here so can you recommend some hardware that would allow you to create this enhancement? (unless wireshark can read Frontline CFA files...)</p><p>thanks, Dan</p></div><div id="comment-50880-info" class="comment-info"><span class="comment-age">(14 Mar '16, 02:31)</span> DanRalley</div></div><span id="50881"></span><div id="comment-50881" class="comment"><div id="post-50881-score" class="comment-score"></div><div class="comment-text"><p>To clarify, some hardware that I can use to provide a decent sniff.</p></div><div id="comment-50881-info" class="comment-info"><span class="comment-age">(14 Mar '16, 02:32)</span> DanRalley</div></div><span id="51719"></span><div id="comment-51719" class="comment not_top_scorer"><div id="post-51719-score" class="comment-score"></div><div class="comment-text"><p>Hi Dan,</p><p>Even I would need Ubertooth + Wireshark to look into decrypted HSP profile packets (Rfcomm + SCO/eSCO). Was just curious if you by chance figured out a work around for this? In my case, I am trying to analyze packets between Android Smart phone and COTS headset.</p><p>Do you know if Android's btsnoop_hci.log captures Profile data decrypted?</p><p>Thanks, Manoj</p></div><div id="comment-51719-info" class="comment-info"><span class="comment-age">(16 Apr '16, 18:42)</span> Manoj Prasad</div></div></div><div id="comment-tools-50685" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-50685-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

