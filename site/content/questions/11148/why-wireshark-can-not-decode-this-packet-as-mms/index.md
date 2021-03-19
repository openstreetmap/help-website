+++
type = "question"
title = "why wireshark can not decode this packet as mms"
description = '''Hi,all.  I captured mms packets from traffic, save it as file name &quot;mmscc7&quot;, there is no problem when use wireshark to decode it. but when I use &quot;editcap.exe -r mmscc7 mmscc7300-400&quot; to get packets 300-400 as another file name &quot;mmscc7300-400&quot;,and use wirshark to decode it. I find that packet 37 can ...'''
date = "2012-05-19T18:49:00Z"
lastmod = "2012-05-20T22:52:00Z"
weight = 11148
keywords = [ "mms" ]
aliases = [ "/questions/11148" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [why wireshark can not decode this packet as mms](/questions/11148/why-wireshark-can-not-decode-this-packet-as-mms)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11148-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,all. I captured mms packets from traffic, save it as file name "mmscc7", there is no problem when use wireshark to decode it. but when I use "editcap.exe -r mmscc7 mmscc7300-400" to get packets 300-400 as another file name "mmscc7300-400",and use wirshark to decode it. I find that packet 37 can not decode as mms, but cotp,the other mms packets are all ok! I don't why, is it a bug of wireshark?</p></div><div id="question-tags" class="tags-container tags">mms</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '12, 18:49</strong></p><img src="https://secure.gravatar.com/avatar/531b3f9baea59eeb0794b2188c1f9424?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="theodoreli&#39;s gravatar image" /><p>theodoreli<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="theodoreli has no accepted answers">0%</span></p></div></div><div id="comments-container-11148" class="comments-container"></div><div id="comment-tools-11148" class="comment-tools"></div><div class="clear"></div><div id="comment-11148-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11167"></span>

<div id="answer-container-11167" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11167-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, Probably some information needed yo determine the content of the packet gets "lost" when filtering the file you could try: Go to Edit-&gt;preferences-&gt;protocol-&gt;PRES and edit the users context tale</p><p>enter context = 'the context of your packet' and OID = 1.0.9506.2.3 and your trace will be dissected as MMS.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '12, 22:52</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-11167" class="comments-container"></div><div id="comment-tools-11167" class="comment-tools"></div><div class="clear"></div><div id="comment-11167-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

