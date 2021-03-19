+++
type = "question"
title = "Wire shark traces info"
description = '''I have set the codec to be used as G.711A and chosen media encryption as AES in PBX.Now when i make a p2p audio call between my endpoints the Wireshark traces shows payload type as unknown.Is it the expected behavior? If i choose other encryption method such as 1-srtp then the payload type shows the...'''
date = "2013-04-18T01:40:00Z"
lastmod = "2013-04-18T02:22:00Z"
weight = 20555
keywords = [ "expert-info", "traces", "wireshark" ]
aliases = [ "/questions/20555" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wire shark traces info](/questions/20555/wire-shark-traces-info)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20555-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20555-score" class="post-score" title="current number of votes">0</div><span id="post-20555-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have set the codec to be used as G.711A and chosen media encryption as AES in PBX.Now when i make a p2p audio call between my endpoints the Wireshark traces shows payload type as unknown.Is it the expected behavior? If i choose other encryption method such as 1-srtp then the payload type shows the codec used.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-expert-info" rel="tag" title="see questions tagged &#39;expert-info&#39;">expert-info</span> <span class="post-tag tag-link-traces" rel="tag" title="see questions tagged &#39;traces&#39;">traces</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '13, 01:40</strong></p><img src="https://secure.gravatar.com/avatar/2e8d7b6590dd90afc0e665537b917066?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rahul_028&#39;s gravatar image" /><p><span>Rahul_028</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rahul_028 has no accepted answers">0%</span></p></div></div><div id="comments-container-20555" class="comments-container"></div><div id="comment-tools-20555" class="comment-tools"></div><div class="clear"></div><div id="comment-20555-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20561"></span>

<div id="answer-container-20561" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20561-score" class="post-score" title="current number of votes">0</div><span id="post-20561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>chosen <strong>media encryption</strong> as AES in PBX.</p></blockquote><p>if you are using RTP, then that's expected behavior, as the RTP dissector does not support decryption.</p><blockquote><p>the Wireshark traces shows payload type as unknown.</p></blockquote><p>That's probably due to an 'unknown encryption' scheme, as the RTP dissector should detect SRTP and the encryption method (AES).</p><p>Is it possible to post a sample capture file somewhere (google docs, dropbox).</p><p>BTW: You could try to use <a href="http://serverfault.com/questions/122024/checking-rtp-stream-audio-quality/122055#122055">pcaputil</a>. That's a small tool of the <a href="http://www.pjsip.org/">pjsip project</a>. I have not yet used it, but the docs say it is able to decrypt SRTP if you give it the master key.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '13, 02:22</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Apr '13, 02:36</strong> </span></p></div></div><div id="comments-container-20561" class="comments-container"></div><div id="comment-tools-20561" class="comment-tools"></div><div class="clear"></div><div id="comment-20561-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

