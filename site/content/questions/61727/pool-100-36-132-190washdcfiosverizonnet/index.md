+++
type = "question"
title = "pool-100-36-132-190.washdc.fios.verizon.net"
description = '''Hello. I just want to know what is going on with this IP. I understand where the fios.verizon.net comes fron. However the pool and washdc parts confuse me. I see the ip address, have looked it up and it says that this particular IP is for a device in Virginia. I searched using whois on networktools....'''
date = "2017-06-01T00:02:00Z"
lastmod = "2017-06-01T14:19:00Z"
weight = 61727
keywords = [ "url" ]
aliases = [ "/questions/61727" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [pool-100-36-132-190.washdc.fios.verizon.net](/questions/61727/pool-100-36-132-190washdcfiosverizonnet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61727-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello. I just want to know what is going on with this IP. I understand where the fios.verizon.net comes fron. However the pool and washdc parts confuse me. I see the ip address, have looked it up and it says that this particular IP is for a device in Virginia. I searched using whois on networktools.com.</p><p>My question is, what is the pool and washdc parts of the url. Also considering this is FTP traffic, is this device an ftp server hosted by verizon, and if it is how do i find out who is responcible for the traffic coming from it.</p><p>Thank you for your time.</p></div><div id="question-tags" class="tags-container tags">url</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '17, 00:02</strong></p><img src="https://secure.gravatar.com/avatar/23ec94e8d1b7d11564dceb074a60c9ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eldenmac99&#39;s gravatar image" /><p>eldenmac99<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eldenmac99 has no accepted answers">0%</span></p></div></div><div id="comments-container-61727" class="comments-container"></div><div id="comment-tools-61727" class="comment-tools"></div><div class="clear"></div><div id="comment-61727-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61733"></span>

<div id="answer-container-61733" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61733-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>it says that this particular IP is for a device in Virginia</p></blockquote><p>In fact, it's probably in <a href="https://en.wikipedia.org/wiki/Northern_Virginia">Northern Virginia</a>, as per the "washdc", as in "Washington, DC".</p><p>"pool-100-36-132-90" probably means that it's a dynamically assigned IP address from Verizon's pool of addresses; the address is 100.36.132.90.</p><blockquote><p>Also considering this is FTP traffic, is this device an ftp server</p></blockquote><p>Not necessarily. It could be an FTP <em>client</em>. What sort of FTP <em>control</em> traffic (commands and responses, as opposed to <em>data</em> traffic) is coming from that host, and what sort of traffic is going to that host? If commands are coming from the host and responses are going to the host, it's an FTP client; if commands are going to the host and responses are coming from the host, it's an FTP server.</p><blockquote><p>hosted by verizon</p></blockquote><p><em>If</em> it's a server - which I suspect it's <em>not</em> - it's probably not stored on one of Verizon's servers; it's probably stored on some Verizon customer's machine.</p><blockquote><p>how do i find out who is responcible for the traffic coming from it.</p></blockquote><p>Ask Verizon who had that IP address <em>during the times when you saw traffic to and from that host</em>. "Dynamic" means it doesn't belong to a particular machine - it's temporarily assigned to that machine for some period of time, but that machine might get a different address assigned to it at another time.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '17, 14:19</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-61733" class="comments-container"><span id="61739"></span><div id="comment-61739" class="comment"><div id="post-61739-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the quick responce. You are right now that I think about it. My geological map is kinda crap (my mental one). It must have been aclient. They were sending commands in to the server as apposed to sending responces. When you say a verizon customer's machine, I asume you are refering to a customer who is serfing the internet through verizon as an ISP?</p></div><div id="comment-61739-info" class="comment-info"><span class="comment-age">(01 Jun '17, 21:00)</span> eldenmac99</div></div><span id="61740"></span><div id="comment-61740" class="comment"><div id="post-61740-score" class="comment-score"></div><div class="comment-text"><blockquote><p>When you say a verizon customer's machine, I asume you are refering to a customer who is serfing the internet through verizon as an ISP?</p></blockquote><p>Yes.</p></div><div id="comment-61740-info" class="comment-info"><span class="comment-age">(01 Jun '17, 21:46)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-61733" class="comment-tools"></div><div class="clear"></div><div id="comment-61733-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

