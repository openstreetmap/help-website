+++
type = "question"
title = "packet sniffer to discover the root of a trojan spammer"
description = '''--- disregard...I placed between our switch and gateway and was able to sniff it all ;) --- it was suggested we use a packet sniffer to discover the root of a trojan spammer behind our firewall, and we have Wireshark Version 0.99.6a (SVN Rev 22276) installed. Does Wireshark have the ability to analy...'''
date = "2012-02-10T09:30:00Z"
lastmod = "2012-02-11T02:22:00Z"
weight = 8947
keywords = [ "sniffer" ]
aliases = [ "/questions/8947" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [packet sniffer to discover the root of a trojan spammer](/questions/8947/packet-sniffer-to-discover-the-root-of-a-trojan-spammer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8947-score" class="post-score" title="current number of votes">0</div><span id="post-8947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>--- disregard...I placed between our switch and gateway and was able to sniff it all ;) ---</p><p>it was suggested we use a packet sniffer to discover the root of a trojan spammer behind our firewall, and we have Wireshark Version 0.99.6a (SVN Rev 22276) installed.</p><p>Does Wireshark have the ability to analyze the network as a whole, or is it specific to a single device?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sniffer" rel="tag" title="see questions tagged &#39;sniffer&#39;">sniffer</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '12, 09:30</strong></p><img src="https://secure.gravatar.com/avatar/faf326878ebe768409a45475449b7bd1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mcrudo&#39;s gravatar image" /><p><span>mcrudo</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mcrudo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Feb '12, 10:50</strong> </span></p></div></div><div id="comments-container-8947" class="comments-container"><span id="8963"></span><div id="comment-8963" class="comment"><div id="post-8963-score" class="comment-score"></div><div class="comment-text"><p>You might also want to look at getting a newer version of Wireshark. 0.99.6a is really, really ancient.</p></div><div id="comment-8963-info" class="comment-info"><span class="comment-age">(11 Feb '12, 02:22)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-8947" class="comment-tools"></div><div class="clear"></div><div id="comment-8947-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8949"></span>

<div id="answer-container-8949" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8949-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8949-score" class="post-score" title="current number of votes">1</div><span id="post-8949-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is a <a href="http://en.wikipedia.org/wiki/Packet_analyzer">packet analyzer</a>, not a whole network analyzer. Any packets that can be seen by the interface(s) it is capturing on will be available for analysis.</p><p>You might want to look at the Wiki <a href="http://wiki.wireshark.org/CaptureSetup">Capture Setup</a> page to determine how you want to run your captures.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '12, 10:10</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-8949" class="comments-container"></div><div id="comment-tools-8949" class="comment-tools"></div><div class="clear"></div><div id="comment-8949-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8950"></span>

<div id="answer-container-8950" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8950-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8950-score" class="post-score" title="current number of votes">1</div><span id="post-8950-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Review the documentation "grahamb" provided. If you have Cisco switches, you can configure a SPAN port. You can connect your wireshark machine to this port to monitor all traffic of the network.</p><p>I am sure you are able to configure span ports on other vendors; however, I do not know the syntex to complete this.</p><p>Good luck</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '12, 10:50</strong></p><img src="https://secure.gravatar.com/avatar/ae897e20625df9db38d37f98126bf90e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jaz0nj4ckal&#39;s gravatar image" /><p><span>jaz0nj4ckal</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jaz0nj4ckal has no accepted answers">0%</span></p></div></div><div id="comments-container-8950" class="comments-container"></div><div id="comment-tools-8950" class="comment-tools"></div><div class="clear"></div><div id="comment-8950-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

