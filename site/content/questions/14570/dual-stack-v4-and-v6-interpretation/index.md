+++
type = "question"
title = "Dual Stack V4 and V6 interpretation"
description = '''I&#x27;m doing a few packet captures for testing purposes with dual stack enabled (Both v4 and v6 addresses) but I&#x27;m unsure how to analyze the packets. Lets say I went to facebook (which has v6 enabled). Is there a way to use wireshark to determine what protocol (v4 or v6) that my browser ends up using f...'''
date = "2012-09-27T07:06:00Z"
lastmod = "2012-09-27T09:09:00Z"
weight = 14570
keywords = [ "dualstack", "ipv4", "ipv6" ]
aliases = [ "/questions/14570" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Dual Stack V4 and V6 interpretation](/questions/14570/dual-stack-v4-and-v6-interpretation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14570-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm doing a few packet captures for testing purposes with dual stack enabled (Both v4 and v6 addresses) but I'm unsure how to analyze the packets. Lets say I went to facebook (which has v6 enabled). Is there a way to use wireshark to determine what protocol (v4 or v6) that my browser ends up using for facebook. I see that it sends both A and AAAA queries and gets them back as well but I don't think it's possible for them to be using both. Does this relate to the response time? Thanks.</p></div><div id="question-tags" class="tags-container tags">dualstack ipv4 ipv6</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Sep '12, 07:06</strong></p><img src="https://secure.gravatar.com/avatar/4f982ffc2974e10ac7ef43dfa38aa0f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sub&#39;s gravatar image" /><p>Sub<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sub has no accepted answers">0%</span></p></div></div><div id="comments-container-14570" class="comments-container"></div><div id="comment-tools-14570" class="comment-tools"></div><div class="clear"></div><div id="comment-14570-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="14574"></span>

<div id="answer-container-14574" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14574-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Usually, clients prefer IPv6 connections if the DNS returns a AAAA answer AND the IPv6 stack has received a valid IPv6 prefix from it's default gateway router - meaning that there should be a valid route into the IPv6 internet.</p><p>If the application (webbrowser) is capable of supporting the "Happy Eyeballs" strategy it will open both IPv4 and Ipv6 connections at the same time and use the one with the faster response - so in that case the response time is a factor, because the slower connection will be torn down.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Sep '12, 09:08</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-14574" class="comments-container"></div><div id="comment-tools-14574" class="comment-tools"></div><div class="clear"></div><div id="comment-14574-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14575"></span>

<div id="answer-container-14575" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14575-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If teh DNS queries return both an AAAA record and an A record, then it is up to the application (browser) to decide to use IPv6 or IPv4. Most browsers will give preference to IPv6 over IPv4 by default. You can check by looking a bit further in the trace where there is a TCP SYN packet that connects to the IPvX address in the dns responses. You can then tell by the ethertype, the IP protocol being used or more easily by the IP addresses whether IPv6 or IPv4 was chosen by the application.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Sep '12, 09:09</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-14575" class="comments-container"><span id="14597"></span><div id="comment-14597" class="comment"><div id="post-14597-score" class="comment-score"></div><div class="comment-text"><p>Thanks for all the help! Would it also be acceptable to filter for http traffic and look for the text/html response and see what IP protocol that comes from?</p></div><div id="comment-14597-info" class="comment-info"><span class="comment-age">(28 Sep '12, 08:05)</span> Sub</div></div><span id="14598"></span><div id="comment-14598" class="comment"><div id="post-14598-score" class="comment-score"></div><div class="comment-text"><p>Yes indeed :-)</p></div><div id="comment-14598-info" class="comment-info"><span class="comment-age">(28 Sep '12, 08:12)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-14575" class="comment-tools"></div><div class="clear"></div><div id="comment-14575-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

