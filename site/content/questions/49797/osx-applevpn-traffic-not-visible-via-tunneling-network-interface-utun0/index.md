+++
type = "question"
title = "OSX AppleVPN traffic not visible via tunneling network interface (utun0)"
description = '''&#x27;m running Mac OS/X 10.11, and the VPN is a Apple IPSec VPN.  I could verify that the host is routing correctly over the VPN interface (which Mac OS/X calls &quot;utun0&quot;) $ netstat -rn Routing tables  Internet: Destination Gateway Flags Refs Use Netif Expire default link#10 UCS 29 0 utun0 ...  However, w...'''
date = "2016-02-03T14:47:00Z"
lastmod = "2016-02-08T09:13:00Z"
weight = 49797
keywords = [ "utun0", "vpn", "osx" ]
aliases = [ "/questions/49797" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSX AppleVPN traffic not visible via tunneling network interface (utun0)](/questions/49797/osx-applevpn-traffic-not-visible-via-tunneling-network-interface-utun0)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49797-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49797-score" class="post-score" title="current number of votes">0</div><span id="post-49797-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>'m running Mac OS/X 10.11, and the VPN is a Apple IPSec VPN. I could verify that the host is routing correctly over the VPN interface (which Mac OS/X calls "utun0")</p><pre><code>$ netstat -rn
Routing tables

Internet:
Destination        Gateway            Flags        Refs      Use   Netif Expire
default            link#10            UCS            29        0   utun0
...</code></pre><p>However, when I run and listen on interface utun0, I couldn't capture any traffic.</p><pre><code>$ sudo tcpdump -i utun0
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on utun0, link-type NULL (BSD loopback), capture size 65535 bytes

(nothing)</code></pre><p>Is there something special I need to do so that packets sent over a VPN link show up?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-utun0" rel="tag" title="see questions tagged &#39;utun0&#39;">utun0</span> <span class="post-tag tag-link-vpn" rel="tag" title="see questions tagged &#39;vpn&#39;">vpn</span> <span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Feb '16, 14:47</strong></p><img src="https://secure.gravatar.com/avatar/a543093d02efde468d2cdeca8ad18703?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kjee&#39;s gravatar image" /><p><span>Kjee</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kjee has no accepted answers">0%</span></p></div></div><div id="comments-container-49797" class="comments-container"><span id="49972"></span><div id="comment-49972" class="comment"><div id="post-49972-score" class="comment-score"></div><div class="comment-text"><p>I tried with Wireshark, but the result is just same.</p></div><div id="comment-49972-info" class="comment-info"><span class="comment-age">(08 Feb '16, 08:11)</span> <span class="comment-user userinfo">Kjee</span></div></div></div><div id="comment-tools-49797" class="comment-tools"></div><div class="clear"></div><div id="comment-49797-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49975"></span>

<div id="answer-container-49975" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49975-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49975-score" class="post-score" title="current number of votes">1</div><span id="post-49975-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I tried with Wireshark, but the result is just same.</p></blockquote><p>Wireshark and tcpdump both capture traffic using libpcap, and libpcap would be using BPF, so they'll both succeed or fail in the exact same way as they're going through the exact same OS code path.</p><p>See the answer to <a href="https://ask.wireshark.org/questions/4812/on-mac-osx-i-cant-capture-packets-sent-over-a-vpn">a similar question somebody asked</a>; it might simply not be possible to capture that traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Feb '16, 09:13</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-49975" class="comments-container"></div><div id="comment-tools-49975" class="comment-tools"></div><div class="clear"></div><div id="comment-49975-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

