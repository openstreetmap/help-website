+++
type = "question"
title = "Difference TShark / Wireshark when load a pcap"
description = '''Hi to all, After merge 2 two pcap with the command &quot;mergepcap -a 1.pcap 2.pcap -w result.pcap&quot; the output from TShark and Wireshark is different.  In detail, if i open the result.pcap with TShark with this command, /usr/bin/tshark -r result.pcap -T fields -e tcp.stream -e frame.time -e tcp.checksum ...'''
date = "2012-01-11T05:38:00Z"
lastmod = "2012-01-12T08:31:00Z"
weight = 8324
keywords = [ "difference", "tshark", "wireshark" ]
aliases = [ "/questions/8324" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Difference TShark / Wireshark when load a pcap](/questions/8324/difference-tshark-wireshark-when-load-a-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8324-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi to all,</p><p>After merge 2 two pcap with the command "mergepcap -a 1.pcap 2.pcap -w result.pcap" the output from TShark and Wireshark is different.</p><p>In detail, if i open the result.pcap with TShark with this command, /usr/bin/tshark -r result.pcap -T fields -e tcp.stream -e frame.time -e tcp.checksum -R "tcp" | grep ".02696400" | more</p><p>The result is "20 Dec 15, 2011 11:12:20.026964000 0xf3a8"</p><p>When i open the result.pcap with Wireshark and the filter is tcp.stream eq 20 i don't have any record.</p><p>The same packet (Dec 15, 2011 11:12:20.026964000 0xf3a8) is visible if i put in the filter of wireshark "tcp.stream eq 56".</p><p>Why ???? i wrong when merge 2 pcap files ?</p></div><div id="question-tags" class="tags-container tags">difference tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jan '12, 05:38</strong></p><img src="https://secure.gravatar.com/avatar/ee5b26ae7dd5ff028a8354f0944a6e01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fcafra&#39;s gravatar image" /><p>fcafra<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fcafra has no accepted answers">0%</span></p></div></div><div id="comments-container-8324" class="comments-container"></div><div id="comment-tools-8324" class="comment-tools"></div><div class="clear"></div><div id="comment-8324-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8339"></span>

<div id="answer-container-8339" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8339-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I doubt that the issue has anything to do with mergecap.</p><p><code>tcp.stream</code> is a generated field: that is: the tcp dissector just increments a counter each time it sees what it thinks is a new "stream" (aka connection aka conversation).</p><p>For example: <code>tcp.stream</code> will probably be different for the same frame in <code>1.pcap</code> vs <code>result.pcap</code>.</p><p>I don't specifically know why you get different results for <code>tshark</code> vs <code>wireshark</code> when reading <code>result.pcap</code>.</p><p>Do you get a different stream value if you remove the <code>-R tcp</code> when invoking <code>tshark</code> ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '12, 08:31</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-8339" class="comments-container"><span id="8367"></span><div id="comment-8367" class="comment"><div id="post-8367-score" class="comment-score"></div><div class="comment-text"><p>Thank's Bill for your response, i try to remove -R tcp but the result is not change... i have the same error.</p><p>Maybe, wireshark adjust the field tcp.stream when loading the pcap file... it's possible this ?</p><p>and if correct this answer, there is a tshark method or another method to adjust tcp.stream field when i try to load entire pcap file ?</p></div><div id="comment-8367-info" class="comment-info"><span class="comment-age">(13 Jan '12, 00:45)</span> fcafra</div></div><span id="8368"></span><div id="comment-8368" class="comment"><div id="post-8368-score" class="comment-score"></div><div class="comment-text"><p>I understand the problem.</p><p>if i launch tshark version TShark 1.6.5 it's all ok....</p><p>when i try, i have use tshark 1.2.7....</p><p>Sorry, and.. thank's...</p></div><div id="comment-8368-info" class="comment-info"><span class="comment-age">(13 Jan '12, 03:29)</span> fcafra</div></div><span id="8384"></span><div id="comment-8384" class="comment"><div id="post-8384-score" class="comment-score"></div><div class="comment-text"><p>(I converted your answer to a comment, please see the FAQ for details)</p><p>Yes, the way tcp.stream numbers are generated has changed between 1.2.7 and 1.6.5</p></div><div id="comment-8384-info" class="comment-info"><span class="comment-age">(14 Jan '12, 02:08)</span> SYN-bit ♦♦</div></div><span id="8449"></span><div id="comment-8449" class="comment"><div id="post-8449-score" class="comment-score"></div><div class="comment-text"><p>Thank's SYNbit and sorry :)</p><p>Can i ask another question here ?</p></div><div id="comment-8449-info" class="comment-info"><span class="comment-age">(18 Jan '12, 02:26)</span> fcafra</div></div><span id="8459"></span><div id="comment-8459" class="comment"><div id="post-8459-score" class="comment-score">1</div><div class="comment-text"><p>If "here" means "on the ask.wireshark.org" site, yes, you can ask another question here.</p><p>If "here" means "as a comment on this answer", then, while the site's software doesn't prevent that, you really <em>shouldn't</em> do that - Q&amp;A sites such as this really work best if each question is asked separately, so that another user with the same or a similar question can more easily find a question. (Note that Q&amp;A sites, such as this, aren't forums.)</p></div><div id="comment-8459-info" class="comment-info"><span class="comment-age">(18 Jan '12, 12:31)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-8339" class="comment-tools"></div><div class="clear"></div><div id="comment-8339-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

