+++
type = "question"
title = "Why am I seeing lots of traffic to 224.0.0.22?"
description = '''Why would I see lots of traffic going to Internet Assigned Numbers Authority (224.0.0.22). I am also seeing lots of checksum errors on the TCP packets. Any thoughts? Regards, Jeffrey'''
date = "2011-01-31T07:36:00Z"
lastmod = "2015-10-29T11:11:00Z"
weight = 2039
keywords = [ "troubleshooting" ]
aliases = [ "/questions/2039" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Why am I seeing lots of traffic to 224.0.0.22?](/questions/2039/why-am-i-seeing-lots-of-traffic-to-2240022)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2039-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2039-score" class="post-score" title="current number of votes">0</div><span id="post-2039-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Why would I see lots of traffic going to Internet Assigned Numbers Authority (224.0.0.22). I am also seeing lots of checksum errors on the TCP packets. Any thoughts?</p><p>Regards,</p><p>Jeffrey</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-troubleshooting" rel="tag" title="see questions tagged &#39;troubleshooting&#39;">troubleshooting</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jan '11, 07:36</strong></p><img src="https://secure.gravatar.com/avatar/12d2fadb97a8c80d4fd22e8fbe0aab40?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jeffrey&#39;s gravatar image" /><p><span>Jeffrey</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jeffrey has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Feb '11, 18:37</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-2039" class="comments-container"></div><div id="comment-tools-2039" class="comment-tools"></div><div class="clear"></div><div id="comment-2039-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="2041"></span>

