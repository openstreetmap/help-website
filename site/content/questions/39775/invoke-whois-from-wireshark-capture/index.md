+++
type = "question"
title = "Invoke who.is from WireShark capture"
description = '''I&#x27;ve been using WireShark of late and find it very, very useful. I realize I can enable DNS resolution, but a lot of IPs do not get resolved. Is there a way, from the WireShark interface, to invoke a who.is function that would bring up the browser as if I had typed in who.si ip.address? I spend a lo...'''
date = "2015-02-10T09:12:00Z"
lastmod = "2015-02-11T04:09:00Z"
weight = 39775
keywords = [ "resolve", "whois", "dns" ]
aliases = [ "/questions/39775" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Invoke who.is from WireShark capture](/questions/39775/invoke-whois-from-wireshark-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39775-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been using WireShark of late and find it very, very useful. I realize I can enable DNS resolution, but a lot of IPs do not get resolved.</p><p>Is there a way, from the WireShark interface, to invoke a who.is function that would bring up the browser as if I had typed in who.si ip.address?</p><p>I spend a lot of time bringing up a browser and copying/pasting the IP address into who.is to get all the info. Is there a plugin for such a thing? I have some coding experience. Is it possible to code such a thing for WireShark?</p><p>For me, this would be very useful.</p><p>Thanks for any tips/ideas.</p></div><div id="question-tags" class="tags-container tags">resolve whois dns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '15, 09:12</strong></p><img src="https://secure.gravatar.com/avatar/061178fb49002a955bde36a1a1fbeb74?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="larryralph&#39;s gravatar image" /><p>larryralph<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="larryralph has no accepted answers">0%</span></p></div></div><div id="comments-container-39775" class="comments-container"></div><div id="comment-tools-39775" class="comment-tools"></div><div class="clear"></div><div id="comment-39775-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39792"></span>

<div id="answer-container-39792" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39792-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there a way, from the WireShark interface, to invoke a who.is function that would bring up the browser as if I had typed in who.si ip.address?</p></blockquote><p>That functionality is not implemented, however it would be a pretty cool feature and it could look like this:</p><ul><li>select any field (ip.addr, tcp.port, whatever)</li><li>right click the item</li><li><p>form the pop-up menu select<br />
</p><ul><li>"External Tools" -&gt; "ping"</li><li>"External Tools" -&gt; "whois lookup"</li><li>"External Tools" -&gt; "ssh"</li></ul></li></ul><p>"External Tools" would contain user defined external programs, started by Wireshark with the field as parameter ("ping %ip", "firefox.exe <a href="http://who.is/lookup=%ip">http://who.is/lookup=%ip",</a> etc.).</p><p>As it does not make sense to run ping on a tcp port, the menu shall only show those external commands that use an adequate parameter for the selected field, like %ip, %port, etc.</p><blockquote><p>I have some coding experience. Is it possible to code such a thing for WireShark?</p></blockquote><p>If you can implement that yourself, go ahead! As I said, that would be a pretty cool feature.</p><p>Otherwise, please file an enhancement bug at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '15, 04:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Feb '15, 04:09</p></div></div><div id="comments-container-39792" class="comments-container"></div><div id="comment-tools-39792" class="comment-tools"></div><div class="clear"></div><div id="comment-39792-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

