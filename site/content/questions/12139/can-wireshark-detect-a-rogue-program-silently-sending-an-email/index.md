+++
type = "question"
title = "Can Wireshark detect a rogue program silently sending an email?"
description = '''How can I use Wireshark to determine that a rogue program (malware) silently sent an email from my computer?'''
date = "2012-06-24T18:45:00Z"
lastmod = "2012-06-26T00:05:00Z"
weight = 12139
keywords = [ "malware" ]
aliases = [ "/questions/12139" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can Wireshark detect a rogue program silently sending an email?](/questions/12139/can-wireshark-detect-a-rogue-program-silently-sending-an-email)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12139-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12139-score" class="post-score" title="current number of votes">0</div><span id="post-12139-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I use Wireshark to determine that a rogue program (malware) silently sent an email from my computer?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-malware" rel="tag" title="see questions tagged &#39;malware&#39;">malware</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jun '12, 18:45</strong></p><img src="https://secure.gravatar.com/avatar/ea4e25bd3793189481835e053c6dfebe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dee&#39;s gravatar image" /><p><span>Dee</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dee has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Jun '12, 19:34</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-12139" class="comments-container"></div><div id="comment-tools-12139" class="comment-tools"></div><div class="clear"></div><div id="comment-12139-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12158"></span>

<div id="answer-container-12158" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12158-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12158-score" class="post-score" title="current number of votes">0</div><span id="post-12158-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can sniff on your computer, but Wireshark will only show that there is <strong>something</strong> sending an e-mail, however it will not show the process name.</p><p>Your options are:</p><ol><li>Use <a href="http://www.microsoft.com/en-us/download/details.aspx?id=4865">Microsoft Network Monitor 3.4</a>. It will show the process name in some cases.</li><li>Use a desktop firewall to block AND log any application that tries to send an e-mail</li></ol><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '12, 00:05</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-12158" class="comments-container"></div><div id="comment-tools-12158" class="comment-tools"></div><div class="clear"></div><div id="comment-12158-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

