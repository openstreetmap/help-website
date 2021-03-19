+++
type = "question"
title = "WinPcap driver (aka NPF)"
description = '''Hi, I&#x27;ve gone thru the wiki info. I have and use Wireshark no problem. I currently manually start the WinPcap driver (aka NPF), use Wireshark, and then manually stop the driver. Is there a way to have this driver start automatically when I launch Wireshark? I read that this driver can be set to star...'''
date = "2015-06-23T14:29:00Z"
lastmod = "2015-06-23T15:02:00Z"
weight = 43485
keywords = [ "winpcap", "npf", "driver" ]
aliases = [ "/questions/43485" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [WinPcap driver (aka NPF)](/questions/43485/winpcap-driver-aka-npf)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43485-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I've gone thru the wiki info. I have and use Wireshark no problem. I currently manually start the WinPcap driver (aka NPF), use Wireshark, and then manually stop the driver.</p><p>Is there a way to have this driver start automatically when I launch Wireshark? I read that this driver can be set to start when I turn on pc, but I don't need things running in the background.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">winpcap npf driver</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jun '15, 14:29</strong></p><img src="https://secure.gravatar.com/avatar/131519b00f41b333b36cc2c9ab4422d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sharksurf&#39;s gravatar image" /><p>sharksurf<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sharksurf has no accepted answers">0%</span></p></div></div><div id="comments-container-43485" class="comments-container"></div><div id="comment-tools-43485" class="comment-tools"></div><div class="clear"></div><div id="comment-43485-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43487"></span>

<div id="answer-container-43487" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43487-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>From command prompt, type the following....</p><p>sc config npf start= auto</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jun '15, 15:02</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p>Rooster_50<br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></div></div><div id="comments-container-43487" class="comments-container"><span id="43488"></span><div id="comment-43488" class="comment"><div id="post-43488-score" class="comment-score"></div><div class="comment-text"><p>Or see the answer from Kurt Knochner who previously answered this very same question.</p><p><a href="https://ask.wireshark.org/questions/4843/the-npf-driver-isnt-running">The NPF driver isn't running</a></p></div><div id="comment-43488-info" class="comment-info"><span class="comment-age">(23 Jun '15, 15:19)</span> Rooster_50</div></div><span id="43533"></span><div id="comment-43533" class="comment"><div id="post-43533-score" class="comment-score"></div><div class="comment-text"><p>If I enter in command prompt: sc config npf start= auto won't that automatically start the driver at pc startup?</p><p>I am looking for a way to automatically start the driver upon launching Wireshark.</p></div><div id="comment-43533-info" class="comment-info"><span class="comment-age">(24 Jun '15, 18:42)</span> sharksurf</div></div><span id="43535"></span><div id="comment-43535" class="comment"><div id="post-43535-score" class="comment-score"></div><div class="comment-text"><p>I guess the only way you can get it to load the driver and start Wireshark at the same time would be to script it.</p></div><div id="comment-43535-info" class="comment-info"><span class="comment-age">(24 Jun '15, 21:53)</span> Rooster_50</div></div></div><div id="comment-tools-43487" class="comment-tools"></div><div class="clear"></div><div id="comment-43487-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

