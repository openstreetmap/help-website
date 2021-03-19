+++
type = "question"
title = "Wireshark with NS2"
description = '''Can I analyse ns2 tracefile in wireshark? As it takes PCAP file as input, so I need to know if I can generate PCAP files using ns2 or any other method which will make me analyse my NS2 simulation on wireshark.'''
date = "2016-01-11T01:49:00Z"
lastmod = "2016-01-11T07:14:00Z"
weight = 49069
keywords = [ "ns2", "wireshark" ]
aliases = [ "/questions/49069" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark with NS2](/questions/49069/wireshark-with-ns2)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49069-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49069-score" class="post-score" title="current number of votes">0</div><span id="post-49069-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can I analyse ns2 tracefile in wireshark? As it takes PCAP file as input, so I need to know if I can generate PCAP files using ns2 or any other method which will make me analyse my NS2 simulation on wireshark.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ns2" rel="tag" title="see questions tagged &#39;ns2&#39;">ns2</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jan '16, 01:49</strong></p><img src="https://secure.gravatar.com/avatar/7db6de14f8338d9c47f43421ced83b4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chetan&#39;s gravatar image" /><p><span>Chetan</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chetan has no accepted answers">0%</span></p></div></div><div id="comments-container-49069" class="comments-container"></div><div id="comment-tools-49069" class="comment-tools"></div><div class="clear"></div><div id="comment-49069-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49082"></span>

<div id="answer-container-49082" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49082-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49082-score" class="post-score" title="current number of votes">0</div><span id="post-49082-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Can I analyse ns2 tracefile in wireshark?</p></blockquote><p>No.</p><p>AFAIK, ns2 can't create pcap files and the ns2 trace files are not well suited to be parsed by Wireshark (wrong and/or not enough information in the trace files).</p><p>However, there are ns-2 trace file analyzers available:</p><blockquote><p><a href="http://sourceforge.net/projects/jtrcezer">http://sourceforge.net/projects/jtrcezer</a><br />
<a href="http://sourceforge.net/projects/trace-analyzer">http://sourceforge.net/projects/trace-analyzer</a><br />
</p></blockquote><p>BTW: ns-3 can write ´pcap files, but ns-3 is not compatible with ns-2.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jan '16, 07:14</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-49082" class="comments-container"></div><div id="comment-tools-49082" class="comment-tools"></div><div class="clear"></div><div id="comment-49082-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

