+++
type = "question"
title = "PC wont take IP given by DHCPACK, tried multiple routers (dhcp servers)"
description = '''Hi all, I have a few machines now that are exhibiting this problem by where i can see the DHCP Discover -&amp;gt; DHCP Offer -&amp;gt; DHCP Request -&amp;gt; DHCP ACK but the client does not take the address given to it. The MAC addresses match so its not like it should not be responding. I have tried multiple ...'''
date = "2013-09-18T20:19:00Z"
lastmod = "2013-09-19T01:02:00Z"
weight = 24935
keywords = [ "dhcp", "cisco", "82579lm", "ios", "server" ]
aliases = [ "/questions/24935" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [PC wont take IP given by DHCPACK, tried multiple routers (dhcp servers)](/questions/24935/pc-wont-take-ip-given-by-dhcpack-tried-multiple-routers-dhcp-servers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24935-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24935-score" class="post-score" title="current number of votes">0</div><span id="post-24935-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I have a few machines now that are exhibiting this problem by where i can see the DHCP Discover -&gt; DHCP Offer -&gt; DHCP Request -&gt; DHCP ACK but the client does not take the address given to it. The MAC addresses match so its not like it should not be responding. I have tried multiple cisco routers using both 12.4 and 15.0 IOS releases, I have tried 867 and 887 routers and i get the same issue. The laptop that I am using to test is plugged straight into the back of the router with nothing else plugged in.</p><p>Has anyone seen this before? Its getting REAL annoying as these are branch offices which are not local, so i cant debug them all that much, do the point where I flew out to one of them, swapped out their router so at least I can have a router back in the office that exhibits this behaviour so i can at least test it.<br />
</p><p>Older machines (without the intel 82579LM chipset) seem to work fine, so its not like its a router issue I dont think.</p><p>I'm out of ideas... can I post the capture perhaps in case there is something i am missing?</p><p>[edit] The clients are Windows 7 x64. I have just tested it on another NIC and it would appear that the intel nic is not doing a DHCP INFORM like it should? what would cause that?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dhcp" rel="tag" title="see questions tagged &#39;dhcp&#39;">dhcp</span> <span class="post-tag tag-link-cisco" rel="tag" title="see questions tagged &#39;cisco&#39;">cisco</span> <span class="post-tag tag-link-82579lm" rel="tag" title="see questions tagged &#39;82579lm&#39;">82579lm</span> <span class="post-tag tag-link-ios" rel="tag" title="see questions tagged &#39;ios&#39;">ios</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Sep '13, 20:19</strong></p><img src="https://secure.gravatar.com/avatar/da570827e4c74174c0b6007fef3e915f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pontiff&#39;s gravatar image" /><p><span>pontiff</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pontiff has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Sep '13, 20:46</strong> </span></p></div></div><div id="comments-container-24935" class="comments-container"></div><div id="comment-tools-24935" class="comment-tools"></div><div class="clear"></div><div id="comment-24935-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24938"></span>

<div id="answer-container-24938" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24938-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24938-score" class="post-score" title="current number of votes">0</div><span id="post-24938-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If a client does not take an IP address that was assigned by a complete DHCP DORA process it usually means that the IP is already in use by another system. Right after the last DHCK ACK you should see that the client is using Gratuitous ARPs to check if the IP it was given is in use. If it receives an answer to that ARP the IP is in use, and the client will discard and never use it. Check if the client does perform this kind of test and if there is a duplicate IP address. Often someone configures a static IP that is part of the DHCP range (by mistake or ignorance), which will cause this kind of problem.</p><p>Worst case is when you have a static IP-to-MAC mapping in the DHCP server so that the client always gets the same IP but can never use it because it is already taken. In that case the DHCP process will go on forever because the client will always refuse the IP and will always get it assigned again in the next run.</p><p>DHCP inform is not mandatory; it may or may not appear.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Sep '13, 22:23</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-24938" class="comments-container"><span id="24939"></span><div id="comment-24939" class="comment"><div id="post-24939-score" class="comment-score"></div><div class="comment-text"><p>Hi jasper, that's what I would have though too but I don't see it doing that, it just goes back to DHCP discover. Is there a way I can post the capture somewhere? This laptop is doing it with 2 different routers as I say so I am pretty sure it's a client issue somewhere.</p><p>No one issuing the ip. This is the very first client on the router so nothing can interfere</p></div><div id="comment-24939-info" class="comment-info"><span class="comment-age">(18 Sep '13, 23:11)</span> <span class="comment-user userinfo">pontiff</span></div></div><span id="24945"></span><div id="comment-24945" class="comment"><div id="post-24945-score" class="comment-score"></div><div class="comment-text"><p>You could post the trace at <a href="http://www.cloudshark.org">http://www.cloudshark.org</a> and post the link here. Is it a trace taken directly at/on the client, oder somewhere else?</p></div><div id="comment-24945-info" class="comment-info"><span class="comment-age">(19 Sep '13, 01:02)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-24938" class="comment-tools"></div><div class="clear"></div><div id="comment-24938-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

