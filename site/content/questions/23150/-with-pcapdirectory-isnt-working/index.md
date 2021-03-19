+++
type = "question"
title = "--with-pcap=directory isn&#x27;t working"
description = '''I am unable to &quot;configure Wireshark with --with-pcap=directory, &quot;. I have my own compiled libpcap.a. Please give some details about where i will get the configuration file. I am using ubuntu 10.10-32 bit. Thanks in advance.'''
date = "2013-07-19T05:48:00Z"
lastmod = "2013-07-23T15:49:00Z"
weight = 23150
keywords = [ "configure", "libpcap" ]
aliases = [ "/questions/23150" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [--with-pcap=directory isn't working](/questions/23150/-with-pcapdirectory-isnt-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23150-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am unable to "configure Wireshark with --with-pcap=directory, ". I have my own compiled libpcap.a.</p><p>Please give some details about where i will get the configuration file. I am using ubuntu 10.10-32 bit.</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">configure libpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jul '13, 05:48</strong></p><img src="https://secure.gravatar.com/avatar/e82780891a1e938f0bf3a529adc858a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baila&#39;s gravatar image" /><p>baila<br />
<span class="score" title="21 reputation points">21</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baila has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted 19 Jul '13, 11:33</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-23150" class="comments-container"><span id="23169"></span><div id="comment-23169" class="comment"><div id="post-23169-score" class="comment-score"></div><div class="comment-text"><p>Is your libpcap.a in the directory you specified as an argument to the --with-pcap= flag to the configure script?</p><p>What does the configure script produce as output?</p><p>Does the configure script succeed or fail? If it succeeds, at what point does the build process fail?</p></div><div id="comment-23169-info" class="comment-info"><span class="comment-age">(19 Jul '13, 11:34)</span> Guy Harris ♦♦</div></div><span id="23294"></span><div id="comment-23294" class="comment"><div id="post-23294-score" class="comment-score"></div><div class="comment-text"><p>thanks Guy, i found it and works too.</p><p>thanks a lot!!</p></div><div id="comment-23294-info" class="comment-info"><span class="comment-age">(23 Jul '13, 09:40)</span> baila</div></div></div><div id="comment-tools-23150" class="comment-tools"></div><div class="clear"></div><div id="comment-23150-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23305"></span>

<div id="answer-container-23305" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23305-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The "configuration file" is the <code>configure</code> script in the top-level source directory.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '13, 15:49</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-23305" class="comments-container"></div><div id="comment-tools-23305" class="comment-tools"></div><div class="clear"></div><div id="comment-23305-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

