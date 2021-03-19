+++
type = "question"
title = "block an ip with iptables"
description = '''hi, for school i have to block an ip with iptables and monitor that with wireshark. the result shoul be like this on the terminal: ping 130.136.4.145 PING 130.136.4.145 (130.136.4.145) 56(84) bytes of data. Destination host unreachable and on wireshark and log http://imageshack.com/a/img823/7972/tqf...'''
date = "2014-01-10T10:12:00Z"
lastmod = "2014-01-10T11:10:00Z"
weight = 28775
keywords = [ "iptables", "ip", "host", "block", "wireshark" ]
aliases = [ "/questions/28775" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [block an ip with iptables](/questions/28775/block-an-ip-with-iptables)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28775-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28775-score" class="post-score" title="current number of votes">0</div><span id="post-28775-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi, for school i have to block an ip with iptables and monitor that with wireshark.</p><p>the result shoul be like this on the terminal: ping 130.136.4.145 PING 130.136.4.145 (130.136.4.145) 56(84) bytes of data. Destination host unreachable</p><p>and on wireshark and log <a href="http://imageshack.com/a/img823/7972/tqf9.jpg">http://imageshack.com/a/img823/7972/tqf9.jpg</a></p><p>the question is: what's the command that blocks the ip?? I tried some command but nothing happened. Thanks for the answer</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-iptables" rel="tag" title="see questions tagged &#39;iptables&#39;">iptables</span> <span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-host" rel="tag" title="see questions tagged &#39;host&#39;">host</span> <span class="post-tag tag-link-block" rel="tag" title="see questions tagged &#39;block&#39;">block</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jan '14, 10:12</strong></p><img src="https://secure.gravatar.com/avatar/664dcc856e8c40b60cd7741416249cb0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="verde&#39;s gravatar image" /><p><span>verde</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="verde has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Jan '14, 10:31</strong> </span></p></div></div><div id="comments-container-28775" class="comments-container"></div><div id="comment-tools-28775" class="comment-tools"></div><div class="clear"></div><div id="comment-28775-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28776"></span>

<div id="answer-container-28776" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28776-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28776-score" class="post-score" title="current number of votes">2</div><span id="post-28776-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You ought to be able to find all that you need with respect to <code>iptables</code> from sources, such as:</p><ul><li>The <a href="http://linux.die.net/man/8/iptables">iptables man page</a></li><li>The <a href="http://en.wikipedia.org/wiki/Iptables">iptables wikipedia article</a></li><li>The <a href="http://www.netfilter.org/projects/iptables/index.html">iptables project page</a>, in particular this <a href="http://www.netfilter.org/documentation/HOWTO//packet-filtering-HOWTO-7.html">Packet Filtering HowTo</a> page.</li><li>Various books about iptables and firewalls, such as:</li><li><a href="http://www.amazon.com/Linux-iptables-Pocket-Reference-Gregor/dp/0596005695">Linux iptables Pocket Reference</a></li><li><a href="http://www.amazon.com/Linux-Firewalls-Edition-Steve-Suehring/dp/0672327716/ref=pd_sim_b_5">Linux Firewalls (3rd Edition)</a></li><li>...</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jan '14, 11:10</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-28776" class="comments-container"></div><div id="comment-tools-28776" class="comment-tools"></div><div class="clear"></div><div id="comment-28776-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

