+++
type = "question"
title = "DRDA dissector misses some codepoints"
description = '''After capturing some Apache Derby traffic (which also use DRDA) there are some unknown codepoints in wireshark.  DDM codepoint 0xc000 Parameter codepoint 0x01 (within a SQLSTT DDM) Parameter codepoint 0xc001(within 0xc000 DDM) Parameter codepoint 0xc002 (within 0xc000 DDM)  It seems also that wiresh...'''
date = "2016-03-29T13:26:00Z"
lastmod = "2016-03-30T05:55:00Z"
weight = 51271
keywords = [ "heuristic", "dissector", "drda" ]
aliases = [ "/questions/51271" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [DRDA dissector misses some codepoints](/questions/51271/drda-dissector-misses-some-codepoints)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51271-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51271-score" class="post-score" title="current number of votes">0</div><span id="post-51271-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>After capturing some Apache Derby traffic (which also use DRDA) there are some unknown codepoints in wireshark.</p><ul><li>DDM codepoint 0xc000</li><li>Parameter codepoint 0x01 (within a SQLSTT DDM)</li><li>Parameter codepoint 0xc001(within 0xc000 DDM)</li><li>Parameter codepoint 0xc002 (within 0xc000 DDM)</li></ul><p>It seems also that wireshark sometimes does not detect parameters within a DDM, see <a href="https://raw.githubusercontent.com/salyh/_pics/master/drda1.png">https://raw.githubusercontent.com/salyh/_pics/master/drda1.png</a></p><p>PCAP: <a href="https://github.com/salyh/_pics/blob/master/drda_toursdb.pcap?raw=true">https://github.com/salyh/_pics/blob/master/drda_toursdb.pcap?raw=true</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-heuristic" rel="tag" title="see questions tagged &#39;heuristic&#39;">heuristic</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-drda" rel="tag" title="see questions tagged &#39;drda&#39;">drda</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Mar '16, 13:26</strong></p><img src="https://secure.gravatar.com/avatar/bc18064b4e13135e4687b1dd93619b4f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="salyh&#39;s gravatar image" /><p><span>salyh</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="salyh has no accepted answers">0%</span></p></div></div><div id="comments-container-51271" class="comments-container"></div><div id="comment-tools-51271" class="comment-tools"></div><div class="clear"></div><div id="comment-51271-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51275"></span>

<div id="answer-container-51275" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51275-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51275-score" class="post-score" title="current number of votes">0</div><span id="post-51275-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please <a href="https://bugs.wireshark.org">open a bug report</a> requesting that Wireshark dissect these code points (and attach the PCAP to the bug report) That's the proper way to report bugs or request enhancements (this is a Q&amp;A site).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '16, 17:08</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-51275" class="comments-container"><span id="51289"></span><div id="comment-51289" class="comment"><div id="post-51289-score" class="comment-score"></div><div class="comment-text"><p>done, see <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12307">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12307</a></p></div><div id="comment-51289-info" class="comment-info"><span class="comment-age">(30 Mar '16, 05:55)</span> <span class="comment-user userinfo">salyh</span></div></div></div><div id="comment-tools-51275" class="comment-tools"></div><div class="clear"></div><div id="comment-51275-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

