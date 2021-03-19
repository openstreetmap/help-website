+++
type = "question"
title = "How do i save logs with selected attributes only?"
description = '''I need to get only the time, size and the number of the packets from the generated logs in the text file and then I can then upload the text file into my software. Can anyone please help me with that?'''
date = "2012-06-03T07:28:00Z"
lastmod = "2012-06-03T09:17:00Z"
weight = 11580
keywords = [ "filtering" ]
aliases = [ "/questions/11580" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do i save logs with selected attributes only?](/questions/11580/how-do-i-save-logs-with-selected-attributes-only)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11580-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11580-score" class="post-score" title="current number of votes">0</div><span id="post-11580-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to get only the time, size and the number of the packets from the generated logs in the text file and then I can then upload the text file into my software. Can anyone please help me with that?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filtering" rel="tag" title="see questions tagged &#39;filtering&#39;">filtering</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jun '12, 07:28</strong></p><img src="https://secure.gravatar.com/avatar/2c02b59a148336ad53d4a48f44a77239?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="manish&#39;s gravatar image" /><p><span>manish</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="manish has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Jun '12, 06:54</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-11580" class="comments-container"></div><div id="comment-tools-11580" class="comment-tools"></div><div class="clear"></div><div id="comment-11580-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11583"></span>

<div id="answer-container-11583" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11583-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11583-score" class="post-score" title="current number of votes">0</div><span id="post-11583-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Presuming you have the capture files, you can use tshark to output the fields you require. The trick is knowing the names of the fields, I usually open the capture in Wireshark, select the fields in the packet tree and the field name will be displayed in the status bar at the bottom.</p><p>In your case you are asking for the time and size, presumably of each packet, and the number, do you mean frame number?</p><p>The command line to produce the time, size and number of each packet is:</p><p><code>tshark -r yourcapturefile -T fields -e frame.time -e frame.len -e frame.number</code></p><p>Read the tshark <a href="http://www.wireshark.org/docs/man-pages/tshark.html">man</a> page for more info on the -T and -e parameters.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jun '12, 09:17</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-11583" class="comments-container"></div><div id="comment-tools-11583" class="comment-tools"></div><div class="clear"></div><div id="comment-11583-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

