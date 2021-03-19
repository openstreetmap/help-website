+++
type = "question"
title = "Why my capture filter captured nothing?"
description = '''Capture Filter1: port 80 Capture Filter2: port 53 Capture Filter3: udp My computer connect the ADSL MODEM directly. Wireshark working well with no capture filter.'''
date = "2011-02-03T03:04:00Z"
lastmod = "2011-02-04T11:00:00Z"
weight = 2125
keywords = [ "wireshark" ]
aliases = [ "/questions/2125" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Why my capture filter captured nothing?](/questions/2125/why-my-capture-filter-captured-nothing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2125-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2125-score" class="post-score" title="current number of votes">0</div><span id="post-2125-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Capture Filter1: port 80<br />
Capture Filter2: port 53<br />
Capture Filter3: udp<br />
My computer connect the ADSL MODEM directly.<br />
Wireshark working well with no capture filter.<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Feb '11, 03:04</strong></p><img src="https://secure.gravatar.com/avatar/f8c25c1ed3d39d52163153efc660bf05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xuesha&#39;s gravatar image" /><p><span>xuesha</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xuesha has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Feb '11, 03:06</strong> </span></p></div></div><div id="comments-container-2125" class="comments-container"><span id="2152"></span><div id="comment-2152" class="comment"><div id="post-2152-score" class="comment-score"></div><div class="comment-text"><p>Today found a situation (with capture filter):<br />
MyPC -&gt; Adsl Modem -&gt; Internet (capture failed)<br />
MyPC-&gt; Router -&gt; Adsl Modem -&gt; Internet (capture success)<br />
<br />
</p><p>According http://wiki.wireshark.org/PPP     :<br />
      There's currently no support for filtering on any PPP fields other than the protocol.<br />
</p><p><br />
So I can not use capture filters under ADSL?<br />
</p></div><div id="comment-2152-info" class="comment-info"><span class="comment-age">(04 Feb '11, 09:06)</span> <span class="comment-user userinfo">xuesha</span></div></div></div><div id="comment-tools-2125" class="comment-tools"></div><div class="clear"></div><div id="comment-2125-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2154"></span>

<div id="answer-container-2154" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2154-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2154-score" class="post-score" title="current number of votes">2</div><span id="post-2154-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="xuesha has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>OK, looks like your packets are PPPoE when directly connected to your ADSL modem, in that case you should use a capture filter like:</p><ul><li><code>pppoes and (port 80)</code></li><li><code>pppoes and (host 1.1.1.1 and port 53)</code></li><li><code>etc</code></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '11, 09:45</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-2154" class="comments-container"><span id="2155"></span><div id="comment-2155" class="comment"><div id="post-2155-score" class="comment-score"></div><div class="comment-text"><p>to SYNbit ♦:<br />
Depending on your method solved the problem!<br />
Thank you very much!<br />
</p></div><div id="comment-2155-info" class="comment-info"><span class="comment-age">(04 Feb '11, 10:23)</span> <span class="comment-user userinfo">xuesha</span></div></div><span id="2156"></span><div id="comment-2156" class="comment"><div id="post-2156-score" class="comment-score"></div><div class="comment-text"><p>You're very welcome, glad it works.</p><p>(I converted your "answers" to comments, as that's the way this Q&amp;A is working best)</p></div><div id="comment-2156-info" class="comment-info"><span class="comment-age">(04 Feb '11, 11:00)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-2154" class="comment-tools"></div><div class="clear"></div><div id="comment-2154-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2135"></span>

<div id="answer-container-2135" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2135-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2135-score" class="post-score" title="current number of votes">1</div><span id="post-2135-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Probably your traffic is VLAN tagged. Try this: 'vlan and port 80'</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '11, 11:57</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span> </br></br></p></div></div><div id="comments-container-2135" class="comments-container"><span id="2143"></span><div id="comment-2143" class="comment"><div id="post-2143-score" class="comment-score"></div><div class="comment-text"><p>to Jaap ♦: but it still captured nothing</p></div><div id="comment-2143-info" class="comment-info"><span class="comment-age">(03 Feb '11, 20:21)</span> <span class="comment-user userinfo">xuesha</span></div></div></div><div id="comment-tools-2135" class="comment-tools"></div><div class="clear"></div><div id="comment-2135-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

