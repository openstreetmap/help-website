+++
type = "question"
title = "Loading more than 1GB PCAP file"
description = '''Hi I am not able to load more than 1 GB PCAP file in wireshark. Is there any solution to this? Please help. Thanks Hiremath'''
date = "2010-09-22T21:54:00Z"
lastmod = "2010-09-23T20:32:00Z"
weight = 283
keywords = [ "wireshark" ]
aliases = [ "/questions/283" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Loading more than 1GB PCAP file](/questions/283/loading-more-than-1gb-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-283-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-283-score" class="post-score" title="current number of votes">0</div><span id="post-283-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I am not able to load more than 1 GB PCAP file in wireshark. Is there any solution to this? Please help.</p><p>Thanks Hiremath</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '10, 21:54</strong></p><img src="https://secure.gravatar.com/avatar/25cfa02e74edcfc331858c638bce6b83?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hiremath&#39;s gravatar image" /><p><span>Hiremath</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hiremath has no accepted answers">0%</span></p></div></div><div id="comments-container-283" class="comments-container"></div><div id="comment-tools-283" class="comment-tools"></div><div class="clear"></div><div id="comment-283-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="284"></span>

<div id="answer-container-284" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-284-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-284-score" class="post-score" title="current number of votes">1</div><span id="post-284-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Use the command line tool <em>editcap</em> to slice it up.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '10, 22:49</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-284" class="comments-container"></div><div id="comment-tools-284" class="comment-tools"></div><div class="clear"></div><div id="comment-284-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="304"></span>

<div id="answer-container-304" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-304-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-304-score" class="post-score" title="current number of votes">0</div><span id="post-304-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Given the size of the capture, I guess that you don't want to study every packet details.</p><ul><li>If you want to study a specific flow inside this haystack, you can try to narrow down the size of the file to load by filtering out unneeded traffic with tcpdump or tshark (check -r and -w options, plus a "good" filter).</li><li>If you want to have statistics over the whole capture, you may try using tshark - the command line tool - instead of wireshark. It may require less memory as it does not have a graphical UI. Statistics are related to the -z option. For example <code>tshark -z rtp,streams -r sip-rtp-g711a.pcap -q</code> gives information about RTP streams without printing a summary line per packet.</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '10, 20:32</strong></p><img src="https://secure.gravatar.com/avatar/5583aa0f44e8c6dd129ad09c3d5d6732?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gteissier&#39;s gravatar image" /><p><span>gteissier</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gteissier has no accepted answers">0%</span></p></div></div><div id="comments-container-304" class="comments-container"></div><div id="comment-tools-304" class="comment-tools"></div><div class="clear"></div><div id="comment-304-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

