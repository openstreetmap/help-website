+++
type = "question"
title = "Unusual Behavior with Stacked VLAN Tags and Capture Filter"
description = '''I have a strange issue that I have attempted to research but would welcome input from anyone else that may have encountered anything similar. Specifics: VM Ubuntu 13 server on ESXi 5.0 with 3 NICs (type VMXNET3). (Note: Today I just rebuilt the VM using the new Ubuntu 14 LTS.) Eth0 is for the local ...'''
date = "2014-04-17T15:26:00Z"
lastmod = "2014-04-21T03:27:00Z"
weight = 31953
keywords = [ "stacking", "vlan", "mirroring", "esx" ]
aliases = [ "/questions/31953" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Unusual Behavior with Stacked VLAN Tags and Capture Filter](/questions/31953/unusual-behavior-with-stacked-vlan-tags-and-capture-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31953-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31953-score" class="post-score" title="current number of votes">0</div><span id="post-31953-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">3</div></div></td><td><div id="item-right"><div class="question-body"><p>I have a strange issue that I have attempted to research but would welcome input from anyone else that may have encountered anything similar.</p><p>Specifics: VM Ubuntu 13 server on ESXi 5.0 with 3 NICs (type VMXNET3). (Note: Today I just rebuilt the VM using the new Ubuntu 14 LTS.) Eth0 is for the local network. Eth1 and Eth2 are dedicated to port mirrors from switches/taps. Eth1 only has single VLAN tags in the mirrored traffic. Eth2 has what I consider stacked tags. (I have included an image below.)</p><p>When I attempt to use a capture filter for VLAN 992 (993, 994, etc), I do not capture any data. I can use a display filter to show the VLAN 992 after it has been captured but this isn't what I desire for troubleshooting purposes due to the high amount of traffic.</p><p>I can capture filter the second VLANs (811, 812, etc) just fine.</p><p>I'm not sure where the issue resides.</p><p>I have experimented with other E1000 NICs in ESXi. I have the virtual switch set properly in ESX for promisc. (If this was set incorrectly I wouldn't have any traffic in the captures.) I have the VM NICs set for promisc (even though they appear not to need it since ESX is handling it). The version of Wireshark is 1.10.6 from the apt repository and whatever pcap is included - I mention this to confirm it's not an issue I created with a custom build/install of source.</p><p>Although I don't think it is worth going into a great amount of detail, I did install a CentOS 6.5 VM today as well and did perform a custom build/install of pcap and wireshark. Same NIC parameters. When I did this, I was no longer able to see the outer VLAN tag. I'm not sure if that is giving me a clue or not.</p><p>I know someone smarter than me could likely shed some light on my mystery.</p><p>Thanks for any assistance!</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Wireshark.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-stacking" rel="tag" title="see questions tagged &#39;stacking&#39;">stacking</span> <span class="post-tag tag-link-vlan" rel="tag" title="see questions tagged &#39;vlan&#39;">vlan</span> <span class="post-tag tag-link-mirroring" rel="tag" title="see questions tagged &#39;mirroring&#39;">mirroring</span> <span class="post-tag tag-link-esx" rel="tag" title="see questions tagged &#39;esx&#39;">esx</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Apr '14, 15:26</strong></p><img src="https://secure.gravatar.com/avatar/73bcc9038f127739c0856748313dbe73?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stjaru&#39;s gravatar image" /><p><span>stjaru</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stjaru has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Apr '14, 15:28</strong> </span></p></div></div><div id="comments-container-31953" class="comments-container"><span id="32011"></span><div id="comment-32011" class="comment"><div id="post-32011-score" class="comment-score"></div><div class="comment-text"><p>There are answers below about how to filter for the inner tag, but when I read this question, it sounds more to me like you're unable to filter the outer tag, 992 in this case. To quote:</p><p><em>When I attempt to use a capture filter for VLAN 992 (993, 994, etc), I do not capture any data. I can use a display filter to show the VLAN 992 after it has been captured but this isn't what I desire for troubleshooting purposes due to the high amount of traffic.</em></p><p>So when you apply a capture filter of, "<code>vlan 992</code>" you don't capture anything? But if you <strong>don't</strong> apply any capture filter, then you can later apply a Wireshark display filter of "<code>vlan.id == 992</code>" to filter the packets of interest? Is that right?</p></div><div id="comment-32011-info" class="comment-info"><span class="comment-age">(20 Apr '14, 10:17)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="32015"></span><div id="comment-32015" class="comment"><div id="post-32015-score" class="comment-score"></div><div class="comment-text"><blockquote><p>There are answers below about <strong>how to filter for the inner tag</strong>,</p></blockquote><p>well, my answer is actually primarily about the problem of filtering several <strong>outer tags</strong> in one capture filter statement.</p></div><div id="comment-32015-info" class="comment-info"><span class="comment-age">(20 Apr '14, 14:46)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="32022"></span><div id="comment-32022" class="comment"><div id="post-32022-score" class="comment-score"></div><div class="comment-text"><p>Thank you Guy for participating in the thread. Good stuff!</p><p>Kurt, wow man, that was fantastic information! I appreciate you taking the time to give such excellent detail and sourcing! I'm very appreciative of everyone taking some time to help on this topic.</p><p>Now that I better understand why my other assumption was incorrect, would anyone have any ideas about why I cannot capture successfully on just the outer tag? That would be the heart of the issue.</p><p>I'm still unable to understand why I cannot use capture with "vlan 99x" and see packets (which is the answer to cmaynard's request for clarification/confirmation). Again, I cannot capture using that filter, but I can display to see the VLAN.</p><p>Thanks all,</p></div><div id="comment-32022-info" class="comment-info"><span class="comment-age">(20 Apr '14, 20:17)</span> <span class="comment-user userinfo">stjaru</span></div></div></div><div id="comment-tools-31953" class="comment-tools"></div><div class="clear"></div><div id="comment-31953-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="31955"></span>

<div id="answer-container-31955" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31955-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31955-score" class="post-score" title="current number of votes">0</div><span id="post-31955-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have you tried filtering on both VLAN ids at the same time? Something like "vlan 992 and vlan 811"? If I remember correctly this is required when filtering on QinQ traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '14, 15:31</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-31955" class="comments-container"><span id="31956"></span><div id="comment-31956" class="comment"><div id="post-31956-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your input Jasper. :)</p><p>I have tried that without success.</p><p>Capture filter "vlan 992 or vlan 811" will not collect anything.</p><p>But I did discover something interesting - Capture filter "vlan 810 or vlan 811" will only collect the first VLAN (810). I would not expect a problem with that capture filter.</p><p>However since I have never been able to capture filter on the outer tag, I normally capture everything on the interface and then use a display filter on the outer tag. Hence the discovery of the behavior.</p><p>I don't know if these problems are related but I'm still wrestling with the original question.</p></div><div id="comment-31956-info" class="comment-info"><span class="comment-age">(17 Apr '14, 15:49)</span> <span class="comment-user userinfo">stjaru</span></div></div><span id="31979"></span><div id="comment-31979" class="comment"><div id="post-31979-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I would not expect a problem with that capture filter.</p></blockquote><p>I would, but that's because I know the rather kludgy way that the "vlan" capture filter works. "vlan" turns everything to the right of it into a test for traffic under that VLAN, so "vlan 810 or vlan 811" doesn't do what you'd expect.</p></div><div id="comment-31979-info" class="comment-info"><span class="comment-age">(18 Apr '14, 13:57)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-31955" class="comment-tools"></div><div class="clear"></div><div id="comment-31955-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="32006"></span>

