+++
type = "question"
title = "Can&#x27;t reanimate a capture file."
description = '''I cannot open a file from a packet capture. Granted the file size is 1.9 GBs. When attempting to open the file I receive this message several minutes later... &quot;This application has requested the Runtime to terminate it in an unusual way. Microsoft Visual C++ Runtime Library&quot; Is this due to the size ...'''
date = "2011-04-22T10:15:00Z"
lastmod = "2011-04-22T10:38:00Z"
weight = 3691
keywords = [ "capture", "open", "help", "file" ]
aliases = [ "/questions/3691" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can't reanimate a capture file.](/questions/3691/cant-reanimate-a-capture-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3691-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3691-score" class="post-score" title="current number of votes">0</div><span id="post-3691-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I cannot open a file from a packet capture. Granted the file size is 1.9 GBs. When attempting to open the file I receive this message several minutes later... "This application has requested the Runtime to terminate it in an unusual way. Microsoft Visual C++ Runtime Library" Is this due to the size of the capture file? Please help, or can someone step me through it? Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-open" rel="tag" title="see questions tagged &#39;open&#39;">open</span> <span class="post-tag tag-link-help" rel="tag" title="see questions tagged &#39;help&#39;">help</span> <span class="post-tag tag-link-file" rel="tag" title="see questions tagged &#39;file&#39;">file</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '11, 10:15</strong></p><img src="https://secure.gravatar.com/avatar/cef1b8b79894c97c4c2096932c5dbf72?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="digirati&#39;s gravatar image" /><p><span>digirati</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="digirati has no accepted answers">0%</span></p></div></div><div id="comments-container-3691" class="comments-container"></div><div id="comment-tools-3691" class="comment-tools"></div><div class="clear"></div><div id="comment-3691-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3693"></span>

<div id="answer-container-3693" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3693-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3693-score" class="post-score" title="current number of votes">1</div><span id="post-3693-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, this is due to the size of the capture file, it is probably too big to be loaded into Wireshark. What you can do is use the command line tool editcap to cut it into smaller files, for example</p><pre><code>editcap -c 100000 &lt;yourbigfile&gt; &lt;outfile&gt;</code></pre><p>You'll get a couple of files with 100,000 frames each, which should work without problems. Editcap is installed along Wireshark into the program directory.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '11, 10:31</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Apr '11, 10:31</strong> </span></p></div></div><div id="comments-container-3693" class="comments-container"><span id="3694"></span><div id="comment-3694" class="comment"><div id="post-3694-score" class="comment-score"></div><div class="comment-text"><p>See also <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">http://wiki.wireshark.org/KnownBugs/OutOfMemory</a></p></div><div id="comment-3694-info" class="comment-info"><span class="comment-age">(22 Apr '11, 10:38)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-3693" class="comment-tools"></div><div class="clear"></div><div id="comment-3693-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

