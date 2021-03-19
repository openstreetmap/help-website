+++
type = "question"
title = "How to Use Tshark to extract tcp hex portion"
description = '''Is there any way to extract tcp segment out of each captured packet from command line and displaying only packet bytes(hex) of and not ASCII? tshark -x is giving both hex and ASCII dump of all the layers.'''
date = "2013-06-12T23:21:00Z"
lastmod = "2013-06-13T17:02:00Z"
weight = 21991
keywords = [ "tshark" ]
aliases = [ "/questions/21991" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to Use Tshark to extract tcp hex portion](/questions/21991/how-to-use-tshark-to-extract-tcp-hex-portion)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21991-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21991-score" class="post-score" title="current number of votes">0</div><span id="post-21991-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there any way to extract tcp segment out of each captured packet from command line and displaying only packet bytes(hex) of and not ASCII?</p><p>tshark -x is giving both hex and ASCII dump of all the layers.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jun '13, 23:21</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Jun '13, 23:22</strong> </span></p></div></div><div id="comments-container-21991" class="comments-container"></div><div id="comment-tools-21991" class="comment-tools"></div><div class="clear"></div><div id="comment-21991-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21999"></span>

<div id="answer-container-21999" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21999-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21999-score" class="post-score" title="current number of votes">0</div><span id="post-21999-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please see my answers to similar questions:</p><blockquote><p><code>http://ask.wireshark.org/questions/16592/tcp-stream-output-in-pdml-format</code><br />
<code>http://ask.wireshark.org/questions/16268/how-do-i-extract-all-the-data-sections</code><br />
<code>http://ask.wireshark.org/questions/15374/dump-raw-packet-data-field-only</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '13, 03:41</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-21999" class="comments-container"><span id="22032"></span><div id="comment-22032" class="comment"><div id="post-22032-score" class="comment-score"></div><div class="comment-text"><p>Kurt, sorry for bugging you again.Below is a sample packet where TCP is from 0020 position:0x8a to 0030 position 0x00(before 0x47) so if i want to display exactly that tcp segment on command line what should be done?</p><p>0000 00 01 5c 31 bb c1 d4 85 64 a7 bf a3 08 00 45 00<br />
0010 01 48 69 87 40 00 80 06 00 00 18 06 ad dc c7 b5<br />
0020 84 f9 8a be 00 50 73 e7 7d 59 c7 0e 66 a7 50 18<br />
0030 40 29 13 cc 00 00 47 45 54 20 2f 20 48 54 54 50<br />
0040 2f 31 2e 31 0d 0a 48 6f 73 74 3a 20 77 77 77 2e<br />
0050 64 69 73 6e 65 79 2e 63 6f 6d 0d 0a 55 73 65 72<br />
0060 2d 41 67 65 6e 74 3a 20 4d 6f 7a 69 6c 6c 61 2f<br />
0070 35 2e 30 20 28 57 69 6e 64 6f 77 73 20 4e 54 20<br />
0080 36 2e 31 3b 20 57 4f 57 36 34 3b 20 72 76 3a 31<br />
0090 36 2e 30 29 20 47 65 63 6b 6f 2f 32 30 31 30 30<br />
00a0 31 30 31 20 46 69 72 65 66 6f 78 2f 31 36 2e 30<br />
00b0 0d 0a 41 63 63 65 70 74 3a 20 74 65 78 74 2f 68<br />
00c0 74 6d 6c 2c 61 70 70 6c 69 63 61 74 69 6f 6e 2f<br />
00d0 78 68 74 6d 6c 2b 78 6d 6c 2c 61 70 70 6c 69 63<br />
00e0 61 74 69 6f 6e 2f 78 6d 6c 3b 71 3d 30 2e 39 2c<br />
00f0 2a 2f 2a 3b 71 3d 30 2e 38 0d 0a 41 63 63 65 70<br />
0100 74 2d 4c 61 6e 67 75 61 67 65 3a 20 65 6e 2d 55<br />
0110 53 2c 65 6e 3b 71 3d 30 2e 35 0d 0a 41 63 63 65<br />
0120 70 74 2d 45 6e 63 6f 64 69 6e 67 3a 20 67 7a 69<br />
0130 70 2c 20 64 65 66 6c 61 74 65 0d 0a 43 6f 6e 6e<br />
0140 65 63 74 69 6f 6e 3a 20 6b 65 65 70 2d 61 6c 69<br />
0150 76 65 0d 0a 0d 0a</p></div><div id="comment-22032-info" class="comment-info"><span class="comment-age">(13 Jun '13, 17:02)</span> <span class="comment-user userinfo">krishnayeddula</span></div></div></div><div id="comment-tools-21999" class="comment-tools"></div><div class="clear"></div><div id="comment-21999-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

