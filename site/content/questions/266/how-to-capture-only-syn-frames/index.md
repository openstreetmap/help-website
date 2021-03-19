+++
type = "question"
title = "how to capture only SYN frames"
description = '''I have been working at a client site where i am only interested in capturing SYN frames. I was unable to locate any way to set a capture filter that would accomplish this task. I was wondering if there is a way to capture using offset to the point where the TCP SYN flag is...? In display filter, I w...'''
date = "2010-09-22T11:36:00Z"
lastmod = "2010-09-22T11:55:00Z"
weight = 266
keywords = [ "capture-filter", "display-filter" ]
aliases = [ "/questions/266" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [how to capture only SYN frames](/questions/266/how-to-capture-only-syn-frames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-266-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have been working at a client site where i am only interested in capturing SYN frames. I was unable to locate any way to set a capture filter that would accomplish this task. I was wondering if there is a way to capture using offset to the point where the TCP SYN flag is...?</p><p>In display filter, I was able to set a filter "flags.tcp.syn", but for some reason, it did not show me only syn frames but alot of what looked like PSH ACK frames as well.</p><p>Thanks for any advice or recommendations on how to capture just the SYN frames.</p><p>kmnruser</p></div><div id="question-tags" class="tags-container tags">capture-filter display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '10, 11:36</strong></p><img src="https://secure.gravatar.com/avatar/9e96b23e3495316e470ba9b487b82a73?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kmnruser&#39;s gravatar image" /><p>kmnruser<br />
<span class="score" title="26 reputation points">26</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kmnruser has no accepted answers">0%</span></p></div></div><div id="comments-container-266" class="comments-container"></div><div id="comment-tools-266" class="comment-tools"></div><div class="clear"></div><div id="comment-266-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="267"></span>

<div id="answer-container-267" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-267-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The filter "tcp.flags.syn" will select all the frames that have the flag tcp.flags.syn, which will be every TCP packet. What you want to filter on is "tcp.flags.syn==1" to make sure you only select the frames which have the SYN bit set. You might even want to add "... and tcp.flags.ack==0" to make sure you only select the SYN packets and not the SYN/ACK packets.</p><p>Now, back to the capture filter. You can use the filter "tcp[0xd]&amp;2=2" which will capture all the frames with the SYN bit set (SYN as well as SYN/ACK). Or use "tcp[0xd]&amp;18=2" to capture only SYN packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '10, 11:55</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Feb '11, 12:10</p></div></div><div id="comments-container-267" class="comments-container"><span id="278"></span><div id="comment-278" class="comment"><div id="post-278-score" class="comment-score"></div><div class="comment-text"><p>SYNbit<br />
Thanks for the great response! Those filters are exactly what I need, and it goes without say that they will make life easier moving forward. Awesome answer! KMNRUser</p></div><div id="comment-278-info" class="comment-info"><span class="comment-age">(22 Sep '10, 15:06)</span> kmnruser</div></div><span id="2354"></span><div id="comment-2354" class="comment"><div id="post-2354-score" class="comment-score"></div><div class="comment-text"><p>I think the correct filter for SYNs and SYN/ACKs is "tcp[0xd]&amp;2=2"</p></div><div id="comment-2354-info" class="comment-info"><span class="comment-age">(15 Feb '11, 12:02)</span> BusiPlay</div></div><span id="2355"></span><div id="comment-2355" class="comment"><div id="post-2355-score" class="comment-score"></div><div class="comment-text"><p>You're absolutely right. I will change it, thanks!</p></div><div id="comment-2355-info" class="comment-info"><span class="comment-age">(15 Feb '11, 12:10)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-267" class="comment-tools"></div><div class="clear"></div><div id="comment-267-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

