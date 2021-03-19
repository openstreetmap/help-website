+++
type = "question"
title = "Capture filter does not work"
description = '''Hi all No packets are captured when i try to find out http traffic (tcp port 80). Althuogh I can find them when I capture all packets (e.g. without any capture filter), applying display filter. I ran Wireshark as administrator but the problem remained. Windows 7 Wireshark 1.6.5 Thanks in advance'''
date = "2012-02-18T01:36:00Z"
lastmod = "2012-02-18T06:15:00Z"
weight = 9118
keywords = [ "filter", "capture", "does", "not", "work" ]
aliases = [ "/questions/9118" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture filter does not work](/questions/9118/capture-filter-does-not-work)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9118-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all</p><p>No packets are captured when i try to find out http traffic (tcp port 80). Althuogh I can find them when I capture all packets (e.g. without any capture filter), applying display filter.</p><p>I ran Wireshark as administrator but the problem remained.</p><p>Windows 7 Wireshark 1.6.5</p><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags">filter capture does not work</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Feb '12, 01:36</strong></p><img src="https://secure.gravatar.com/avatar/40fe06d218362c9c1f418447c70a369a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="clipsya&#39;s gravatar image" /><p>clipsya<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="clipsya has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Feb '12, 01:38</p></div></div><div id="comments-container-9118" class="comments-container"><span id="9120"></span><div id="comment-9120" class="comment"><div id="post-9120-score" class="comment-score"></div><div class="comment-text"><p>The capture filter "tcp port 80" or "tcp port http" works fine for me. Do you see any traffic with the above filters?</p></div><div id="comment-9120-info" class="comment-info"><span class="comment-age">(18 Feb '12, 03:20)</span> grahamb ♦</div></div><span id="9121"></span><div id="comment-9121" class="comment"><div id="post-9121-score" class="comment-score"></div><div class="comment-text"><p>thanks but both filters "tcp port 80" and "tcp port http" don't capture anything</p></div><div id="comment-9121-info" class="comment-info"><span class="comment-age">(18 Feb '12, 05:13)</span> clipsya</div></div><span id="9122"></span><div id="comment-9122" class="comment"><div id="post-9122-score" class="comment-score"></div><div class="comment-text"><p>And if you remove the capture filter you see tcp traffic on port 80? And you aren't making any other changes? Very odd.</p></div><div id="comment-9122-info" class="comment-info"><span class="comment-age">(18 Feb '12, 05:57)</span> grahamb ♦</div></div><span id="9123"></span><div id="comment-9123" class="comment"><div id="post-9123-score" class="comment-score"></div><div class="comment-text"><p>yes, as I mentioned above if I don't apply any capture filter all of the packets are captured successfuly and I can find http packets among all of it using display filter. But it is not convenient way for me :(</p></div><div id="comment-9123-info" class="comment-info"><span class="comment-age">(18 Feb '12, 06:15)</span> clipsya</div></div></div><div id="comment-tools-9118" class="comment-tools"></div><div class="clear"></div><div id="comment-9118-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9124"></span>

<div id="answer-container-9124" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9124-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you do see HTTP packets when you don't use a capture filter and you don't see HTTP when you <em>do</em> use a capture filter, then the capture filter filters the HTTP packets out. This usually happens when traffic is being encapsulated. Depending on the encapsulation type, you need to extend the capture filter:</p><ul><li><strong>802.1Q vlan tagging</strong> : vlan and tcp port 80</li><li><strong>PPPoE</strong> : pppoes and tcp port 80</li></ul><p>If these do not work for you, please update this question with the full (text) output of 1 HTTP packet to check what encapsulation you are encountering.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Feb '12, 06:15</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Feb '12, 06:22</p></div></div><div id="comments-container-9124" class="comments-container"><span id="9125"></span><div id="comment-9125" class="comment"><div id="post-9125-score" class="comment-score"></div><div class="comment-text"><p>Great thanks! PPPoE is my case! I didn' t even think about encapsulation.. Thanks a lot again!</p></div><div id="comment-9125-info" class="comment-info"><span class="comment-age">(18 Feb '12, 06:27)</span> clipsya</div></div></div><div id="comment-tools-9124" class="comment-tools"></div><div class="clear"></div><div id="comment-9124-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

