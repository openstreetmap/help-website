+++
type = "question"
title = "Using Multiple IP ranges in one capture"
description = '''Hey, I haven&#x27;t been able to get this filter to work. Im trying to use multiple IP ranges. 4 of them.  I have been trying to use net Ex. net 192.168.0.0/88 but I want to use multiple at one time (net 192.168.0.0/88 and net 192.168.1.0/99 and net 192.168.2.0/77 and net 192.168.3.066)  I have tried  (n...'''
date = "2011-03-21T08:12:00Z"
lastmod = "2011-03-21T09:49:00Z"
weight = 2968
keywords = [ "ranges", "ip", "net", "multiple" ]
aliases = [ "/questions/2968" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Using Multiple IP ranges in one capture](/questions/2968/using-multiple-ip-ranges-in-one-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2968-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey,</p><p>I haven't been able to get this filter to work. Im trying to use multiple IP ranges. 4 of them.</p><p>I have been trying to use net</p><p>Ex. net 192.168.0.0/88</p><p>but I want to use multiple at one time</p><p>(net 192.168.0.0/88 and net 192.168.1.0/99 and net 192.168.2.0/77 and net 192.168.3.066)</p><p>I have tried (net 192.168.0.0/88) and (net 192.168.1.0/99) and (net 192.168.2.0/77) and (net 192.168.3.066)</p><p>What am I missing?</p></div><div id="question-tags" class="tags-container tags">ranges ip net multiple</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '11, 08:12</strong></p><img src="https://secure.gravatar.com/avatar/9ca5c8e0858cf475cbb33978d8c75e42?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hmacken&#39;s gravatar image" /><p>hmacken<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hmacken has no accepted answers">0%</span></p></div></div><div id="comments-container-2968" class="comments-container"></div><div id="comment-tools-2968" class="comment-tools"></div><div class="clear"></div><div id="comment-2968-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2973"></span>

<div id="answer-container-2973" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2973-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Just as Joke has said, you need to use "or" instead of "and" to collect packets from one of the given subnets. Regarding the subnet masks, what are the subnets exactly, as 192.168.0.0/88 is indeed an invalid notation. There are only 32 bits in an IPv4 address, so having a network mask of 88 bits is not possible. If you would like to collect packets for all 4 C-class subnets, you will have to use:</p><pre><code>net 192.168.0.0  or net 192.168.1.0  or net 192.168.2.0 or net 192.168.3.0</code></pre><p>Which of course can be shortened to</p><pre><code>net 192.168.0.0  mask 255.255.252.0</code></pre><p>If you only need parts of these subnets, for instance only the first 16 ip addresses of each subnet, you can use:</p><pre><code>    net 192.168.0.0 mask 255.255.255.240 or net 192.168.1.0 mask 255.255.255.240 or net 192.168.2.0 mask 255.255.255.240 or net 192.168.3.0 mask 255.255.255.240</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '11, 09:49</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2973" class="comments-container"><span id="2974"></span><div id="comment-2974" class="comment"><div id="post-2974-score" class="comment-score"></div><div class="comment-text"><p>I suppose I was reading the wiki incorrect then. im looking for a capture string for something like this</p><p>• 10.24.19.75 thru .87 • 10.22.20.77 thru .90</p></div><div id="comment-2974-info" class="comment-info"><span class="comment-age">(21 Mar '11, 10:07)</span> hmacken</div></div><span id="2976"></span><div id="comment-2976" class="comment"><div id="post-2976-score" class="comment-score"></div><div class="comment-text"><p>Any help here?</p></div><div id="comment-2976-info" class="comment-info"><span class="comment-age">(21 Mar '11, 11:27)</span> hmacken</div></div><span id="2977"></span><div id="comment-2977" class="comment"><div id="post-2977-score" class="comment-score">1</div><div class="comment-text"><p>BPF syntax does not have a range for IP addresses, just hosts and (sub)nets. You will have to break up the ip-address range into a set of subnets and hosts.</p></div><div id="comment-2977-info" class="comment-info"><span class="comment-age">(21 Mar '11, 11:46)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-2973" class="comment-tools"></div><div class="clear"></div><div id="comment-2973-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2970"></span>

<div id="answer-container-2970" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2970-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use or instead of and:<br />
net 192.168.0.0/88 or net 192.168.1.0/99 or net 192.168.2.0/77 or net 192.168.3.066</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '11, 08:50</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></p></div></div><div id="comments-container-2970" class="comments-container"><span id="2972"></span><div id="comment-2972" class="comment"><div id="post-2972-score" class="comment-score"></div><div class="comment-text"><p>Invalid capture filter: "net IP or net IP or net IP or net IP" That string isnt a valid capture filter (mask length must be &lt;=32)</p><p>Any ideas?</p></div><div id="comment-2972-info" class="comment-info"><span class="comment-age">(21 Mar '11, 09:33)</span> hmacken</div></div></div><div id="comment-tools-2970" class="comment-tools"></div><div class="clear"></div><div id="comment-2970-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

