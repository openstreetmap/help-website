+++
type = "question"
title = "Show IPV4 instead of IPV6 in Wireshark 1.10.xx (Mac)"
description = '''Hi, as the title said, I&#x27;d like to see ipv4 instead of ipv6 in my columns. Is there a quick way set it? Also, being new to this particular technology, I was wondering if there is simple way to export the summary list of website names/uri, time, source ip (v4)? Many thanks.'''
date = "2014-02-23T17:05:00Z"
lastmod = "2014-02-23T17:22:00Z"
weight = 30110
keywords = [ "uri", "ipv4", "ipv6" ]
aliases = [ "/questions/30110" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Show IPV4 instead of IPV6 in Wireshark 1.10.xx (Mac)](/questions/30110/show-ipv4-instead-of-ipv6-in-wireshark-110xx-mac)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30110-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, as the title said, I'd like to see ipv4 instead of ipv6 in my columns. Is there a quick way set it? Also, being new to this particular technology, I was wondering if there is simple way to export the summary list of website names/uri, time, source ip (v4)? Many thanks.</p></div><div id="question-tags" class="tags-container tags">uri ipv4 ipv6</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Feb '14, 17:05</strong></p><img src="https://secure.gravatar.com/avatar/1d20dc262a2159fad200a865f34d571d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="J%20A&#39;s gravatar image" /><p>J A<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="J A has no accepted answers">0%</span></p></div></div><div id="comments-container-30110" class="comments-container"></div><div id="comment-tools-30110" class="comment-tools"></div><div class="clear"></div><div id="comment-30110-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30111"></span>

<div id="answer-container-30111" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30111-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is no "instead of." An IPv6 packet doesn't have IPv4 addresses to show, unless there is some sort of tunneling going on and IPv4 packets are encapsulated inside IPv6 packets.</p><p>Wireshark's default Source and Destination address columns will show the highest layer addresses in the packet, whether that's Ethernet, IPv4, or IPv6.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Feb '14, 17:22</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-30111" class="comments-container"><span id="30112"></span><div id="comment-30112" class="comment"><div id="post-30112-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your prompt response, much appreciated. Wondering if you have any bright idea about the second part of the question...</p></div><div id="comment-30112-info" class="comment-info"><span class="comment-age">(23 Feb '14, 17:31)</span> J A</div></div><span id="30114"></span><div id="comment-30114" class="comment"><div id="post-30114-score" class="comment-score"></div><div class="comment-text"><p>It's best not to ask two unrelated questions at once; a Q&amp;A site isn't a forum, it's supposed to be a site where you can see if somebody's asked a given question already, and read the answer if they have, and ask if they haven't. Think of it as being like, to go all buzzwordy, a "crowdsourced FAQ".</p><p>So you might want to ask your second question separately, so people can find the answer if they have the same question.</p></div><div id="comment-30114-info" class="comment-info"><span class="comment-age">(23 Feb '14, 19:11)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-30111" class="comment-tools"></div><div class="clear"></div><div id="comment-30111-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

