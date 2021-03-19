+++
type = "question"
title = "Failed to allocate memory"
description = '''Hi all,  I&#x27;m using source code of wireshark-1.10.9 in order to modify some pieces of code in packet-data.c. I use functions to allocate memory like this:  At first, I use  &quot;sccp_sonnh = wmem_alloc(wmem_packet_scope(), sizeof(guint8)*nSccp_length)&quot;  but when I run tshark -r vnp.pcap, it shows the Seg...'''
date = "2014-09-24T03:05:00Z"
lastmod = "2014-09-24T03:05:00Z"
weight = 36559
keywords = [ "allocate", "tshark", "memory" ]
aliases = [ "/questions/36559" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Failed to allocate memory](/questions/36559/failed-to-allocate-memory)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36559-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I'm using source code of wireshark-1.10.9 in order to modify some pieces of code in packet-data.c. I use functions to allocate memory like this:</p><ul><li>At first, I use</li></ul><p>"<code>sccp_sonnh = wmem_alloc(wmem_packet_scope(), sizeof(guint8)*nSccp_length</code>)"</p><p>but when I run <code>tshark -r vnp.pcap</code>, it shows the Segmentation Fault right after running. it can run in Windows but cannot run in Linux.</p><ul><li>Then, I use</li></ul><p>"<code>sccp_sonnh = ep_alloc_array(guint8,nSccp_length);</code>"</p><p>to allocate. It can run but I see the memory increasing very fast. Finally, I got the error:</p><blockquote><p>GLib-ERROR **: gmem.c:170: failed to allocate 919295276 bytes aborting...</p></blockquote><p>when the memory is at 95% and about 1837440 packets were read even I check log and see that every time, my program only allocates 140 or 90... bytes. As mentioned in README.malloc, "The ephemeral functions allocate memory that will be automatically freed once the current packet dissection completes" but in my case, it look like the memory is not freed. So, please help if you have an idea for this:</p><ol><li>With "tshark -r" , when 1837440 packets were read, does it mean these packets are freed?</li><li>If No, how can I free these memory?</li><li>Is this the bug out of memory of Wireshark or just my mistake of coding? (We are dissecting UDP)</li><li>are there other ways to allocate memory and how can make sure that this memory is freed each time when the packet is dissected?</li></ol><p>P/S: When I use static memory allocation, it run faster and memory increases slower but still get increasing and stop after running 10 minutes.</p></div><div id="question-tags" class="tags-container tags">allocate tshark memory</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Sep '14, 03:05</strong></p><img src="https://secure.gravatar.com/avatar/824a7342f59ff90e6040505b38626416?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hoangsonk49&#39;s gravatar image" /><p>hoangsonk49<br />
<span class="score" title="81 reputation points">81</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hoangsonk49 has 2 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Sep '14, 19:59</p></div></div><div id="comments-container-36559" class="comments-container"><span id="36626"></span><div id="comment-36626" class="comment"><div id="post-36626-score" class="comment-score"></div><div class="comment-text"><p>Hi, I suspect it's something else eating the memory - what are you doing with the sccp_sonnh array? I doupt packet-data.c is the right place to put the modification as it might be called from many dissectors not only packet-udp.c</p><blockquote><p>my program only allocates 140 or 90... bytes.</p></blockquote><p>Are you sure about this? nSccp_length couldn't take an arbittary value?</p><p>Also in "normal" cases Wireshark/tshark will run out of memory eventually because of state keept between packets. Your milage depends on the protocols in the trace and available RAM or appliction memory allocation limits.</p></div><div id="comment-36626-info" class="comment-info"><span class="comment-age">(26 Sep '14, 01:55)</span> Anders ♦</div></div><span id="36670"></span><div id="comment-36670" class="comment"><div id="post-36670-score" class="comment-score"></div><div class="comment-text"><ul><li>I use sccp_sonnh array to store some values getting from tvb_tree (data.data). As mentioned in README.malloc, it will be freed automatically right after switching to other packet.</li><li>I'm pretty sure that " my program only allocates 140 or 90... bytes " . I print this value right before ep_alloc_array. Also, I check this value with the data getting from tvb_tree. It is matched.</li><li>From GUI of wireshark, I can see that the dissector stops at UDP protocol, it means no other dissector running after packet-data.c</li><li>The last protocol of this data is UDP with data.data and My server has 32 Gb RAM</li></ul><p>For more information: - When I comment out these modification, it can run without any increment of memory.</p></div><div id="comment-36670-info" class="comment-info"><span class="comment-age">(28 Sep '14, 20:10)</span> hoangsonk49</div></div></div><div id="comment-tools-36559" class="comment-tools"></div><div class="clear"></div><div id="comment-36559-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

