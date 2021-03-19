+++
type = "question"
title = "Capture on all interfaces in tshark"
description = '''Capture on all interfaces in tshark without mentioning interface id&#x27;s please help on this'''
date = "2014-03-26T05:43:00Z"
lastmod = "2014-03-26T08:46:00Z"
weight = 31171
keywords = [ "tshark" ]
aliases = [ "/questions/31171" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Capture on all interfaces in tshark](/questions/31171/capture-on-all-interfaces-in-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31171-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Capture on all interfaces in tshark without mentioning interface id's please help on this</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Mar '14, 05:43</strong></p><img src="https://secure.gravatar.com/avatar/98d48c0f0ae8827be74a11d027ce078a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shreeshail&#39;s gravatar image" /><p>shreeshail<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shreeshail has no accepted answers">0%</span></p></div></div><div id="comments-container-31171" class="comments-container"></div><div id="comment-tools-31171" class="comment-tools"></div><div class="clear"></div><div id="comment-31171-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31179"></span>

<div id="answer-container-31179" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31179-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>on Linux, Unix, *BSD you can use</p><blockquote><p>tshark -ni <strong>any</strong></p></blockquote><p>on Windows, <strong>any</strong> does not work, so you'll have to specify the interface ID or number</p><blockquote><p>tshark -ni 1 -ni 2 -ni 3 (this will work on Linux, Unix, *BSD as well)</p></blockquote><p>You can get the interface number with</p><blockquote><p>dumpcap -D -M</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '14, 08:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Mar '14, 08:47</p></div></div><div id="comments-container-31179" class="comments-container"><span id="31182"></span><div id="comment-31182" class="comment"><div id="post-31182-score" class="comment-score"></div><div class="comment-text"><p>Just for completeness, the <code>n</code> flag has nothing to do with the interface specification, it disables name resolution.</p><p>I have no idea what the <code>M</code> flag does but I don't require it on Windows to get the interface id numbers. Note the id number to use with the <code>-i</code> flag is the digit at the start, you no longer need to use the long guid name.</p></div><div id="comment-31182-info" class="comment-info"><span class="comment-age">(26 Mar '14, 08:57)</span> grahamb ♦</div></div><span id="31186"></span><div id="comment-31186" class="comment"><div id="post-31186-score" class="comment-score"></div><div class="comment-text"><blockquote><p>, it disables name resolution.</p></blockquote><p>sure. Just an old habit of mine. I always use -ni, as I type it without thinking ;-)</p><blockquote><p>I have no idea what the M flag does</p></blockquote><p>it prints "machine-readable" output, according to the man page, but the more interesting part: <strong>It prints the IP address</strong>, which helps to identify the right interface.</p></div><div id="comment-31186-info" class="comment-info"><span class="comment-age">(26 Mar '14, 09:06)</span> Kurt Knochner ♦</div></div><span id="31191"></span><div id="comment-31191" class="comment"><div id="post-31191-score" class="comment-score"></div><div class="comment-text"><p>Duh, I was looking at tshark with the -D, not dumpcap. For whatever reason tshark doesn't have that flag, maybe it should.</p></div><div id="comment-31191-info" class="comment-info"><span class="comment-age">(26 Mar '14, 10:07)</span> grahamb ♦</div></div><span id="31196"></span><div id="comment-31196" class="comment"><div id="post-31196-score" class="comment-score"></div><div class="comment-text"><blockquote><p>maybe it should.</p></blockquote><p>I believe I suggested it here some time ago (maybe 1-2 years), but I never opened an enhancement request nor did I feel a strong temptation to change the code myself ;-)</p></div><div id="comment-31196-info" class="comment-info"><span class="comment-age">(26 Mar '14, 10:40)</span> Kurt Knochner ♦</div></div><span id="31209"></span><div id="comment-31209" class="comment"><div id="post-31209-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt Knochner</p><p>Is this possible to get 'interface id' given the 'interface ip address' since I will get ip address as user input. Or is there any way i can provide directly ip address of interface to tshark as argument in place of interface id..?</p></div><div id="comment-31209-info" class="comment-info"><span class="comment-age">(26 Mar '14, 23:18)</span> shreeshail</div></div><span id="31231"></span><div id="comment-31231" class="comment not_top_scorer"><div id="post-31231-score" class="comment-score"></div><div class="comment-text"><p>No that's not possible. You'll have to <strong>parse the output</strong> of <code>dumpcap -D -M</code> and search for the IP address to get the interface number.</p></div><div id="comment-31231-info" class="comment-info"><span class="comment-age">(27 Mar '14, 11:45)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-31179" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-31179-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

