+++
type = "question"
title = "reassembled tcp bytes cannot be displayed"
description = '''Running version 1.8.0. When Wireshark opens a captured file, the reassembled tcp bytes cannot be displayed in the Packet Bytes Pane, and the corresponding packet bytes cannot be displayed either. How can I fix it?  UPDATE: '''
date = "2012-06-28T20:41:00Z"
lastmod = "2012-09-25T19:18:00Z"
weight = 12298
keywords = [ "reassembly", "tcp" ]
aliases = [ "/questions/12298" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [reassembled tcp bytes cannot be displayed](/questions/12298/reassembled-tcp-bytes-cannot-be-displayed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12298-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Running version 1.8.0. When Wireshark opens a captured file, the reassembled tcp bytes cannot be displayed in the Packet Bytes Pane, and the corresponding packet bytes cannot be displayed either.</p><p>How can I fix it?</p><p><strong>UPDATE:</strong></p><p><img src="https://osqa-ask.wireshark.org/upfiles/reassembled_tcp_3.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">reassembly tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jun '12, 20:41</strong></p><img src="https://secure.gravatar.com/avatar/85b30d9eb7197478a7e0ed4159ea28b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mildblues&#39;s gravatar image" /><p>mildblues<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mildblues has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 30 Jun '12, 03:48</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-12298" class="comments-container"><span id="12304"></span><div id="comment-12304" class="comment"><div id="post-12304-score" class="comment-score"></div><div class="comment-text"><p>please post a screenshot.</p></div><div id="comment-12304-info" class="comment-info"><span class="comment-age">(29 Jun '12, 02:14)</span> Kurt Knochner ♦</div></div><span id="12356"></span><div id="comment-12356" class="comment"><div id="post-12356-score" class="comment-score"></div><div class="comment-text"><p>did you try to re-install and delete the "personal settings" (only if you don't need them!!)?</p></div><div id="comment-12356-info" class="comment-info"><span class="comment-age">(01 Jul '12, 03:25)</span> Kurt Knochner ♦</div></div><span id="12389"></span><div id="comment-12389" class="comment"><div id="post-12389-score" class="comment-score"></div><div class="comment-text"><p>Yes, I have tried re-install and delete the "personal settings", but the problem remains.</p><p>I have also tried intsall Wireshark version 1.8.0 on a clean Windows XP OS, and the problem remains, too.</p></div><div id="comment-12389-info" class="comment-info"><span class="comment-age">(03 Jul '12, 01:53)</span> mildblues</div></div><span id="12390"></span><div id="comment-12390" class="comment"><div id="post-12390-score" class="comment-score"></div><div class="comment-text"><p>Not much help to you, but it works fine for me. Is it possible to share your capture, e.g. on <a href="http://cloudshark.org/">cloudshark</a> just in case there is something odd in there.</p></div><div id="comment-12390-info" class="comment-info"><span class="comment-age">(03 Jul '12, 04:55)</span> grahamb ♦</div></div><span id="12428"></span><div id="comment-12428" class="comment"><div id="post-12428-score" class="comment-score"></div><div class="comment-text"><p>I have uploaded a captured file on cloudshark. Its url is <a href="https://www.cloudshark.org/captures/cc139051433b">https://www.cloudshark.org/captures/cc139051433b</a></p></div><div id="comment-12428-info" class="comment-info"><span class="comment-age">(03 Jul '12, 20:47)</span> mildblues</div></div><span id="12446"></span><div id="comment-12446" class="comment not_top_scorer"><div id="post-12446-score" class="comment-score"></div><div class="comment-text"><p>no problem here...</p></div><div id="comment-12446-info" class="comment-info"><span class="comment-age">(04 Jul '12, 11:23)</span> Kurt Knochner ♦</div></div><span id="12618"></span><div id="comment-12618" class="comment not_top_scorer"><div id="post-12618-score" class="comment-score"></div><div class="comment-text"><p>No Problem on <a href="http://Cloudshark.com">Cloudshark.com</a> either. But then again, it does not look like the same capture file...</p></div><div id="comment-12618-info" class="comment-info"><span class="comment-age">(11 Jul '12, 05:08)</span> SYN-bit ♦♦</div></div><span id="14522"></span><div id="comment-14522" class="comment not_top_scorer"><div id="post-14522-score" class="comment-score"></div><div class="comment-text"><p>The OS on my computer is simplified Chinese version Windows XP.</p><p>Maybe Wireshark 1.8 doesn't work well on it?</p><p>However, Wireshark 1.6.5 works well.</p></div><div id="comment-14522-info" class="comment-info"><span class="comment-age">(25 Sep '12, 18:53)</span> mildblues</div></div></div><div id="comment-tools-12298" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-12298-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14523"></span>

<div id="answer-container-14523" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14523-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is a known problem, being tracked as <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7185">bug 7185</a> and <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7629">bug 7629</a>. As indicated in those bug reports, there has apparently been a fix for this, but it has not been backported to the 1.8 branch yet. Unfortunately, due to the extent of the changes made, it may not be backported.</p><p>In the meantime, as indicated in the bug reports, you might want to try one of the latest <a href="https://www.wireshark.org/download/automated/">automated</a> builds, which should resolve this problem for you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '12, 19:18</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-14523" class="comments-container"><span id="15175"></span><div id="comment-15175" class="comment"><div id="post-15175-score" class="comment-score"></div><div class="comment-text"><p>yeah, the automated builds work well. thanks!</p></div><div id="comment-15175-info" class="comment-info"><span class="comment-age">(22 Oct '12, 23:59)</span> mildblues</div></div></div><div id="comment-tools-14523" class="comment-tools"></div><div class="clear"></div><div id="comment-14523-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

