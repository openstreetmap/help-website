+++
type = "question"
title = "Decryption of Zigbee packets, works in Win32 version, not in Linux version"
description = '''I am having difficulty decrypting Zigbee packets on my 1.6.5 installation on Gentoo Linux, installed from an ebuild. However, the same version installed on a win32 (WinXP) system auto decrypts and finds the key correctly (same .pcap file). I have tried manally entering the key into the Linux release...'''
date = "2012-03-16T23:56:00Z"
lastmod = "2012-03-20T21:44:00Z"
weight = 9597
keywords = [ "zigbee", "win32", "linux", "gentoo", "wireshark" ]
aliases = [ "/questions/9597" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Decryption of Zigbee packets, works in Win32 version, not in Linux version](/questions/9597/decryption-of-zigbee-packets-works-in-win32-version-not-in-linux-version)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9597-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9597-score" class="post-score" title="current number of votes">0</div><span id="post-9597-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am having difficulty decrypting Zigbee packets on my 1.6.5 installation on Gentoo Linux, installed from an ebuild. However, the same version installed on a win32 (WinXP) system auto decrypts and finds the key correctly (same .pcap file). I have tried manally entering the key into the Linux release and it still does not decrypt the encrypted packets. You can find the .pcap file at the following URL, <a href="https://eecs.wsu.edu/~adrassal/output.pcap">https://eecs.wsu.edu/~adrassal/output.pcap</a></p><p>If someone has time, please download the .pcap file and see if it will decrypt on your Linux system, I can't get the packets to auto decrypt on my Win32 system. The .pcap file includes a packet with the key, so it auto decrypts the whole file. If you find any useful results, please let me know by reply post.</p><p>Thanks. Allan Drassal Washington State University</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-zigbee" rel="tag" title="see questions tagged &#39;zigbee&#39;">zigbee</span> <span class="post-tag tag-link-win32" rel="tag" title="see questions tagged &#39;win32&#39;">win32</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span> <span class="post-tag tag-link-gentoo" rel="tag" title="see questions tagged &#39;gentoo&#39;">gentoo</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Mar '12, 23:56</strong></p><img src="https://secure.gravatar.com/avatar/396635874c32c82dd60009df222be59a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="drasal&#39;s gravatar image" /><p><span>drasal</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="drasal has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Mar '12, 23:57</strong> </span></p></div></div><div id="comments-container-9597" class="comments-container"><span id="9670"></span><div id="comment-9670" class="comment"><div id="post-9670-score" class="comment-score"></div><div class="comment-text"><p>I am running the same version on Win32 and Linux (Gentoo) (ersion 1.6.5). I have the same settings for the Zigbee protocol preferences. At first, in the Linux version, I tried to enter the key in so many different ways, but never got it to work correctly. I eventually installed it on my Win32 workstation and it automatically decoded packets (from a fresh install, no changing any preferences). But, I did check and the Zigbee configuration is the same.</p><p>Has anyone else had troule decrypting Zigbee packets on the Linux build (version 1.6.5)?</p></div><div id="comment-9670-info" class="comment-info"><span class="comment-age">(20 Mar '12, 21:44)</span> <span class="comment-user userinfo">drasal</span></div></div></div><div id="comment-tools-9597" class="comment-tools"></div><div class="clear"></div><div id="comment-9597-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9623"></span>

<div id="answer-container-9623" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9623-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9623-score" class="post-score" title="current number of votes">0</div><span id="post-9623-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you running the same version of Wireshark on the Linux box and the Windows box?</p><p>Did you check the 802.15.4 and Zigbee protocol preferences on both boxes? Are they the same?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Mar '12, 23:49</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-9623" class="comments-container"></div><div id="comment-tools-9623" class="comment-tools"></div><div class="clear"></div><div id="comment-9623-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9625"></span>

<div id="answer-container-9625" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9625-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9625-score" class="post-score" title="current number of votes">0</div><span id="post-9625-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>After focusing on 6LoWPAN and ZigBee networks, I found the Perytons Analyzer a much more flexible and friendly tool for me. They have a 30 days free evaluation download in their site and although they don't have a Linux version (only Windows), their tool saved me a lot of work and headaches in my designs. You may want to try it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '12, 02:48</strong></p><img src="https://secure.gravatar.com/avatar/0169872b21ad8da114515f99ee7eeef6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AviDrugi&#39;s gravatar image" /><p><span>AviDrugi</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AviDrugi has no accepted answers">0%</span></p></div></div><div id="comments-container-9625" class="comments-container"></div><div id="comment-tools-9625" class="comment-tools"></div><div class="clear"></div><div id="comment-9625-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

