+++
type = "question"
title = "strange relative sequence numbers"
description = '''The client sends 4 SYNs and receives RST,ACK for every one of them. Every time the relative sequence number of RST,ACK is different. Why is that so?  I - SYN seq=0; RST,ACK seq=1, ack=1  II - SYN seq=0; RST,ACK seq=1696235139, ack=1  III - SYN seq=0; RST,ACK seq=1544964366  IV- SYN seq=0; RST,ACK se...'''
date = "2011-10-12T02:59:00Z"
lastmod = "2011-10-12T03:47:00Z"
weight = 6864
keywords = [ "rst", "relative", "syn", "tcp", "sequence" ]
aliases = [ "/questions/6864" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [strange relative sequence numbers](/questions/6864/strange-relative-sequence-numbers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6864-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6864-score" class="post-score" title="current number of votes">0</div><span id="post-6864-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The client sends 4 SYNs and receives RST,ACK for every one of them. Every time the relative sequence number of RST,ACK is different. Why is that so?</p><p>I - SYN seq=0; RST,ACK seq=1, ack=1<br />
II - SYN seq=0; RST,ACK seq=1696235139, ack=1<br />
III - SYN seq=0; RST,ACK seq=1544964366<br />
IV- SYN seq=0; RST,ACK seq=937511781, ack=1</p><p>For the first SYN, RST,ACK has seq=1. What has changed for the following RSTs?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span> <span class="post-tag tag-link-relative" rel="tag" title="see questions tagged &#39;relative&#39;">relative</span> <span class="post-tag tag-link-syn" rel="tag" title="see questions tagged &#39;syn&#39;">syn</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-sequence" rel="tag" title="see questions tagged &#39;sequence&#39;">sequence</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Oct '11, 02:59</strong></p><img src="https://secure.gravatar.com/avatar/7820f7b9638e63d42e5c6fb4de7262d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brklp&#39;s gravatar image" /><p><span>brklp</span><br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brklp has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Feb '12, 21:24</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></br></p></div></div><div id="comments-container-6864" class="comments-container"></div><div id="comment-tools-6864" class="comment-tools"></div><div class="clear"></div><div id="comment-6864-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6866"></span>

<div id="answer-container-6866" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6866-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6866-score" class="post-score" title="current number of votes">0</div><span id="post-6866-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think looking at the absolute sequence numbers might make more sense here.</p><p>What is happening is that the client sends the SYN with a random sequence number and wireshark records it to be able to calculate relative sequence numbers. Then the first RST willdo the same for the opposite flow.</p><p>Then when the second SYN comes in, it has the same sequence number, so Wireshark sees is as the same session. Since the server did not create a TCP control block, it has no knowledge of the sequence number it previously used and so it chosen a new random sequence number. Wireshark still thinks the numbers should start from the sequence number of the first reset and will calculate the difference.</p><p>This is the corner case when no session really existed and the client does not honor the teardown of the session (which was requested by the RST).</p><p>Can you post the absolute sequence numbers to verify this? Cause if the client did start a new TCP session (different seq number in each SYN), then there is something not working quite right in the TCP dissector IMHO.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Oct '11, 03:31</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-6866" class="comments-container"><span id="6867"></span><div id="comment-6867" class="comment"><div id="post-6867-score" class="comment-score"></div><div class="comment-text"><p>Thnx for the quick reply!</p><p>Here are the absolute numbers:</p><p>SYN seq=505a312e RST seq=00000000, ack=505a312f<br />
SYN seq=505a312e RST seq=dcd254ee, ack=505a312f<br />
SYN seq=505a312e RST seq=1adc11a1, ack=505a312f<br />
SYN seq=505a312e RST seq=1d2cb23f, ack=505a312f</p><p>The fifth time the client sends SYN seq=505a312e and the server responds with SYN,ACK seq=96d277of(relative 2530375440), ack=505a312f (relative 1), the client responds with appropriate ack and the session establishment is successful.</p></div><div id="comment-6867-info" class="comment-info"><span class="comment-age">(12 Oct '11, 03:47)</span> <span class="comment-user userinfo">brklp</span></div></div></div><div id="comment-tools-6866" class="comment-tools"></div><div class="clear"></div><div id="comment-6866-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

