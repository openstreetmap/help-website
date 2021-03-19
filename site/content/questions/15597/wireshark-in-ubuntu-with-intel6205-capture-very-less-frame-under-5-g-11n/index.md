+++
type = "question"
title = "wireshark in ubuntu with intel6205 capture very less frame under 5 G 11N"
description = '''i am doing a test using my ubuntu box which used intel 6205, once i set the ap into wide channel under 5GHZ, the wireshark capture speed seems like be very slow, then i did a compare, i found that indeed for 11N 40MHZ frame wireshark with 6205 only can capture 50% frame than other card, if possible ...'''
date = "2012-11-06T18:05:00Z"
lastmod = "2012-11-07T13:39:00Z"
weight = 15597
keywords = [ "intel6205" ]
aliases = [ "/questions/15597" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark in ubuntu with intel6205 capture very less frame under 5 G 11N](/questions/15597/wireshark-in-ubuntu-with-intel6205-capture-very-less-frame-under-5-g-11n)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15597-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i am doing a test using my ubuntu box which used intel 6205, once i set the ap into wide channel under 5GHZ, the wireshark capture speed seems like be very slow, then i did a compare, i found that indeed for 11N 40MHZ frame wireshark with 6205 only can capture 50% frame than other card, if possible can i know if this a wireshark problem or the card limitation, indeed i already upgrade the kernel to 3.6, so seems like not because kernel too old.</p></div><div id="question-tags" class="tags-container tags">intel6205</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Nov '12, 18:05</strong></p><img src="https://secure.gravatar.com/avatar/5b65bbde4e19e1cf2949e3d20025aa9a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vca86&#39;s gravatar image" /><p>vca86<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vca86 has no accepted answers">0%</span></p></div></div><div id="comments-container-15597" class="comments-container"></div><div id="comment-tools-15597" class="comment-tools"></div><div class="clear"></div><div id="comment-15597-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15660"></span>

<div id="answer-container-15660" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15660-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>do you have any connectivity issues (lost pings, slow download speed, etc.)? I think it's more a problem with the interface (or driver) itself, rather than Wireshark.</p><p>BTW: How did you figure out, that Wireshark is only capturing 50% of the traffic?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '12, 13:39</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-15660" class="comments-container"><span id="15663"></span><div id="comment-15663" class="comment"><div id="post-15663-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Thanks for your kindly reply,i think the connectivity should be ok, for that once i use this card to connect internet everything seems be good, i found this issue is because i also have a windows laptop which can run the same capture, after i found wireshark+intel6205 become slow then i did a compare between the windows and linux, the 50% is a roughly number,but wireshark linux with intel6205 is really slow.</p><p>Regards Allen</p></div><div id="comment-15663-info" class="comment-info"><span class="comment-age">(07 Nov '12, 15:05)</span> vca86</div></div><span id="15667"></span><div id="comment-15667" class="comment"><div id="post-15667-score" class="comment-score"></div><div class="comment-text"><p>Just to be sure we talk about the same thing:</p><p>Did you caputre a WLAN session of a <strong>third</strong> machine with Windows and Linux <strong>at the same time</strong> and the Linux capture file contained only 50% of the packets? If so, were the missing packets random packets or only packets in one direction (e.g. only client -&gt; server)?</p><p>What do you mean by "Wireshark with intel6205 is really slow?" Slow in terms of what?</p><p>BTW: Talking about Wireshark beeing slow. Did you enable Name resolving in Wireshark? If so, that could explain why Wireshark appears to be slow, especially if the nameserver on your linux system is configured but unreachable.</p><blockquote><p><code>Edit -&gt; Preferences -&gt; Name Resolution</code><br />
</p></blockquote><p>Please check the option: <strong>Enable Network Name Resolution</strong></p><p>If that option is checked, please uncheck it and retry.</p></div><div id="comment-15667-info" class="comment-info"><span class="comment-age">(07 Nov '12, 15:19)</span> Kurt Knochner ♦</div></div><span id="15745"></span><div id="comment-15745" class="comment"><div id="post-15745-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt, thanks for your reply, yes i did that at same time by using a third laptop produce traffic,according my test the missing package involved both upload and download, most of missing package is control/management frame, follow your suggestion, after check the wireshark setting, i found that the "Enable Network Name Resolution" is disabled in my environment.</p></div><div id="comment-15745-info" class="comment-info"><span class="comment-age">(08 Nov '12, 17:15)</span> vca86</div></div><span id="15748"></span><div id="comment-15748" class="comment"><div id="post-15748-score" class="comment-score"></div><div class="comment-text"><p>O.K. then I assume it's a problem with either the driver or the hardware itself. Both are pretty hard to troubleshoot.</p></div><div id="comment-15748-info" class="comment-info"><span class="comment-age">(08 Nov '12, 19:04)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-15660" class="comment-tools"></div><div class="clear"></div><div id="comment-15660-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

