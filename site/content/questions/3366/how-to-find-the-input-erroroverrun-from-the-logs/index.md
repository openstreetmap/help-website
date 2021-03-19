+++
type = "question"
title = "How to Find the input error(overrun) from the logs"
description = '''Hi I have a large file of the logs captured from an Gig interface. The other side we have a CISCO 7206VXR router where we see the overrun counter increasing. How do I identify which packets causing the overrun problem? Could you please Help me? Regards Siva'''
date = "2011-04-06T00:42:00Z"
lastmod = "2011-04-06T07:07:00Z"
weight = 3366
keywords = [ "overrun" ]
aliases = [ "/questions/3366" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to Find the input error(overrun) from the logs](/questions/3366/how-to-find-the-input-erroroverrun-from-the-logs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3366-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3366-score" class="post-score" title="current number of votes">0</div><span id="post-3366-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I have a large file of the logs captured from an Gig interface. The other side we have a CISCO 7206VXR router where we see the overrun counter increasing.</p><p>How do I identify which packets causing the overrun problem?</p><p>Could you please Help me?</p><p>Regards Siva</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-overrun" rel="tag" title="see questions tagged &#39;overrun&#39;">overrun</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '11, 00:42</strong></p><img src="https://secure.gravatar.com/avatar/a0baddd05cdd181d97edbeedc7334c15?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Siva&#39;s gravatar image" /><p><span>Siva</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Siva has no accepted answers">0%</span></p></div></div><div id="comments-container-3366" class="comments-container"></div><div id="comment-tools-3366" class="comment-tools"></div><div class="clear"></div><div id="comment-3366-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3367"></span>

<div id="answer-container-3367" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3367-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3367-score" class="post-score" title="current number of votes">0</div><span id="post-3367-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Just a couple of ideas:</p><p>You might want to identify when and where packets are lost, which you could do by using the I/O Graph (to be found in the statistics menu) and adding a graph showing all retransmissions by entering the <code>tcp.analysis.retransmission</code> filter to one of the empty graph lines below the trace (I usually use Graph2 because it is red, and set it to "FBar" style). Keep in mind to scale the Y-axis to logarithmic since you might not see any retransmission at first because the number of packets/bytes is far greater than the lost packets/bytes. You might see times when lots of packets are lost and go from there to find out what is happening in that time frame.</p><p>You could use the conversation statistics to see which communications put the most packets/bytes on the line by sorting the list by packets or bytes. Then you should check if those communications have suspicious amounts of lost packets and retransmissions caused by the overload - for example by filtering for the conversations through the popup menu in the statistics and later adding "<code>and tcp.analysis.retransmission</code>" to the conversation filter.</p><p>You could also go the other way arround: filter for <code>tcp.analysis.retransmission</code> and then use the conversation statistics with the "Limit to display filter" option at the bottom to get statistics of the conversations with retransmission. Sort them by number of packets and you know which one lost the most packets. Those connections often caused the problem themselves by putting lots of traffic on the line.</p><p>That will help finding the cause if it is just a couple of connections creating the overrun by massive transfers of data. If the overload is caused just by the sheer number of connections with just a little traffic you might have more work ahead of you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Apr '11, 01:00</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-3367" class="comments-container"></div><div id="comment-tools-3367" class="comment-tools"></div><div class="clear"></div><div id="comment-3367-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3370"></span>

<div id="answer-container-3370" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3370-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3370-score" class="post-score" title="current number of votes">0</div><span id="post-3370-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Jasper</p><p>I did the above and found less number of packets. The difference between the output error before and after the data capture was about 420+. The Wireshark shows only 144 flows.</p><p>Wondering because this does not match with the counter on the interface.</p><p>Any other thoughts</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Apr '11, 05:01</strong></p><img src="https://secure.gravatar.com/avatar/a0baddd05cdd181d97edbeedc7334c15?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Siva&#39;s gravatar image" /><p><span>Siva</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Siva has no accepted answers">0%</span></p></div></div><div id="comments-container-3370" class="comments-container"><span id="3371"></span><div id="comment-3371" class="comment"><div id="post-3371-score" class="comment-score"></div><div class="comment-text"><p>Where did you capture, and how? I was under the impression that you capture on the link that is going with high speed into the router that is then dropping packets.</p><p>If your gigabit link is really busy you might not be able to capture packets without sacrifice unless you have really powerful capture hardware; Most notebooks for example drop up to 80% of all packets on a crowded gigabit link.</p></div><div id="comment-3371-info" class="comment-info"><span class="comment-age">(06 Apr '11, 05:19)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="3372"></span><div id="comment-3372" class="comment"><div id="post-3372-score" class="comment-score"></div><div class="comment-text"><p>This was captured on the Gig interface of the Switch. Most likely the customer might have enabled port span and captured it</p><p>Regards</p></div><div id="comment-3372-info" class="comment-info"><span class="comment-age">(06 Apr '11, 06:13)</span> <span class="comment-user userinfo">Siva</span></div></div><span id="3374"></span><div id="comment-3374" class="comment"><div id="post-3374-score" class="comment-score"></div><div class="comment-text"><p>Depending on the ammount of traffic on the gig link and the way the customer captured it you might not be able to troubleshoot unless you know exactly what was done and how. Most unexperienced users that capture without really knowing what to look for do not even notice they are dropping packets right left and center...</p></div><div id="comment-3374-info" class="comment-info"><span class="comment-age">(06 Apr '11, 07:07)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-3370" class="comment-tools"></div><div class="clear"></div><div id="comment-3370-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

