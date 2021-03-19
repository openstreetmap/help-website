+++
type = "question"
title = "Installing a recent Wireshark on Linux"
description = '''Hi guys We have a VMware box in our server room and I have set up a SUSE Linux VM where one of the interfaces has a wandering network lead connected to a suitable switch/hub so that we can effectively sample network traffic by patching it into wherever we need.  So far so good. It works. BUT.. its a...'''
date = "2013-01-07T04:32:00Z"
lastmod = "2013-01-07T17:15:00Z"
weight = 17488
keywords = [ "installation", "linux" ]
aliases = [ "/questions/17488" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Installing a recent Wireshark on Linux](/questions/17488/installing-a-recent-wireshark-on-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17488-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys</p><p>We have a VMware box in our server room and I have set up a SUSE Linux VM where one of the interfaces has a wandering network lead connected to a suitable switch/hub so that we can effectively sample network traffic by patching it into wherever we need.</p><p>So far so good. It works. BUT.. its an old version (1.4.10) and I'd like a more recent version!</p><p>I have tried following instructions I found on the net to set up Wireshark from source on an Ubuntu VM, but it didn't work (incomprehensible compile errors to a linux novice like me).</p><p>I have also looked for ready made VM wireshark appliances and not found any.<br />
</p><p>Am I stuck with this old version or is there any way forward for a linux novice?</p></div><div id="question-tags" class="tags-container tags">installation linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jan '13, 04:32</strong></p><img src="https://secure.gravatar.com/avatar/7eed5ae78aac7a495d5bfecab5c9ceea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dave%20Woolcock&#39;s gravatar image" /><p>Dave Woolcock<br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dave Woolcock has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-17488" class="comments-container"></div><div id="comment-tools-17488" class="comment-tools"></div><div class="clear"></div><div id="comment-17488-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="17489"></span>

<div id="answer-container-17489" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17489-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I have also looked for ready made VM wireshark appliances and not found any.</p></blockquote><p>What about <a href="http://www.backtrack-linux.org/">BackTrack Linux?</a>. They currently use Wireshark 1.8.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '13, 04:36</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-17489" class="comments-container"><span id="17490"></span><div id="comment-17490" class="comment"><div id="post-17490-score" class="comment-score"></div><div class="comment-text"><p>Great idea, thanks ... wonder if it will install as a VM?</p></div><div id="comment-17490-info" class="comment-info"><span class="comment-age">(07 Jan '13, 05:38)</span> Dave Woolcock</div></div><span id="17500"></span><div id="comment-17500" class="comment"><div id="post-17500-score" class="comment-score"></div><div class="comment-text"><p>yes, it will.</p><p><strong>HINT:</strong> If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-17500-info" class="comment-info"><span class="comment-age">(07 Jan '13, 08:07)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-17489" class="comment-tools"></div><div class="clear"></div><div id="comment-17489-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17542"></span>

<div id="answer-container-17542" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17542-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>try updating "YUM" then run an update via yum.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '13, 17:15</strong></p><img src="https://secure.gravatar.com/avatar/c93a321ca3ac4165064b09429ac595a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KornKontry&#39;s gravatar image" /><p>KornKontry<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KornKontry has no accepted answers">0%</span></p></div></div><div id="comments-container-17542" class="comments-container"><span id="17565"></span><div id="comment-17565" class="comment"><div id="post-17565-score" class="comment-score"></div><div class="comment-text"><p>Innocent question - why would I want to if BT5-wireshark is working OK as it is?</p><p>btw is it true you can't set a static IP address from the GUI? (coudn't find anywhere - and had to edit /etc/network/interfaces)</p></div><div id="comment-17565-info" class="comment-info"><span class="comment-age">(08 Jan '13, 07:29)</span> Dave Woolcock</div></div></div><div id="comment-tools-17542" class="comment-tools"></div><div class="clear"></div><div id="comment-17542-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17543"></span>

<div id="answer-container-17543" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17543-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It might ask you to update python libs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '13, 17:15</strong></p><img src="https://secure.gravatar.com/avatar/c93a321ca3ac4165064b09429ac595a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KornKontry&#39;s gravatar image" /><p>KornKontry<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KornKontry has no accepted answers">0%</span></p></div></div><div id="comments-container-17543" class="comments-container"></div><div id="comment-tools-17543" class="comment-tools"></div><div class="clear"></div><div id="comment-17543-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

