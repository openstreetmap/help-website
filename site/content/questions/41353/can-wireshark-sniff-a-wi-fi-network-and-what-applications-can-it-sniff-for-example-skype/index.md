+++
type = "question"
title = "Can Wireshark sniff a Wi-Fi network, and what applications can it sniff (for example, Skype)?"
description = '''Hi, I have some questions about Wireshark that I hope I get answers for. Can Wireshark be used to view whatever is being sent in a WiFi network? In other words: If I installed Wireshark on my computer, can I view whatever other users on the same WiFi network are doing? Can I record their Skype calls...'''
date = "2015-04-10T09:49:00Z"
lastmod = "2015-04-10T10:06:00Z"
weight = 41353
keywords = [ "wi-fi", "wireshark", "skype" ]
aliases = [ "/questions/41353" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can Wireshark sniff a Wi-Fi network, and what applications can it sniff (for example, Skype)?](/questions/41353/can-wireshark-sniff-a-wi-fi-network-and-what-applications-can-it-sniff-for-example-skype)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41353-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have some questions about Wireshark that I hope I get answers for.</p><p>Can Wireshark be used to view whatever is being sent in a WiFi network? In other words: If I installed Wireshark on my computer, can I view whatever other users on the same WiFi network are doing? Can I record their Skype calls and videos? If so, Isn't there an application other than Skype that Wireshark can't get its data (text, voice, video)?</p></div><div id="question-tags" class="tags-container tags">wi-fi wireshark skype</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Apr '15, 09:49</strong></p><img src="https://secure.gravatar.com/avatar/440d566d57e3704b2afad6a8de233c92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ammar&#39;s gravatar image" /><p>ammar<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ammar has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Apr '15, 14:04</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-41353" class="comments-container"></div><div id="comment-tools-41353" class="comment-tools"></div><div class="clear"></div><div id="comment-41353-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41354"></span>

<div id="answer-container-41354" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41354-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, you can record everything that is sent over the air, as long as you have your WiFi adapter(s) tuned to the channels the others are sending on (usually the channel used by the access point(s)). You can record all applications that send packets.</p><p>Sounds too good to be true? It is. Because all of those packets will be at least encrypted once, since most applications use encryption like HTTPS/SSL by now. Twice, if the WiFi is encrypted, too. So yes, you can capture it all, but reading it in clear text is another matter entirely.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Apr '15, 10:06</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-41354" class="comments-container"><span id="41356"></span><div id="comment-41356" class="comment"><div id="post-41356-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper. So you say that encryption HTTPS/SSL prevents Wireshark from reading packets. According to your experience, is it possible to record Skype/Viber/Redphone calls? Is it possible to record calls? What calling apps you know that Wireshark can't read its packets?</p></div><div id="comment-41356-info" class="comment-info"><span class="comment-age">(10 Apr '15, 10:24)</span> ammar</div></div><span id="41357"></span><div id="comment-41357" class="comment"><div id="post-41357-score" class="comment-score">1</div><div class="comment-text"><p>No, encryption prevents Wireshark from <strong>displaying</strong> clear text or playing back voice/audio. It can read the packets nonetheless.</p><p>And yes, you can record the calls, but you can't break the encryption and play them back. So the recordings are basically useless if that's what you want.</p></div><div id="comment-41357-info" class="comment-info"><span class="comment-age">(10 Apr '15, 10:27)</span> Jasper ♦♦</div></div><span id="41358"></span><div id="comment-41358" class="comment"><div id="post-41358-score" class="comment-score"></div><div class="comment-text"><p>No. I'm really asking about displaying the packets. So, yes I can record Skype/Viber/Redphone calls but I can't play them and hear the actual conversation? But I'v seen some web pages that teach how to do that (Link:<a href="http://www.markwilson.co.uk/blog/2008/11/recording-voip-calls-using-wireshark.htm)">http://www.markwilson.co.uk/blog/2008/11/recording-voip-calls-using-wireshark.htm)</a> !</p></div><div id="comment-41358-info" class="comment-info"><span class="comment-age">(10 Apr '15, 10:38)</span> ammar</div></div><span id="41359"></span><div id="comment-41359" class="comment"><div id="post-41359-score" class="comment-score">1</div><div class="comment-text"><p>Yes, correct.</p><p>And regarding that blog post: that's about SIP calls (not Skype), and it's from 2008 where SIP was mostly unencrypted. Skype uses a proprietary audio protocol and it is heavily encrypted with no Wireshark decoder available.</p></div><div id="comment-41359-info" class="comment-info"><span class="comment-age">(10 Apr '15, 10:50)</span> Jasper ♦♦</div></div><span id="41360"></span><div id="comment-41360" class="comment"><div id="post-41360-score" class="comment-score"></div><div class="comment-text"><p>Aha. Thanks man. You were helpful</p></div><div id="comment-41360-info" class="comment-info"><span class="comment-age">(10 Apr '15, 10:58)</span> ammar</div></div></div><div id="comment-tools-41354" class="comment-tools"></div><div class="clear"></div><div id="comment-41354-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

