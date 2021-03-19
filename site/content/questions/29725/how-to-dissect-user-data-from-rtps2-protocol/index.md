+++
type = "question"
title = "How to dissect user data from rtps2 protocol?"
description = '''I am using OpenSplice DDS and wants to retrieve user data from wireshark. Can you please let me know how to retrieve the same?'''
date = "2014-02-11T20:28:00Z"
lastmod = "2014-02-12T02:04:00Z"
weight = 29725
keywords = [ "dds" ]
aliases = [ "/questions/29725" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to dissect user data from rtps2 protocol?](/questions/29725/how-to-dissect-user-data-from-rtps2-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29725-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using OpenSplice DDS and wants to retrieve user data from wireshark. Can you please let me know how to retrieve the same?</p></div><div id="question-tags" class="tags-container tags">dds</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '14, 20:28</strong></p><img src="https://secure.gravatar.com/avatar/47fb5efd9424262c89bece9f08d3c704?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Usha&#39;s gravatar image" /><p>Usha<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Usha has no accepted answers">0%</span></p></div></div><div id="comments-container-29725" class="comments-container"></div><div id="comment-tools-29725" class="comment-tools"></div><div class="clear"></div><div id="comment-29725-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29746"></span>

<div id="answer-container-29746" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29746-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use tshark</p><blockquote><p>tshark -nr input.pcap -Y "rtps" -T fields -e frame.number -e rtps.param.userData</p></blockquote><p>See the <a href="http://www.wireshark.org/docs/dfref/r/rtps.html">Real-Time Publish-Subscribe Wire Protocol display filter reference</a> for more fields.</p><p>You can also add that field (rtps.param.userData) as a new column in Wireshark</p><blockquote><p><a href="http://www.lovemytool.com/blog/2009/10/chris_greer_10.html">http://www.lovemytool.com/blog/2009/10/chris_greer_10.html</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '14, 02:04</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-29746" class="comments-container"></div><div id="comment-tools-29746" class="comment-tools"></div><div class="clear"></div><div id="comment-29746-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

