+++
type = "question"
title = "Wireshark not recognizing Atheros on Ubuntu 10.04"
description = '''I installed Wireshark on my Ubuntu 10.04 netbook but it won&#x27;t recognize either of my RJ45 LAN or wireless Atheros card. Can anyone help me out?'''
date = "2010-09-30T12:56:00Z"
lastmod = "2010-11-19T21:03:00Z"
weight = 380
keywords = [ "atheros", "ubuntu" ]
aliases = [ "/questions/380" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark not recognizing Atheros on Ubuntu 10.04](/questions/380/wireshark-not-recognizing-atheros-on-ubuntu-1004)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-380-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-380-score" class="post-score" title="current number of votes">0</div><span id="post-380-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I installed Wireshark on my Ubuntu 10.04 netbook but it won't recognize either of my RJ45 LAN or wireless Atheros card. Can anyone help me out?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-atheros" rel="tag" title="see questions tagged &#39;atheros&#39;">atheros</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Sep '10, 12:56</strong></p><img src="https://secure.gravatar.com/avatar/b8dd02a98602cd645c26f9e4b02e487a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Grafixx01&#39;s gravatar image" /><p><span>Grafixx01</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Grafixx01 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Sep '10, 23:36</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-380" class="comments-container"></div><div id="comment-tools-380" class="comment-tools"></div><div class="clear"></div><div id="comment-380-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="399"></span>

<div id="answer-container-399" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-399-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-399-score" class="post-score" title="current number of votes">0</div><span id="post-399-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What does <code>dumpcap -D</code> say? If it's something like</p><pre><code>dumpcap: There are no interfaces on which a capture can be done</code></pre><p>Then you may need to enable capture privileges (<code>CAP_NET_ADMIN</code> and <code>CAP_NET_RAW</code>) in dumpcap. Instructions for doing this can be found in many places including</p><ul><li><a href="https://blog.wireshark.org/2010/02/running-wireshark-as-you/">The Wireshark blog</a></li><li><a href="http://packetlife.net/blog/2010/mar/19/sniffing-wireshark-non-root-user/">Packet Life</a></li><li><a href="http://brainstorm.ubuntu.com/idea/14140/">Ubuntu Brainstorm</a></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Oct '10, 08:31</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-399" class="comments-container"><span id="401"></span><div id="comment-401" class="comment"><div id="post-401-score" class="comment-score"></div><div class="comment-text"><p>I did that and got the message that you stated above.</p><p>However, I followed the instructions and it can't find "packetcapture" so it still doesn't recognize the Atheros card.</p></div><div id="comment-401-info" class="comment-info"><span class="comment-age">(01 Oct '10, 12:45)</span> <span class="comment-user userinfo">Grafixx01</span></div></div><span id="402"></span><div id="comment-402" class="comment"><div id="post-402-score" class="comment-score"></div><div class="comment-text"><p>Which instructions did you follow? "packetcapture" is the name of a group that you create.</p></div><div id="comment-402-info" class="comment-info"><span class="comment-age">(01 Oct '10, 13:29)</span> <span class="comment-user userinfo">Gerald Combs ♦♦</span></div></div></div><div id="comment-tools-399" class="comment-tools"></div><div class="clear"></div><div id="comment-399-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1029"></span>

<div id="answer-container-1029" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1029-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1029-score" class="post-score" title="current number of votes">0</div><span id="post-1029-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you running Wireshark as root or is your user in the right group? When I run it as a normal user, it doesn't see the cards. When I sudo wireshark it runs and sees the network cards. (Of course, I do get the warning that it is dangerous to run Wireshark as root. So you may want to add your user to the group that can Wireshark rather than sudo.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '10, 21:03</strong></p><img src="https://secure.gravatar.com/avatar/23a870b78afd4f7b7e9a654811935cce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stoner455&#39;s gravatar image" /><p><span>stoner455</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stoner455 has no accepted answers">0%</span></p></div></div><div id="comments-container-1029" class="comments-container"></div><div id="comment-tools-1029" class="comment-tools"></div><div class="clear"></div><div id="comment-1029-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

