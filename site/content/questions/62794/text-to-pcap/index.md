+++
type = "question"
title = "Text to pcap"
description = '''hi, i use tshark to convert a pcap file to txt file. i use this command: tshark -r input.pcap -x &amp;gt; output.txt How can i convert this text file (output.txt) to a pcap file?  packets start by IP.'''
date = "2017-07-14T23:47:00Z"
lastmod = "2017-07-15T00:57:00Z"
weight = 62794
keywords = [ "tshark" ]
aliases = [ "/questions/62794" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Text to pcap](/questions/62794/text-to-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62794-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62794-score" class="post-score" title="current number of votes">0</div><span id="post-62794-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi, i use tshark to convert a pcap file to txt file. i use this command: tshark -r input.pcap -x &gt; output.txt How can i convert this text file (output.txt) to a pcap file? packets start by IP.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jul '17, 23:47</strong></p><img src="https://secure.gravatar.com/avatar/0b6bdfea45d7093830a2a0638a758239?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hhw&#39;s gravatar image" /><p><span>hhw</span><br />
<span class="score" title="10 reputation points">10</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hhw has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Jul '17, 23:49</strong> </span></p></div></div><div id="comments-container-62794" class="comments-container"></div><div id="comment-tools-62794" class="comment-tools"></div><div class="clear"></div><div id="comment-62794-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62796"></span>

<div id="answer-container-62796" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62796-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62796-score" class="post-score" title="current number of votes">0</div><span id="post-62796-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hhw has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can if you have the original packet bytes in the text output as well. There's the command line tool <a href="https://www.wireshark.org/docs/man-pages/text2pcap.html">text2pcap</a>, or you can use the 'Import from hex dump' feature from Wireshark. Make sure that the text file matches the required input, so some preprocessing of the text file may be required.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '17, 00:57</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-62796" class="comments-container"></div><div id="comment-tools-62796" class="comment-tools"></div><div class="clear"></div><div id="comment-62796-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

