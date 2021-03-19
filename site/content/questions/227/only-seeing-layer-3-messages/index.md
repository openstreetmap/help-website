+++
type = "question"
title = "Only seeing Layer 3 messages"
description = '''I purchased a new laptop running windows 7 and installed Wireshark 64 bit version 1.4.0 Everything worked correctly for 3-4 days and now I only see Layer 3 messages. I have made sure there are no filters, all protocols are selected. I have uninstalled and reinstalled and even went to the 32 bit ap. ...'''
date = "2010-09-20T07:25:00Z"
lastmod = "2010-09-20T10:48:00Z"
weight = 227
keywords = [ "layer3" ]
aliases = [ "/questions/227" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Only seeing Layer 3 messages](/questions/227/only-seeing-layer-3-messages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-227-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-227-score" class="post-score" title="current number of votes">0</div><span id="post-227-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I purchased a new laptop running windows 7 and installed Wireshark 64 bit version 1.4.0 Everything worked correctly for 3-4 days and now I only see Layer 3 messages. I have made sure there are no filters, all protocols are selected. I have uninstalled and reinstalled and even went to the 32 bit ap. I removed Win PCAP and reinstalled it also. I am at a loss as to what to try next. I can use my old laptop and see all the data but I can not get the new laptop to show everything. Any ideas that I can try?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-layer3" rel="tag" title="see questions tagged &#39;layer3&#39;">layer3</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Sep '10, 07:25</strong></p><img src="https://secure.gravatar.com/avatar/8e55c7a31d03f2998b60c4335266a0fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="8300&#39;s gravatar image" /><p><span>8300</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="8300 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Sep '10, 01:54</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-227" class="comments-container"></div><div id="comment-tools-227" class="comment-tools"></div><div class="clear"></div><div id="comment-227-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="228"></span>

<div id="answer-container-228" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-228-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-228-score" class="post-score" title="current number of votes">0</div><span id="post-228-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It sounds like your NIC might not be going into promiscuous mode. Are you sure that a) you're running with sufficient privileges to do that (typically administrator), and b) that the "promiscuous mode" box is checked in the capture options?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '10, 08:03</strong></p><img src="https://secure.gravatar.com/avatar/8d955195202bfccc131e41c435bc382a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jswan&#39;s gravatar image" /><p><span>jswan</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jswan has no accepted answers">0%</span></p></div></div><div id="comments-container-228" class="comments-container"></div><div id="comment-tools-228" class="comment-tools"></div><div class="clear"></div><div id="comment-228-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="231"></span>

<div id="answer-container-231" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-231-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-231-score" class="post-score" title="current number of votes">0</div><span id="post-231-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>By "only see layer 3 messages" do you mean that you see the TCP connection setup (SYN + SYN/ACK + ACK) but not the actual data? If so this could be due to <a href="http://wiki.wireshark.org/CaptureSetup/Offloading#TCP_Chimney">chimney offloading</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '10, 10:48</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-231" class="comments-container"></div><div id="comment-tools-231" class="comment-tools"></div><div class="clear"></div><div id="comment-231-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

