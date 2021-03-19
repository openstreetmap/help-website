+++
type = "question"
title = "802.11 Decryption is different on Mac and Windows"
description = '''Ladies and Gents,  Thanks in advance for looking at this problem. As I was learning about monitoring wifi traffic, I found something that bothered me. First of all, I am running Wireshark on MacBook Late 2011 with Intel i7 processor. I was trying to decrypt the example that is attached to 802.11 dec...'''
date = "2015-01-29T16:32:00Z"
lastmod = "2015-01-30T08:37:00Z"
weight = 39492
keywords = [ "windows", "decryption", "802.11", "macbook" ]
aliases = [ "/questions/39492" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [802.11 Decryption is different on Mac and Windows](/questions/39492/80211-decryption-is-different-on-mac-and-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39492-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39492-score" class="post-score" title="current number of votes">0</div><span id="post-39492-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Ladies and Gents,</p><p>Thanks in advance for looking at this problem.</p><p>As I was learning about monitoring wifi traffic, I found something that bothered me.</p><p>First of all, I am running Wireshark on MacBook Late 2011 with Intel i7 processor.</p><p>I was trying to decrypt the example that is attached to 802.11 decryption wiki page with phrase: Induction and SSID: Coherer.</p><p>However I found that how it shows on Data seems little bit off. Frame 99 is the first frame that suppose to be decrypted. After I put the decryption key in, Window version of Wireshark decrypted successfully while Mac did not. I used the same file for both.</p><p>I found that in data field, Windows version Wireshark has 344 bytes while Mac version had 348 bytes.</p><p>In Data field, Windows version shows as following:</p><p>Data: 7eccf60ac1ddffb04796c3...</p><p>While Mac version shows as following</p><p>Data: 000000007eccf60ac1ddffb04796c3...</p><p>I don't know this is a Mac version Wireshark problem or I am doing something wrong. I ask experts' for a help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span> <span class="post-tag tag-link-macbook" rel="tag" title="see questions tagged &#39;macbook&#39;">macbook</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '15, 16:32</strong></p><img src="https://secure.gravatar.com/avatar/4446c851e960ac5207edd95260b24a05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Daniel_H&#39;s gravatar image" /><p><span>Daniel_H</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Daniel_H has no accepted answers">0%</span></p></div></div><div id="comments-container-39492" class="comments-container"><span id="39503"></span><div id="comment-39503" class="comment"><div id="post-39503-score" class="comment-score"></div><div class="comment-text"><p>Which version of Wireshark is running on each system? Are your Wireshark preferences the same on both systems? On my Windows 7 64-bit PC, I tested with Wireshark versions 1.99.2, 1.12.3, 1.10.7 and 1.8.7, and for frame 99 I get 336 bytes of "Decrypted CCMP data", broken out as:</p><pre><code>Logical-Link Control (llc):         8 bytes
Internet Protocol Version 4 (ip):  20 bytes
User Datagram Protocol (udp):       8 bytes
Bootstrap Protocol (bootp):       300 bytes
--------------------------------------------
TOTAL:                            336 bytes</code></pre><p>When not encrypted, all versions show 344 bytes, with 4 trailing bytes of 2c a8 94 27 not highlighted, so presumably those bytes are just padding. The 4 bytes of 00 00 00 00 preceding the data are decoded as part of the 8 bytes comprising the "CCMP Ext. Initialization Vector".</p><p>I don't have a Mac to compare, and I can't say if 344 or 348 is correct. If there's some bug with the Windows version, it looks like it's been there for quite a while.</p></div><div id="comment-39503-info" class="comment-info"><span class="comment-age">(30 Jan '15, 08:37)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-39492" class="comment-tools"></div><div class="clear"></div><div id="comment-39492-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

