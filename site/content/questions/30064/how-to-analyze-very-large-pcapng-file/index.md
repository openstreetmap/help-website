+++
type = "question"
title = "How to analyze very large pcapng file?"
description = '''I have a very large pcapng file (about 21GB), and I want to analyze the file in wireshark. Should I split it into small files with editcap? Can editcap handle such a large file? If not, how to do?'''
date = "2014-02-20T17:31:00Z"
lastmod = "2014-02-23T18:56:00Z"
weight = 30064
keywords = [ "very", "large", "analyze", "file" ]
aliases = [ "/questions/30064" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to analyze very large pcapng file?](/questions/30064/how-to-analyze-very-large-pcapng-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30064-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a very large pcapng file (about 21GB), and I want to analyze the file in wireshark. Should I split it into small files with editcap? Can editcap handle such a large file? If not, how to do?</p></div><div id="question-tags" class="tags-container tags">very large analyze file</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Feb '14, 17:31</strong></p><img src="https://secure.gravatar.com/avatar/13679628c84abac93be65773340d2589?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="metamatrix&#39;s gravatar image" /><p>metamatrix<br />
<span class="score" title="56 reputation points">56</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="metamatrix has one accepted answer">100%</span></p></div></div><div id="comments-container-30064" class="comments-container"></div><div id="comment-tools-30064" class="comment-tools"></div><div class="clear"></div><div id="comment-30064-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="30070"></span>

<div id="answer-container-30070" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30070-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>editcap <strong>should</strong> be able to handle the file and it think it's <strong>absolutely</strong> necessary to split or pre-filter the file, as there is no way to load a 21GB file into wireshark or tshark.</p><p>You can pre-filter the file with tcpdump (e.g. in Linux), by using capture filter, if you know what to look for</p><blockquote><p>tcpdump -nr input.pcap -w output_x_y.pcap 'host x.x.x.x or host y.y.y.y'</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Feb '14, 21:48</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-30070" class="comments-container"><span id="30073"></span><div id="comment-30073" class="comment"><div id="post-30073-score" class="comment-score"></div><div class="comment-text"><p>Thank you,Kurt. Should I use editcap directly on Windows to split the file? What's the proper parameters if I want to split this file into 2GB files?</p></div><div id="comment-30073-info" class="comment-info"><span class="comment-age">(20 Feb '14, 23:09)</span> metamatrix</div></div><span id="30083"></span><div id="comment-30083" class="comment"><div id="post-30083-score" class="comment-score"></div><div class="comment-text"><p>You can do it on any platform that editcap supports. Unfortunately you cannot split based on file size with editcap, but you can split based on time and/or number of frames, see the editcap man page. If you need the size feature, there are other tools. Just google for: 'pcap file split'</p></div><div id="comment-30083-info" class="comment-info"><span class="comment-age">(21 Feb '14, 08:44)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-30070" class="comment-tools"></div><div class="clear"></div><div id="comment-30070-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30113"></span>

<div id="answer-container-30113" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30113-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please try splitcap, its a free tool that can be used for filtering very large PCAP files. its very fast and efficient. With a few operators you can split a large file into into its individual IP pair conversations of even further port pair's</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Feb '14, 18:56</strong></p><img src="https://secure.gravatar.com/avatar/3e5e9d76a54debaa630d909e37048da8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="deepacket&#39;s gravatar image" /><p>deepacket<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="deepacket has no accepted answers">0%</span></p></div></div><div id="comments-container-30113" class="comments-container"></div><div id="comment-tools-30113" class="comment-tools"></div><div class="clear"></div><div id="comment-30113-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

