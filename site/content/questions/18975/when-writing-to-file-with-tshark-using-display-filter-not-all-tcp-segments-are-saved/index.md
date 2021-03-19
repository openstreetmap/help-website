+++
type = "question"
title = "When writing to file with tshark using display filter, not all TCP segments are saved."
description = '''When a application like SIP has a message that spans multiple TCP segments, if I filter on the application using the wireshark GUI, then export displayed packets as a new file, it successfully saves all the TCP segments that form each SIP request/response. However, if I do the same thing via tshark,...'''
date = "2013-02-28T07:05:00Z"
lastmod = "2013-03-02T08:57:00Z"
weight = 18975
keywords = [ "export", "tshark", "display-filter" ]
aliases = [ "/questions/18975" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [When writing to file with tshark using display filter, not all TCP segments are saved.](/questions/18975/when-writing-to-file-with-tshark-using-display-filter-not-all-tcp-segments-are-saved)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18975-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When a application like SIP has a message that spans multiple TCP segments, if I filter on the application using the wireshark GUI, then export displayed packets as a new file, it successfully saves all the TCP segments that form each SIP request/response.</p><p>However, if I do the same thing via tshark, it does NOT save all the segments, and I'm left in incomplete data.</p><p>Example: tshark -r big_trace.pcap -R 'sip.Call-ID == whatever' -w filtered.pcap</p><p>If big_trace.pcap contains large SIP requests/responses that span multiple TCP segments, the new file, filtered.pcap, will not contain all those segments, leaving me with incomplete data.</p><p>Sometimes I end up with very large captures that my customers provide and they're too large to work with in the GUI, so I want to filter out what I need with the CLI tool and then look at the resulting data in the GUI.</p></div><div id="question-tags" class="tags-container tags">export tshark display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '13, 07:05</strong></p><img src="https://secure.gravatar.com/avatar/89981ff7056cf5f19881f813132a2390?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gsgleason&#39;s gravatar image" /><p>gsgleason<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gsgleason has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Feb '13, 07:07</p></div></div><div id="comments-container-18975" class="comments-container"><span id="18977"></span><div id="comment-18977" class="comment"><div id="post-18977-score" class="comment-score"></div><div class="comment-text"><p>I have also noticed this. I was under the impression that the tshark CLI filters are equivalent to the wireshark displays filters. I am using version 1.8.5.</p></div><div id="comment-18977-info" class="comment-info"><span class="comment-age">(28 Feb '13, 07:17)</span> jclogan</div></div></div><div id="comment-tools-18975" class="comment-tools"></div><div class="clear"></div><div id="comment-18975-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="19092"></span>

<div id="answer-container-19092" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19092-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Apparently <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8223">bug 8223</a> already covers this. There's a patch to fix it, but waiting on a decision of how to invoke this new behavior from tshark's command options.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Mar '13, 08:57</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-19092" class="comments-container"><span id="19095"></span><div id="comment-19095" class="comment"><div id="post-19095-score" class="comment-score"></div><div class="comment-text"><p>Thanks. I did find the bug report and saw your comments there as well. I will wait patiently for an enhancement.</p></div><div id="comment-19095-info" class="comment-info"><span class="comment-age">(02 Mar '13, 12:17)</span> gsgleason</div></div></div><div id="comment-tools-19092" class="comment-tools"></div><div class="clear"></div><div id="comment-19092-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19008"></span>

<div id="answer-container-19008" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19008-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I believe Wireshark didn't export the other TCP segments either, until just last year when <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3315">enhancement 3315</a> was implemented. But that only added support for Wireshark doing it, not tshark. I suggest you submit a new enhancement request for this for tshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '13, 21:08</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-19008" class="comments-container"><span id="19031"></span><div id="comment-19031" class="comment"><div id="post-19031-score" class="comment-score"></div><div class="comment-text"><p>I would have expected it to work by passing the <code>-2</code> option to tshark, but unfortunately that wasn't the case in my testing. So yeah, it looks like a new bug request is in order.</p></div><div id="comment-19031-info" class="comment-info"><span class="comment-age">(01 Mar '13, 07:18)</span> cmaynard ♦♦</div></div><span id="19067"></span><div id="comment-19067" class="comment"><div id="post-19067-score" class="comment-score"></div><div class="comment-text"><p>It definitely will also require a second pass, maybe even a third. But right now the code that does the dependency settings/checking for previous frames only exists in Wireshark.</p></div><div id="comment-19067-info" class="comment-info"><span class="comment-age">(01 Mar '13, 13:01)</span> Hadriel</div></div></div><div id="comment-tools-19008" class="comment-tools"></div><div class="clear"></div><div id="comment-19008-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18985"></span>

<div id="answer-container-18985" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18985-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Sometimes I end up with very large captures that my customers provide and they're too large to work with in the GUI, so I want to filter out what I need with the CLI tool and then look at the resulting data in the GUI.</p></blockquote><p>O.K. then you need to first get the TCP stream and then, in a second step, you can write all frames of that stream to a file.</p><blockquote><p>`tshark -r big_trace.pcap -R 'sip.Call-ID == whatever' -T fields -e tcp.stream</p></blockquote><p>Then take all the stream numbers of that output and run tshark</p><blockquote><p><code>tshark -r big_trace.pcap -R 'tcp.stream == xxx or tcp.stream == yy' -w filtered.pcap</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '13, 09:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-18985" class="comments-container"><span id="18986"></span><div id="comment-18986" class="comment"><div id="post-18986-score" class="comment-score"></div><div class="comment-text"><p>Kurt, In this case, however, the TCP stream contains many different SIP calls. The application has one socket up for all traffic.</p></div><div id="comment-18986-info" class="comment-info"><span class="comment-age">(28 Feb '13, 10:14)</span> gsgleason</div></div><span id="18987"></span><div id="comment-18987" class="comment"><div id="post-18987-score" class="comment-score"></div><div class="comment-text"><blockquote><p>however, the TCP stream contains many different SIP calls.</p></blockquote><p>in that case, how did you filter the data in wireshark?</p></div><div id="comment-18987-info" class="comment-info"><span class="comment-age">(28 Feb '13, 10:18)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-18985" class="comment-tools"></div><div class="clear"></div><div id="comment-18985-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

