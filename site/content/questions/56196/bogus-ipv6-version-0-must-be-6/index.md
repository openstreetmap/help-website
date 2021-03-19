+++
type = "question"
title = "Bogus IPV6 version (0, must be 6)"
description = '''Hi there, I&#x27;m using Wireshark 2.1 for MAC, and I have a problem to decode traces taken in our core network. Every single packet shows the error &quot;Bogus IPV6 version (0, must be 6)&quot;, as you can see in the image attached. It works for my colleagues who are using downgraded versions of Wireshark (v 1.XX...'''
date = "2016-10-06T08:27:00Z"
lastmod = "2016-10-06T08:27:00Z"
weight = 56196
keywords = [ "mac" ]
aliases = [ "/questions/56196" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Bogus IPV6 version (0, must be 6)](/questions/56196/bogus-ipv6-version-0-must-be-6)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56196-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2016-10-06_at_8.19.43_AM.png" alt="alt text" />Hi there,</p><p>I'm using Wireshark 2.1 for MAC, and I have a problem to decode traces taken in our core network. Every single packet shows the error "Bogus IPV6 version (0, must be 6)", as you can see in the image attached.</p><p>It works for my colleagues who are using downgraded versions of Wireshark (v 1.XX).</p><p>Is there any way to tweak a preference and make it work in any version?</p></div><div id="question-tags" class="tags-container tags">mac</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Oct '16, 08:27</strong></p><img src="https://secure.gravatar.com/avatar/77d15d44eb10ef3280620a5f09552b94?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="artrilla&#39;s gravatar image" /><p>artrilla<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="artrilla has no accepted answers">0%</span></p></img></div></div><div id="comments-container-56196" class="comments-container"><span id="56198"></span><div id="comment-56198" class="comment"><div id="post-56198-score" class="comment-score"></div><div class="comment-text"><p>The current stable version is 2.2.1, can you try that version?</p></div><div id="comment-56198-info" class="comment-info"><span class="comment-age">(06 Oct '16, 08:29)</span> grahamb ♦</div></div><span id="56200"></span><div id="comment-56200" class="comment"><div id="post-56200-score" class="comment-score"></div><div class="comment-text"><p>More interesting would be - is the IP version really 0? If you expand the IPv6 layer, what does the value for "Version" say?</p></div><div id="comment-56200-info" class="comment-info"><span class="comment-age">(06 Oct '16, 09:11)</span> Jasper ♦♦</div></div><span id="56217"></span><div id="comment-56217" class="comment"><div id="post-56217-score" class="comment-score"></div><div class="comment-text"><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>?</p></div><div id="comment-56217-info" class="comment-info"><span class="comment-age">(07 Oct '16, 04:19)</span> Jaap ♦</div></div><span id="56225"></span><div id="comment-56225" class="comment"><div id="post-56225-score" class="comment-score"></div><div class="comment-text"><p>HI There,</p><p>Same problem is shown in version 2.2.1</p><p>If I expand the IP layer, the version shown is 0 (I know, this is incorrect, but previous versions of Wireshark are ignoring this problem)</p><p>I just installed v 1.99.8 and the traces are shown without issues.</p><p>So the problem is that v2.XX is picky with the validation of values in certain fields.</p></div><div id="comment-56225-info" class="comment-info"><span class="comment-age">(07 Oct '16, 11:54)</span> artrilla</div></div><span id="56226"></span><div id="comment-56226" class="comment"><div id="post-56226-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-56226-info" class="comment-info"><span class="comment-age">(07 Oct '16, 12:40)</span> Jaap ♦</div></div><span id="56229"></span><div id="comment-56229" class="comment not_top_scorer"><div id="post-56229-score" class="comment-score"></div><div class="comment-text"><p>No, the problem is that whatever's capturing your packets is mangling them.</p><p>What tool was used to capture that traffic?</p></div><div id="comment-56229-info" class="comment-info"><span class="comment-age">(07 Oct '16, 13:59)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-56196" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-56196-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

