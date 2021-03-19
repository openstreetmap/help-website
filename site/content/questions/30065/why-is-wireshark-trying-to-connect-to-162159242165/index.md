+++
type = "question"
title = "Why is Wireshark trying to connect to 162.159.242.165 ???"
description = '''I have just openend a capture session and looking at the packets go by I get TLS connections to 162.159.242.165. Whois resolves to Cloudfare and blog.wireshark.org. WTF? http://162.159.242.165.ipaddress.com/ http://blog.wireshark.org.ipaddress.com/ http://www.herdprotect.com/ip-address-162.159.242.1...'''
date = "2014-02-20T17:56:00Z"
lastmod = "2014-02-20T18:54:00Z"
weight = 30065
keywords = [ "162.159.242.165", "whois", "wireshark" ]
aliases = [ "/questions/30065" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why is Wireshark trying to connect to 162.159.242.165 ???](/questions/30065/why-is-wireshark-trying-to-connect-to-162159242165)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30065-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30065-score" class="post-score" title="current number of votes">0</div><span id="post-30065-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have just openend a capture session and looking at the packets go by I get TLS connections to 162.159.242.165. Whois resolves to Cloudfare and blog.wireshark.org. WTF?</p><p><a href="http://162.159.242.165.ipaddress.com/">http://162.159.242.165.ipaddress.com/</a> <a href="http://blog.wireshark.org.ipaddress.com/">http://blog.wireshark.org.ipaddress.com/</a> <a href="http://www.herdprotect.com/ip-address-162.159.242.165.aspx">http://www.herdprotect.com/ip-address-162.159.242.165.aspx</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-162.159.242.165" rel="tag" title="see questions tagged &#39;162.159.242.165&#39;">162.159.242.165</span> <span class="post-tag tag-link-whois" rel="tag" title="see questions tagged &#39;whois&#39;">whois</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Feb '14, 17:56</strong></p><img src="https://secure.gravatar.com/avatar/3c020d0ed05db3ac140568603d4be581?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Leinad&#39;s gravatar image" /><p><span>Leinad</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Leinad has no accepted answers">0%</span></p></div></div><div id="comments-container-30065" class="comments-container"><span id="30066"></span><div id="comment-30066" class="comment"><div id="post-30066-score" class="comment-score"></div><div class="comment-text"><p><img src="https://osqa-ask.wireshark.org/upfiles/shark.png" alt="alt text" /></p></div><div id="comment-30066-info" class="comment-info"><span class="comment-age">(20 Feb '14, 17:58)</span> <span class="comment-user userinfo">Leinad</span></div></div></div><div id="comment-tools-30065" class="comment-tools"></div><div class="clear"></div><div id="comment-30065-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30067"></span>

<div id="answer-container-30067" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30067-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30067-score" class="post-score" title="current number of votes">1</div><span id="post-30067-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Note that this address is also used by the main site:</p><pre><code>$ host www.wireshark.org
www.wireshark.org has address 162.159.241.165
www.wireshark.org has address 162.159.242.165</code></pre><p>As well as this site, the bug tracker, and others:</p><pre><code>$ host ask.wireshark.org
ask.wireshark.org has address 162.159.242.165
ask.wireshark.org has address 162.159.241.165

$ host bugs.wireshark.org
bugs.wireshark.org has address 162.159.241.165
bugs.wireshark.org has address 162.159.242.165</code></pre><p>Does the TLS connection contain an SNI field? Wireshark periodically checks www.wireshark.org for updates, which is likely the traffic you're seeing. You can disable this via <em>Edit→Preferences→User Interface</em>. (...and if you disable this setting and <em>still</em> see this behavior please <a href="https://bugs.wireshark.org/">let us know</a>.)</p><p>We currently use CloudFlare because they're effective at blocking DDoS attacks. I'm not sure why we get DDoS attacks. You'd have to ask the attackers.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Feb '14, 18:54</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></img></div></div><div id="comments-container-30067" class="comments-container"></div><div id="comment-tools-30067" class="comment-tools"></div><div class="clear"></div><div id="comment-30067-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

