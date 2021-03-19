+++
type = "question"
title = "DNS and ssh tunnelling"
description = '''Hi..I have an ssh server setup at home which I&#x27;m using to tunnel from work.I&#x27;m mainly just trying to learn I&#x27;m not trying to bypass anything at work since I think they could care less and I don&#x27;t really go anywhere but youtube to listen to songs while I work. but anyway, I know the tunneling is work...'''
date = "2011-08-04T06:22:00Z"
lastmod = "2011-08-04T06:53:00Z"
weight = 5495
keywords = [ "chrome", "switchy", "dns" ]
aliases = [ "/questions/5495" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [DNS and ssh tunnelling](/questions/5495/dns-and-ssh-tunnelling)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5495-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi..I have an ssh server setup at home which I'm using to tunnel from work.I'm mainly just trying to learn I'm not trying to bypass anything at work since I think they could care less and I don't really go anywhere but youtube to listen to songs while I work. but anyway, I know the tunneling is working because my company blocks fedoraforum.org and I can get to it just fine.I'm using Chrome with the proxy switchy installed..I'm using socks5 in switchy. I have putty running and adding dynamic port 5080.so my switchy config looks like this socks host 127.0.0.1 amd port 5080. Now when I capture traffic using wireshark I set up a filter for only DNS but I noticed it still uses the company dns so kind of defeats the purpose since the dns server will know which site I'm trying to go to.. How do I get it to use dns server that my home ssh server uses? one other off thing is that I can't get to intranet sites when switchy (chrome) is set up to use the proxy. any help is appreciated.</p></div><div id="question-tags" class="tags-container tags">chrome switchy dns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Aug '11, 06:22</strong></p><img src="https://secure.gravatar.com/avatar/ec4e08884167a9e28f5bbc215b4f381e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wire149&#39;s gravatar image" /><p>wire149<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wire149 has no accepted answers">0%</span></p></div></div><div id="comments-container-5495" class="comments-container"></div><div id="comment-tools-5495" class="comment-tools"></div><div class="clear"></div><div id="comment-5495-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5499"></span>

<div id="answer-container-5499" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5499-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>What you are doing has quite a potential to get you (and your company) into trouble.</p><p>The ssh-tunnel undermines whatever security filter was established by your network administrator, for example in a proxy server. While the tunnel certainly is cool it works both ways: Your network at home is probably not as secure as the company net. You have to ask yourself if you really want to provide that potential jump point to your employer?</p><p>Your company has a good reason for it's acceptable use policy; they might even had you sign a copy that policy as part of the hiring process. I highly recommend that you observe that policy.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Aug '11, 06:53</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-5499" class="comments-container"><span id="5502"></span><div id="comment-5502" class="comment"><div id="post-5502-score" class="comment-score"></div><div class="comment-text"><p>Yeah that's true..I was jut curious and trying to learn this stuff..BTW seems like fireproxy worked for me.think it's just chrome switchy is not working..btw how do I view packets only going through the tunnel?</p></div><div id="comment-5502-info" class="comment-info"><span class="comment-age">(04 Aug '11, 07:31)</span> wire149</div></div><span id="5503"></span><div id="comment-5503" class="comment"><div id="post-5503-score" class="comment-score"></div><div class="comment-text"><p>I'd still like to know how to just view traffic going to tunnel with some type of filter..do I need to filter for ssh only or port?</p></div><div id="comment-5503-info" class="comment-info"><span class="comment-age">(04 Aug '11, 09:30)</span> wire149</div></div><span id="5510"></span><div id="comment-5510" class="comment"><div id="post-5510-score" class="comment-score"></div><div class="comment-text"><p>@wire149, I'd go with both.</p></div><div id="comment-5510-info" class="comment-info"><span class="comment-age">(04 Aug '11, 16:21)</span> helloworld</div></div></div><div id="comment-tools-5499" class="comment-tools"></div><div class="clear"></div><div id="comment-5499-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

