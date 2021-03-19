+++
type = "question"
title = "Mac OS X 10.6.6 - Wireshark capture starves other apps of data"
description = '''Running Wireshark 1.4.3 64-bit on a MacBook Pro (model MacBookPro2,2 according to System Profiler). If I start capturing on the ethernet port, after about a second or two of capturing everything it sees, two things happen: (a) only packets generated on the computer (or targeted to the computer) get ...'''
date = "2011-01-25T12:00:00Z"
lastmod = "2011-01-25T12:00:00Z"
weight = 1931
keywords = [ "osx", "macbook", "10.6.6" ]
aliases = [ "/questions/1931" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Mac OS X 10.6.6 - Wireshark capture starves other apps of data](/questions/1931/mac-os-x-1066-wireshark-capture-starves-other-apps-of-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1931-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Running Wireshark 1.4.3 64-bit on a MacBook Pro (model MacBookPro2,2 according to System Profiler). If I start capturing on the ethernet port, after about a second or two of capturing everything it sees, two things happen:</p><p>(a) only packets generated on the computer (or targeted to the computer) get captured (b) no other process running on the computer can transmit or receive data over the network</p><p>Is there a way around this? (And yes, the ChmodBPF script is in place and operating properly).</p><p>John Francini</p></div><div id="question-tags" class="tags-container tags">osx macbook 10.6.6</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jan '11, 12:00</strong></p><img src="https://secure.gravatar.com/avatar/57e3f874031295d056188031ff295ef8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="francini&#39;s gravatar image" /><p>francini<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="francini has no accepted answers">0%</span></p></div></div><div id="comments-container-1931" class="comments-container"><span id="1933"></span><div id="comment-1933" class="comment"><div id="post-1933-score" class="comment-score"></div><div class="comment-text"><p>Does this also happen if you capture with tcpdump? If so, it's probably a bug in OS X's BPF.</p><p>The OS version - I assume it's 10.6.6 - is probably more important than the hardware.</p></div><div id="comment-1933-info" class="comment-info"><span class="comment-age">(25 Jan '11, 14:50)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-1931" class="comment-tools"></div><div class="clear"></div><div id="comment-1931-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

