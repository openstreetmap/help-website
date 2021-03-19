+++
type = "question"
title = "How to make tshark consider tcp messages going through a particular port (other than 3868) as diameter in linux?"
description = '''I have this setup where a diameter connection is established which uses a tcp port which is different than the default port 3868.I have to take a pcap and analyze the diameter messages.Now the problem is we can analyze the pcap in wireshark GUI where I can add the other port along with 3868 in the v...'''
date = "2014-04-30T06:01:00Z"
lastmod = "2014-04-30T06:36:00Z"
weight = 32309
keywords = [ "tshark" ]
aliases = [ "/questions/32309" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to make tshark consider tcp messages going through a particular port (other than 3868) as diameter in linux?](/questions/32309/how-to-make-tshark-consider-tcp-messages-going-through-a-particular-port-other-than-3868-as-diameter-in-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32309-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32309-score" class="post-score" title="current number of votes">0</div><span id="post-32309-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have this setup where a diameter connection is established which uses a tcp port which is different than the default port 3868.I have to take a pcap and analyze the diameter messages.Now the problem is we can analyze the pcap in wireshark GUI where I can add the other port along with 3868 in the view -&gt;preferences -&gt; diameter,then it will consider messages at this port also as diameter but how can I do the same in tshark CLI,should I set it in services file (/root/wireshark_182/wireshark-1.8.2/services) ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Apr '14, 06:01</strong></p><img src="https://secure.gravatar.com/avatar/6bd1643355800491cb981366f08340d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="babin&#39;s gravatar image" /><p><span>babin</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="babin has no accepted answers">0%</span></p></div></div><div id="comments-container-32309" class="comments-container"></div><div id="comment-tools-32309" class="comment-tools"></div><div class="clear"></div><div id="comment-32309-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32310"></span>

<div id="answer-container-32310" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32310-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32310-score" class="post-score" title="current number of votes">1</div><span id="post-32310-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From tshark -h -o &lt;name&gt;:&lt;value&gt; ... override preference setting</p><p>But the easiest is to start Wireshark change the preference and save, then run tshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '14, 06:36</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-32310" class="comments-container"></div><div id="comment-tools-32310" class="comment-tools"></div><div class="clear"></div><div id="comment-32310-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

