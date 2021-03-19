+++
type = "question"
title = "Splitting conversations"
description = '''Beside writing a script using tshark, what would you recommend to split a capture to have one capture per conversation, e.g. UDP, TCP, or Ethernet? Would it be possible to create a feature to split the opened capture into each of the conversations?'''
date = "2013-11-25T13:40:00Z"
lastmod = "2013-11-25T15:14:00Z"
weight = 27363
keywords = [ "conversation" ]
aliases = [ "/questions/27363" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Splitting conversations](/questions/27363/splitting-conversations)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27363-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27363-score" class="post-score" title="current number of votes">0</div><span id="post-27363-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Beside writing a script using tshark, what would you recommend to split a capture to have one capture per conversation, e.g. UDP, TCP, or Ethernet? Would it be possible to create a feature to split the opened capture into each of the conversations?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-conversation" rel="tag" title="see questions tagged &#39;conversation&#39;">conversation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '13, 13:40</strong></p><img src="https://secure.gravatar.com/avatar/0667d303e35d445fb4ea33f6e0c072aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wnatter&#39;s gravatar image" /><p><span>wnatter</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wnatter has no accepted answers">0%</span></p></div></div><div id="comments-container-27363" class="comments-container"></div><div id="comment-tools-27363" class="comment-tools"></div><div class="clear"></div><div id="comment-27363-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27364"></span>

<div id="answer-container-27364" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27364-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27364-score" class="post-score" title="current number of votes">1</div><span id="post-27364-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you insist on an unscripted, manual method through the GUI, easiest way right now would probably be:</p><ul><li>Go to Statistics &gt; Conversations</li><li>Right-click a conversation, and select "Apply as Filter"</li><li>Go to File &gt; Export Specified Packets &gt; Displayed</li></ul><p>Now, through scripted methods there are a bunch of things you can do. One script I wrote a while ago used the tshark protocol hierarchy printout to dynamically learn each protocol type in the capture to not only save per-protocol capture files but to break them into their own folders where each packet capture file was a given protocol type over a given time period (using a combination of tshark and editcap). Even further than that, I built in tshark -z io,stats counters on a per-protocol basis, per time period, so that it would generate an excel file report of performance metrics over time for any protocol that was supported for it and found in the file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '13, 14:19</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Nov '13, 14:21</strong> </span></p></div></div><div id="comments-container-27364" class="comments-container"><span id="27365"></span><div id="comment-27365" class="comment"><div id="post-27365-score" class="comment-score"></div><div class="comment-text"><p>Impressive! I have done the manual GUI way at first, then the script I wrote using tshark (I extract the timeframe of the flow of interest, its basic characteristics like tcp ports, and store it as a unique file with its own info). I think it would make sense to offer the ability to split a capture into all of its individual conversation in a painless manner. I just don't know how to ask for a feature to be added into Wireshark... :-)</p><p>In my case, I need to gather captures from multiple points, then I merge them into one so I can observe the movement of packets through the network easily. It's easier to then look at a single flow (src IP, dst IP, src port, dst port, transport) at a time. Right now, I'm looking at 1003 flows taken over 1.5 hours for a single laptop of interest. It's easier to find a needle in an organized haystack...</p></div><div id="comment-27365-info" class="comment-info"><span class="comment-age">(25 Nov '13, 14:48)</span> <span class="comment-user userinfo">wnatter</span></div></div><span id="27366"></span><div id="comment-27366" class="comment"><div id="post-27366-score" class="comment-score"></div><div class="comment-text"><p>Oh, to request a feature you can do it as a bug report. Just make sure to list the severity as "enhancement" to mark it as a feature request: <a href="https://bugs.wireshark.org/bugzilla/">https://bugs.wireshark.org/bugzilla/</a></p><p>As for the needle in a haystack, what exactly is the needle you're looking for from the large trace file?</p></div><div id="comment-27366-info" class="comment-info"><span class="comment-age">(25 Nov '13, 15:14)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-27364" class="comment-tools"></div><div class="clear"></div><div id="comment-27364-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

