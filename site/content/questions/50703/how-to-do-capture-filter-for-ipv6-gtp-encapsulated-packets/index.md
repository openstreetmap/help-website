+++
type = "question"
title = "How to do capture filter for IPv6 GTP encapsulated packets?"
description = '''Hi, is there a way to do capture filter for IPv6 on GTP encapsulated packets? (ip[64:16]==0x2a008a00200000350000000000000011) or (ip6[64:16]==0x2a008a00200000350000000000000011) I tried both, don&#x27;t seem to work. Thanks! Joseph'''
date = "2016-03-03T06:54:00Z"
lastmod = "2016-03-04T13:12:00Z"
weight = 50703
keywords = [ "gtp" ]
aliases = [ "/questions/50703" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to do capture filter for IPv6 GTP encapsulated packets?](/questions/50703/how-to-do-capture-filter-for-ipv6-gtp-encapsulated-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50703-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50703-score" class="post-score" title="current number of votes">0</div><span id="post-50703-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>is there a way to do capture filter for IPv6 on GTP encapsulated packets?</p><p>(ip[64:16]==0x2a008a00200000350000000000000011) or (ip6[64:16]==0x2a008a00200000350000000000000011)</p><p>I tried both, don't seem to work.</p><p>Thanks! Joseph</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gtp" rel="tag" title="see questions tagged &#39;gtp&#39;">gtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Mar '16, 06:54</strong></p><img src="https://secure.gravatar.com/avatar/7035162f27c4b75a86d214a1769ac443?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joseph75074&#39;s gravatar image" /><p><span>joseph75074</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joseph75074 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Mar '16, 09:46</strong> </span></p></div></div><div id="comments-container-50703" class="comments-container"></div><div id="comment-tools-50703" class="comment-tools"></div><div class="clear"></div><div id="comment-50703-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50707"></span>

<div id="answer-container-50707" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50707-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50707-score" class="post-score" title="current number of votes">0</div><span id="post-50707-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From the <a href="http://www.tcpdump.org/manpages/pcap-filter.7.html">pcap-filter</a> man page, you can only specify sizes of 1, 2, or 4.</p><pre><code>proto [ expr : size ]

Size is optional and indicates the number of bytes in the field of interest; it can be either one, two, or four, and defaults to one.</code></pre><p>The <code>relop</code> is wrong too; you should be using <code>=</code>, not <code>==</code>, at least according to the man page.</p><pre><code>expr relop expr
    True if the relation holds, where relop is one of &gt;, &lt;, &gt;=, &lt;=, =, !=, and expr is an arithmetic expression composed of ...</code></pre><p>So, assuming the packet is IPv4-encapsulated, you probably need something like:</p><pre><code>ip[64:4]=0x2a008a00 and ip[68:4]=0x20000035 and ip[72:4]=0x00000000 and ip[76:4]=0x00000011</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Mar '16, 09:13</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Mar '16, 09:14</strong> </span></p></div></div><div id="comments-container-50707" class="comments-container"><span id="50710"></span><div id="comment-50710" class="comment"><div id="post-50710-score" class="comment-score"></div><div class="comment-text"><p>Hi, cmaynard:</p><p>Thanks for your reply! I tried with '=', still not working, this is for IPv6 GTP encapsulated packets.</p></div><div id="comment-50710-info" class="comment-info"><span class="comment-age">(03 Mar '16, 11:22)</span> <span class="comment-user userinfo">joseph75074</span></div></div><span id="50711"></span><div id="comment-50711" class="comment"><div id="post-50711-score" class="comment-score"></div><div class="comment-text"><p>Maybe you could post a small capture file then? A single packet should suffice to get an idea of what the traffic looks like exactly.</p></div><div id="comment-50711-info" class="comment-info"><span class="comment-age">(03 Mar '16, 11:44)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="50719"></span><div id="comment-50719" class="comment"><div id="post-50719-score" class="comment-score"></div><div class="comment-text"><p>Sorry I am new to this website, how do I upload a pcap file? seems like .pcapng type is not allowed in the edit page.</p></div><div id="comment-50719-info" class="comment-info"><span class="comment-age">(04 Mar '16, 07:17)</span> <span class="comment-user userinfo">joseph75074</span></div></div><span id="50720"></span><div id="comment-50720" class="comment not_top_scorer"><div id="post-50720-score" class="comment-score"></div><div class="comment-text"><p>Post the capture somewhere publicly accessible, e.g. Google Drive, Dropbox etc. and then edit your question with a link to the file.</p></div><div id="comment-50720-info" class="comment-info"><span class="comment-age">(04 Mar '16, 07:20)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="50721"></span><div id="comment-50721" class="comment"><div id="post-50721-score" class="comment-score">1</div><div class="comment-text"><p>Another possibility, since we probably only need to look at a single packet to determine the correct offsets (which is where I suspect the problem lies), you could also just convert a single packet to text using Wireshark's <code>File -&gt; Export Packet Dissections -&gt; as "Plain Text" file...</code> mechanism.</p><p>Choose only the <em>Selected Packet</em>, then deselect everything under the <em>Packet Format</em> section except <strong>DO</strong> select <em>Packet Bytes</em>. You can then just edit your question or add a comment with the resulting text output that represent the bytes of the packet.</p><p>It ought to be possible to determine the correct offsets and data needed from the text alone and the packet can always be reconstructed using <code>text2pcap</code>, if needed.</p></div><div id="comment-50721-info" class="comment-info"><span class="comment-age">(04 Mar '16, 09:08)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="50723"></span><div id="comment-50723" class="comment"><div id="post-50723-score" class="comment-score">1</div><div class="comment-text"><p>EDIT: I'm not sure why the previous comment was deleted, but the posted text essentially showed the following stack:</p><pre><code>Ethernet (14 bytes)
