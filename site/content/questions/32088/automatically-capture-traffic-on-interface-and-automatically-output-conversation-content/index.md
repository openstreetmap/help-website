+++
type = "question"
title = "automatically capture traffic on interface and automatically output conversation content"
description = '''i plan to write a shell script (use dumpcap, tshark etc) which can automatically capture traffic on some interface and automatically output every conversation contents , start time of the conversation , end time of the conversation , source ip, source port, destination ip, destination port to a text...'''
date = "2014-04-23T00:52:00Z"
lastmod = "2014-04-24T08:59:00Z"
weight = 32088
keywords = [ "capture", "automate", "output" ]
aliases = [ "/questions/32088" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [automatically capture traffic on interface and automatically output conversation content](/questions/32088/automatically-capture-traffic-on-interface-and-automatically-output-conversation-content)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32088-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32088-score" class="post-score" title="current number of votes">0</div><span id="post-32088-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i plan to write a shell script (use dumpcap, tshark etc) which can automatically capture traffic on some interface and automatically output every conversation contents , start time of the conversation , end time of the conversation , source ip, source port, destination ip, destination port to a text file. but i have no idea to realize it, can you give me some advice?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-automate" rel="tag" title="see questions tagged &#39;automate&#39;">automate</span> <span class="post-tag tag-link-output" rel="tag" title="see questions tagged &#39;output&#39;">output</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '14, 00:52</strong></p><img src="https://secure.gravatar.com/avatar/885666c057a323159826c414b83eae37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fred&#39;s gravatar image" /><p><span>fred</span><br />
<span class="score" title="26 reputation points">26</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fred has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Apr '14, 09:08</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-32088" class="comments-container"></div><div id="comment-tools-32088" class="comment-tools"></div><div class="clear"></div><div id="comment-32088-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32116"></span>

<div id="answer-container-32116" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32116-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32116-score" class="post-score" title="current number of votes">2</div><span id="post-32116-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="fred has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please take a look at <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark</a>.</p><blockquote><p>tshark -nr input.pcap -T fields -e frame.number -e ip.src -e ip.dst ....</p></blockquote><p>You can add whatever field you need with more -e options. Please read the display filter reference to find those fields.</p><blockquote><p><a href="http://www.wireshark.org/docs/dfref/">http://www.wireshark.org/docs/dfref/</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '14, 11:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-32116" class="comments-container"><span id="32152"></span><div id="comment-32152" class="comment"><div id="post-32152-score" class="comment-score"></div><div class="comment-text"><p>good job,thanks.</p></div><div id="comment-32152-info" class="comment-info"><span class="comment-age">(24 Apr '14, 08:59)</span> <span class="comment-user userinfo">fred</span></div></div></div><div id="comment-tools-32116" class="comment-tools"></div><div class="clear"></div><div id="comment-32116-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

