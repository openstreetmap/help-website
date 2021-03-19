+++
type = "question"
title = "how does ringbuffer work in dumpcap ?"
description = '''Hi all,  I found here http://code.metager.de/source/xref/wireshark/dumpcap.c the implementation of dumpcap. 1) is it the right code / algorithm ? 2) if 1) is true then which part of the code shows us the old file deletion when the file number limit is reached ? is there really old file deletion or t...'''
date = "2014-05-07T06:54:00Z"
lastmod = "2014-05-07T07:30:00Z"
weight = 32595
keywords = [ "dumpacp", "ringbuffer" ]
aliases = [ "/questions/32595" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how does ringbuffer work in dumpcap ?](/questions/32595/how-does-ringbuffer-work-in-dumpcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32595-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32595-score" class="post-score" title="current number of votes">0</div><span id="post-32595-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I found here <a href="http://code.metager.de/source/xref/wireshark/dumpcap.c">http://code.metager.de/source/xref/wireshark/dumpcap.c</a> the implementation of dumpcap. 1) is it the right code / algorithm ? 2) if 1) is true then which part of the code shows us the old file deletion when the file number limit is reached ? is there really old file deletion or the old file is truncated ?</p><p>Thanks for your help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dumpacp" rel="tag" title="see questions tagged &#39;dumpacp&#39;">dumpacp</span> <span class="post-tag tag-link-ringbuffer" rel="tag" title="see questions tagged &#39;ringbuffer&#39;">ringbuffer</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '14, 06:54</strong></p><img src="https://secure.gravatar.com/avatar/31856543dad1a12f24073c17126cb1e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ikuzar&#39;s gravatar image" /><p><span>ikuzar</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ikuzar has no accepted answers">0%</span></p></div></div><div id="comments-container-32595" class="comments-container"></div><div id="comment-tools-32595" class="comment-tools"></div><div class="clear"></div><div id="comment-32595-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32601"></span>

<div id="answer-container-32601" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32601-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32601-score" class="post-score" title="current number of votes">2</div><span id="post-32601-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Odd place to be looking at Wireshark code, why not use the <strong>actual</strong> <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=tree">Wireshark repository</a>?</p><p>I think you want function <code>ringbuf_switch_file()</code> in <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=ringbuffer.c">ringbuffer.c</a> which then calls <code>ringbuf_open_file()</code> for the new filename, and if that exists then it calls <code>ws_unlink()</code> on it (in <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=wsutil/file_util.c">wsutil/file_util.c</a>). Depending on your platform, <code>ws_unlink()</code> then calls the appropriate unlink function.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '14, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-32601" class="comments-container"></div><div id="comment-tools-32601" class="comment-tools"></div><div class="clear"></div><div id="comment-32601-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

