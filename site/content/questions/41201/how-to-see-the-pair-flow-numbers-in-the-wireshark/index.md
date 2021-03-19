+++
type = "question"
title = "How to see the pair flow numbers in the wireshark?"
description = '''Hi I research DDoS attack solution. but, i can&#x27;t find how to see the pair flow number in the wireshark. pair flow means below example host 1 --&amp;gt; src(1.1.1.1) dst(2.2.2.2) host 2 --&amp;gt; src(2.2.2.2) dst(1.1.1.1) host1 and host2 are pair pair flow number is very important element for DDoS detection...'''
date = "2015-04-05T20:45:00Z"
lastmod = "2015-04-06T03:16:00Z"
weight = 41201
keywords = [ "traffic-analysis" ]
aliases = [ "/questions/41201" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to see the pair flow numbers in the wireshark?](/questions/41201/how-to-see-the-pair-flow-numbers-in-the-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41201-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41201-score" class="post-score" title="current number of votes">0</div><span id="post-41201-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I research DDoS attack solution. but, i can't find how to see the pair flow number in the wireshark. pair flow means below example</p><p>host 1 --&gt; src(1.1.1.1) dst(2.2.2.2) host 2 --&gt; src(2.2.2.2) dst(1.1.1.1)</p><p>host1 and host2 are pair</p><p>pair flow number is very important element for DDoS detection. pleases help me.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-traffic-analysis" rel="tag" title="see questions tagged &#39;traffic-analysis&#39;">traffic-analysis</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Apr '15, 20:45</strong></p><img src="https://secure.gravatar.com/avatar/89da163c13027a6536ccdc883adead9e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Soong&#39;s gravatar image" /><p><span>Soong</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Soong has no accepted answers">0%</span></p></div></div><div id="comments-container-41201" class="comments-container"></div><div id="comment-tools-41201" class="comment-tools"></div><div class="clear"></div><div id="comment-41201-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41209"></span>

<div id="answer-container-41209" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41209-score" class="post-score" title="current number of votes">0</div><span id="post-41209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is no built-in function in Wireshark to do that. You can use tshark and some scripting to find the pair flows.</p><blockquote><p>tshark -nr input.pcap -T fields -e ip.src -e ip.dst -e ip.proto -e tcp.port -e udp.port -E separator=, -E header=y &gt; output.txt</p></blockquote><p>Then parse the output to find the pair flows that match your definition.</p><p>BTW: I added the IP protocol (ip.proto) and the ports, because the following paper includes the <strong>identical protocol</strong> as part of the "pair-flow" definition. If you don't need them, remove the options or ignore them in your script.</p><blockquote><p><a href="http://goo.gl/mJGXZS">http://goo.gl/mJGXZS</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Apr '15, 03:16</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Apr '15, 03:18</strong> </span></p></div></div><div id="comments-container-41209" class="comments-container"></div><div id="comment-tools-41209" class="comment-tools"></div><div class="clear"></div><div id="comment-41209-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