<div id="answer-container-2041" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2041-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2041-score" class="post-score" title="current number of votes">1</div><span id="post-2041-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>224.0.0.22 is the multicast address for Internet Group Management Protocol. This is normal traffic, and it stays on your local network.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jan '11, 08:31</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-2041" class="comments-container"><span id="2042"></span><div id="comment-2042" class="comment"><div id="post-2042-score" class="comment-score"></div><div class="comment-text"><p>OK thanks. How about the bad checksums, almost everyone has an issue. I was also seeing issues with downloaded files being corrupt and also connections constantly being lost with a VPN. Any thoughts?</p></div><div id="comment-2042-info" class="comment-info"><span class="comment-age">(31 Jan '11, 10:14)</span> <span class="comment-user userinfo">Jeffrey</span></div></div><span id="2044"></span><div id="comment-2044" class="comment"><div id="post-2044-score" class="comment-score"></div><div class="comment-text"><p>If you are capturing on one of the end hosts involved in the communication, then the bad checksums are probably caused by TCP checksum offload. When TCP checksum offload is enabled, calculation of the TCP checksum is done by the NIC driver software, rather than by the computer's CPU. Wireshark sees the packet before it's passed to the NIC driver, so the checksum has not yet been calculated, which results in the error. The correct checksum is calculated before the packet is put on the wire. In this case, the checksum isn't really bad, and the error is cosmetic.</p><p>If this is the case, you can eliminate the error display in one of two ways:</p><ol><li><p>Disable TCP checksum offload in the NIC driver. This will force the TCP checksum to be calculated by the computer before the packet is passed to the NIC driver,so Wireshark will see the correct checksum.</p></li><li><p>Turn off TCP checksum validation in Wireshark. Wireshark still won't see the correct checksum, but the error messages will be suppressed.</p></li></ol><p>If the checksums really were bad, every packet with a bad checksum would be retransmitted or the communication would fail. So, if the communication succeeds, and you don't see retransmissions of the packets with bad checksums, then TCP checksum offload is the cause.</p><p>Another clue that TCP checksum offload is involved is that the bad checksums will only appear on packets SENT by the system where the capture was done. Packets received from other systems will show a correct checksum.</p><p>If the checksums are really bad, then some device along the path is mangling your packets.</p></div><div id="comment-2044-info" class="comment-info"><span class="comment-age">(31 Jan '11, 11:14)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div><span id="2113"></span><div id="comment-2113" class="comment"><div id="post-2113-score" class="comment-score"></div><div class="comment-text"><p>(changed the additional answers to comments to adhere to the Q&amp;A character of this site)</p></div><div id="comment-2113-info" class="comment-info"><span class="comment-age">(02 Feb '11, 11:10)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-2041" class="comment-tools"></div><div class="clear"></div><div id="comment-2041-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47077"></span>

<div id="answer-container-47077" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47077-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47077-score" class="post-score" title="current number of votes">0</div><span id="post-47077-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The connection to 224.0.0.252:5355 with protocol UDP is used by recent versions of Windows for Link Local Multicast Name Resolution (LLMNR) searching for local network computers. If you have no local network you may disable LLMNR with a peculiar registry setting. Create and execute the file "disable-LLMNR.reg" containing:</p><p>Windows Registry Editor Version 5.00</p><p>[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\DNSClient] "EnableMulticast"=dword:00000000</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Oct '15, 11:11</strong></p><img src="https://secure.gravatar.com/avatar/68517ffc32a0e00d152e1288b0303c35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gil06&#39;s gravatar image" /><p><span>gil06</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gil06 has no accepted answers">0%</span></p></div></div><div id="comments-container-47077" class="comments-container"></div><div id="comment-tools-47077" class="comment-tools"></div><div class="clear"></div><div id="comment-47077-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20297"></span>

<div id="answer-container-20297" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20297-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20297-score" class="post-score" title="current number of votes">-1</div><span id="post-20297-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>With windows 7 i see broadcasts to, 224.0.0.1, 224.0.0.22, 224.0.0.252, and some crazy 239.235 combinations haha.<br />
</p><p>It doesn't always specify a port for some reason I guess because it is internal broadcast like an above poster said. But still.....kind of gullible feeling. Kind of feeling like u can't trust anyone feeling. Even on my home network nowadays, who knows whats on it spoofing things at any time. Feels like every website and program that exists is already hacked before it gets to my computer. And they tell us torrents have viruses? hahaha Hey look up the Michaelangelo virus and Chernobyl(CIH) virus that ibm was spreading with new pcs years ago....lol Now its 2013 and ten times worse, your oblivious to think otherwise..... Anyways,<br />
</p><p>i have alot of services disabled. upnp, in windows and router(i had to use a secret text link to a hidden page in my Verizon router to shut this off. I guess verizon sees it as people disabling upnp and then calling tech support when their game or voip or w/e device doesn't work, even they don't take security serious or wanna educate their customers....lol).</p><p>I have ipv6 disabled everywhere you see it in windows settings and firewall and router, ...every once in a while i still see a network broadcast on it. But i have no idea.....which address is for which protocols in the predefined rules. Maybe some nice Microsoft Gentleman will shed some light on the 224.0.0.0 addresses.</p><p>someone please correct me. but i believe netbios file sharing in windows is ports 137, 138.</p><p>look for the ip of the computers on your network thats all you need to allow.</p><p>and i think the only broadcast you would need to allow is most liked 192.168.1.255. This might correlate with your router....mine is default ip. and I believe its the only one i had to allow to share files on my home network.</p><p>possibly in addition 224.0.0.1. but i would try without it first. Block everything else ip subnet from 224.0.0.0 to 255.255.255.255, 10.0.0.0 - 255, 127.0.0.0-255, 169,254.0.0-, 192.0.0.0-, 198.18.0.0, 198.51.100.0, 203.0.113.0, everything to 255.255.255.255, those are all internal addresses.</p><p>sometimes when your router doesn't know who you are it will give you a 169.254 internal address. You can set dhcp to w/e you want or do it manually. default is 192.168.</p><p>good luck.</p><p>just to add: Sometimes you gotta wonder why so many programs wanna broadcast out to those internal addresses as well......and why so many websites, even major corporations, have so many unknown ip's associated with them.</p><p>port 80 and 443 and 53 are just becoming flood gates of all streams of servers. These companies are gonna have to start registering every single ip address and domain associated with their site.</p><p>Even microsoft is like secretive what ips they use specifically for updates!! When the whole web becomes all httpS, they gonna have to let us know who the heck is connecting to my pc. Thats the truth, its getting ridiculous out here. SO many dam viruses. SO many spies, so many ads lol.</p><p>Their needs to be a public listing, something better then public domain tools.</p><p>I thought this site is pretty cool tks for letting me post.</p><p>Rich.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Apr '13, 19:06</strong></p><img src="https://secure.gravatar.com/avatar/48f0b9b35a277de93321a13b4e2ee460?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CooloutAC&#39;s gravatar image" /><p><span>CooloutAC</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CooloutAC has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Apr '13, 21:36</strong> </span></p></div></div><div id="comments-container-20297" class="comments-container"></div><div id="comment-tools-20297" class="comment-tools"></div><div class="clear"></div><div id="comment-20297-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

