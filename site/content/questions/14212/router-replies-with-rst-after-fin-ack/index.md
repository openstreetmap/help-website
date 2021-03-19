+++
type = "question"
title = "Router replies with [RST] after [FIN, ACK]"
description = '''I&#x27;m testing an application which downloads info from photovoltaic equipment, so I have to connect to a remote power plant via Internet, using a TCP connection, I download info with my application and then I disconnect... Sometimes when I try to reconnect with remote power plant after few minutes, I ...'''
date = "2012-09-12T09:56:00Z"
lastmod = "2012-09-13T10:49:00Z"
weight = 14212
keywords = [ "ack", "router", "fin", "tcp", "rst" ]
aliases = [ "/questions/14212" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Router replies with \[RST\] after \[FIN, ACK\]](/questions/14212/router-replies-with-rst-after-fin-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14212-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14212-score" class="post-score" title="current number of votes">0</div><span id="post-14212-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm testing an application which downloads info from photovoltaic equipment, so I have to connect to a remote power plant via Internet, using a TCP connection, I download info with my application and then I disconnect... Sometimes when I try to reconnect with remote power plant after few minutes, I can't do it, so, looking for a clue I have started capturing packets with wireshark and I can see that sometimes I send [FIN, ACK] and I get [ACK], then I get [FIN,ACK] and I send [ACK] and everything is OK for next connection, but sometimes I send [FIN,ACK] and I get [RST] and then I have to wait about 5 minutes before I can reconnect with remote router........ Any idea?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-router" rel="tag" title="see questions tagged &#39;router&#39;">router</span> <span class="post-tag tag-link-fin" rel="tag" title="see questions tagged &#39;fin&#39;">fin</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '12, 09:56</strong></p><img src="https://secure.gravatar.com/avatar/a696635d4120877e20a5414259e82696?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pedrojpz&#39;s gravatar image" /><p><span>pedrojpz</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pedrojpz has no accepted answers">0%</span></p></div></div><div id="comments-container-14212" class="comments-container"></div><div id="comment-tools-14212" class="comment-tools"></div><div class="clear"></div><div id="comment-14212-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="14222"></span>

<div id="answer-container-14222" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14222-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14222-score" class="post-score" title="current number of votes">1</div><span id="post-14222-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It sounds like (from your description) that the photovoltaic equipment is getting stuck in some FINWAIT state. In other words, it's not gracefully handling the tcp tear down and when that happens, you have to wait for a timeout (some multiples of MSL). I'm not sure you'll be able to do anything since you probably can't touch the tcp stack.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '12, 14:30</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p><span>hansangb</span><br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span></p></div></div><div id="comments-container-14222" class="comments-container"><span id="14226"></span><div id="comment-14226" class="comment"><div id="post-14226-score" class="comment-score"></div><div class="comment-text"><p>This is driving me crazy... Thanks for your reply.</p></div><div id="comment-14226-info" class="comment-info"><span class="comment-age">(13 Sep '12, 00:50)</span> <span class="comment-user userinfo">pedrojpz</span></div></div><span id="14238"></span><div id="comment-14238" class="comment"><div id="post-14238-score" class="comment-score"></div><div class="comment-text"><p>I'd try to capture as close as possible to the remote system to see if what you send gets there unmodified. That way you can also have an unbiased look at the exact stack behaviour of the photovoltaic system, and see if Hansang's idea seems plausible (in which case you'll have to kick the vendor of the thing to get it's stack done right). Industrial TCP stacks in embedded systems are a certifiable nightmare in my experience, the developers seem to stick to RFCs only as much as they absolutely have to to get the thing to work under perfect circumstances...</p></div><div id="comment-14238-info" class="comment-info"><span class="comment-age">(13 Sep '12, 10:19)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-14222" class="comment-tools"></div><div class="clear"></div><div id="comment-14222-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14239"></span>

<div id="answer-container-14239" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14239-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14239-score" class="post-score" title="current number of votes">0</div><span id="post-14239-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>but sometimes I send [FIN,ACK] and I get [RST] and then I have to wait about 5 minutes before I can reconnect with remote router........ Any idea?</p></blockquote><p>Just a wild idea...</p><p>sounds like the service that handles the TCP port crashes and then the OS sends a RST, as the local socket is no longer available. Then after 5 minutes some kind of 'watchdog' restarts the service and then you can reconnect.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '12, 10:28</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-14239" class="comments-container"><span id="14240"></span><div id="comment-14240" class="comment"><div id="post-14240-score" class="comment-score"></div><div class="comment-text"><p>I think you may be on to something. I didn't go into it, but I didn't like trace evidence as much to support the FINWAIT argument. I didn't want to get into it too deeply because, let's face it, what exactly can you do if the stack is bad? I think it'll come down to the fact that the stack is not handling exceptions correctly and starting the process.</p></div><div id="comment-14240-info" class="comment-info"><span class="comment-age">(13 Sep '12, 10:49)</span> <span class="comment-user userinfo">hansangb</span></div></div></div><div id="comment-tools-14239" class="comment-tools"></div><div class="clear"></div><div id="comment-14239-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

