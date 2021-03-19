+++
type = "question"
title = "problem with dissecting a large pcap file as FAST"
description = '''I have a 200GB pcap file which I need to decode as FAST. As wireshark cannot open that huge file, I have to split the file into smaller files and decode each file and it has to be done using a script because I will end up with around 1000 files. So I need to be able to decode a file through a comman...'''
date = "2013-02-20T13:29:00Z"
lastmod = "2013-02-20T14:09:00Z"
weight = 18785
keywords = [ "large", "dissector", "pcap", "fast" ]
aliases = [ "/questions/18785" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [problem with dissecting a large pcap file as FAST](/questions/18785/problem-with-dissecting-a-large-pcap-file-as-fast)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18785-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a 200GB pcap file which I need to decode as FAST. As wireshark cannot open that huge file, I have to split the file into smaller files and decode each file and it has to be done using a script because I will end up with around 1000 files. So I need to be able to decode a file through a command line interface. As I've observed in the wireshark user guide there's a -d option which is the same as Decode as in the GUI version. however, my wireshark does not recognize -d as a valid option. I have also used tshark but it does not FAST as a valid dissector. I would appreciate if anyone could help me with this problem. Why there is no -d option in wireshark and tshark does not recognize FAST while there is FAST dissector available in wireshark GUI version. What's the best way to dissect a massive pcap file?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">large dissector pcap fast</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Feb '13, 13:29</strong></p><img src="https://secure.gravatar.com/avatar/023ec4b0dfece2e93187a50ec2fee0d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fhaghigh&#39;s gravatar image" /><p>fhaghigh<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fhaghigh has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Feb '13, 18:57</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-18785" class="comments-container"></div><div id="comment-tools-18785" class="comment-tools"></div><div class="clear"></div><div id="comment-18785-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18787"></span>

<div id="answer-container-18787" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18787-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you talking about the <a href="http://code.google.com/p/fast-wireshark/">FAST dissector plugin</a>? If so, then it might be better to ask the authors of that plugin how and if it works with your version of Wireshark.</p><p>Their web site</p><blockquote><p><code>http://code.google.com/p/fast-wireshark/</code><br />
</p></blockquote><p>There is an example how to "decode as FAST" (tshark option -o).</p><blockquote><p><code>http://code.google.com/p/fast-wireshark/source/browse/trunk/util/client/example-tshark.sh</code><br />
</p></blockquote><p>Regarding your question how to split a large capture file. Please read the following questions/answers.</p><blockquote><p><code>http://ask.wireshark.org/questions/18730/problem-in-opening-large-size-wireshark-file</code><br />
<code>http://ask.wireshark.org/questions/16690/split-pcap-file-into-smaller-pcap-file-according-to-tcp-flow</code><br />
</p></blockquote><p>Maybe SplitCap and/or CapLoader are also interesting for you</p><blockquote><p><code>http://www.netresec.com/?page=SplitCap</code><br />
<code>http://www.netresec.com/?page=CapLoader</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Feb '13, 14:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Feb '13, 14:16</p></div></div><div id="comments-container-18787" class="comments-container"><span id="18799"></span><div id="comment-18799" class="comment"><div id="post-18799-score" class="comment-score"></div><div class="comment-text"><p>Thanks so much for your help.</p></div><div id="comment-18799-info" class="comment-info"><span class="comment-age">(21 Feb '13, 06:33)</span> fhaghigh</div></div><span id="18800"></span><div id="comment-18800" class="comment"><div id="post-18800-score" class="comment-score"></div><div class="comment-text"><p>You're welcome.</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-18800-info" class="comment-info"><span class="comment-age">(21 Feb '13, 08:01)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-18787" class="comment-tools"></div><div class="clear"></div><div id="comment-18787-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

