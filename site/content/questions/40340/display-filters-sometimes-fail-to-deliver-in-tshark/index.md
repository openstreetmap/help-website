+++
type = "question"
title = "Display filters sometimes fail to deliver in tshark"
description = '''Hi, Testing some display filters for my home WLAN in tshark. Have noticed that quite a few of them don&#x27;t work for me. As an example, if I capture one single beacon packet to test on and apply a filter like this: tshark -r myfile.pcap -R &quot;wlan.da==ff:ff:ff:ff:ff:ff&quot; -T fields -e wlan_mgt.fixed.chanwi...'''
date = "2015-03-06T20:57:00Z"
lastmod = "2015-03-06T22:24:00Z"
weight = 40340
keywords = [ "tshark", "display-filter" ]
aliases = [ "/questions/40340" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Display filters sometimes fail to deliver in tshark](/questions/40340/display-filters-sometimes-fail-to-deliver-in-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40340-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Testing some display filters for my home WLAN in tshark. Have noticed that quite a few of them don't work for me. As an example, if I capture one single beacon packet to test on and apply a filter like this:</p><p>tshark -r myfile.pcap -R "wlan.da==ff:ff:ff:ff:ff:ff" -T fields -e wlan_mgt.fixed.chanwidth</p><p>it doesn't show anything. But if I check the exact same packet in Wireshark the parameter is visible there.</p><p>Am I doing something wrong with my tshark filter? Some filters work and some don't.</p><p>Thanks.</p><p>Regards, Sam</p></div><div id="question-tags" class="tags-container tags">tshark display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '15, 20:57</strong></p><img src="https://secure.gravatar.com/avatar/c19324dc35615378dc81ba8a3d71b0b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SamA&#39;s gravatar image" /><p>SamA<br />
<span class="score" title="11 reputation points">11</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SamA has no accepted answers">0%</span></p></div></div><div id="comments-container-40340" class="comments-container"><span id="40351"></span><div id="comment-40351" class="comment"><div id="post-40351-score" class="comment-score"></div><div class="comment-text"><p>Hi Pascal, Thanks, but it doesn't solve my problem. I think I understand what you try to do, but I have no problem listing multiple fields with the -R switch. I can list 3-4 columns with info if I want by just adding more -e &lt;field&gt; values.</p><p>It's just that the filter mentioned (and quite a few other filters) don't give any output in tshark. But if I check in Wireshark I find all the fields there.</p></div><div id="comment-40351-info" class="comment-info"><span class="comment-age">(07 Mar '15, 10:43)</span> SamA</div></div><span id="40354"></span><div id="comment-40354" class="comment"><div id="post-40354-score" class="comment-score">1</div><div class="comment-text"><p>Could you please share the capture? There is absolutely no reason that a field available in Wireshark is not present in tshark, especially if you use the 2 pass option (-2). Note that your initial command line is not correct when you use a single pass, as explained in the man page</p></div><div id="comment-40354-info" class="comment-info"><span class="comment-age">(07 Mar '15, 13:57)</span> Pascal Quantin</div></div><span id="40372"></span><div id="comment-40372" class="comment"><div id="post-40372-score" class="comment-score"></div><div class="comment-text"><p>Hi Pascal, You were right. Got it working finally after doing as you suggested. Thanks!</p></div><div id="comment-40372-info" class="comment-info"><span class="comment-age">(08 Mar '15, 19:05)</span> SamA</div></div></div><div id="comment-tools-40340" class="comment-tools"></div><div class="clear"></div><div id="comment-40340-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40341"></span>

<div id="answer-container-40341" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40341-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming that you use tshark 1.12.x, did you give a try to</p><p>tshark -r myfile.pcap -Y "wlan.da==ff:ff:ff:ff:ff:ff" -T fields -e wlan_mgt.fixed.chanwidth</p><p>? Alternatively you could try</p><p>tshark -r myfile.pcap -2R "wlan.da==ff:ff:ff:ff:ff:ff" -T fields -e wlan_mgt.fixed.chanwidth</p><p>See <a href="https://www.wireshark.org/docs/man-pages/tshark.html">https://www.wireshark.org/docs/man-pages/tshark.html</a> for an explanation of the difference between -R and -Y</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '15, 22:24</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-40341" class="comments-container"></div><div id="comment-tools-40341" class="comment-tools"></div><div class="clear"></div><div id="comment-40341-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