<div id="answer-container-32006" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32006-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32006-score" class="post-score" title="current number of votes">0</div><span id="post-32006-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Capture filter "vlan 992 or vlan 811" will not collect anything.<br />
Capture filter "vlan 810 or vlan 811" will only collect the first VLAN (810).</p></blockquote><p>as <span><span>@Guy Harris</span></span> already mentioned the <strong>vlan</strong> capture filter 'primitive' does some magic behind the curtains, and thus it does not work as you might expect it, based on the behavior of other <strong>logical OR</strong> operations in capture filters.</p><p>See <a href="http://www.tcpdump.org/manpages/pcap-filter.7.html">man page of pcap-filter</a>:</p><pre><code>vlan [vlan_id]
   Note that the first vlan keyword encountered in expression changes 
   the decoding offsets for the remainder of expression on the 
   assumption that the packet is a VLAN packet.

   The  vlan [vlan_id] expression may be used more than once, to filter on 
   VLAN hierarchies. Each use of that expression increments the filter 
   offsets by 4.</code></pre><p>So, lets have a look at the BPF code for the following capture filter</p><blockquote><p>tcpdump -ni eth0 -d <strong>'vlan 100'</strong></p></blockquote><pre><code>(000) ldh      [12]           
(001) jeq      #0x8100          jt 2    jf 6
(002) ldh      [14]
(003) and      #0xfff
(004) jeq      #0x64            jt 5    jf 6
(005) ret      #65535
(006) ret      #0</code></pre><p><strong>(000):</strong> Load the location of the ethertype.<br />
<strong>(001):</strong> Is it a VLAN tag (0x8100)?<br />
<strong>(002-004):</strong> If true: load the value at position 14 (the VLAN tag) and compare it with 0x64 (100 decimal)<br />
</p><p>So far, so good.</p><p>Now lets check the BPF code of the following capture filter</p><blockquote><p>tcpdump -ni eth0 -d <strong>'vlan 100 or vlan 200'</strong></p></blockquote><pre><code>(000) ldh      [12]
(001) jeq      #0x8100          jt 2    jf 5
(002) ldh      [14]
(003) and      #0xfff
(004) jeq      #0x64            jt 10   jf 5

(005) ldh      [16]          &lt;&lt;=== PROBLEM HERE !!!

