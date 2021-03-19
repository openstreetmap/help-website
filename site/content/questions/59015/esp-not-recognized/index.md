+++
type = "question"
title = "ESP not recognized"
description = '''Hi, I have an ESP encrypted traffic between two endpoints and Wireshark sees it as UDP, when I left click on one of those packets and click &quot;decode as&quot; ESP doesn&#x27;t shows as an option. The traffic goes through UDP/4501, maybe it&#x27;s not recognizing it because it doesn&#x27;t goes through UDP/4500? Any thoug...'''
date = "2017-01-24T11:27:00Z"
lastmod = "2017-01-24T13:02:00Z"
weight = 59015
keywords = [ "decode_as", "udp", "esp" ]
aliases = [ "/questions/59015" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [ESP not recognized](/questions/59015/esp-not-recognized)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59015-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59015-score" class="post-score" title="current number of votes">0</div><span id="post-59015-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have an ESP encrypted traffic between two endpoints and Wireshark sees it as UDP, when I left click on one of those packets and click "decode as" ESP doesn't shows as an option. The traffic goes through UDP/4501, maybe it's not recognizing it because it doesn't goes through UDP/4500?</p><p>Any thoughts? Thanks! Keliath</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode_as" rel="tag" title="see questions tagged &#39;decode_as&#39;">decode_as</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-esp" rel="tag" title="see questions tagged &#39;esp&#39;">esp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jan '17, 11:27</strong></p><img src="https://secure.gravatar.com/avatar/7bd725a7869c1cd5de4f0e63c9d1ae14?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="keliath&#39;s gravatar image" /><p><span>keliath</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="keliath has one accepted answer">100%</span></p></div></div><div id="comments-container-59015" class="comments-container"></div><div id="comment-tools-59015" class="comment-tools"></div><div class="clear"></div><div id="comment-59015-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="59018"></span>

<div id="answer-container-59018" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59018-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59018-score" class="post-score" title="current number of votes">1</div><span id="post-59018-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cmaynard has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Just answered my question, the protocol to decode as is "udpencap". Now I can see the ESP payloads.</p><p>Thanks!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '17, 12:45</strong></p><img src="https://secure.gravatar.com/avatar/7bd725a7869c1cd5de4f0e63c9d1ae14?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="keliath&#39;s gravatar image" /><p><span>keliath</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="keliath has one accepted answer">100%</span></p></div></div><div id="comments-container-59018" class="comments-container"><span id="59020"></span><div id="comment-59020" class="comment"><div id="post-59020-score" class="comment-score"></div><div class="comment-text"><p>Nice. I was looking for "ESP" in the <em>"Decode As"</em>, but now I too see "UDPENCAP".</p></div><div id="comment-59020-info" class="comment-info"><span class="comment-age">(24 Jan '17, 13:02)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-59018" class="comment-tools"></div><div class="clear"></div><div id="comment-59018-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="59017"></span>

<div id="answer-container-59017" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59017-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59017-score" class="post-score" title="current number of votes">0</div><span id="post-59017-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><em>maybe it's not recognizing it because it doesn't goes through UDP/4500?</em></p><p>Correct. <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-ipsec-udp.c;h=6863d656bb5aa2cdbcd2e453bfedac33e200a741;hb=HEAD#l32">Wireshark expects ESP to be on UDP port 4500 only</a>. Wireshark would need to be modified for it to recognize the packets as ESP on UDP/4501. Alternatively, you could run the capture file through a tool like <a href="https://www.tracewrangler.com/">Tracewrangler</a> and replace port 4501 with port 4500 so Wireshark can recognize the packets as ESP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '17, 12:09</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-59017" class="comments-container"></div><div id="comment-tools-59017" class="comment-tools"></div><div class="clear"></div><div id="comment-59017-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

