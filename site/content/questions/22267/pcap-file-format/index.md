+++
type = "question"
title = ".pcap File format"
description = '''hey , I need to develop a program that saves a file in .pcap format , I have no information about this format , I would like to know the structure of a file .pcap. Please can anywone help me. Thank you '''
date = "2013-06-24T01:52:00Z"
lastmod = "2013-06-24T18:33:00Z"
weight = 22267
keywords = [ "pcap" ]
aliases = [ "/questions/22267" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [.pcap File format](/questions/22267/pcap-file-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22267-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hey ,</p><p>I need to develop a program that saves a file in .pcap format , I have no information about this format , I would like to know the structure of a file .pcap.</p><p>Please can anywone help me.</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags">pcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jun '13, 01:52</strong></p><img src="https://secure.gravatar.com/avatar/9fbe9f669a6d14e31178d8193125c39a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cruz&#39;s gravatar image" /><p>cruz<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cruz has no accepted answers">0%</span></p></div></div><div id="comments-container-22267" class="comments-container"></div><div id="comment-tools-22267" class="comment-tools"></div><div class="clear"></div><div id="comment-22267-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22268"></span>

<div id="answer-container-22268" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22268-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could google for it, and find pages like this:</p><p><a href="http://wiki.wireshark.org/Development/LibpcapFileFormat">http://wiki.wireshark.org/Development/LibpcapFileFormat</a></p><p>or, better yet, use the new PCAPng format:</p><p><a href="http://www.winpcap.org/ntar/draft/PCAP-DumpFileFormat.html">http://www.winpcap.org/ntar/draft/PCAP-DumpFileFormat.html</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '13, 01:57</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-22268" class="comments-container"><span id="22269"></span><div id="comment-22269" class="comment"><div id="post-22269-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your answer</p></div><div id="comment-22269-info" class="comment-info"><span class="comment-age">(24 Jun '13, 02:00)</span> cruz</div></div><span id="22270"></span><div id="comment-22270" class="comment"><div id="post-22270-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-22270-info" class="comment-info"><span class="comment-age">(24 Jun '13, 02:17)</span> grahamb ♦</div></div></div><div id="comment-tools-22268" class="comment-tools"></div><div class="clear"></div><div id="comment-22268-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22301"></span>

<div id="answer-container-22301" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22301-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I need to develop a program that saves a file in .pcap format</p></blockquote><p>You could also try using libpcap/WinPcap to write the file out. You need a <code>pcap_t</code> in order to create the pcap file with libpcap/WinPcap when you call <code>pcap_dump_open()</code>, but in current versions of libpcap you can use <code>pcap_open_dead()</code> to get a <code>pcap_t</code> with a specified link-layer header type and snapshot length.</p><p>(If you're already using libpcap/WinPcap to capture packets or read an existing pcap or pcap-ng file, you already have a <code>pcap_t</code>.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '13, 18:33</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-22301" class="comments-container"></div><div id="comment-tools-22301" class="comment-tools"></div><div class="clear"></div><div id="comment-22301-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

