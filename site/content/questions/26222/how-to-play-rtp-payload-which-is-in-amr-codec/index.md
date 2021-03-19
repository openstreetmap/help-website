+++
type = "question"
title = "How to play RTP payload which is in AMR codec"
description = '''Hello Expert, I would like a question about AMR codec in RTP. With a pcap of sip call, I have known that the payload can be played in Wireshark if tht codec is PCMU. But it seems like the original wireshark does not support AMR very well. Is it possibe to make wireshark to play AMR payload? Thanks a...'''
date = "2013-10-20T00:04:00Z"
lastmod = "2013-10-21T03:22:00Z"
weight = 26222
keywords = [ "amr" ]
aliases = [ "/questions/26222" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to play RTP payload which is in AMR codec](/questions/26222/how-to-play-rtp-payload-which-is-in-amr-codec)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26222-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Expert,</p><p>I would like a question about AMR codec in RTP. With a pcap of sip call, I have known that the payload can be played in Wireshark if tht codec is PCMU.</p><p>But it seems like the original wireshark does not support AMR very well. Is it possibe to make wireshark to play AMR payload?</p><p>Thanks a lot. BR, Gao</p></div><div id="question-tags" class="tags-container tags">amr</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Oct '13, 00:04</strong></p><img src="https://secure.gravatar.com/avatar/0b5c0046c2a732f3bf824a3a0d236731?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gao&#39;s gravatar image" /><p>gao<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gao has no accepted answers">0%</span></p></div></div><div id="comments-container-26222" class="comments-container"></div><div id="comment-tools-26222" class="comment-tools"></div><div class="clear"></div><div id="comment-26222-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="26223"></span>

<div id="answer-container-26223" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26223-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As far as I know the AMR codec requires a license and can't be included in Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '13, 07:41</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-26223" class="comments-container"></div><div id="comment-tools-26223" class="comment-tools"></div><div class="clear"></div><div id="comment-26223-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26231"></span>

<div id="answer-container-26231" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26231-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As AMR is not supported by Wireshark, here is what you can do.</p><ul><li>extract the RTP payload: <code>http://ask.wireshark.org/questions/21193/extracting-rtp-payload-and-dumping-to-a-ts-file</code></li><li>Play the file with an external player: <code>http://www.amrplayer.com/</code></li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '13, 03:22</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-26231" class="comments-container"></div><div id="comment-tools-26231" class="comment-tools"></div><div class="clear"></div><div id="comment-26231-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

