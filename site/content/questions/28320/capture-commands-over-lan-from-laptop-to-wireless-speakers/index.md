+++
type = "question"
title = "capture commands over LAN from laptop to wireless speakers"
description = '''I&#x27;ve got some tasty Philips speakers connected to my network and want to bypass the dodgy Philips software and send commands directly from my OpenRemote app. I&#x27;ve requested an API or developers pack from Philips but they seem reluctant...well the reply was a flat &#x27;no&#x27;! I&#x27;m looking at the traffic bet...'''
date = "2013-12-22T05:09:00Z"
lastmod = "2013-12-23T11:38:00Z"
weight = 28320
keywords = [ "capture", "speaker", "command" ]
aliases = [ "/questions/28320" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [capture commands over LAN from laptop to wireless speakers](/questions/28320/capture-commands-over-lan-from-laptop-to-wireless-speakers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28320-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've got some tasty Philips speakers connected to my network and want to bypass the dodgy Philips software and send commands directly from my OpenRemote app. I've requested an API or developers pack from Philips but they seem reluctant...well the reply was a flat 'no'!</p><p>I'm looking at the traffic between my laptop and speakers and guessing most of it is streaming mp3. Ideally want to capture commands when i click pause/play/skip/vol+/vol-. Once I have captured this I can reproduce it using OpenRemote. At the very least I would like to be able to capture volume commands.</p><p>Maybe my approach is far too simplistic and I'm missing a huge chunk!</p><p>your thoughts welcome - cheers!</p></div><div id="question-tags" class="tags-container tags">capture speaker command</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '13, 05:09</strong></p><img src="https://secure.gravatar.com/avatar/9a1733de0f509235a08ee51f1e2c68c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spezzer&#39;s gravatar image" /><p>spezzer<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spezzer has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Dec '13, 11:15</p></div></div><div id="comments-container-28320" class="comments-container"><span id="28329"></span><div id="comment-28329" class="comment"><div id="post-28329-score" class="comment-score"></div><div class="comment-text"><p>What's the speaker model?</p></div><div id="comment-28329-info" class="comment-info"><span class="comment-age">(22 Dec '13, 13:51)</span> Kurt Knochner ♦</div></div><span id="28337"></span><div id="comment-28337" class="comment"><div id="post-28337-score" class="comment-score"></div><div class="comment-text"><p>Fidelio AW9000</p></div><div id="comment-28337-info" class="comment-info"><span class="comment-age">(23 Dec '13, 04:57)</span> spezzer</div></div></div><div id="comment-tools-28320" class="comment-tools"></div><div class="clear"></div><div id="comment-28320-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28347"></span>

<div id="answer-container-28347" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28347-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Maybe my approach is far too simplistic and I'm missing a huge chunk!</p></blockquote><p>Sounds O.K. Go ahead and sniff the traffic for different commands.</p><p><strong>However</strong>: There are some obstacles you should consider.</p><ul><li>If they are using SSL (https), you won't be able to decrypt the traffic and then you won't be able to identify single commands. You'll see as soon as you've captured traffic</li><li>Often those tools use some form of authentication. If that's the case, you can't simply send the command by replaying the network traffic. If they use authentication, you'll have to mimic that as well in OpenRemote.</li><li>They might use a custom protocol unknwon to Wireshark (instead of HTTP). In that case you will only see the raw data and you'll have to reverse engineer the meaning of the bits and bytes.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Dec '13, 11:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-28347" class="comments-container"></div><div id="comment-tools-28347" class="comment-tools"></div><div class="clear"></div><div id="comment-28347-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