(006) jeq      #0x8100          jt 7    jf 11
(007) ldh      [18]
(008) and      #0xfff
(009) jeq      #0xc8            jt 10   jf 11
(010) ret      #65535
(011) ret      #0</code></pre><p><strong>(000-004):</strong> same as before<br />
<strong>(005):</strong> The whole problem occurs here. As the <strong>vlan</strong> primitive increases the decoding offset by 4 (see man page above - regardless of logical operator), the second <strong>vlan</strong> primitive will simply look at the wrong place for the ethertype. It should look at position 12 in the ethernet frame, but due to the decoding offset increase of 4, it looks at position 16, which is apparently wrong for a <strong>logical OR</strong> vlan operation (at least as one would assume/expect how it should work).</p><p>Due to this behavior (call is a bug or not), you cannot capture for several vlan tags in a single capture filter, combined with a <strong>logical OR</strong> operation. Furthermore, if you use a <strong>logical AND</strong> operation, you will only see double tagged or QinQ frames (as <span><span>@Jasper</span></span>) mentioned.</p><p>Solution: Run several instances of tcpdump, each with a single vlan capture filter and later merge the capture files with mergecap.</p><blockquote><p>tcpdump -ni eth0 -w /tmp/vlan811.pcap 'vlan 811'&amp;<br />
tcpdump -ni eth0 -w /tmp/vlan800.pcap 'vlan 800'&amp;<br />
tcpdump -ni eth0 -w /tmp/vlan900.pcap 'vlan 900'&amp;<br />
sleep 500<br />
killall tcpdump<br />
mergecap -w /tmp/vlan800+811+900.pcap /tmp/vlan800.pcap /tmp/vlan811.pcap /tmp/vlan900.pcap<br />
</p></blockquote><p><strong>+++ UPDATE +++</strong></p><p>I have to correct myself. <strong>It is possible</strong> to capture multiple (outer) vlan tags in a single capture filter, by doing the vlan tag matching 'manually'.</p><blockquote><p>tcpdump -ni eth0 'vlan and (ether[14:2]&amp;0xfff=100 or ether[14:2]&amp;0xfff=200)'</p></blockquote><p>If you look at the BPF code, you'll see that it is essentially the same as 'vlan 100' combined with 'vlan 200', which is essentially the same as 'vlan 100 or vlan 200'.</p><pre><code>(000) ldh      [12]
(001) jeq      #0x8100          jt 2    jf 7
(002) ldh      [14]
(003) and      #0xfff
(004) jeq      #0x64            jt 6    jf 5
(005) jeq      #0xc8            jt 6    jf 7
(006) ret      #65535
(007) ret      #0</code></pre><p><strong>(000):</strong> Load the location of the ethertype.<br />
<strong>(001):</strong> Is it a VLAN tag (0x8100)?<br />
<strong>(002):</strong> If true: load the value at position 14 (the vlan tag)<br />
<strong>(004):</strong> compare the vlan tag with 0x64 (100 decimal)<br />
<strong>(005):</strong> compare the vlan tag with 0xc8 (200 decimal)<br />
</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '14, 16:45</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Apr '14, 14:48</strong> </span></p></div></div><div id="comments-container-32006" class="comments-container"><span id="32027"></span><div id="comment-32027" class="comment"><div id="post-32027-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I'm still unable to understand why I cannot use capture with "vlan 99x" and see packets</p></blockquote><p>O.K. we need more information. Here are some questions for you:</p><ul><li>How did you capture the traffic (tcpdump, dumpcap, tshark, Wireshark)</li><li>Is your capturing system configured to use VLAN tags on the capturing interface?</li></ul><p>You say:</p><blockquote><p>When I attempt to use a <strong>capture filter for VLAN 992 (993, 994, etc) - OUTER tag -</strong> , I do not capture any data.<br />
I can capture filter the second VLANs (811, 812, etc) - INNER tag - just fine.</p></blockquote><p>O.K. so, either there are no frames with VLAN tag 99x, <strong>or something on your system strip the outer VLAN tag</strong> before the capturing system gets the frame, which would explain, why you do see the inner tag.</p><p><strong>However</strong>, if the outer tag would have been removed, it does not explain why you see the outer tag in the capture file, with a display filter. But maybe I misunderstand what you did in that case!?!</p><p>So, can you please add more details about your capturing setup: What do you see in the capture file, if you</p><ul><li>don't use any capture filter</li><li>use a capture filter for the outer tag: <code>vlan 99x</code></li><li>use a combined capture filter for the outer tag: <code>vlan 99x or vlan 99y</code></li><li>use a capture filter for the inner tag: <code>vlan 88x</code></li><li>use a combined capture filter for the inner tag: <code>vlan 88x or vlan 88y</code></li><li>use a capture filter as shown in my answer: <code>vlan and ether[14:2]&amp;0xfff=99x</code></li></ul><p>BTW: Can you provide a sample capture somewhere (google docs, dropbox, cloudshark.org)?</p></div><div id="comment-32027-info" class="comment-info"><span class="comment-age">(21 Apr '14, 03:27)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-32006" class="comment-tools"></div><div class="clear"></div><div id="comment-32006-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

