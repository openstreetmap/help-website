+++
type = "question"
title = "FCS check is not displayed"
description = '''I cannot seem to configure Wireshark version 1.6.2 to identify an Ethernet FCS. I am using Wireshark to help verify the contents for a Frame Generator application that I am developing. The application is dumping out the contents of Ethernet frames in a &quot;text dump file&quot; in hex format that is able to ...'''
date = "2011-09-12T11:41:00Z"
lastmod = "2011-09-17T12:28:00Z"
weight = 6293
keywords = [ "fcs" ]
aliases = [ "/questions/6293" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [FCS check is not displayed](/questions/6293/fcs-check-is-not-displayed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6293-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6293-score" class="post-score" title="current number of votes">0</div><span id="post-6293-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I cannot seem to configure Wireshark version 1.6.2 to identify an Ethernet FCS. I am using Wireshark to help verify the contents for a Frame Generator application that I am developing. The application is dumping out the contents of Ethernet frames in a "text dump file" in hex format that is able to be read into Wireshark . I simply input the "text dump file" into Wireshark by clicking <strong>File-&gt;Import-&gt;(file name)</strong> with the format set to "hexadecimal" and the encapsulation set to "Ethernet".</p><p>Below is the content of my "text dump file" that includes an Ethernet/IPv6/UDP frame with 11 bytes payload and a broken FCS (CRC-32 is "b1 0a 91 2f "):</p><pre><code>00000000   0d f3 0b b9 4a bb bf ec 
00000008   ff 49 88 32 86 dd 40 4d 
00000010   f4 da 8f d0 11 a4 8e ef 
00000018   07 33 4f 18 39 03 f5 89 
00000020   2b 66 38 68 f1 97 03 ab 
00000028   e1 7d 15 4a 07 c9 ba dd 
00000030   42 1c 47 dc 0b de 7f 76 
00000038   ef 4e 00 13 00 04 ad da 
00000040   68 ec 4e 61 90 8d 1e 26 
00000048   c1 b1 0a 91 2f</code></pre><p>After importing the frame, I see the entire expected Ethernet frame. In my example, I see all the Ethernet/IPv6/UDP fields and 11-byte payload as expected, but I do NOT see the 32-bit FCS identified &amp; checked by Wireshark.</p><p>Looking through some of the posts in this forum, it seemed as if the <strong>Edit-&gt;Preferences-&gt;Protocols-&gt;Ethernet-&gt;"Assume Packet has FCS"</strong> would help, but it did not solve my FCS issue.</p><p>Looking through my Wireshark <code>preferences</code> file, I see the following settings that look interesting, but they do not seem to help:</p><pre><code>erf.ethfcs: TRUE  
eth.assume_fcs: TRUE</code></pre><p>In Wireshark documentation, I also see information about a <em>CyclicRedundancyCheck</em> (CRC) algorithm to detect transmission errors and a <em>FrameCheckSequence</em> field, but I am not sure how to enable these features.</p><ul><li>Is there a Ethernet FCS/CRC configuration switch that I need to enable?</li><li>Do I need to create or use a a Wireshark plug-in extension?</li><li>Do I need to create a User Encapsulation Type?</li><li>Does this have something to do with libpcap?</li></ul></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fcs" rel="tag" title="see questions tagged &#39;fcs&#39;">fcs</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '11, 11:41</strong></p><img src="https://secure.gravatar.com/avatar/996c38bdf8c0457b7c4d35b4d05313b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="steved&#39;s gravatar image" /><p><span>steved</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="steved has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Sep '11, 23:38</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6293" class="comments-container"></div><div id="comment-tools-6293" class="comment-tools"></div><div class="clear"></div><div id="comment-6293-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6308"></span>

<div id="answer-container-6308" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6308-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6308-score" class="post-score" title="current number of votes">2</div><span id="post-6308-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark's heuristics for detecting the presence of an FCS in an Ethernet packet rely, for packets with a type field rather than a length field, on the protocol running atop Ethernet having a valid length field, so it knows how much of the packet is either trailer or FCS. The packet in question has a length value of 36816 bytes, which means it appears that every single octet of what remains in the packet after the Ethernet header is packet data, not trailer or FCS.</p><p>In theory, "eth.assume_fcs: TRUE" should cause Wireshark to treat the last 4 octets of the frame as an FCS, but it doesn't, in fact, do so. I'll look at that bug.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '11, 23:29</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-6308" class="comments-container"><span id="6331"></span><div id="comment-6331" class="comment"><div id="post-6331-score" class="comment-score"></div><div class="comment-text"><p>The FCS handling was broken when the Ethernet dissector was changed to parse VLAN headers itself; I've checked in a fix for that in the trunk, and will schedule the fix to go into 1.6.3.</p></div><div id="comment-6331-info" class="comment-info"><span class="comment-age">(13 Sep '11, 14:18)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="6429"></span><div id="comment-6429" class="comment"><div id="post-6429-score" class="comment-score"></div><div class="comment-text"><p>It looks like the Ethernet dissector and VLAN headers will be split again as it seems to have caused more problems than it solved. See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5680">bug 5680</a>. In light of this, maybe the FCS handling fix shouldn't be scheduled for backporting just yet as it might become obsolete if the two are split up again?</p></div><div id="comment-6429-info" class="comment-info"><span class="comment-age">(16 Sep '11, 20:08)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="6434"></span><div id="comment-6434" class="comment"><div id="post-6434-score" class="comment-score"></div><div class="comment-text"><p>Backporting the FCS fix fixes a bug if we don't undo the VLAN change, and might make backporting the undo easier if we do undo the VLAN change (backporting undo-the-VLAN-change might require manual intervention if we don't first backport the FCS fix).</p></div><div id="comment-6434-info" class="comment-info"><span class="comment-age">(17 Sep '11, 12:28)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-6308" class="comment-tools"></div><div class="clear"></div><div id="comment-6308-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

