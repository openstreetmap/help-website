+++
type = "question"
title = "editcap doesn&#x27;t seem to work in the new version I installed 1.8.7"
description = '''Hi, I am using the following command to convert from the pcap I&#x27;ve got to MTP2 (E1). It worked fine in previous versions but in 1.8.7 it simply doesn&#x27;t encapsulate it;  editcap.exe -T mtp2 &quot;file.pcap&quot; &quot;file_converted.pcap&quot;  Thank you, Diana'''
date = "2013-05-29T06:43:00Z"
lastmod = "2013-05-29T23:31:00Z"
weight = 21560
keywords = [ "editcap" ]
aliases = [ "/questions/21560" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [editcap doesn't seem to work in the new version I installed 1.8.7](/questions/21560/editcap-doesnt-seem-to-work-in-the-new-version-i-installed-187)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21560-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21560-score" class="post-score" title="current number of votes">0</div><span id="post-21560-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am using the following command to convert from the pcap I've got to MTP2 (E1). It worked fine in previous versions but in 1.8.7 it simply doesn't encapsulate it;</p><blockquote><p>editcap.exe -T mtp2 "file.pcap" "file_converted.pcap"</p></blockquote><p>Thank you, Diana</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-editcap" rel="tag" title="see questions tagged &#39;editcap&#39;">editcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 May '13, 06:43</strong></p><img src="https://secure.gravatar.com/avatar/900044aef60dc6223168781e5d576bfb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dianalab9&#39;s gravatar image" /><p><span>Dianalab9</span><br />
<span class="score" title="26 reputation points">26</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dianalab9 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 May '13, 22:08</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-21560" class="comments-container"><span id="21582"></span><div id="comment-21582" class="comment"><div id="post-21582-score" class="comment-score"></div><div class="comment-text"><p>"Convert" in what sense? Editcap won't transform the contents of packets; all that the -T flag does is let you fix a capture file that has the wrong encapsulation type to have a different encapsulation type, it doesn't actually change the packet headers from the old type to the new type (and never did).</p></div><div id="comment-21582-info" class="comment-info"><span class="comment-age">(29 May '13, 12:20)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-21560" class="comment-tools"></div><div class="clear"></div><div id="comment-21560-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21580"></span>

<div id="answer-container-21580" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21580-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21580-score" class="post-score" title="current number of votes">3</div><span id="post-21580-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The following might work for you:</p><pre><code>editcap.exe -T mtp2 -F libpcap &quot;file.pcap&quot; &quot;file_converted.pcap&quot;</code></pre><p>See also <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=2868">bug2868</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 May '13, 11:07</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-21580" class="comments-container"><span id="21588"></span><div id="comment-21588" class="comment"><div id="post-21588-score" class="comment-score"></div><div class="comment-text"><p>It works! thank you very much</p></div><div id="comment-21588-info" class="comment-info"><span class="comment-age">(29 May '13, 23:31)</span> <span class="comment-user userinfo">Dianalab9</span></div></div></div><div id="comment-tools-21580" class="comment-tools"></div><div class="clear"></div><div id="comment-21580-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

