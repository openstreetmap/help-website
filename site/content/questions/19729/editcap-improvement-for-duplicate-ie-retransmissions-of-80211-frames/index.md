+++
type = "question"
title = "editcap improvement for &quot;duplicate&quot; i.e retransmissions of 802.11 frames"
description = '''A WLAN capture executed in monitor mode shows lots of wireless retransmissions occuring. Editcap is not able to remove the duplicates since the packets are not actually duplicates, the radiotap header changes for each packet. Could it be possible to improve editcap to specify from which header the d...'''
date = "2013-03-21T12:24:00Z"
lastmod = "2013-03-22T06:39:00Z"
weight = 19729
keywords = [ "duplicate", "802.11", "retransmissions" ]
aliases = [ "/questions/19729" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [editcap improvement for "duplicate" i.e retransmissions of 802.11 frames](/questions/19729/editcap-improvement-for-duplicate-ie-retransmissions-of-80211-frames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19729-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19729-score" class="post-score" title="current number of votes">0</div><span id="post-19729-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>A WLAN capture executed in monitor mode shows lots of wireless retransmissions occuring. Editcap is not able to remove the duplicates since the packets are not actually duplicates, the radiotap header changes for each packet. Could it be possible to improve editcap to specify from which header the duplicate analysis should be done? E.g. look for duplicates while ignoring header X,Y,Z (in decapsulation order). I filed bug 8511 but would like to have some input from the community.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-duplicate" rel="tag" title="see questions tagged &#39;duplicate&#39;">duplicate</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span> <span class="post-tag tag-link-retransmissions" rel="tag" title="see questions tagged &#39;retransmissions&#39;">retransmissions</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '13, 12:24</strong></p><img src="https://secure.gravatar.com/avatar/e177d49ca6cc8f53ee58cb3de1c4fbaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yul_analyzer&#39;s gravatar image" /><p><span>yul_analyzer</span><br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yul_analyzer has no accepted answers">0%</span></p></div></div><div id="comments-container-19729" class="comments-container"></div><div id="comment-tools-19729" class="comment-tools"></div><div class="clear"></div><div id="comment-19729-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19732"></span>

<div id="answer-container-19732" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19732-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19732-score" class="post-score" title="current number of votes">0</div><span id="post-19732-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, that would be possible, but the code needs to be written by someone taking an interest in this functionality.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '13, 13:07</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-19732" class="comments-container"><span id="19749"></span><div id="comment-19749" class="comment"><div id="post-19749-score" class="comment-score"></div><div class="comment-text"><p>Regarding the specific issue of ignoring/removing wireless retransmissions, the tshark "-y RAW" option will not capture the radiotap header hence creating real duplicates for retransmissions that can be easily removed with editcap afterwards.</p></div><div id="comment-19749-info" class="comment-info"><span class="comment-age">(22 Mar '13, 06:39)</span> <span class="comment-user userinfo">yul_analyzer</span></div></div></div><div id="comment-tools-19732" class="comment-tools"></div><div class="clear"></div><div id="comment-19732-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

