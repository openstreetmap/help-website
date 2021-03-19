+++
type = "question"
title = "cisco span"
description = '''When sniffing on a cisco span, it looks like the Rx and TX traffic are buffered. If I look at one tcp session I get a range off Tx packets and after that a whole rage of Rx tcp ack packages. (more then 20 in a row). Is this normal span behavoir?'''
date = "2015-10-07T04:57:00Z"
lastmod = "2015-10-07T11:59:00Z"
weight = 46388
keywords = [ "span", "cisco" ]
aliases = [ "/questions/46388" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [cisco span](/questions/46388/cisco-span)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46388-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46388-score" class="post-score" title="current number of votes">0</div><span id="post-46388-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>When sniffing on a cisco span, it looks like the Rx and TX traffic are buffered. If I look at one tcp session I get a range off Tx packets and after that a whole rage of Rx tcp ack packages. (more then 20 in a row). Is this normal span behavoir?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-span" rel="tag" title="see questions tagged &#39;span&#39;">span</span> <span class="post-tag tag-link-cisco" rel="tag" title="see questions tagged &#39;cisco&#39;">cisco</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Oct '15, 04:57</strong></p><img src="https://secure.gravatar.com/avatar/640f31c3684eea11e2848f86425d506f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stobbe99&#39;s gravatar image" /><p><span>stobbe99</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stobbe99 has no accepted answers">0%</span></p></div></div><div id="comments-container-46388" class="comments-container"></div><div id="comment-tools-46388" class="comment-tools"></div><div class="clear"></div><div id="comment-46388-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46409"></span>

<div id="answer-container-46409" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46409-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46409-score" class="post-score" title="current number of votes">3</div><span id="post-46409-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think your question is: "By creating a SPAN port, does traffic to the SPAN port become affect?"</p><p>The answer is: YES! Even Cisco in their own white paper states:</p><p>"Cisco warns that the switch treats SPAN data with a lower priority than regular port-to-port data. In other words, if any resource under load must choose between passing normal traffic and SPAN data, the SPAN loses and the mirrored frames are arbitrarily discarded. This rule applies to preserving network traffic in any situation. For instance, when transporting remote SPAN traffic through an Inter Switch Link (ISL), which shares the ISL bandwidth with regular network traffic, the network traffic takes priority. If there is not enough capacity for the remote SPAN traffic, the switch drops it."</p><p>Link to white paper: <a href="http://www.cisco.com/c/en/us/solutions/collateral/data-center-virtualization/san-consolidation-solution/net_implementation_white_paper0900aecd802cbe92.html">http://www.cisco.com/c/en/us/solutions/collateral/data-center-virtualization/san-consolidation-solution/net_implementation_white_paper0900aecd802cbe92.html</a></p><p>So depending on the load of your switch, your traffic might be affected.</p><p>Also, here is another great article: <a href="http://www.lovemytool.com/blog/2007/08/span-ports-or-t.html">http://www.lovemytool.com/blog/2007/08/span-ports-or-t.html</a></p><p>In the article, it states: "Spanning or mirroring changes the timing of the frame interaction (what you see is not what you get)"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '15, 11:59</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-46409" class="comments-container"></div><div id="comment-tools-46409" class="comment-tools"></div><div class="clear"></div><div id="comment-46409-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

