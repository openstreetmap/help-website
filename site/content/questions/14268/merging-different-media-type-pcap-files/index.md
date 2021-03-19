+++
type = "question"
title = "Merging Different media type PCAP files"
description = '''Can I merge or concatanate a wireless PCAP capture file with a wired PCAP capture file?'''
date = "2012-09-14T09:15:00Z"
lastmod = "2012-09-14T12:53:00Z"
weight = 14268
keywords = [ "merge" ]
aliases = [ "/questions/14268" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Merging Different media type PCAP files](/questions/14268/merging-different-media-type-pcap-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14268-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can I merge or concatanate a wireless PCAP capture file with a wired PCAP capture file?</p></div><div id="question-tags" class="tags-container tags">merge</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '12, 09:15</strong></p><img src="https://secure.gravatar.com/avatar/4f278359f7489e4a5c75ac40c52a1bff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MSshark&#39;s gravatar image" /><p>MSshark<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MSshark has no accepted answers">0%</span></p></div></div><div id="comments-container-14268" class="comments-container"></div><div id="comment-tools-14268" class="comment-tools"></div><div class="clear"></div><div id="comment-14268-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14272"></span>

<div id="answer-container-14272" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14272-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>No that's not possible as mergecap will print this error message:</p><blockquote><p><code>mergecap -w out.cap http.cap wlan.pcap</code><br />
<code>mergecap: Can't open or create out.cap: Files from that network type can't be saved in that format</code><br />
</p></blockquote><p>You can force a new encapsulation type with <code>-T</code> (e.g. ether), but then Wireshark cannot dissect the included wireless frames.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '12, 12:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-14272" class="comments-container"><span id="14279"></span><div id="comment-14279" class="comment"><div id="post-14279-score" class="comment-score"></div><div class="comment-text"><p>...and if you try to use <code>-F</code> to force the output file to be a pcap-ng file, the resulting file won't be readable, due to bugs.</p></div><div id="comment-14279-info" class="comment-info"><span class="comment-age">(14 Sep '12, 14:37)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-14272" class="comment-tools"></div><div class="clear"></div><div id="comment-14272-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

