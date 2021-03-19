+++
type = "question"
title = "Extra octets in packets in a capture file"
description = '''Greetings, Let me explain the context first. I have an application that filters pcap files in bulk. And then I got some pcap files from a third part, and the application just would not work. After analyzing this pcap file, I found out that there are 4 extra octets in the beginning of every packet in...'''
date = "2013-12-06T04:51:00Z"
lastmod = "2013-12-06T06:03:00Z"
weight = 27862
keywords = [ "wireshark", "packet", "octets", "extra" ]
aliases = [ "/questions/27862" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extra octets in packets in a capture file](/questions/27862/extra-octets-in-packets-in-a-capture-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27862-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27862-score" class="post-score" title="current number of votes">0</div><span id="post-27862-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings,</p><p>Let me explain the context first. I have an application that filters pcap files in bulk. And then I got some pcap files from a third part, and the application just would not work.</p><p>After analyzing this pcap file, I found out that there are 4 extra octets in the beginning of every packet in the file (analysis made by extracting the raw data from the pcap file). Due to these bytes, all the information is shifted, so the bytes informing that it is an IP packet are the 16th and 17th instead of the 12th and 13th expected.</p><p>However, wireshark can read this file just fine.</p><p>So here are the questions:</p><p>1) Is it possible to convert this file to remove these extra octets?</p><p>2) Why would there be these extra octets?</p><p>3) How does wireshark detect it?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-octets" rel="tag" title="see questions tagged &#39;octets&#39;">octets</span> <span class="post-tag tag-link-extra" rel="tag" title="see questions tagged &#39;extra&#39;">extra</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Dec '13, 04:51</strong></p><img src="https://secure.gravatar.com/avatar/10e6b7587db546377675e7039750aac7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lacovisk&#39;s gravatar image" /><p><span>Lacovisk</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lacovisk has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Dec '13, 14:52</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-27862" class="comments-container"></div><div id="comment-tools-27862" class="comment-tools"></div><div class="clear"></div><div id="comment-27862-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27865"></span>

<div id="answer-container-27865" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27865-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27865-score" class="post-score" title="current number of votes">1</div><span id="post-27865-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><ol><li>Yes, you can use the command line tool "editcap" (comes with Wireshark) using the -C parameter (capital "C", not lower case). Run editcap without parameters to get help.</li><li>Not sure, but some devices use additional bytes in the packet to store meta data along with the packet. Some TAP vendors do this, but usually at the end of each frame.</li><li>Wireshark probably either has some heuristic to do this, or the file has some indicator that tells Wireshark how to read the frames correctly, e.g. a special Link Layer Type.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Dec '13, 04:57</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-27865" class="comments-container"><span id="27866"></span><div id="comment-27866" class="comment"><div id="post-27866-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>2) Why would there be these extra octets?</p></blockquote><p>That's probably a VLAN tag. You should see the following in the Packet details pane, if it is a VLAN tag.</p><pre><code>   Frame
   Ethernet II
   802.1Q Virtual LAN
   Internet Protocol Version 4</code></pre><blockquote><p>3) How does wireshark detect it?</p></blockquote><p>Based on the ethertype: 0x8100 for a VLAN tagged frame. 0x0800 for a 'regular' IP frame.</p><blockquote><p>1) Is it possible to convert this file to remove these extra octets?</p></blockquote><p>If it is a VLAN tag: see the answer of <span></span><span>@Jasper</span> or use <a href="http://tcpreplay.synfin.net/wiki/tcprewrite">tcprewrite</a></p><blockquote><p>tcprewrite --enet-vlan=del --infile=input.pcap --outfile=output.pcap</p></blockquote><p>Regards<br />
Kurt</p></div><div id="comment-27866-info" class="comment-info"><span class="comment-age">(06 Dec '13, 05:14)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="27867"></span><div id="comment-27867" class="comment"><div id="post-27867-score" class="comment-score"></div><div class="comment-text"><p>VLAN tag! Of course, silly me!</p><p>Thanks very much!</p></div><div id="comment-27867-info" class="comment-info"><span class="comment-age">(06 Dec '13, 06:03)</span> <span class="comment-user userinfo">Lacovisk</span></div></div></div><div id="comment-tools-27865" class="comment-tools"></div><div class="clear"></div><div id="comment-27865-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

