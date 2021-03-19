+++
type = "question"
title = "Only one of three computers can capture RTP packets...?"
description = '''I installed ubuntu 14.04 on 3 PCs, and use &quot;apt-get install wireshark&quot; to installed wireshark on them. They all work under monitor mode, but only one of them (desktop) can capture RTP packets, the other two laptops can sniffer other packets, but except RTP packets.......... why...?'''
date = "2015-04-24T19:31:00Z"
lastmod = "2015-04-24T23:26:00Z"
weight = 41814
keywords = [ "rtp" ]
aliases = [ "/questions/41814" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Only one of three computers can capture RTP packets...?](/questions/41814/only-one-of-three-computers-can-capture-rtp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41814-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I installed ubuntu 14.04 on 3 PCs, and use "apt-get install wireshark" to installed wireshark on them.</p><p>They all work under monitor mode, but only one of them (desktop) can capture RTP packets, the other two laptops can sniffer other packets, but except RTP packets..........</p><p>why...?</p></div><div id="question-tags" class="tags-container tags">rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Apr '15, 19:31</strong></p><img src="https://secure.gravatar.com/avatar/d10e76912ae0a0d745f3451d29395d86?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DiveDave&#39;s gravatar image" /><p>DiveDave<br />
<span class="score" title="21 reputation points">21</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DiveDave has one accepted answer">100%</span></p></div></div><div id="comments-container-41814" class="comments-container"><span id="41815"></span><div id="comment-41815" class="comment"><div id="post-41815-score" class="comment-score"></div><div class="comment-text"><blockquote><p>They all work under monitor mode ... the other two laptops can sniffer other packets</p></blockquote><p>By "other packets" do you mean "IP packets" (so that Wireshark shows them as IP, perhaps with TCP or UDP or...) or do you mean "802.11 packets" (which probably means they're encrypted with WEP or WPA/WPA2 and not being decrypted by Wireshark)?</p></div><div id="comment-41815-info" class="comment-info"><span class="comment-age">(24 Apr '15, 20:12)</span> Guy Harris ♦♦</div></div><span id="41817"></span><div id="comment-41817" class="comment"><div id="post-41817-score" class="comment-score"></div><div class="comment-text"><p>Thanks. I can see ip address parsed and protocol types parsed (it's a test wifi, so there is no password). I've already figured out the root course, see below:</p></div><div id="comment-41817-info" class="comment-info"><span class="comment-age">(24 Apr '15, 23:17)</span> DiveDave</div></div></div><div id="comment-tools-41814" class="comment-tools"></div><div class="clear"></div><div id="comment-41814-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41818"></span>

<div id="answer-container-41818" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41818-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Find the root course: the wifi channel results in this problem.</p><p>When the problem happened, my router wifi is using channel 6. I didn't noticed it. By accident I switch to another router, which uses channel 1. And I found that two laptop captured RTP packets, but the desktop stopped.</p><p>I tried all 11 channels, 1 &amp; 3 are compatible for two laptops, 2 &amp; 6 compatible for desktop. And I didn't find one channel works for all three computers. Finally I confirmed that all of them can connect to the wifi signal on either 1&amp;3 or 2&amp;6 to access internet.</p><p>So that means when doing sniffing, probably wireless network card cannot work on every channel, just part of all channels.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Apr '15, 23:26</strong></p><img src="https://secure.gravatar.com/avatar/d10e76912ae0a0d745f3451d29395d86?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DiveDave&#39;s gravatar image" /><p>DiveDave<br />
<span class="score" title="21 reputation points">21</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DiveDave has one accepted answer">100%</span></p></div></div><div id="comments-container-41818" class="comments-container"><span id="41819"></span><div id="comment-41819" class="comment"><div id="post-41819-score" class="comment-score">1</div><div class="comment-text"><p>Wi-Fi adapters are generally tuned to a particular channel; I'm not sure how good they are at picking up packets from adjacent channels (being good at that would, in general, probably <em>not</em> be considered a feature - you don't want interference from adjacent channels).</p><p>Your adapters on both the laptops and the desktop should be able to use any channel in the set of channels supported by the 802.11 mode the adapter is using (b, g, a, n, ac). They might currently be configured to use different channels.</p></div><div id="comment-41819-info" class="comment-info"><span class="comment-age">(24 Apr '15, 23:39)</span> Guy Harris ♦♦</div></div><span id="41820"></span><div id="comment-41820" class="comment"><div id="post-41820-score" class="comment-score"></div><div class="comment-text"><p>that makes sense. Is it possible to configure specific channel by manual under Ubuntu?</p></div><div id="comment-41820-info" class="comment-info"><span class="comment-age">(24 Apr '15, 23:41)</span> DiveDave</div></div><span id="41821"></span><div id="comment-41821" class="comment"><div id="post-41821-score" class="comment-score">1</div><div class="comment-text"><p>If the "View" menu has a "Wireless Toolbar" item, try selecting it; if that works, you'll have a toolbar that should, in theory, let you select the channel to capture on.</p></div><div id="comment-41821-info" class="comment-info"><span class="comment-age">(24 Apr '15, 23:44)</span> Guy Harris ♦♦</div></div><span id="41822"></span><div id="comment-41822" class="comment"><div id="post-41822-score" class="comment-score"></div><div class="comment-text"><p>Didn't find it..., but thank you very much, will notice this, maybe can find it someday :)</p><p>Happy weekend~</p></div><div id="comment-41822-info" class="comment-info"><span class="comment-age">(24 Apr '15, 23:48)</span> DiveDave</div></div></div><div id="comment-tools-41818" class="comment-tools"></div><div class="clear"></div><div id="comment-41818-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

