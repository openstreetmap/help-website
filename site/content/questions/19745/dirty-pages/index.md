+++
type = "question"
title = "Dirty pages"
description = '''How to find number of dirty pages using wireshark?'''
date = "2013-03-22T00:16:00Z"
lastmod = "2013-03-22T00:34:00Z"
weight = 19745
keywords = [ "dirty", "pages" ]
aliases = [ "/questions/19745" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Dirty pages](/questions/19745/dirty-pages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19745-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to find number of dirty pages using wireshark?</p></div><div id="question-tags" class="tags-container tags">dirty pages</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '13, 00:16</strong></p><img src="https://secure.gravatar.com/avatar/b94d0e14c0341f26caa6dd992f79a055?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Geek&#39;s gravatar image" /><p>Geek<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Geek has no accepted answers">0%</span></p></div></div><div id="comments-container-19745" class="comments-container"></div><div id="comment-tools-19745" class="comment-tools"></div><div class="clear"></div><div id="comment-19745-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19746"></span>

<div id="answer-container-19746" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19746-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark watches network traffic.</p><p>If your system has a local hard drive or solid-state drive, at least some of the dirty pages are backed by "swap space" (a swap partition or a swap file/paging file/whatever the OS calls it) that's on the local drive, so if those pages are written to the backing store, that doesn't involve any network traffic, so Wireshark won't see it.</p><p>Even if you happen to be paging to a file over the network, dirty pages won't show up in the network traffic until the system needs to write them to the backing store.</p><p>Therefore, Wireshark is <em>not</em> the right tool to use to determine how many dirty pages are in main memory. You should use whatever tools your operating system provides for this, if any. Different operating systems may provide different tools, although some of the "free software" desktop environments <em>might</em> have portable GUI tools that can use the operating-system-dependent APIs on Linux/*BSD/Solaris/etc. to find a free-page count.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '13, 00:34</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-19746" class="comments-container"></div><div id="comment-tools-19746" class="comment-tools"></div><div class="clear"></div><div id="comment-19746-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

