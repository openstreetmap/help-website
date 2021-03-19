+++
type = "question"
title = "Wireshark doesn&#x27;t read same IPv6 fragment offset value from pcap as microsoft network monitor"
description = '''I found an interesting issue from below pcap log: https://www.dropbox.com/s/g7fgpmhcepy2yw5/04_05_FragmentHeader.cap?dl=0  For 2nd packet, wireshark reads fragment offset value in fragment reader as &#x27;181&#x27; while Microsoft Network Monitor interpret it as &#x27;1448&#x27;. It looks like a bug to me. Wondering an...'''
date = "2015-02-04T18:07:00Z"
lastmod = "2015-02-05T01:47:00Z"
weight = 39652
keywords = [ "fragmentation", "ipv6" ]
aliases = [ "/questions/39652" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark doesn't read same IPv6 fragment offset value from pcap as microsoft network monitor](/questions/39652/wireshark-doesnt-read-same-ipv6-fragment-offset-value-from-pcap-as-microsoft-network-monitor)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39652-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39652-score" class="post-score" title="current number of votes">0</div><span id="post-39652-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I found an interesting issue from below pcap log: <a href="https://www.dropbox.com/s/g7fgpmhcepy2yw5/04_05_FragmentHeader.cap?dl=0">https://www.dropbox.com/s/g7fgpmhcepy2yw5/04_05_FragmentHeader.cap?dl=0</a><br />
</p><p>For 2nd packet, wireshark reads fragment offset value in fragment reader as '181' while Microsoft Network Monitor interpret it as '1448'. It looks like a bug to me.</p><p>Wondering anyone else is seeing the same ?</p><p>PS: I am using Version 1.12.1 (v1.12.1-0-g01b65bf from master-1.12)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fragmentation" rel="tag" title="see questions tagged &#39;fragmentation&#39;">fragmentation</span> <span class="post-tag tag-link-ipv6" rel="tag" title="see questions tagged &#39;ipv6&#39;">ipv6</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '15, 18:07</strong></p><img src="https://secure.gravatar.com/avatar/5bf84cea20bbef3b33f74637c8814804?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gallon&#39;s gravatar image" /><p><span>Gallon</span><br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gallon has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-39652" class="comments-container"></div><div id="comment-tools-39652" class="comment-tools"></div><div class="clear"></div><div id="comment-39652-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39658"></span>

<div id="answer-container-39658" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39658-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39658-score" class="post-score" title="current number of votes">2</div><span id="post-39658-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Per RFC 2460:</p><pre><code>Fragment Offset: 13-bit unsigned integer.  The offset, in 8-octet
                 units, of the data following this header,
                 relative to the start of the Fragmentable Part
                 of the original packet.</code></pre><p>What Wireshark is displaying is the raw value in 8 bytes unit, not the number of bytes. 181*8 = 1448.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '15, 01:47</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-39658" class="comments-container"></div><div id="comment-tools-39658" class="comment-tools"></div><div class="clear"></div><div id="comment-39658-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

