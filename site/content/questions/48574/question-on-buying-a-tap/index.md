+++
type = "question"
title = "Question on buying a tap"
description = '''Hi Everyone, My goal is to acquire a realitively inexpensive tap solution that will allow me to pickup ALL FRAMES as well as packets using wire shark and 2 dedicated network interface cards on the TX and RX traffic up to gigabit speed. My goal is to read Accurate Delta times between TCP handshakes a...'''
date = "2015-12-16T06:46:00Z"
lastmod = "2017-01-10T03:34:00Z"
weight = 48574
keywords = [ "taps" ]
aliases = [ "/questions/48574" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Question on buying a tap](/questions/48574/question-on-buying-a-tap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48574-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48574-score" class="post-score" title="current number of votes">0</div><span id="post-48574-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Everyone, My goal is to acquire a realitively inexpensive tap solution that will allow me to pickup ALL FRAMES as well as packets using wire shark and 2 dedicated network interface cards on the TX and RX traffic up to gigabit speed.</p><p>My goal is to read Accurate Delta times between TCP handshakes and I believe the following TAP I have will be a viable option for a TAP to serve this purpose. It's a passive tap made by a bought out company called "NetOptics" Model: TP-CU3 Here's the <a href="http://www.netoptics.com/sites/default/files/PUBTPCU3ZDU.pdf">specs</a>.</p><p>I also plan to combine this specific TAP with a USB 3.0 Dual Port Gigabit Ethernet Adapter to my laptop. Can someone with experience using wireshark and the proposed solution please confirm if this configuration will allow me to obtain my goal or guide me to a better solution??</p><p>Thanks in advance, Joe</p><p>Any suggestions much appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-taps" rel="tag" title="see questions tagged &#39;taps&#39;">taps</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Dec '15, 06:46</strong></p><img src="https://secure.gravatar.com/avatar/def6b2cca57ef69f23bf3d3322226798?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="candulj&#39;s gravatar image" /><p><span>candulj</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="candulj has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Dec '15, 06:52</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-48574" class="comments-container"></div><div id="comment-tools-48574" class="comment-tools"></div><div class="clear"></div><div id="comment-48574-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="48577"></span>

<div id="answer-container-48577" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48577-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48577-score" class="post-score" title="current number of votes">0</div><span id="post-48577-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you're looking for a portable solution you you might want to check out <a href="http://www.profitap.com/profishark-1g/">ProfiShark</a>, which does aggregated Gigabit captures with notebook connectivity via USB3. It's probably more expensive than the TP-CU3 though. An alternative to the Netoptics TAP (which is kinda noisy and does breakout only) is the <a href="http://cdn2.hubspot.net/hub/393566/file-2267218377-pdf/Data_sheets/GTDS_P1GxxA_Dec2014.pdf?t=1450279510606">Garland P1GCCA</a>, which has dip switches allowing it to do either breakout, aggregation or SPAN regeneration. It is fanless and completely quiet, but a bit more expensive than the Netopics TAP.</p><p>The primary question is probably the performance of the USB3 dual port ethernet adapter. In theory it should be fast enough to capture all packets, but most tests have shown that standard PC network cards often still drop packets (this is a problem the Profishark doesn't have). So while either Netoptics and Garland TAP are going to work just fine, the performance of the network card is going to the key factor. You should try to test it before deciding on the TAP if you can.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Dec '15, 07:54</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-48577" class="comments-container"><span id="48592"></span><div id="comment-48592" class="comment"><div id="post-48592-score" class="comment-score"></div><div class="comment-text"><p>Much appreciate your invaluable feedback. Bottom line is I'll have to make due with what I have until I can find something that will provide me with the ROI I expect. J</p></div><div id="comment-48592-info" class="comment-info"><span class="comment-age">(16 Dec '15, 17:35)</span> <span class="comment-user userinfo">candulj</span></div></div><span id="58634"></span><div id="comment-58634" class="comment"><div id="post-58634-score" class="comment-score"></div><div class="comment-text"><p>You might want to have a look at a few words I wrote down about the ProfiShark 1G that Jasper mentioned: <a href="https://wireshark.no/index.php/2017/01/06/profishark-1g-a-1-gigabit-network-tap-from-profitap/">https://wireshark.no/index.php/2017/01/06/profishark-1g-a-1-gigabit-network-tap-from-profitap/</a></p></div><div id="comment-58634-info" class="comment-info"><span class="comment-age">(10 Jan '17, 03:34)</span> <span class="comment-user userinfo">www_wireshar...</span></div></div></div><div id="comment-tools-48577" class="comment-tools"></div><div class="clear"></div><div id="comment-48577-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="48578"></span>

<div id="answer-container-48578" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48578-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48578-score" class="post-score" title="current number of votes">0</div><span id="post-48578-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Joe,</p><p>the tap seems fine in terms that if it introduces any measurable delay, it is a determinable and fixed one (the "Zero Delay" comes out to be just a marketing name based on an unrelated feature).</p><p>You should be much more concerned about the accuracy of timestamp assignment at the side of your laptop. I mean accuracy, not resolution, because the time of arrival of the packet is one thing and the time when the kernel learns about the arrival is a different one, and the delay between the two is very likely to be variable and depend on load of your notebook, architecture of the dual-NIC adaptor (like e.g. raising of a single interrupt for several packets which have arrived "almost simultaneously", delays caused by the USB overhead etc and dependent on the "phase" of the USB frame at the moment the packet has arrived)</p><p>But first of all and something which is intrinsic to any dual-port NIC over USB: if two packets, overlapping each other in time, arrive each to another GigE port of your dual-port NIC, the one which started arriving second will have to wait until the first one will have been transmitted to the laptop completely - because there is only a single channel available in the USB cable and they have to time-share it.</p><p>To me, "precise timing" in the same sentence with "USB" and/or "laptop" simply sounds like dry water, sorry. If you are really that much after precise timing, you'll need a dedicated hardware for that purpose, which has been designed without bottlenecks and with hardware timestamping.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Dec '15, 08:06</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Dec '15, 08:09</strong> </span></p></div></div><div id="comments-container-48578" class="comments-container"></div><div id="comment-tools-48578" class="comment-tools"></div><div class="clear"></div><div id="comment-48578-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

