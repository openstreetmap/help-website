+++
type = "question"
title = "304 and 404 errors"
description = '''Hi, I have a problem with Wireshark. The idea is that when listening on HTTP packets they show an error of 304 and 404 and i can&#x27;t read the address of the page. I use it on the Back Track 5 R3. Before running the Wiresharka I use the command &quot;echo 1/proc/sys/net/ipv4/ip_forward &amp;gt; and&quot; arpspoof-i ...'''
date = "2013-08-25T07:04:00Z"
lastmod = "2013-08-25T11:56:00Z"
weight = 24022
keywords = [ "error", "404", "304", "wireshark", "backtrack" ]
aliases = [ "/questions/24022" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [304 and 404 errors](/questions/24022/304-and-404-errors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24022-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a problem with Wireshark. The idea is that when listening on HTTP packets they show an error of 304 and 404 and i can't read the address of the page. I use it on the Back Track 5 R3. Before running the Wiresharka I use the command "echo 1/proc/sys/net/ipv4/ip_forward &gt; and" arpspoof-i eth0-t 192.168.1.1 192.168.1.9 "in order to be able to listen. Gets them, but flawed with errors. PS: Sorry for my English.</p><p>I see it:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/error_1.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">error 404 304 wireshark backtrack</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Aug '13, 07:04</strong></p><img src="https://secure.gravatar.com/avatar/81260db0918558fbd545e820dba86540?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marcinxxl2&#39;s gravatar image" /><p>Marcinxxl2<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marcinxxl2 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 25 Aug '13, 07:56</p></div></div><div id="comments-container-24022" class="comments-container"><span id="24027"></span><div id="comment-24027" class="comment"><div id="post-24027-score" class="comment-score"></div><div class="comment-text"><blockquote><p>The idea is that when listening on HTTP packets they show an error of 304 and 404</p></blockquote><p>304 typically means that the system fetching the page has a cached copy and is asking 1) whether the page has been modified since a certain time (the time when the cached copy was fetched) and 2) for a copy of the page if it has been modified since then. 404, of course, means that the page in question doesn't exist.</p><blockquote><p>and i can't read the address of the page</p></blockquote><p>By "the address of the page" I assume you mean the URL of the page; you'll see that in the HTTP <em>request</em>, not the <em>reply</em>. Are you not capturing the requests? Or are they not being sent from 192.168.1.9, so that they're not showing up with your display filter?</p></div><div id="comment-24027-info" class="comment-info"><span class="comment-age">(25 Aug '13, 10:05)</span> Guy Harris ♦♦</div></div><span id="24033"></span><div id="comment-24033" class="comment"><div id="post-24033-score" class="comment-score"></div><div class="comment-text"><p>And intercepts the request and they are sent from this address. I do not know why all the HTTP packets give error 304 or 404. When I run Wireshark on listening computer does not show on these errors, and the URL of the page.</p></div><div id="comment-24033-info" class="comment-info"><span class="comment-age">(25 Aug '13, 11:31)</span> Marcinxxl2</div></div></div><div id="comment-tools-24022" class="comment-tools"></div><div class="clear"></div><div id="comment-24022-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24036"></span>

<div id="answer-container-24036" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24036-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><pre><code>arpspoof -i eth0 -t 192.168.1.1 192.168.1.9</code></pre><p>To quote <a href="http://linux.die.net/man/8/arpspoof">the arpspoof man page</a>:</p><blockquote><p><strong>Synopsis</strong></p><p><strong>arpspoof</strong> [<strong>-i</strong> <em>interface</em>] [<strong>-t</strong> <em>target</em>] <em>host</em></p><p><strong>Description</strong></p><p><strong>arpspoof</strong> redirects packets from a target host (or all hosts) on the LAN intended for another host on the LAN by forging ARP replies. This is an extremely effective way of sniffing traffic on a switch.</p></blockquote><pre><code>...</code></pre><blockquote><p><strong>Options</strong></p><p><strong>-i</strong> <em>interface</em></p><p>Specify the interface to use.</p><p><strong>-t</strong> <em>target</em></p><p>Specify a particular host to ARP poison (if not specified, all hosts on the LAN).</p><p><em>host</em></p><p>Specify the host you wish to intercept packets for (usually the local gateway).</p></blockquote><p>so that command is ARP-spoofing so that traffic <em>to</em> 192.168.1.9 is redirected through 192.168.1.1, but it doesn't affect traffic <em>from</em> 192.168.1.9, so you will only see the HTTP replies <em>to</em> 192.168.1.9, not HTTP requests <em>from</em> 192.168.1.9, so you won't see the requests, and therefore will not see the URLs.</p><p>As I said in my comment, the HTTP packets that get a 304 do so because the HTTP request said "send me the page only if it's been modified after this time" and it <em>hasn't</em> been modified since that time, and the HTTP packets that get a 404 do so because the HTTP request said "send me the page with this URL" and there <strong><em>IS</em></strong> no page with that URL; <a href="http://tools.ietf.org/html/rfc2616">that's how HTTP <em>works</em></a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Aug '13, 11:56</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Aug '13, 11:58</p></div></div><div id="comments-container-24036" class="comments-container"><span id="24037"></span><div id="comment-24037" class="comment"><div id="post-24037-score" class="comment-score"></div><div class="comment-text"><p>Actually, sorry, my mistake. You know how to do that was in two pages?</p></div><div id="comment-24037-info" class="comment-info"><span class="comment-age">(25 Aug '13, 12:14)</span> Marcinxxl2</div></div><span id="24040"></span><div id="comment-24040" class="comment"><div id="post-24040-score" class="comment-score"></div><div class="comment-text"><blockquote><p>You know how to do that was in two pages?</p></blockquote><p>I'm not sure I understand what you're asking here.</p></div><div id="comment-24040-info" class="comment-info"><span class="comment-age">(25 Aug '13, 12:50)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-24036" class="comment-tools"></div><div class="clear"></div><div id="comment-24036-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

