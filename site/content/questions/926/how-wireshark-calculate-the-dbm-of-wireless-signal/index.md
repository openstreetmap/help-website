+++
type = "question"
title = "How wireshark calculate the dbm of wireless signal?"
description = '''Please, I want to know how wireshark calculate the SSI signal of the wireless network. According to the capture result, the &quot;SSI Signal&quot; is -70 dBm, but the displayed hexadecimal value is &quot;ba&quot;. Convert the &quot;ba&quot; to decimal = 186 and not -70. So, I really want to know how wireshark calculate that, bec...'''
date = "2010-11-11T17:51:00Z"
lastmod = "2010-11-15T09:35:00Z"
weight = 926
keywords = [ "dbm" ]
aliases = [ "/questions/926" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How wireshark calculate the dbm of wireless signal?](/questions/926/how-wireshark-calculate-the-dbm-of-wireless-signal)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-926-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-926-score" class="post-score" title="current number of votes">0</div><span id="post-926-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Please, I want to know how wireshark calculate the SSI signal of the wireless network.</p><p>According to the capture result, the "SSI Signal" is -70 dBm, but the displayed hexadecimal value is "ba". Convert the "ba" to decimal = 186 and not -70. So, I really want to know how wireshark calculate that, because my final year project is about 802.11 capturing.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dbm" rel="tag" title="see questions tagged &#39;dbm&#39;">dbm</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Nov '10, 17:51</strong></p><img src="https://secure.gravatar.com/avatar/ddded634e7343570dd18dd601c9fa179?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cshong87&#39;s gravatar image" /><p><span>cshong87</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cshong87 has no accepted answers">0%</span></p></div></div><div id="comments-container-926" class="comments-container"></div><div id="comment-tools-926" class="comment-tools"></div><div class="clear"></div><div id="comment-926-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="928"></span>

<div id="answer-container-928" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-928-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-928-score" class="post-score" title="current number of votes">0</div><span id="post-928-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Ick - math.</p><p>Ok... you are right - 0xba converts to decimal 186, but Wireshark displays -70.</p><p>Short answer = subtract the actual decimal number in that field from 256 and then make it a negative number (e.g., 256-186 = 70 which you make -70).</p><p>Believe it's done in two's complement math - see the example at http://en.wikipedia.org/wiki/Twos_complement.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '10, 19:25</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p><span>lchappell ♦</span><br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-928" class="comments-container"><span id="957"></span><div id="comment-957" class="comment"><div id="post-957-score" class="comment-score"></div><div class="comment-text"><p>FYI, I was looking at the Radiotap header applied by an AirPcap adapter.</p></div><div id="comment-957-info" class="comment-info"><span class="comment-age">(15 Nov '10, 09:35)</span> <span class="comment-user userinfo">lchappell ♦</span></div></div></div><div id="comment-tools-928" class="comment-tools"></div><div class="clear"></div><div id="comment-928-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="954"></span>

<div id="answer-container-954" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-954-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-954-score" class="post-score" title="current number of votes">0</div><span id="post-954-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>AFAIK Wireshark does not really calculate the signal strength, it only displays what is being delivered from the "driver".</p><p>Signal Values from my experience are strongly depended on the type of wireless NIC plus the monitoring driver and it's headers.</p><p>I have lots of captures with negative values and ALSO lots of captures from other cards with a positive value...</p><p>If you capture directly with wireshark/tshark you should be given the PRISM header information. If your tracefile comes from another software there might be other headers indicating physical properties of the wireless network.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Nov '10, 02:52</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p><span>Landi</span><br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-954" class="comments-container"></div><div id="comment-tools-954" class="comment-tools"></div><div class="clear"></div><div id="comment-954-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

