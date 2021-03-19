+++
type = "question"
title = "1.10.6-7: Memory Leak"
description = '''Running either 1.10.6 or 1.10.7 I can watch the memory usage of wireshark.exe continue to climb until it finally crashes. Setup;  Windows 7 64-bit 600GB Intel SSD Dual core Atom processor 2GB mem Capture to multiple files, 10MB each Working via remote desktop Capturing with disply of packets turned ...'''
date = "2014-04-23T15:23:00Z"
lastmod = "2014-04-23T16:32:00Z"
weight = 32131
keywords = [ "memory_leak" ]
aliases = [ "/questions/32131" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [1.10.6-7: Memory Leak](/questions/32131/1106-7-memory-leak)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32131-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32131-score" class="post-score" title="current number of votes">0</div><span id="post-32131-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Running either 1.10.6 or 1.10.7 I can watch the memory usage of wireshark.exe continue to climb until it finally crashes.</p><p>Setup;</p><ul><li>Windows 7 64-bit</li><li>600GB Intel SSD</li><li>Dual core Atom processor</li><li>2GB mem</li><li>Capture to multiple files, 10MB each</li><li>Working via remote desktop</li><li>Capturing with disply of packets turned off (update of packets in real time unchecked).</li></ul><p>Wireshark starts with about 54MB of memory. As soon as I start the capture it climbs to just over 159MB. While its running I can watch the memory continue to climb at a rate of 8-20k per second. Note that dumpcap remains around 3MB at all times.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-memory_leak" rel="tag" title="see questions tagged &#39;memory_leak&#39;">memory_leak</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '14, 15:23</strong></p><img src="https://secure.gravatar.com/avatar/b588ec81dd49f3fb8719dc5c098f541b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="VanAwful&#39;s gravatar image" /><p><span>VanAwful</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="VanAwful has no accepted answers">0%</span></p></div></div><div id="comments-container-32131" class="comments-container"></div><div id="comment-tools-32131" class="comment-tools"></div><div class="clear"></div><div id="comment-32131-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="32135"></span>

<div id="answer-container-32135" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32135-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32135-score" class="post-score" title="current number of votes">2</div><span id="post-32135-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is not a memory leak, it is just Wireshark creating and holding additional information about the packets, like reassembly data. Dumpcap just writes files without creating that kind of data, which is why its memory consumption is stable.</p><p>See this blog post for more info: <a href="http://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/">http://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '14, 15:39</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-32135" class="comments-container"></div><div id="comment-tools-32135" class="comment-tools"></div><div class="clear"></div><div id="comment-32135-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="32136"></span>

<div id="answer-container-32136" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32136-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32136-score" class="post-score" title="current number of votes">0</div><span id="post-32136-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Is your display depth set to 16 bits? If so this might be due to a <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9914">memory leak in GTK+</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '14, 16:32</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-32136" class="comments-container"></div><div id="comment-tools-32136" class="comment-tools"></div><div class="clear"></div><div id="comment-32136-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

