+++
type = "question"
title = "Sniffing on 60GHz band"
description = '''Is 802.11ad supported in Wireshark? If not, when this feature will be available? Thank you.'''
date = "2014-01-27T05:01:00Z"
lastmod = "2014-05-26T07:57:00Z"
weight = 29178
keywords = [ "802.11ad" ]
aliases = [ "/questions/29178" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Sniffing on 60GHz band](/questions/29178/sniffing-on-60ghz-band)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29178-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is 802.11ad supported in Wireshark? If not, when this feature will be available? Thank you.</p></div><div id="question-tags" class="tags-container tags">802.11ad</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jan '14, 05:01</strong></p><img src="https://secure.gravatar.com/avatar/814198449843650360298c6124f7f26d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexf&#39;s gravatar image" /><p>alexf<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexf has no accepted answers">0%</span></p></div></div><div id="comments-container-29178" class="comments-container"></div><div id="comment-tools-29178" class="comment-tools"></div><div class="clear"></div><div id="comment-29178-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="29179"></span>

<div id="answer-container-29179" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29179-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark does not access the hardware directly, it's the capturing library it is using (libpcap or WinPcap), together with certain OS kernel APIs. So, it's not a question when Wireshark supports 802.11ad. The question is, when your OS supports such a device and if the capturing library on that OS works with that device/driver. As soon as those conditions are fulfilled, you will be able to capture 802.11ad traffic with Wireshark or similar tools (like: tcpdump).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jan '14, 06:00</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Jan '14, 08:25</p></div></div><div id="comments-container-29179" class="comments-container"></div><div id="comment-tools-29179" class="comment-tools"></div><div class="clear"></div><div id="comment-29179-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="29205"></span>

<div id="answer-container-29205" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29205-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>"Supported" in what sense?</p><p>If you mean "does Wireshark support capturing with hardware that supports 802.11ad", the answer to that question is, as Kurt Knochner noted, "Wireshark supports what the hardware, OS, and drivers supports".</p><p>If you mean "does Wireshark support radio metadata information for new 802.11ad features", I'm not sure any of the radio metadata formats Wireshark supports when capturing (radiotap and PPI) currently have any such information.</p><p>If you mean "does Wireshark support the changes to packet formats made in 802.11ad", the answer is, from a quick look at the code, "not currently", and the answer to "when this feature will be available?" is "when somebody writes code to support those changes and contributes it to Wireshark" - we have no roadmap for adding particular protocol features, it's up to individual developers to add them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jan '14, 14:46</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-29205" class="comments-container"><span id="29217"></span><div id="comment-29217" class="comment"><div id="post-29217-score" class="comment-score"></div><div class="comment-text"><p>Thank you Kurt and Guy for your prompt answers.</p><p>Maybe I should have asked: How can I sniff today on 60Ghz? I apologize if my question sounded aggressive or imprecise/ inappropriate to you. I just wanted to keep it simple/short (but unfortunately I was wrong). When mentioning "feature" I was thinking about the AirPcap device that might support it in the future. Thank you for your time spent developing Wireshark and helping others on this forum.</p><p>Regarding contribution to Wireshark through writing code, I stumbled upon this project description Sniffer for 802.11ad (60g) WiFi protocol <a href="http://lccn.cs.technion.ac.il/Past_Projects/Winter2013_Current_Index.shtml">http://lccn.cs.technion.ac.il/Past_Projects/Winter2013_Current_Index.shtml</a></p></div><div id="comment-29217-info" class="comment-info"><span class="comment-age">(28 Jan '14, 00:16)</span> alexf</div></div><span id="29218"></span><div id="comment-29218" class="comment"><div id="post-29218-score" class="comment-score"></div><div class="comment-text"><p>Yes, imprecise. Precise questions are easier to answer correctly.</p><p>If you aren't concerned about radio metadata or correct dissection of new packet types, a quick google for <code>801.11ad linux</code> found <a href="http://wireless.kernel.org/en/users/Drivers/wil6210">a page about the Wilocity wil6210 card</a> that seems to indicate that Linux supports it and that it can be put into monitor mode, but "Due to hardware/firmware deficiency, sniffer can capture either only control PHY (CP) or only data PHY (DP).", so you <em>might</em> be able to sniff <em>with Linux</em> <em>on a machine with a wil6210 card</em>.</p><p>There is currently no AirPcap adapter with 11ad support, so there's currently no support for capturing 802.11ad traffic with Wireshark on Windows.</p></div><div id="comment-29218-info" class="comment-info"><span class="comment-age">(28 Jan '14, 00:27)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-29205" class="comment-tools"></div><div class="clear"></div><div id="comment-29205-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33086"></span>

<div id="answer-container-33086" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33086-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Patch for 11ad support is in process of merging, see <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8594">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8594</a></p><p>With this patch, one can decode 802.11ad MAC headers.</p><p>If you are interesting in 802.11ad sniffer, you can help merging this patch.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 May '14, 07:57</strong></p><img src="https://secure.gravatar.com/avatar/41958164f7e9def67e630ab2e1c22885?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vladimir%20Kondratiev&#39;s gravatar image" /><p>Vladimir Kon...<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vladimir Kondratiev has no accepted answers">0%</span></p></div></div><div id="comments-container-33086" class="comments-container"></div><div id="comment-tools-33086" class="comment-tools"></div><div class="clear"></div><div id="comment-33086-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

