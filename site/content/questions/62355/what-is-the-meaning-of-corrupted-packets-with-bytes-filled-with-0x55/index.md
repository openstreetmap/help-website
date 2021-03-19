+++
type = "question"
title = "What is the meaning of corrupted packets with bytes filled with 0x55?"
description = '''I started seeing corrupted packets that I&#x27;ve never seen before and wanted to know what the root cause is. I suspect an overloaded network, but a bug or a defective sender might also be the possible (or something completely different). This is a sample of a corrupted packet: 0000 68 58 c5 55 55 55 55...'''
date = "2017-06-28T05:53:00Z"
lastmod = "2017-06-28T08:22:00Z"
weight = 62355
keywords = [ "corrupt", "ethernet", "overloaded", "wireshark" ]
aliases = [ "/questions/62355" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What is the meaning of corrupted packets with bytes filled with 0x55?](/questions/62355/what-is-the-meaning-of-corrupted-packets-with-bytes-filled-with-0x55)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62355-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62355-score" class="post-score" title="current number of votes">0</div><span id="post-62355-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I started seeing corrupted packets that I've never seen before and wanted to know what the root cause is.</p><p>I suspect an overloaded network, but a bug or a defective sender might also be the possible (or something completely different).</p><h1 id="this-is-a-sample-of-a-corrupted-packet">This is a sample of a corrupted packet:</h1><pre><code>0000   68 58 c5 55 55 55 55 55 55 55 55 55 55 55 55 55
0010   55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55
0020   55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55
0030   55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55
0040   55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55
0050   55 55 55</code></pre><p>They don't occur too often, but often enough to be visible.</p><p>Is my assumption correct that these are caused by collisions or network overload?</p><p>I'm using Wireshark 2.2.3 and the development network these packets are from has a lot of broadcasts.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-corrupt" rel="tag" title="see questions tagged &#39;corrupt&#39;">corrupt</span> <span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span> <span class="post-tag tag-link-overloaded" rel="tag" title="see questions tagged &#39;overloaded&#39;">overloaded</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jun '17, 05:53</strong></p><img src="https://secure.gravatar.com/avatar/fc7bdb55fd917ecec08fcb0159eebbc2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Blutkoete&#39;s gravatar image" /><p><span>Blutkoete</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Blutkoete has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Jun '17, 05:54</strong> </span></p></div></div><div id="comments-container-62355" class="comments-container"><span id="62357"></span><div id="comment-62357" class="comment"><div id="post-62357-score" class="comment-score"></div><div class="comment-text"><p>The answer largely depends on what hardware you use to capture the packets and what type of network you use. A normal Ethernet card would silently drop any incoming packet with a wrong CRC, so either it doesn't because it is a hardware specially designed to capture everything including corrupt packets, or the source sends them with correct CRC. And yes, there is also a theoretical possibility that the CRC of the packet above is <code>55 55 55 55</code>, but somehow I don't believe it :-)</p><p>I'm afraid you'll need to identify the source by splitting the network into halves and capturing just one direction between them, and then splitting the guilty half into halves again, etc., until you get to the last switch where you'll need to check port by port.</p></div><div id="comment-62357-info" class="comment-info"><span class="comment-age">(28 Jun '17, 06:44)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="62359"></span><div id="comment-62359" class="comment"><div id="post-62359-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much!</p><p>I feared there's no simple answer to my problem.</p></div><div id="comment-62359-info" class="comment-info"><span class="comment-age">(28 Jun '17, 07:13)</span> <span class="comment-user userinfo">Blutkoete</span></div></div><span id="62361"></span><div id="comment-62361" class="comment"><div id="post-62361-score" class="comment-score"></div><div class="comment-text"><p>Having TDM / VoIP equipment in the 'development network'?</p></div><div id="comment-62361-info" class="comment-info"><span class="comment-age">(28 Jun '17, 07:36)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="62362"></span><div id="comment-62362" class="comment"><div id="post-62362-score" class="comment-score"></div><div class="comment-text"><p>I would maybe start by using a network card based on a different chipset (and, preferably, even chipset vendor) for capturing, in order to exclude the receiving side from the search. This should be relatively simple as world is full of USB network cards.</p></div><div id="comment-62362-info" class="comment-info"><span class="comment-age">(28 Jun '17, 07:37)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="62363"></span><div id="comment-62363" class="comment"><div id="post-62363-score" class="comment-score"></div><div class="comment-text"><p>I'll try to record a trace with a USB network card and check every part of the network step by step. It was just I hoped that there was a simple answer like 'Ah! 0x55! That's a clear indicator of X!', but that is obviously not the case :).</p><p>The development network is connecting reference systems for position and distance measurements, if there is a sender in there issuing VoIP packets than something has gone really wrong in the lab.</p></div><div id="comment-62363-info" class="comment-info"><span class="comment-age">(28 Jun '17, 07:49)</span> <span class="comment-user userinfo">Blutkoete</span></div></div><span id="62364"></span><div id="comment-62364" class="comment not_top_scorer"><div id="post-62364-score" class="comment-score"></div><div class="comment-text"><p>What <a href="https://ask.wireshark.org/users/4/jaap">@Jaap</a> was thinking of was that 0x55 is PCMA (type of voice codec) zero, so a chain of 0x55 is PCMA silence. But there should be much more other bytes in front of it even if you would capture at raw IP level (no Ethernet layer in the captured frame).</p></div><div id="comment-62364-info" class="comment-info"><span class="comment-age">(28 Jun '17, 07:54)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-62355" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-62355-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62366"></span>

<div id="answer-container-62366" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62366-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62366-score" class="post-score" title="current number of votes">0</div><span id="post-62366-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>0x55 is the bit pattern "01010101", which is used as the preamble and can sometimes be seen when a collision on a half duplex network occurs. In your case it crashed into the beginning of a new frame from the MAC starting with 68:58:c5 before "disaster" strikes (meaning, another node starting to send it's preamble to the wire).</p><p>So yes, these are caused by collisions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jun '17, 08:22</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-62366" class="comments-container"></div><div id="comment-tools-62366" class="comment-tools"></div><div class="clear"></div><div id="comment-62366-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

