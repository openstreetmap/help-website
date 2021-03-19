+++
type = "question"
title = "Http response"
description = '''I see some HTTP response that are occasionally being decoded by wireshark as TCP segments, as opposed to HTTP Response OK&#x27;s. The total response spans approx 300 packets (450KBytes). Would such a large response hinder Wiresharks ability to decode/reassemble properly ?? If so, what is the limit ?  If ...'''
date = "2012-03-13T12:52:00Z"
lastmod = "2012-03-13T18:17:00Z"
weight = 9523
keywords = [ "decode", "http" ]
aliases = [ "/questions/9523" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Http response](/questions/9523/http-response)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9523-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9523-score" class="post-score" title="current number of votes">0</div><span id="post-9523-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I see some HTTP response that are occasionally being decoded by wireshark as TCP segments, as opposed to HTTP Response OK's. The total response spans approx 300 packets (450KBytes). Would such a large response hinder Wiresharks ability to decode/reassemble properly ?? If so, what is the limit ?</p><p>If not, what is the likely reason for such behavior ??</p><p>thanks, wk<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '12, 12:52</strong></p><img src="https://secure.gravatar.com/avatar/2b12f1f0687101a1dd8f75db884aed8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wakelt&#39;s gravatar image" /><p><span>wakelt</span><br />
<span class="score" title="13 reputation points">13</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wakelt has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Mar '12, 14:22</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-9523" class="comments-container"></div><div id="comment-tools-9523" class="comment-tools"></div><div class="clear"></div><div id="comment-9523-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9524"></span>

<div id="answer-container-9524" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9524-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9524-score" class="post-score" title="current number of votes">0</div><span id="post-9524-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Check out if there are any TCP retransmissions, out-of-order packets, or other "oddities" in the TCP sequence that has the HTTP response. Wireshark frequently has trouble with those; see for example <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=4715">bug 4715</a>.</p><p>(Of course any holes the TCP stream would also cause a problem.)</p><p>One thing you can try is to ignore (Edit-&gt;Ignore Packet) the troublesome TCP packets.</p><p>[If this answers your question, don't forget to stop by and Accept the answer.]</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '12, 15:03</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-9524" class="comments-container"><span id="9525"></span><div id="comment-9525" class="comment"><div id="post-9525-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jeff..I'll take a look at the capture in the morning.</p><p>Assuming it has something to do with retransmissions, is there a way to tell wireshark to ignore ALL retransmitted packets so that the HTTP response can be properly reassembled ??</p><p>I realize that if packets are out-of-order, I may be out of luck :-)</p><p>Is there a api somewhere that I could use to write a dissector for wireshark that takes into consideration these type of network events ?? Or is there an existing tool I can feed the cap file into that does the reassembly even under these circumstances ?</p><p>thanks again, wk</p></div><div id="comment-9525-info" class="comment-info"><span class="comment-age">(13 Mar '12, 15:27)</span> <span class="comment-user userinfo">wakelt</span></div></div><span id="9527"></span><div id="comment-9527" class="comment"><div id="post-9527-score" class="comment-score"></div><div class="comment-text"><p>[I converted your Answer into a Comment--please see the FAQ.]</p><p>To ignore all the retransmissions, you'd probably have to filter out all the retransmissions (tcp.analysis.retransmission) and then ignore each packet.</p><p>Out-of-order packets would be a lot more work; I think technically 'editcap' can move packets around, but that would be a pain.</p><p>I'm not aware of another tool that would do it better, but I don't generally work with TCP much, so I wouldn't know. The bugs exist to make Wireshark do it better, but there are a lot of bugs and not so many developers and time...</p></div><div id="comment-9527-info" class="comment-info"><span class="comment-age">(13 Mar '12, 18:17)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-9524" class="comment-tools"></div><div class="clear"></div><div id="comment-9524-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

