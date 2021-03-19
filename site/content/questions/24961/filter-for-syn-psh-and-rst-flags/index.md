+++
type = "question"
title = "Filter for SYN, PSH and RST flags"
description = '''Hey, I want to add to this question. I&#x27;m actually trying to display the SYN flags using the display function from above, but I am also trying to display the PSH and RST flags at the same time. This might be a stupid question, but how do I write a display function to combine all three of these?'''
date = "2013-09-19T10:40:00Z"
lastmod = "2013-09-19T14:32:00Z"
weight = 24961
keywords = [ "rst", "filter", "psh", "syn" ]
aliases = [ "/questions/24961" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filter for SYN, PSH and RST flags](/questions/24961/filter-for-syn-psh-and-rst-flags)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24961-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24961-score" class="post-score" title="current number of votes">0</div><span id="post-24961-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey, I want to add to this question.</p><p>I'm actually trying to display the SYN flags using the display function from above, but I am also trying to display the PSH and RST flags at the same time.</p><p>This might be a stupid question, but how do I write a display function to combine all three of these?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span> <span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-psh" rel="tag" title="see questions tagged &#39;psh&#39;">psh</span> <span class="post-tag tag-link-syn" rel="tag" title="see questions tagged &#39;syn&#39;">syn</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Sep '13, 10:40</strong></p><img src="https://secure.gravatar.com/avatar/364a1c57580172a8932806c51cd32b5a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RajTrivedi&#39;s gravatar image" /><p><span>RajTrivedi</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RajTrivedi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>19 Sep '13, 14:22</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-24961" class="comments-container"><span id="24967"></span><div id="comment-24967" class="comment"><div id="post-24967-score" class="comment-score"></div><div class="comment-text"><p>Hm, is this what you want? "tcp[13]==14||tcp[13]==2" for all [RST,ACK] or [SYN] packets (Client only)<br />
"tcp[13]==14||tcp[13]&amp;2" for all [RST,ACK] or [SYN] or [SYN,ACK] packets</p><p>'A combination of all three of these: [SYN,RST,ACK] ? I think this is an invalid combination. How about opening a new thread to separate it from this already positively answered question</p></div><div id="comment-24967-info" class="comment-info"><span class="comment-age">(19 Sep '13, 12:51)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="24973"></span><div id="comment-24973" class="comment"><div id="post-24973-score" class="comment-score"></div><div class="comment-text"><p>I've converted this to a question, please don't ask new questions as "answers" to an existing one.</p></div><div id="comment-24973-info" class="comment-info"><span class="comment-age">(19 Sep '13, 14:23)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-24961" class="comment-tools"></div><div class="clear"></div><div id="comment-24961-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24974"></span>

<div id="answer-container-24974" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24974-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24974-score" class="post-score" title="current number of votes">0</div><span id="post-24974-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Do you want a display filter which shows frames in which any of those 3 bits are set?</p><p><code>(tcp.flags.syn == 1) || (tcp.flags.push == 1) || (tcp.flags.reset == 1)</code></p><p>would do that.</p><p>A way to build up a filter like that is to look at the Flags section of a TCP fragment and then, for each bit you're interested in, right-click on the field for that bit and select "Prepare as filter" and then select "... or Selected". (You might need to change the value of what comes after the equals sign.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Sep '13, 14:32</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span> </br></p></div></div><div id="comments-container-24974" class="comments-container"></div><div id="comment-tools-24974" class="comment-tools"></div><div class="clear"></div><div id="comment-24974-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

