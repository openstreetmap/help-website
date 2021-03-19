+++
type = "question"
title = "Wireshark is not detecting my Wireless interface..."
description = '''I&#x27;m using a proprietary wireless interface I installed its drivers but Wireshark is not detecting it I&#x27;m using UBUNTU'''
date = "2014-02-09T07:54:00Z"
lastmod = "2014-12-17T17:54:00Z"
weight = 29574
keywords = [ "wireless", "interface", "ubuntu" ]
aliases = [ "/questions/29574" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark is not detecting my Wireless interface...](/questions/29574/wireshark-is-not-detecting-my-wireless-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29574-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29574-score" class="post-score" title="current number of votes">0</div><span id="post-29574-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using a proprietary wireless interface I installed its drivers but Wireshark is not detecting it I'm using UBUNTU</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireless" rel="tag" title="see questions tagged &#39;wireless&#39;">wireless</span> <span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '14, 07:54</strong></p><img src="https://secure.gravatar.com/avatar/739c2d0d12ca542437bc5b06d8c27510?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mcool4151&#39;s gravatar image" /><p><span>mcool4151</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mcool4151 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Feb '14, 07:56</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-29574" class="comments-container"><span id="29575"></span><div id="comment-29575" class="comment"><div id="post-29575-score" class="comment-score"></div><div class="comment-text"><p>What version of Wireshark, what version of Ubuntu and most importantly what is your wireless card and what drivers are being loaded for it?</p></div><div id="comment-29575-info" class="comment-info"><span class="comment-age">(09 Feb '14, 07:57)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="29586"></span><div id="comment-29586" class="comment"><div id="post-29586-score" class="comment-score"></div><div class="comment-text"><p>What is the output of the following commands</p><blockquote><p>ifconfig -a<br />
dumpcap -D -M</p></blockquote></div><div id="comment-29586-info" class="comment-info"><span class="comment-age">(09 Feb '14, 12:35)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-29574" class="comment-tools"></div><div class="clear"></div><div id="comment-29574-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29600"></span>

<div id="answer-container-29600" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29600-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29600-score" class="post-score" title="current number of votes">1</div><span id="post-29600-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>when you install the wireshark on UBUNTU be sure</p><ol><li><code>sudo groupadd wireshark</code></li><li><code>sudo usermod -a -G wireshark $USER</code></li><li><code>sudo chgrp wirshark /usr/bin/dumpcap</code></li><li><code>sudo setcap cap_net_raw,cap_net_admin=eip /usr/bin/dumpcap</code></li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '14, 01:31</strong></p><img src="https://secure.gravatar.com/avatar/7a7c81f94a4020ece8ee84d0f66c3367?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adamali&#39;s gravatar image" /><p><span>adamali</span><br />
<span class="score" title="25 reputation points">25</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adamali has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Feb '14, 04:19</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-29600" class="comments-container"><span id="29604"></span><div id="comment-29604" class="comment"><div id="post-29604-score" class="comment-score"></div><div class="comment-text"><blockquote><p>You need to install a winpcap driver (software ) for your UBUNTU.(linux)</p></blockquote><p>There is no <strong>Win</strong>Pcap for Linux!!</p></div><div id="comment-29604-info" class="comment-info"><span class="comment-age">(10 Feb '14, 02:23)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="29610"></span><div id="comment-29610" class="comment"><div id="post-29610-score" class="comment-score"></div><div class="comment-text"><p>Nor AirPCap, that's Windows only as well.</p></div><div id="comment-29610-info" class="comment-info"><span class="comment-age">(10 Feb '14, 03:12)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="29613"></span><div id="comment-29613" class="comment"><div id="post-29613-score" class="comment-score"></div><div class="comment-text"><p>sudo groupadd wireshark<br />
<strong><em>* sudo usermod -a -G wireshark $USER</em></strong>* sudo chgrp wirshark /usr/bin/dumpcap<strong>*</strong> sudo setcap cap_net_raw,cap_net_admin=eip /usr/bin/dumpcap</p></div><div id="comment-29613-info" class="comment-info"><span class="comment-age">(10 Feb '14, 03:58)</span> <span class="comment-user userinfo">adamali</span></div></div><span id="29617"></span><div id="comment-29617" class="comment"><div id="post-29617-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@adamali</span></p><p>If you change your answer, then you make all the subsequent comments look odd, instead <strong>edit</strong> your answer to add the new info.</p><p>In addition the user will have to log off and log on again after adding their account to the group.</p></div><div id="comment-29617-info" class="comment-info"><span class="comment-age">(10 Feb '14, 04:18)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="38615"></span><div id="comment-38615" class="comment"><div id="post-38615-score" class="comment-score"></div><div class="comment-text"><p>This worked for me Ubuntu 14.04</p></div><div id="comment-38615-info" class="comment-info"><span class="comment-age">(17 Dec '14, 17:54)</span> <span class="comment-user userinfo">mechsin</span></div></div></div><div id="comment-tools-29600" class="comment-tools"></div><div class="clear"></div><div id="comment-29600-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

