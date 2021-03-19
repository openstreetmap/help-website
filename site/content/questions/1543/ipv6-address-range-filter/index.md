+++
type = "question"
title = "IPv6 address range filter"
description = '''How do I filter on a range of ipv6 addresses, for example an ipv6 filter similar to ipv4 192.168.0.0/16? I would like to filter on ipv6 addresses on my lan fe80::/10 but cannot seem to find the correct syntax. Thanks!'''
date = "2010-12-30T20:32:00Z"
lastmod = "2011-01-02T18:24:00Z"
weight = 1543
keywords = [ "filter", "capture", "ipv6" ]
aliases = [ "/questions/1543" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [IPv6 address range filter](/questions/1543/ipv6-address-range-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1543-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do I filter on a <em>range</em> of ipv6 addresses, for example an ipv6 filter similar to ipv4 192.168.0.0/16? I would like to filter on ipv6 addresses on my lan fe80::/10 but cannot seem to find the correct syntax.</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">filter capture ipv6</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Dec '10, 20:32</strong></p><img src="https://secure.gravatar.com/avatar/ecc6ae4a4b2a62d462723805508a7ff9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="debianuser&#39;s gravatar image" /><p>debianuser<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="debianuser has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Jan '11, 18:24</p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span></p></div></div><div id="comments-container-1543" class="comments-container"></div><div id="comment-tools-1543" class="comment-tools"></div><div class="clear"></div><div id="comment-1543-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="1593"></span>

<div id="answer-container-1593" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1593-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you trying to apply masks to IPv6 addresses in capture filters or display filters? For capture filters you'd use <code>net</code>:</p><pre><code>ip6 net fe00::/10</code></pre><p>As Sake said, you can't apply masks to IPv6 addresses in display filters (not yet, at least) but you can use comparison operators:</p><pre><code>ipv6.src &gt;= fe80:: &amp;&amp; ipv6.src &lt; fec0::</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '11, 18:24</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-1593" class="comments-container"><span id="1594"></span><div id="comment-1594" class="comment"><div id="post-1594-score" class="comment-score"></div><div class="comment-text"><p>Love that one, Gerald!</p></div><div id="comment-1594-info" class="comment-info"><span class="comment-age">(02 Jan '11, 19:01)</span> martyvis</div></div></div><div id="comment-tools-1593" class="comment-tools"></div><div class="clear"></div><div id="comment-1593-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1544"></span>

<div id="answer-container-1544" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1544-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>i just tried a few combinations myself, and am also stumped (using both WS 1.2 and 1.4). I thought that I had used this in past, but I'm not sure now.</p><p>Even looking through this Sharkfest '10 presentation, I can't find any clues there (lots of mentions of networks with masks, though no screenshots showing a relevant display filter). <a href="http://www.cacetech.com/sharkfest.10/B-6_Leutert%20Discovering%20IPv6%20with%20Wireshark.pdf">link text</a></p><p>Maybe no one has implemented this yet. If you don't get any positive responses, file a feature request bug.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Dec '10, 21:36</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p>martyvis<br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-1544" class="comments-container"></div><div id="comment-tools-1544" class="comment-tools"></div><div class="clear"></div><div id="comment-1544-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1548"></span>

<div id="answer-container-1548" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1548-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I just looked at the sourcecode and there is indeed no functionality implemented yet to accept a prefix-length in a display filter. I'm looking into it right now, but as I have not done much with the display filter engine, I'm not sure I will come up with a solution shortly.</p><p>Could you file an enhancement request on <a href="https://bugzilla.wireshark.org">https://bugzilla.wireshark.org</a> to be sure it won't get lost?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Dec '10, 00:59</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1548" class="comments-container"><span id="1552"></span><div id="comment-1552" class="comment"><div id="post-1552-score" class="comment-score"></div><div class="comment-text"><p>Done - <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5538">bug 5538</a></p></div><div id="comment-1552-info" class="comment-info"><span class="comment-age">(31 Dec '10, 04:55)</span> martyvis</div></div></div><div id="comment-tools-1548" class="comment-tools"></div><div class="clear"></div><div id="comment-1548-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

