+++
type = "question"
title = "Wireshark capture displays inner IP when traffic is IPinIP"
description = '''Hello All, The traffic captured is Ethernet/IP/IP It is basically a IP in IP packets. But when I viewed the captured file, I observed the Inner IP displayed in the Upper Pane of the Wireshark capture screen. I think this is a bug ... It should display outer Ip because that is important than inner IP...'''
date = "2012-11-20T22:26:00Z"
lastmod = "2013-06-13T04:52:00Z"
weight = 16140
keywords = [ "ipinip", "wireshark" ]
aliases = [ "/questions/16140" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark capture displays inner IP when traffic is IPinIP](/questions/16140/wireshark-capture-displays-inner-ip-when-traffic-is-ipinip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16140-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All,</p><p>The traffic captured is Ethernet/IP/IP It is basically a IP in IP packets.</p><p>But when I viewed the captured file, I observed the Inner IP displayed in the Upper Pane of the Wireshark capture screen.</p><p>I think this is a bug ... It should display outer Ip because that is important than inner IP. Please let us know if there is a way to view the packets based on outer IP.</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags">ipinip wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Nov '12, 22:26</strong></p><img src="https://secure.gravatar.com/avatar/e492ab6be9f3acea8f06d41b778d5cf0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RajaSekhar&#39;s gravatar image" /><p>RajaSekhar<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RajaSekhar has no accepted answers">0%</span></p></div></div><div id="comments-container-16140" class="comments-container"><span id="16349"></span><div id="comment-16349" class="comment"><div id="post-16349-score" class="comment-score"></div><div class="comment-text"><p>Hi, I am experiencing the same problem with tshark - tunneled packets display the inner IP-header, not the outer one. Seems that tcpdump does this better - no graphics, though. Regards, willi</p></div><div id="comment-16349-info" class="comment-info"><span class="comment-age">(27 Nov '12, 10:56)</span> willi</div></div></div><div id="comment-tools-16140" class="comment-tools"></div><div class="clear"></div><div id="comment-16140-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="16352"></span>

<div id="answer-container-16352" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16352-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is not a bug. Someone else might feel the inner IP addresses are more important and thus say (wire|t)shark does a better job out-of-the-box.</p><p>With (wire|t)shark you do get the possibility to view the outer IP addresses by changing adding two more columns with a custom field pointing to "ip.src" and "ip.dst" and selecting occurrence "1".</p><p>Changing the columns in Wireshark will also change the displayed columns in Tshark. If Wireshark is not available on your system, you can edit wiresharks preferences file by hand to include the following line in the "gui.column.format:" preference:</p><pre><code>&quot;Outer-SRC&quot;, &quot;%Cus:ip.src:1:R&quot;,
&quot;Outer-DST&quot;, &quot;%Cus:ip.dst:1:R&quot;,</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '12, 11:48</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-16352" class="comments-container"></div><div id="comment-tools-16352" class="comment-tools"></div><div class="clear"></div><div id="comment-16352-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16145"></span>

<div id="answer-container-16145" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16145-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Who says it's more important than the inner IP?</p><p>Anyway, Wireshark always shows the inner most of a protocol layer in the packet overview pane, apart from error packet contents.</p><p>Stacked protocol presentation/filter isn't one of Wiresharks' strong points.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '12, 23:30</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-16145" class="comments-container"></div><div id="comment-tools-16145" class="comment-tools"></div><div class="clear"></div><div id="comment-16145-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22003"></span>

<div id="answer-container-22003" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22003-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yup outer IP is nothing but external Ip that you asking for.. You can get external/WAN ip address from</p><p><a href="http://www.ip-details.com"></a><a href="http://www.ip-details.com">http://www.ip-details.com</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '13, 04:52</strong></p><img src="https://secure.gravatar.com/avatar/94c3b1ebf70df030934c156b893da3a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frozengal&#39;s gravatar image" /><p>frozengal<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frozengal has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Jun '13, 23:21</p></div></div><div id="comments-container-22003" class="comments-container"></div><div id="comment-tools-22003" class="comment-tools"></div><div class="clear"></div><div id="comment-22003-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

