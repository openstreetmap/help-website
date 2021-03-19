+++
type = "question"
title = "Tshark command"
description = '''Hi, We run the Tshark command from command prompt for particular frame number, In this situation for large pcap files it will take more time to get the packet details.How to minimize the time for tshark. Ex: tshark.exe -2 -r 1.pcap -Y &quot;frame.number==13725&quot; -T pdml &amp;gt; 1.pdml Regards, Swathi.'''
date = "2016-06-14T07:08:00Z"
lastmod = "2016-06-15T00:46:00Z"
weight = 53436
keywords = [ "tshark" ]
aliases = [ "/questions/53436" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark command](/questions/53436/tshark-command)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53436-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53436-score" class="post-score" title="current number of votes">0</div><span id="post-53436-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>We run the Tshark command from command prompt for particular frame number, In this situation for large pcap files it will take more time to get the packet details.How to minimize the time for tshark.</p><p>Ex: tshark.exe -2 -r 1.pcap -Y "frame.number==13725" -T pdml &gt; 1.pdml</p><p>Regards, Swathi.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jun '16, 07:08</strong></p><img src="https://secure.gravatar.com/avatar/a34282ab2b31d84bc63d5ea83c15d775?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swathi%20jakkam&#39;s gravatar image" /><p><span>swathi jakkam</span><br />
<span class="score" title="6 reputation points">6</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swathi jakkam has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Jun '16, 10:41</strong> </span></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span></p></div></div><div id="comments-container-53436" class="comments-container"></div><div id="comment-tools-53436" class="comment-tools"></div><div class="clear"></div><div id="comment-53436-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53438"></span>

<div id="answer-container-53438" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53438-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53438-score" class="post-score" title="current number of votes">0</div><span id="post-53438-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at editcap</p><p><code>editcap.exe -r 1.pcap frame13725.pcap 13725</code></p><p>Then use tshark on this file</p><p><code>tshark.exe -2 -r 13725.pcap -T pdml &gt; 1.pdml</code></p><p>Warning: This also causes none of the context of the original capture being available when dissecting this single frame. Therefore results may differ.</p><p>Still editcap may be helpful, eg. if you are able to cut capture files in half or smaller.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '16, 07:27</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Jun '16, 10:42</strong> </span></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span></p></div></div><div id="comments-container-53438" class="comments-container"><span id="53454"></span><div id="comment-53454" class="comment"><div id="post-53454-score" class="comment-score"></div><div class="comment-text"><p>Thanks for reply.the above commands are working for normal pcap file. But I have another doubt, How to apply the ssl key file (-o ssl.keylog_file) to editcap.exe command.</p><p>Regards, Swathi.</p></div><div id="comment-53454-info" class="comment-info"><span class="comment-age">(15 Jun '16, 00:46)</span> <span class="comment-user userinfo">swathi jakkam</span></div></div></div><div id="comment-tools-53438" class="comment-tools"></div><div class="clear"></div><div id="comment-53438-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

