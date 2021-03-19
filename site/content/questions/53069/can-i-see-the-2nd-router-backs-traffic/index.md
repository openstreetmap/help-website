+++
type = "question"
title = "can I see the 2nd router back&#x27;s traffic?"
description = '''My adapter shows traffic on its network and its ip gateway is 192.168.11.1 and it is connected to 192.168.1.1. I want to see the traffic on 192.168.1.1.'''
date = "2016-05-31T04:52:00Z"
lastmod = "2016-05-31T05:15:00Z"
weight = 53069
keywords = [ "sniffing", "wan", "lan", "without" ]
aliases = [ "/questions/53069" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [can I see the 2nd router back's traffic?](/questions/53069/can-i-see-the-2nd-router-backs-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53069-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My adapter shows traffic on its network and its ip gateway is 192.168.11.1 and it is connected to 192.168.1.1. I want to see the traffic on 192.168.1.1.</p></div><div id="question-tags" class="tags-container tags">sniffing wan lan without</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 May '16, 04:52</strong></p><img src="https://secure.gravatar.com/avatar/3aec97f586733128d6f5f7fc18b805bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="racing4funn&#39;s gravatar image" /><p>racing4funn<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="racing4funn has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 May '16, 04:53</p></div></div><div id="comments-container-53069" class="comments-container"><span id="53072"></span><div id="comment-53072" class="comment"><div id="post-53072-score" class="comment-score"></div><div class="comment-text"><p>Your question is unclear. Can you please explain the network connections, i.e.</p><pre><code>   pc &lt;----&gt;  router  &lt;----&gt; router
192.168.1  192.168.11.1       ????</code></pre></div><div id="comment-53072-info" class="comment-info"><span class="comment-age">(31 May '16, 05:17)</span> grahamb ♦</div></div><span id="53081"></span><div id="comment-53081" class="comment"><div id="post-53081-score" class="comment-score"></div><div class="comment-text"><p>the 192.168.1.1 IP is a router.. I need to go from my LAN to the LAN before my router.</p><p>ISP to router 192.168.1.1 then to second router 192.168.11.1 and then to my computer 192.168.11.101</p><p>I want to see packets on the 192.168.1.1 LAN but I dont have physical access. to that LAN</p></div><div id="comment-53081-info" class="comment-info"><span class="comment-age">(31 May '16, 10:31)</span> racing4funn</div></div></div><div id="comment-tools-53069" class="comment-tools"></div><div class="clear"></div><div id="comment-53069-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53071"></span>

<div id="answer-container-53071" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53071-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Then you need to capture <strong>on</strong> the device with the IP 192.168.1.1 (or use a SPAN port/TAP to get access to it's physical link).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '16, 05:15</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-53071" class="comments-container"><span id="53080"></span><div id="comment-53080" class="comment"><div id="post-53080-score" class="comment-score"></div><div class="comment-text"><p>the 192.168.1.1 IP is a router.. I need to go from my LAN to the LAN before my router.</p><p>ISP to router 192.168.1.1 then to second router 192.168.11.1 and then to my computer 192.168.11.101</p><p>I want to see packets on the 192.168.1.1 LAN but I dont have physical access. to that LAN</p></div><div id="comment-53080-info" class="comment-info"><span class="comment-age">(31 May '16, 10:30)</span> racing4funn</div></div><span id="53082"></span><div id="comment-53082" class="comment"><div id="post-53082-score" class="comment-score"></div><div class="comment-text"><p>Then you need to get physical access to it, otherwise you can't capture.</p></div><div id="comment-53082-info" class="comment-info"><span class="comment-age">(31 May '16, 11:29)</span> Jasper ♦♦</div></div></div><div id="comment-tools-53071" class="comment-tools"></div><div class="clear"></div><div id="comment-53071-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

