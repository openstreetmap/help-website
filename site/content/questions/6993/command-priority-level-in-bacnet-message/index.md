+++
type = "question"
title = "Command priority  level in BACNET message"
description = '''Hi anyone please let me know how to check the priority level in Wireshark? I need to check the priority level send by two devices, please suggest me the filter and let me know where I can find the priority level in the message?'''
date = "2011-10-19T14:01:00Z"
lastmod = "2011-10-19T14:34:00Z"
weight = 6993
keywords = [ "bacnet" ]
aliases = [ "/questions/6993" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Command priority level in BACNET message](/questions/6993/command-priority-level-in-bacnet-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6993-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6993-score" class="post-score" title="current number of votes">0</div><span id="post-6993-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi anyone please let me know how to check the priority level in Wireshark?</p><p>I need to check the priority level send by two devices, please suggest me the filter and let me know where I can find the priority level in the message?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bacnet" rel="tag" title="see questions tagged &#39;bacnet&#39;">bacnet</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '11, 14:01</strong></p><img src="https://secure.gravatar.com/avatar/cc1c2ad2470fe701738f5fd1129f7c79?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ravi%20S&#39;s gravatar image" /><p><span>Ravi S</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ravi S has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Oct '11, 07:30</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-6993" class="comments-container"></div><div id="comment-tools-6993" class="comment-tools"></div><div class="clear"></div><div id="comment-6993-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6995"></span>

<div id="answer-container-6995" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6995-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6995-score" class="post-score" title="current number of votes">0</div><span id="post-6995-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I know nothing about the BACnet protocol. :)</p><p>However, I think if you use Wireshark to open a file containing BACnet frames and look at the dissection of the BACnet frames you should see what you seek. ;)</p><p>(Use bacnet as a filter to find the BACnet frames in a capture_).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '11, 14:21</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-6995" class="comments-container"><span id="6996"></span><div id="comment-6996" class="comment"><div id="post-6996-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the info.</p><p>I have did it. But the finding priority level is very difficult. If we know the exact filter and how I can identify and where I can identify, that will help me alot</p></div><div id="comment-6996-info" class="comment-info"><span class="comment-age">(19 Oct '11, 14:24)</span> <span class="comment-user userinfo">Ravi S</span></div></div><span id="6997"></span><div id="comment-6997" class="comment"><div id="post-6997-score" class="comment-score"></div><div class="comment-text"><p>As I said, I know nothing about the protocol.</p><p>However, I do note that there are some bits in the Control byte of the NPDU level of the BACnet frame that might be what you want.</p><p>So: I suggest you look again at a BACnet dissection. :)</p><p>If that's not what you want, then I'll not be able to help.</p><p>P.S.:</p><p>If you click on any particular field (line) in the details (middle) pane of the Wireshark diosplay, you will see the filter (if any) for that field in the bottom status display line in the window in the form bacnet.xxxx.</p></div><div id="comment-6997-info" class="comment-info"><span class="comment-age">(19 Oct '11, 14:34)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-6995" class="comment-tools"></div><div class="clear"></div><div id="comment-6995-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

