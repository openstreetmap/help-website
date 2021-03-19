+++
type = "question"
title = "FIX Protocol: Is it possible to send request(s) from buy side to sell side using tshark?"
description = '''Hi, Thanks in advance. This is Deb, new to Wireshark. I am currently using Wireshark 1.12.3 on Windows 8. I (Buy side) can capture FIX messages using tshark. Then I like to do some analysis on captured messages using lua. Depending on the outcome, can I send message(s) (or requests) to sell side usi...'''
date = "2015-02-24T03:11:00Z"
lastmod = "2015-02-24T06:45:00Z"
weight = 40042
keywords = [ "lua", "fix", "tshark", "wireshark" ]
aliases = [ "/questions/40042" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [FIX Protocol: Is it possible to send request(s) from buy side to sell side using tshark?](/questions/40042/fix-protocol-is-it-possible-to-send-requests-from-buy-side-to-sell-side-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40042-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40042-score" class="post-score" title="current number of votes">0</div><span id="post-40042-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Thanks in advance.</p><p>This is Deb, new to Wireshark. I am currently using Wireshark 1.12.3 on Windows 8.</p><p>I (Buy side) can capture FIX messages using tshark. Then I like to do some analysis on captured messages using lua. Depending on the outcome, can I send message(s) (or requests) to sell side using tshark?</p><p>If yes, one example please. Any reference to explore further is appreciated.</p><p>Once again, thank you very much for the time you have given.</p><p>Regards,</p><p>Deb</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-fix" rel="tag" title="see questions tagged &#39;fix&#39;">fix</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Feb '15, 03:11</strong></p><img src="https://secure.gravatar.com/avatar/1ac9c0fcb115b7f3736da7bbe4f393dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Deb&#39;s gravatar image" /><p><span>Deb</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Deb has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Feb '15, 03:17</strong> </span></p></div></div><div id="comments-container-40042" class="comments-container"></div><div id="comment-tools-40042" class="comment-tools"></div><div class="clear"></div><div id="comment-40042-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="40043"></span>

<div id="answer-container-40043" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40043-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40043-score" class="post-score" title="current number of votes">0</div><span id="post-40043-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>can I send message(s) (or requests) to sell side using tshark?</p></blockquote><p>tshark/wireshark don't have any packet injection/sending functionality, so the answer to your question is: no, that's not possible with tshark/wireshark.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Feb '15, 03:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-40043" class="comments-container"></div><div id="comment-tools-40043" class="comment-tools"></div><div class="clear"></div><div id="comment-40043-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40046"></span>

<div id="answer-container-40046" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40046-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40046-score" class="post-score" title="current number of votes">0</div><span id="post-40046-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As Kurt mentions, this is not possible with <code>tshark</code>, but you might be able to find a workable solution to your problem using other tools, such as those listed on the Wireshark's <a href="http://wiki.wireshark.org/Tools#Traffic_generators">Tools</a> wiki page. Of those listed, <a href="http://www.secdev.org/projects/scapy/">scapy</a> or <a href="http://netexpect.org/wiki/">netexpect</a> might be of particular interest to you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Feb '15, 06:45</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-40046" class="comments-container"></div><div id="comment-tools-40046" class="comment-tools"></div><div class="clear"></div><div id="comment-40046-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

