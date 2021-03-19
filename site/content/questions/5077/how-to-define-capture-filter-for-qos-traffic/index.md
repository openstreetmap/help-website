+++
type = "question"
title = "how to define capture filter for QoS traffic"
description = '''I would like to capture all traffic that are marked with DSCP value 184. I am able to do so using display filter &quot;ip.dsfield==184&quot; but how do i use the equivalent filter on capture filter ?'''
date = "2011-07-16T23:11:00Z"
lastmod = "2011-07-19T07:06:00Z"
weight = 5077
keywords = [ "qos" ]
aliases = [ "/questions/5077" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to define capture filter for QoS traffic](/questions/5077/how-to-define-capture-filter-for-qos-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5077-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5077-score" class="post-score" title="current number of votes">0</div><span id="post-5077-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to capture all traffic that are marked with DSCP value 184. I am able to do so using display filter "ip.dsfield==184" but how do i use the equivalent filter on capture filter ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-qos" rel="tag" title="see questions tagged &#39;qos&#39;">qos</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jul '11, 23:11</strong></p><img src="https://secure.gravatar.com/avatar/709a254e7fc9548a5d63585b70c04333?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chenhsien&#39;s gravatar image" /><p><span>chenhsien</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chenhsien has no accepted answers">0%</span></p></div></div><div id="comments-container-5077" class="comments-container"></div><div id="comment-tools-5077" class="comment-tools"></div><div class="clear"></div><div id="comment-5077-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5078"></span>

<div id="answer-container-5078" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5078-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5078-score" class="post-score" title="current number of votes">1</div><span id="post-5078-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The capture filter equivalent of "ip.dsfield==184" would be "ip[1]=184".</p><p>However when the dsfield value is 184, the dscp value is actually 46, as the dscp field consists of the higher 6 bits of the dsfield, the other two bits are for Explicit Congestion Notification.</p><p>Your filter "ip.dsfield==184" will only show packets woth DSCP value 46 and both ECN bith zero. So you might miss packets that have a ECN bit set. It's better to use the display filter "ip.dsfield.dscp==46", for which the capture filter equivalent is "ip[1]&gt;&gt;2=46"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '11, 01:17</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5078" class="comments-container"><span id="5110"></span><div id="comment-5110" class="comment"><div id="post-5110-score" class="comment-score"></div><div class="comment-text"><p>thank you, it works !</p></div><div id="comment-5110-info" class="comment-info"><span class="comment-age">(18 Jul '11, 23:27)</span> <span class="comment-user userinfo">chenhsien</span></div></div><span id="5119"></span><div id="comment-5119" class="comment"><div id="post-5119-score" class="comment-score"></div><div class="comment-text"><p>Good to hear that it works.</p><p>(I changed your "answer" to a "comment", see the FAQ for more info. Also, questions stay on the "unanswered" list until they have been accepted, which is where the "checkmark" button on the left is for)</p></div><div id="comment-5119-info" class="comment-info"><span class="comment-age">(19 Jul '11, 06:16)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="5123"></span><div id="comment-5123" class="comment"><div id="post-5123-score" class="comment-score"></div><div class="comment-text"><p>(I changed your "answer" to a "comment", see the FAQ for more info) ;)</p></div><div id="comment-5123-info" class="comment-info"><span class="comment-age">(19 Jul '11, 07:06)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-5078" class="comment-tools"></div><div class="clear"></div><div id="comment-5078-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

