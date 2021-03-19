+++
type = "question"
title = "LTE RRC dissector"
description = '''Hi, Is it possible to send LTE RRC frames over UDP somehow and for wireshark to decode them. Like in case of MAC PDUs there is a UDP format defined (http://wiki.wireshark.org/MAC-LTE), is there a similar format for RRC frames as well. I couldn&#x27;t find anything regarding this on the internet. Any help...'''
date = "2012-07-12T22:01:00Z"
lastmod = "2015-12-01T11:16:00Z"
weight = 12687
keywords = [ "rrc", "lte" ]
aliases = [ "/questions/12687" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [LTE RRC dissector](/questions/12687/lte-rrc-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12687-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12687-score" class="post-score" title="current number of votes">0</div><span id="post-12687-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Is it possible to send LTE RRC frames over UDP somehow and for wireshark to decode them. Like in case of MAC PDUs there is a UDP format defined (<a href="http://wiki.wireshark.org/MAC-LTE),">http://wiki.wireshark.org/MAC-LTE),</a> is there a similar format for RRC frames as well. I couldn't find anything regarding this on the internet.</p><p>Any help regarding this would be highly appreciated.</p><p>Thanks, Saurabh</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rrc" rel="tag" title="see questions tagged &#39;rrc&#39;">rrc</span> <span class="post-tag tag-link-lte" rel="tag" title="see questions tagged &#39;lte&#39;">lte</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jul '12, 22:01</strong></p><img src="https://secure.gravatar.com/avatar/9671ca387ae90de65e7436a376ee7e70?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="saurabhklr&#39;s gravatar image" /><p><span>saurabhklr</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="saurabhklr has no accepted answers">0%</span></p></div></div><div id="comments-container-12687" class="comments-container"></div><div id="comment-tools-12687" class="comment-tools"></div><div class="clear"></div><div id="comment-12687-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48153"></span>

<div id="answer-container-48153" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48153-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48153-score" class="post-score" title="current number of votes">0</div><span id="post-48153-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>you need to have eth MAC +IP + UDP + LTE MAC +RLC + PDCP + RRC, in pcap file, the wireshark does the implicit call</p></div><div class="answer-controls post-controls"><div class="community-wiki">This answer is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Dec '15, 11:16</strong></p><img src="https://secure.gravatar.com/avatar/aac777599ea2adb09230dc27672c4f6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Viswanathan%20Jagadeesan&#39;s gravatar image" /><p><span>Viswanathan ...</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Viswanathan Jagadeesan has no accepted answers">0%</span></p></div></div><div id="comments-container-48153" class="comments-container"></div><div id="comment-tools-48153" class="comment-tools"></div><div class="clear"></div><div id="comment-48153-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

