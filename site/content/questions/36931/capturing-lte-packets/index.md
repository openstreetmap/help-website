+++
type = "question"
title = "Capturing LTE packets"
description = '''I searched for LTE and found two posts. I want to capture LTE packets (I&#x27;m trying to put up a cheap lab for my students) I read some articles, googling around, and found print screens of lte packets captured. I bought a mini modem 4G, enabled lte (rrc, mac, rlc) protocols in Wireshark, but captured ...'''
date = "2014-10-08T11:36:00Z"
lastmod = "2014-10-08T15:56:00Z"
weight = 36931
keywords = [ "capture", "lte" ]
aliases = [ "/questions/36931" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing LTE packets](/questions/36931/capturing-lte-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36931-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I searched for LTE and found two posts. I want to capture LTE packets (I'm trying to put up a cheap lab for my students) I read some articles, googling around, and found print screens of lte packets captured. I bought a mini modem 4G, enabled lte (rrc, mac, rlc) protocols in Wireshark, but captured no LTE packet. Do I need a special dongle hardware?</p></div><div id="question-tags" class="tags-container tags">capture lte</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Oct '14, 11:36</strong></p><img src="https://secure.gravatar.com/avatar/d3160fc3e66e993656578c89b2bc0a54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Albuquerque&#39;s gravatar image" /><p>Albuquerque<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Albuquerque has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted to question 08 Oct '14, 13:14</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-36931" class="comments-container"></div><div id="comment-tools-36931" class="comment-tools"></div><div class="clear"></div><div id="comment-36931-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="36934"></span>

<div id="answer-container-36934" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36934-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>A commercial LTE modem will only provide a standard network interface and will never allow you to capture LTE packets. To be able to see them, you will need to have access to the proprietary debug tool from the LTE baseband provider, or to purchase a tool like Accuser XCAP, Anite Nemo or any other similar tool.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '14, 15:44</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-36934" class="comments-container"><span id="36956"></span><div id="comment-36956" class="comment"><div id="post-36956-score" class="comment-score"></div><div class="comment-text"><p>Speaking of WiFi, I can capture radio packet headers configuring the card to Monitor Mode.</p><p>I thought it would be possible, also, with LTE.</p><p>I saw print screens of LTE packets (published on the wiki.wireshark by MartinMathieson) but I don't know what's his e-mail to contact him and ask what hardware/software he used.</p><p>I contacted Accuver and Anite, asking for more info and prices. Waiting for their answers.</p><p>Thanks for the infos.</p></div><div id="comment-36956-info" class="comment-info"><span class="comment-age">(10 Oct '14, 04:24)</span> Albuquerque</div></div><span id="36957"></span><div id="comment-36957" class="comment"><div id="post-36957-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I thought it would be possible, also, with LTE. No that assumtion is wrong as per the above, 2G/3G/4G phones and modems does not give access to the base band signaling to the puplic.</p></blockquote><p>Martin works with test tools for LTE eqipment providers I beleve and thuss have access to the signaling trough the tools or the operators.</p><p>Encryption might also pose a problem when trying to look at public "radio signaling data"</p><p>I would guess at the traces you have seen comes from labs set up to test LTE equipment where the signaling is more optainable and encryption keys are known or encryption not activated.</p></div><div id="comment-36957-info" class="comment-info"><span class="comment-age">(10 Oct '14, 06:23)</span> Anders ♦</div></div><span id="36958"></span><div id="comment-36958" class="comment"><div id="post-36958-score" class="comment-score"></div><div class="comment-text"><p>As Anders says, your best bets are either logging PDUs from test equipment, or use PDUs logged by real equipment, although this may be developer-private and not available to general customers.</p></div><div id="comment-36958-info" class="comment-info"><span class="comment-age">(10 Oct '14, 07:14)</span> MartinM</div></div><span id="37333"></span><div id="comment-37333" class="comment"><div id="post-37333-score" class="comment-score"></div><div class="comment-text"><p>Hi Martin. What have you used to capture those LTE protocol packets?</p></div><div id="comment-37333-info" class="comment-info"><span class="comment-age">(24 Oct '14, 03:23)</span> Albuquerque</div></div><span id="37336"></span><div id="comment-37336" class="comment"><div id="post-37336-score" class="comment-score"></div><div class="comment-text"><p>Hi, You are missing the point, we have acces to the network equipment in the LTE network. As you don't it will be very hard to do what you want, if not impossible.</p></div><div id="comment-37336-info" class="comment-info"><span class="comment-age">(24 Oct '14, 04:24)</span> Anders ♦</div></div></div><div id="comment-tools-36934" class="comment-tools"></div><div class="clear"></div><div id="comment-36934-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="36935"></span>

<div id="answer-container-36935" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36935-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The short answer is yes, you need special tools or hardware to capture the radio interface into a .pcap file (eg: I believe Qualcomm QXDM can do it, and some vendor eNodeBs can do it). A USB modem won't work though because the information it passes to the computer is normal PPP traffic.</p><p>Is the question specific to the radio side? For a lab like that, to do it justice a trace that includes the whole EPS call flow would be ideal I think, to put the radio in context. It's frustrating on my part because I have a wealth of such packet captures but an inability to actually distribute any of them. I did most of a video series on that stuff on Youtube (eg: <a href="https://www.youtube.com/watch?v=1h-hyQeqg2Q),">https://www.youtube.com/watch?v=1h-hyQeqg2Q),</a> but even there I was very limited in terms of actual captures I could use for it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '14, 15:56</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-36935" class="comments-container"><span id="37757"></span><div id="comment-37757" class="comment"><div id="post-37757-score" class="comment-score"></div><div class="comment-text"><p>I read about open source LTE HW and SW Do you know any? Maybe airmon-ng people will deploy a new version with LTE, included. Any news about it? Tks,</p></div><div id="comment-37757-info" class="comment-info"><span class="comment-age">(11 Nov '14, 08:46)</span> Albuquerque</div></div><span id="37758"></span><div id="comment-37758" class="comment"><div id="post-37758-score" class="comment-score"></div><div class="comment-text"><p>I'm not aware of any open source LTE SW stack or HW (while working in the domain since years). I would not put too much hope in such a solution for now.</p></div><div id="comment-37758-info" class="comment-info"><span class="comment-age">(11 Nov '14, 10:45)</span> Pascal Quantin</div></div><span id="37760"></span><div id="comment-37760" class="comment"><div id="post-37760-score" class="comment-score"></div><div class="comment-text"><p>I'm not aware of any either. In my experience all these tools are very closed source and very expensive.</p></div><div id="comment-37760-info" class="comment-info"><span class="comment-age">(11 Nov '14, 11:07)</span> Quadratic</div></div><span id="39198"></span><div id="comment-39198" class="comment"><div id="post-39198-score" class="comment-score"></div><div class="comment-text"><p>For a SW LTE stack have a look at: <a href="http://www.openairinterface.org/">http://www.openairinterface.org/</a></p></div><div id="comment-39198-info" class="comment-info"><span class="comment-age">(16 Jan '15, 04:22)</span> sebastianheld</div></div><span id="39200"></span><div id="comment-39200" class="comment"><div id="post-39200-score" class="comment-score"></div><div class="comment-text"><p>Note that it's a quite lite implementation of an eNB L2/3 (more a demonstration) as the project is more focusing on the PHY aspects.</p></div><div id="comment-39200-info" class="comment-info"><span class="comment-age">(16 Jan '15, 04:53)</span> Pascal Quantin</div></div><span id="60367"></span><div id="comment-60367" class="comment not_top_scorer"><div id="post-60367-score" class="comment-score"></div><div class="comment-text"><p>I am also looking for an alternative to baseband capture without the commitment to Accuser XCAP or Anite Nemo.</p></div><div id="comment-60367-info" class="comment-info"><span class="comment-age">(27 Mar '17, 13:33)</span> EvelBoDevil</div></div></div><div id="comment-tools-36935" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-36935-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

