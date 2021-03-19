+++
type = "question"
title = "Wireshark cannot see any interface on Ubuntu 13.10"
description = '''Hello everyone, I&#x27;ve installed Wireshark 1.10.2 through GNS3 (latest release 0.8.6); when I use it outside GNS3, no interface is listed. What should be done?'''
date = "2014-03-06T02:09:00Z"
lastmod = "2014-03-06T02:12:00Z"
weight = 30473
keywords = [ "interface" ]
aliases = [ "/questions/30473" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark cannot see any interface on Ubuntu 13.10](/questions/30473/wireshark-cannot-see-any-interface-on-ubuntu-1310)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30473-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone,</p><p>I've installed Wireshark 1.10.2 through GNS3 (latest release 0.8.6); when I use it outside GNS3, no interface is listed.</p><p>What should be done?</p></div><div id="question-tags" class="tags-container tags">interface</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '14, 02:09</strong></p><img src="https://secure.gravatar.com/avatar/c86fb9accfde44bdbe661d8582c39b7b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="actionmystique&#39;s gravatar image" /><p>actionmystique<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="actionmystique has no accepted answers">0%</span></p></div></div><div id="comments-container-30473" class="comments-container"><span id="30497"></span><div id="comment-30497" class="comment"><div id="post-30497-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I've installed Wireshark 1.10.2 <strong>through GNS3</strong></p></blockquote><p>what does that mean: <strong>through</strong> GNS3</p></div><div id="comment-30497-info" class="comment-info"><span class="comment-age">(06 Mar '14, 13:15)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-30473" class="comment-tools"></div><div class="clear"></div><div id="comment-30473-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30474"></span>

<div id="answer-container-30474" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30474-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>See this <a href="http://wiki.wireshark.org/CaptureSetup/CapturePrivileges">Wiki Page</a>.</p><p>Usually for me it is running this command once:</p><pre><code>2. &quot;setcap &#39;CAP_NET_RAW+eip CAP_NET_ADMIN+eip&#39; /usr/bin/dumpcap&quot;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '14, 02:12</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-30474" class="comments-container"><span id="30475"></span><div id="comment-30475" class="comment"><div id="post-30475-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your prompt answer.</p><p>I've found <strong>all the following recommended steps</strong>:</p><p>sudo addgroup -system wireshark</p><p>sudo usermod -a -G wireshark YOUR_USER_NAME</p><p>sudo chown root:wireshark /usr/bin/dumpcap</p><p>sudo setcap cap_net_raw,cap_net_admin=eip /usr/bin/dumpcap</p><p>and reboot</p></div><div id="comment-30475-info" class="comment-info"><span class="comment-age">(06 Mar '14, 02:42)</span> actionmystique</div></div><span id="30476"></span><div id="comment-30476" class="comment"><div id="post-30476-score" class="comment-score"></div><div class="comment-text"><p>Yes, those steps are necessary when not installing from a package I think.</p></div><div id="comment-30476-info" class="comment-info"><span class="comment-age">(06 Mar '14, 03:07)</span> Jasper ♦♦</div></div></div><div id="comment-tools-30474" class="comment-tools"></div><div class="clear"></div><div id="comment-30474-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

