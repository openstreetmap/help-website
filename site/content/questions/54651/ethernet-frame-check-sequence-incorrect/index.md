+++
type = "question"
title = "ethernet frame check sequence incorrect"
description = '''Why do I see this all the time - clearly the checksum cannot be wrong, and I dont think I have wireshark configured to check this anyway - see attachments Can I turn this off somewhere? All my googling suggests the two places below should have done this?? I&#x27;m using Version 2.0.5   '''
date = "2016-08-08T05:43:00Z"
lastmod = "2016-08-08T17:01:00Z"
weight = 54651
keywords = [ "badchecksum" ]
aliases = [ "/questions/54651" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [ethernet frame check sequence incorrect](/questions/54651/ethernet-frame-check-sequence-incorrect)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54651-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Why do I see this all the time - clearly the checksum cannot be wrong, and I dont think I have wireshark configured to check this anyway - see attachments</p><p>Can I turn this off somewhere? All my googling suggests the two places below should have done this??</p><p>I'm using Version 2.0.5<img src="https://osqa-ask.wireshark.org/upfiles/checksequence.png" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/checksequencea.png" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/checksequence1_bmBIGGe.png" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/checksequence2.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">badchecksum</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Aug '16, 05:43</strong></p><img src="https://secure.gravatar.com/avatar/bea4cdfe055efcd9c40a789a2b381c8a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wratty&#39;s gravatar image" /><p>wratty<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wratty has no accepted answers">0%</span></p></img></div></div><div id="comments-container-54651" class="comments-container"></div><div id="comment-tools-54651" class="comment-tools"></div><div class="clear"></div><div id="comment-54651-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="54652"></span>

<div id="answer-container-54652" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54652-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>IP and UDP/TCP are layer 3 and 4, but your CRC error is on Ethernet, which is layer 2. So clearly those settings you mention are irrelevant.</p><p>You should check if "Assume packets have FCS" and "Validate the Ethernet checksum if possible" are enabled for the Ethernet protocol dissector.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '16, 05:47</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></img></div></div><div id="comments-container-54652" class="comments-container"><span id="54654"></span><div id="comment-54654" class="comment"><div id="post-54654-score" class="comment-score"></div><div class="comment-text"><p>Yes you are correct - I was being an idiot. Thanks. Sorted.</p></div><div id="comment-54654-info" class="comment-info"><span class="comment-age">(08 Aug '16, 05:54)</span> wratty</div></div><span id="54655"></span><div id="comment-54655" class="comment"><div id="post-54655-score" class="comment-score">1</div><div class="comment-text"><p>Don't be too hard on yourself - everybody can mistake those things every once in a while :-)</p></div><div id="comment-54655-info" class="comment-info"><span class="comment-age">(08 Aug '16, 05:56)</span> Jasper ♦♦</div></div></div><div id="comment-tools-54652" class="comment-tools"></div><div class="clear"></div><div id="comment-54652-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54679"></span>

<div id="answer-container-54679" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54679-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark's code to try to detect the presence of an Ethernet FCS might not be working. Please file a bug on this at <a href="http://bugs.wireshark.org">the Wireshark Bugzilla</a>, attaching, if you can, a small capture that shows it - one frame would be sufficient.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '16, 17:01</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></img></div></div><div id="comments-container-54679" class="comments-container"></div><div id="comment-tools-54679" class="comment-tools"></div><div class="clear"></div><div id="comment-54679-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

