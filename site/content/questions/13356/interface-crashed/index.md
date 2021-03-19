+++
type = "question"
title = "Interface crashed"
description = '''while trying to capture packets that I was sending from another machine, I got a message saying that wireshark has crashed. Now I am not able to capture the packets that I am sending from the other machine. Does anyone have any idea why?'''
date = "2012-08-03T09:18:00Z"
lastmod = "2012-08-03T10:42:00Z"
weight = 13356
keywords = [ "wireshark_crashed" ]
aliases = [ "/questions/13356" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Interface crashed](/questions/13356/interface-crashed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13356-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13356-score" class="post-score" title="current number of votes">0</div><span id="post-13356-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>while trying to capture packets that I was sending from another machine, I got a message saying that wireshark has crashed. Now I am not able to capture the packets that I am sending from the other machine. Does anyone have any idea why?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark_crashed" rel="tag" title="see questions tagged &#39;wireshark_crashed&#39;">wireshark_crashed</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Aug '12, 09:18</strong></p><img src="https://secure.gravatar.com/avatar/4626e19b706e53860c1ff4e3277b32d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Noob&#39;s gravatar image" /><p><span>Noob</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Noob has no accepted answers">0%</span></p></div></div><div id="comments-container-13356" class="comments-container"></div><div id="comment-tools-13356" class="comment-tools"></div><div class="clear"></div><div id="comment-13356-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13357"></span>

<div id="answer-container-13357" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13357-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13357-score" class="post-score" title="current number of votes">0</div><span id="post-13357-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It probably crashed because you were capturing too much data for Wireshark to handle. You should try capturing with dumpcap instead, which is a command line tool installed with Wireshark. It doesn't keep the frame details in memory, so it isn't likely to crash like Wireshark will if there's too much data to be kept.</p><p>You can use <code>dumpcap -D</code> to get a list of interfaces, and then <code>dumpcap -i &lt;interfaceindex&gt; -w filename</code> to capture to file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '12, 09:54</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-13357" class="comments-container"><span id="13358"></span><div id="comment-13358" class="comment"><div id="post-13358-score" class="comment-score"></div><div class="comment-text"><p>Hmm if I try capturing using wireshark again with lesser data, it should right? It isn't capturing even one packet now. And what type of file should I write into. When I tried a text file, the file shows encoded data. Any help with this?</p></div><div id="comment-13358-info" class="comment-info"><span class="comment-age">(03 Aug '12, 10:26)</span> <span class="comment-user userinfo">Noob</span></div></div><span id="13359"></span><div id="comment-13359" class="comment"><div id="post-13359-score" class="comment-score"></div><div class="comment-text"><p>Wireshark should not crash when capturing packets unless there are A LOT of packets. If it does crash even when capturing a few packets you might want to open a detailed bug report at <a href="http://bugs.wireshark.org">http://bugs.wireshark.org</a>.</p><p>You should usually use pcapng or pcap files. It doesn't make much sense capturing into text files, since you can't do much with them - it is far better to use an actual trace file format like pcapng, which Wireshark can open and decode for you. If you need text dumps, you can export them from Wireshark later anyway.</p></div><div id="comment-13359-info" class="comment-info"><span class="comment-age">(03 Aug '12, 10:42)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-13357" class="comment-tools"></div><div class="clear"></div><div id="comment-13357-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

