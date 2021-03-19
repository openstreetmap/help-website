+++
type = "question"
title = "actrace dissector not working in wireshark"
description = '''Hi,  has anyone had any luck with the dissector? I have a trace and already had a look at the dissector c code. But if a select &quot;decode as&quot; wireshark still just shows the normal udp data. I put a trace file on a webserver http://download.3imedia.de/Swyx/Tools/isdn.trace.pcapng.zip in the source I fo...'''
date = "2014-03-18T03:52:00Z"
lastmod = "2014-03-20T06:20:00Z"
weight = 30923
keywords = [ "dissector", "actrace", "packet-display" ]
aliases = [ "/questions/30923" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [actrace dissector not working in wireshark](/questions/30923/actrace-dissector-not-working-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30923-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, has anyone had any luck with the dissector? I have a trace and already had a look at the dissector c code. But if a select "decode as" wireshark still just shows the normal udp data. I put a trace file on a webserver <a href="http://download.3imedia.de/Swyx/Tools/isdn.trace.pcapng.zip">http://download.3imedia.de/Swyx/Tools/isdn.trace.pcapng.zip</a></p><p>in the source I found :</p><p>/ is ISDN packet? * the ISDN packets have 0x49446463 for packets from PSTN to the Blade and * 0x49644443 for packets from the Blade to the PSTN at offset 4 / isdn_header = tvb_get_ntohl(tvb, offset+4); if ( (tvb_len &gt;= 50) &amp;&amp; ( (isdn_header == PSTN_TO_BLADE) || (isdn_header == BLADE_TO_PSTN)) ) return ACTRACE_ISDN;</p><p>and a Display filter like</p><p>data[4:] contains 49:44:64:63 or data[4:] contains 49:64:44:43</p><p>works and returns all the pakets. But that is where I'm stuck. Is there any possbilty to debug the dissector? Or find out what is wrong with the trace or if it is a problem with the dissector?</p><p>Thanks.</p><p>Greetings</p><p>Jochen</p></div><div id="question-tags" class="tags-container tags">dissector actrace packet-display</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Mar '14, 03:52</strong></p><img src="https://secure.gravatar.com/avatar/89820cbc14d97016d87c1b1ec7b15f70?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen&#39;s gravatar image" /><p>Jochen<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Mar '14, 09:59</p></div></div><div id="comments-container-30923" class="comments-container"><span id="30926"></span><div id="comment-30926" class="comment"><div id="post-30926-score" class="comment-score"></div><div class="comment-text"><p>You'll either need to debug the dissector yourself, or post a copy of your capture somewhere for others to debug it.</p></div><div id="comment-30926-info" class="comment-info"><span class="comment-age">(18 Mar '14, 04:19)</span> grahamb ♦</div></div></div><div id="comment-tools-30923" class="comment-tools"></div><div class="clear"></div><div id="comment-30923-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="30984"></span>

<div id="answer-container-30984" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30984-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>somehow you need a plugin from audiocodes to work with this dissector. without it, it will not work.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '14, 06:20</strong></p><img src="https://secure.gravatar.com/avatar/89820cbc14d97016d87c1b1ec7b15f70?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen&#39;s gravatar image" /><p>Jochen<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Mar '14, 06:54</p></div></div><div id="comments-container-30984" class="comments-container"><span id="30987"></span><div id="comment-30987" class="comment"><div id="post-30987-score" class="comment-score"></div><div class="comment-text"><p>Do you have a reference for that?</p></div><div id="comment-30987-info" class="comment-info"><span class="comment-age">(20 Mar '14, 06:45)</span> grahamb ♦</div></div><span id="30988"></span><div id="comment-30988" class="comment"><div id="post-30988-score" class="comment-score"></div><div class="comment-text"><p>some Internet search showed the following texts:</p><p>"AudioCodes proprietary plug-ins (supplied in the software kit) must be placed in the 'plugins' folder of the installed Wireshark version (typically, C:\Program Files\Wireshark\plugins\0.99.4)" from "http://empiricalmusing.com/Lists/Posts/Post.aspx?ID=13" and a webinar from audiocodes has the same Information in a slide at the beginning here: "http://www.audiocodes.com/Data/Uploads/PSTN-Trace-Recording.htm"</p><p>And then i called our reseller and he told me he has something which works for wireshark 1.6 but he doesn't have the permission to share the plugin with others.</p></div><div id="comment-30988-info" class="comment-info"><span class="comment-age">(20 Mar '14, 06:53)</span> Jochen</div></div></div><div id="comment-tools-30984" class="comment-tools"></div><div class="clear"></div><div id="comment-30984-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30935"></span>

<div id="answer-container-30935" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30935-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The problem is that the magic 0x49644443 is at offset 19 in the UDP data payload, and not 4 as the heuristic expects. So the packets are not considered as valid AC packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Mar '14, 15:26</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-30935" class="comments-container"><span id="30943"></span><div id="comment-30943" class="comment"><div id="post-30943-score" class="comment-score"></div><div class="comment-text"><p>so would this be a bug, i should report somewhere? Is there anything i could do to get it working? (changing the 4 to 19 and then compile, but that is not sooooo easy i guess.)</p></div><div id="comment-30943-info" class="comment-info"><span class="comment-age">(19 Mar '14, 00:41)</span> Jochen</div></div><span id="30944"></span><div id="comment-30944" class="comment"><div id="post-30944-score" class="comment-score"></div><div class="comment-text"><p>Maybe there's some other intervening protocol being used to transport the AC data over UDP?</p><p>How did you make the capture?</p></div><div id="comment-30944-info" class="comment-info"><span class="comment-age">(19 Mar '14, 03:56)</span> grahamb ♦</div></div><span id="30946"></span><div id="comment-30946" class="comment"><div id="post-30946-score" class="comment-score"></div><div class="comment-text"><p>i activated it in the gateway and it then sends the output as udp traffic to an ip (my pc) and here i let wireshark capture the traffic</p></div><div id="comment-30946-info" class="comment-info"><span class="comment-age">(19 Mar '14, 04:51)</span> Jochen</div></div></div><div id="comment-tools-30935" class="comment-tools"></div><div class="clear"></div><div id="comment-30935-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

