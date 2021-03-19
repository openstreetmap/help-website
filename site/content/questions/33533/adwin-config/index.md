+++
type = "question"
title = "Adwin Config"
description = '''I&#x27;m very new to wireshark and currently in learning stage . I would like to get much out of it to developed my careers. So please help. Recently I scan my network and I got STP and ADwin congig entry which I want to understand more about. Not sure why I am getting STP entry as,when I my my STP turn ...'''
date = "2014-06-06T16:06:00Z"
lastmod = "2014-06-12T07:02:00Z"
weight = 33533
keywords = [ "stp" ]
aliases = [ "/questions/33533" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Adwin Config](/questions/33533/adwin-config)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33533-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33533-score" class="post-score" title="current number of votes">0</div><span id="post-33533-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm very new to wireshark and currently in learning stage . I would like to get much out of it to developed my careers. So please help.</p><p>Recently I scan my network and I got STP and ADwin congig entry which I want to understand more about. Not sure why I am getting STP entry as,when I my my STP turn off</p><pre><code>Source                  Destination                      Protocal  Length
Procuvre_1d:3c:cf       Spanning-tree-(for-bridges)_00     STP      60</code></pre><p>And ADwin Config,</p><pre><code>Source                   destination       Protocal        lenght  Info
192.168.82.91/202/201    255.255.255.255   ADwin Congif    64       UDPOut</code></pre>Could you please help me understand this please.</div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-stp" rel="tag" title="see questions tagged &#39;stp&#39;">stp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jun '14, 16:06</strong></p><img src="https://secure.gravatar.com/avatar/077ff54bb06aa9232e9dfd38fa62b912?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wire46&#39;s gravatar image" /><p><span>wire46</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wire46 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Jun '14, 02:39</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-33533" class="comments-container"></div><div id="comment-tools-33533" class="comment-tools"></div><div class="clear"></div><div id="comment-33533-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33713"></span>

<div id="answer-container-33713" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33713-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33713-score" class="post-score" title="current number of votes">0</div><span id="post-33713-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I want to understand more about.</p></blockquote><p>good.</p><blockquote><p>Not sure why I am getting STP entry as,when I my my STP turn off</p></blockquote><p>apparently STP was not disabled on at least one switch, that's why you see it in the capture file ;-)</p><p>Regarding ADwin: You cannot explain <strong>why</strong> a system sends packets of a certain protocol to the network, by looking at the capture files with Wireshark. You can only analyze the content of those frames. If you want to know <strong>why</strong>, you must check the configuration of the involved systems.</p><p>Some info about ADwin<br />
</p><blockquote><p><a href="http://wiki.wireshark.org/Protocols/adwin_config">http://wiki.wireshark.org/Protocols/adwin_config</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '14, 07:02</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-33713" class="comments-container"></div><div id="comment-tools-33713" class="comment-tools"></div><div class="clear"></div><div id="comment-33713-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

