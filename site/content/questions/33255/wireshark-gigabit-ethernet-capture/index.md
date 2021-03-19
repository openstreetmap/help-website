+++
type = "question"
title = "Wireshark Gigabit Ethernet Capture"
description = '''Is it possible for Wireshark to Capture Real Time Packets with No Packet Drop for Gigabit Ethernet Capturing? If no, is there any other packet analyzer to do such? If yes, how to do it? Thanks!'''
date = "2014-06-01T23:07:00Z"
lastmod = "2014-06-02T01:59:00Z"
weight = 33255
keywords = [ "gige" ]
aliases = [ "/questions/33255" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Gigabit Ethernet Capture](/questions/33255/wireshark-gigabit-ethernet-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33255-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible for Wireshark to Capture Real Time Packets with No Packet Drop for Gigabit Ethernet Capturing? If no, is there any other packet analyzer to do such? If yes, how to do it? Thanks!</p></div><div id="question-tags" class="tags-container tags">gige</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '14, 23:07</strong></p><img src="https://secure.gravatar.com/avatar/d303b1ae63827e0b8c00aac3805bcde5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KTC&#39;s gravatar image" /><p>KTC<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KTC has no accepted answers">0%</span></p></div></div><div id="comments-container-33255" class="comments-container"></div><div id="comment-tools-33255" class="comment-tools"></div><div class="clear"></div><div id="comment-33255-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33261"></span>

<div id="answer-container-33261" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33261-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Depends on how much traffic there is on the Gigabit link and how fast the packets are coming in. Worst case - no, you can't capture a full gigabit link with standard PC equipment, as Chris Greer has demonstrated on the Wireshark conference last year.</p><p>If you really need zero packet drop under all circumstances you'll need special capture equipment, e.g. one of the commercial capture solutions like Wildpackets, Solera Networks etc.</p><p>Or you buy a Napatech or Fiberblaze capture card and build your own system with it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '14, 01:59</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-33261" class="comments-container"><span id="33328"></span><div id="comment-33328" class="comment"><div id="post-33328-score" class="comment-score"></div><div class="comment-text"><p>How about High End Servers instead of standard PC equipment? Could it possibly work? Thanks for the response!</p></div><div id="comment-33328-info" class="comment-info"><span class="comment-age">(02 Jun '14, 17:14)</span> KTC</div></div><span id="33331"></span><div id="comment-33331" class="comment"><div id="post-33331-score" class="comment-score"></div><div class="comment-text"><p>As far as I know there is no recent studies on capturing on commodity HW. Geting close to 1 Gb/s is a challenge and would probably need the <em>best</em> possible HW and OS. but do you realy need to listen to a fully loaded Gigabit link the amount of data captured would be huge and a challenge to analyse after capture.</p><p>Using dumpcap and just write to disk with libpcap &gt;= 1.5.3 might give good results.</p><ul><li>If you do switch monitoring the switch might get overloaded and drop packets.</li></ul><p>I imagine CPU and memory speed(RAM) is a factor together with disc speed. As the capturing process isn't multitreaded number of cores does not mather that much.</p><p>Capture filters to reduce the number of packets to actually save might help.</p><p>That said you can get far on commodity HW but taps with HW filtering might be the first thing to consider if that isn't working.</p></div><div id="comment-33331-info" class="comment-info"><span class="comment-age">(02 Jun '14, 22:05)</span> Anders ♦</div></div><span id="33337"></span><div id="comment-33337" class="comment"><div id="post-33337-score" class="comment-score">1</div><div class="comment-text"><p>At the demo of Chris last year I captured with a 8 core Intel Core I7 directly to a SSD, and still lost about 80% of the packets if the generator pushed them out as fast as possible. This was a synthetic test but it showed that on really busy links standard hardware has its limits. I guess the capture card is the problem because it has to process incoming data fast and precisely.</p></div><div id="comment-33337-info" class="comment-info"><span class="comment-age">(03 Jun '14, 02:48)</span> Jasper ♦♦</div></div><span id="33338"></span><div id="comment-33338" class="comment"><div id="post-33338-score" class="comment-score"></div><div class="comment-text"><p>I guess that was on Windows, I got a feeling that Linux and BSD is doing (much) better.</p></div><div id="comment-33338-info" class="comment-info"><span class="comment-age">(03 Jun '14, 03:11)</span> Anders ♦</div></div><span id="33339"></span><div id="comment-33339" class="comment"><div id="post-33339-score" class="comment-score"></div><div class="comment-text"><p>I don't remember if that was with dumpcap, tshark or wireshark and wether a larger buffer than 1 mb was used.</p></div><div id="comment-33339-info" class="comment-info"><span class="comment-age">(03 Jun '14, 03:13)</span> Anders ♦</div></div></div><div id="comment-tools-33261" class="comment-tools"></div><div class="clear"></div><div id="comment-33261-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

