+++
type = "question"
title = "How do I get the interface name for use with the -i flag in Windows"
description = '''How do I know the name of the interface for the -i flag in windows? I tried the reported name (Intel(r) 82579LM Gigabit Network Connection) both with and without quotes around it.. as well as the interface listed when you go to Capture Interfaces -&amp;gt; Details.. which shows &#92;Devices&#92;NPF_{362508C4-F6...'''
date = "2012-06-20T08:49:00Z"
lastmod = "2012-06-20T15:11:00Z"
weight = 12075
keywords = [ "windows", "interface", "wireshark" ]
aliases = [ "/questions/12075" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I get the interface name for use with the -i flag in Windows](/questions/12075/how-do-i-get-the-interface-name-for-use-with-the-i-flag-in-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12075-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12075-score" class="post-score" title="current number of votes">0</div><span id="post-12075-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do I know the name of the interface for the -i flag in windows? I tried the reported name (Intel(r) 82579LM Gigabit Network Connection) both with and without quotes around it.. as well as the interface listed when you go to Capture Interfaces -&gt; Details.. which shows</p><p>\Devices\NPF_{362508C4-F6CC-4A4A-AB17-9DA1017E4C41} (I tried using just the NPF and the rest to the right with the -i flag)</p><p>Any help would be great as I'm writing this into a script...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jun '12, 08:49</strong></p><img src="https://secure.gravatar.com/avatar/6bc9aaaa40b8df3688818c6710a877ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rjr162&#39;s gravatar image" /><p><span>rjr162</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rjr162 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>20 Jun '12, 13:20</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-12075" class="comments-container"><span id="12076"></span><div id="comment-12076" class="comment"><div id="post-12076-score" class="comment-score"></div><div class="comment-text"><p>Never mind.. I guess adding the \Devices\ part was the answer!</p></div><div id="comment-12076-info" class="comment-info"><span class="comment-age">(20 Jun '12, 08:50)</span> <span class="comment-user userinfo">rjr162</span></div></div><span id="12084"></span><div id="comment-12084" class="comment"><div id="post-12084-score" class="comment-score"></div><div class="comment-text"><p>Note that the "reported name" is, I think, the vendor-supplied description, and that might, on a (probably server) machine with multiple adapters of the same type, not be unique.</p><p>Supporting using the description as a "-i" argument might not be a bad idea - it'd presumably fail if there's more than one interface with the same description. You might want to file an enhancement request on <a href="http://bugs.wireshark.org/">the Wireshark bugzilla</a> for that. (Supporting the "friendly name" might also be nice; that'd require extending pcap to support that or having *shark do it directly.)</p></div><div id="comment-12084-info" class="comment-info"><span class="comment-age">(20 Jun '12, 15:11)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-12075" class="comment-tools"></div><div class="clear"></div><div id="comment-12075-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12083"></span>

<div id="answer-container-12083" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12083-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12083-score" class="post-score" title="current number of votes">2</div><span id="post-12083-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark (and tshark and dumpcap and windump) all take a -D flag which will display the interface names which can be captured on, and the index of the interfaces. The -i flag will use the index or the name which can be easier for scripting.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jun '12, 13:30</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-12083" class="comments-container"></div><div id="comment-tools-12083" class="comment-tools"></div><div class="clear"></div><div id="comment-12083-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