802.1Q   (4 bytes)
IPv6     (40 bytes)
UDP      (8 bytes)
GTP      (8 bytes)
IPv6     (40 bytes)
DNS      (&quot;who cares&quot; bytes)</code></pre><p>Well, that wasn't the format I was looking for, but it's probably enough to answer the question. You've got a vlan tag with outer IPv6 and your desired filter has changed, so try this instead:</p><pre><code>vlan and ip6[64:4]=0x20030490 and ip6[68:4]=0xcff200d9 and ip6[72:4]=0x00000000 and ip6[76:4]=0x00563f01</code></pre><p>I think the important piece you were missing was the vlan primitive. From the <a href="http://www.tcpdump.org/manpages/pcap-filter.7.html">pcap-filter</a> man page:</p><pre><code>vlan [vlan_id]
    True if the packet is an IEEE 802.1Q VLAN packet. If [vlan_id] is specified, only true if the packet has the specified vlan_id. Note that the first vlan keyword encountered in expression changes the decoding offsets for the remainder of expression on the assumption that the packet is a VLAN packet. The vlan [vlan_id] expression may be used more than once, to filter on VLAN hierarchies. Each use of that expression increments the filter offsets by 4.</code></pre></div><div id="comment-50723-info" class="comment-info"><span class="comment-age">(04 Mar '16, 10:11)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="50725"></span><div id="comment-50725" class="comment not_top_scorer"><div id="post-50725-score" class="comment-score"></div><div class="comment-text"><p>Thanks! Cmaynard. This works! I was able to capture for those packets with that header size. But my problem is that I have other GTP SIP messages that have different header sizes, and I was not able to capture all of them related to the IPv6 address, is there an easy way to capture based on GTP IPv6 address, irregardless of the header sizes?</p></div><div id="comment-50725-info" class="comment-info"><span class="comment-age">(04 Mar '16, 12:58)</span> <span class="comment-user userinfo">joseph75074</span></div></div><span id="50726"></span><div id="comment-50726" class="comment not_top_scorer"><div id="post-50726-score" class="comment-score"></div><div class="comment-text"><p>It might be possible. If there are only a few different fixed-sized headers, then you might simply <code>or</code> them all together.</p><p>For example, suppose you have some headers such that the inner-IPv6 address starts at offset 64 from the outer-IPv6 header but others start at offset 80, then you might do something like so:</p><pre><code>vlan and (ip6[64:4]=0x20030490 and ip6[68:4]=0xcff200d9 and ip6[72:4]=0x00000000 and ip6[76:4]=0x00563f01) or (ip6[80:4]=0x20030490 and ip6[84:4]=0xcff200d9 and ip6[88:4]=0x00000000 and ip6[92:4]=0x00563f01)</code></pre><p>If there are too many different offsets, then it might be possible to dynamically find the offset for the given packet, but this really depends on your traffic, so you'd really need to post a capture file somewhere to see if it would be possible. Graham mentioned above some places where you can upload a capture file.</p></div><div id="comment-50726-info" class="comment-info"><span class="comment-age">(04 Mar '16, 13:12)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-50707" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-50707-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

