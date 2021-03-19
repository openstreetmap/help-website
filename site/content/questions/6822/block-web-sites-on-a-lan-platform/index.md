+++
type = "question"
title = "Block web sites on a lan platform"
description = '''Hi Can I use Wire Shark to block certain web sites? I want to use it in an office environment and block certain sites that are not work related. Jani '''
date = "2011-10-10T02:43:00Z"
lastmod = "2011-10-10T02:49:00Z"
weight = 6822
keywords = [ "application" ]
aliases = [ "/questions/6822" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Block web sites on a lan platform](/questions/6822/block-web-sites-on-a-lan-platform)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6822-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>Can I use Wire Shark to block certain web sites?</p><p>I want to use it in an office environment and block certain sites that are not work related.</p><p>Jani</p></div><div id="question-tags" class="tags-container tags">application</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Oct '11, 02:43</strong></p><img src="https://secure.gravatar.com/avatar/fe633e865653fa933c802e62849ab162?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jani%20Louw%20Fourie&#39;s gravatar image" /><p>Jani Louw Fo...<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jani Louw Fourie has no accepted answers">0%</span></p></div></div><div id="comments-container-6822" class="comments-container"></div><div id="comment-tools-6822" class="comment-tools"></div><div class="clear"></div><div id="comment-6822-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6823"></span>

<div id="answer-container-6823" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6823-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, you can't. Think of Wireshark as a passive diagnostic tool, just like a doctor uses a stethoscope to listen to a patients body. It's doesn't affect it, it just listens.</p><p>What you need is to force your surfers to use a filtering proxy, meaning that they can't surf directly anymore but need to ask a web proxy for whatever they want. On that proxy, you can then filter content.</p><p>Take a look at Squid for example: <a href="http://www.squid-cache.org">www.squid-cache.org</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Oct '11, 02:49</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-6823" class="comments-container"><span id="6825"></span><div id="comment-6825" class="comment"><div id="post-6825-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper</p><p>Thank you for your help!</p></div><div id="comment-6825-info" class="comment-info"><span class="comment-age">(10 Oct '11, 04:45)</span> Jani Louw Fo...</div></div><span id="6837"></span><div id="comment-6837" class="comment"><div id="post-6837-score" class="comment-score"></div><div class="comment-text"><p>BTW<br />
You can use Wireshark to create ACL entries.<br />
Go to:<br />
- Tools<br />
- Firewall ACL Rules<br />
<br />
This allows you to create command-line ACL rules for many different firewall products, including Cisco IOS, Linux Netfilter (iptables), OpenBSD pf and Windows Firewall (via netsh). Rules for MAC addresses, IPv4 addresses, TCP and UDP ports, and IPv4+port combinations are supported.<br />
<a href="http://www.wireshark.org/docs/wsug_html_chunked/ChUseToolsMenuSection.html">http://www.wireshark.org/docs/wsug_html_chunked/ChUseToolsMenuSection.html</a></p></div><div id="comment-6837-info" class="comment-info"><span class="comment-age">(10 Oct '11, 11:47)</span> joke</div></div></div><div id="comment-tools-6823" class="comment-tools"></div><div class="clear"></div><div id="comment-6823-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

