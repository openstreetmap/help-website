+++
type = "question"
title = "Wirshark crashes after I run Telephony -&gt; VoIP Calls -&gt; Flow on Ubuntu 14.04"
description = '''Hi, everyone.  My Wireshark crashes just after I open a PCAP-trace and run Telephony -&amp;gt; VoIP Calls -&amp;gt; Flow.  My Ubuntu version is 14.04.  Installed Wireshark from Ubuntu Applications Center.  Can anyone help me with how I can fix this crash? Should I install different Ubuntu version?  I have h...'''
date = "2015-10-21T05:27:00Z"
lastmod = "2015-10-22T03:47:00Z"
weight = 46797
keywords = [ "ubuntu" ]
aliases = [ "/questions/46797" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wirshark crashes after I run Telephony -&gt; VoIP Calls -&gt; Flow on Ubuntu 14.04](/questions/46797/wirshark-crashes-after-i-run-telephony-voip-calls-flow-on-ubuntu-1404)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46797-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46797-score" class="post-score" title="current number of votes">0</div><span id="post-46797-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, everyone.<br />
My Wireshark crashes just after I open a PCAP-trace and run Telephony -&gt; VoIP Calls -&gt; Flow.<br />
My Ubuntu version is 14.04.<br />
Installed Wireshark from Ubuntu Applications Center.<br />
Can anyone help me with how I can fix this crash? Should I install different Ubuntu version?<br />
I have heard that Wireshark hardly works on Ubuntu 14.04.<br />
Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '15, 05:27</strong></p><img src="https://secure.gravatar.com/avatar/d61aba9492ff25233c1ab080ffdff06e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anton%20Bagaterenko&#39;s gravatar image" /><p><span>Anton Bagate...</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anton Bagaterenko has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-46797" class="comments-container"><span id="46801"></span><div id="comment-46801" class="comment"><div id="post-46801-score" class="comment-score"></div><div class="comment-text"><p>What is your Wireshark version?</p></div><div id="comment-46801-info" class="comment-info"><span class="comment-age">(21 Oct '15, 08:19)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="46805"></span><div id="comment-46805" class="comment"><div id="post-46805-score" class="comment-score"></div><div class="comment-text"><p>Version 1.10.6</p></div><div id="comment-46805-info" class="comment-info"><span class="comment-age">(21 Oct '15, 09:36)</span> <span class="comment-user userinfo">Anton Bagate...</span></div></div></div><div id="comment-tools-46797" class="comment-tools"></div><div class="clear"></div><div id="comment-46797-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="46820"></span>

<div id="answer-container-46820" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46820-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46820-score" class="post-score" title="current number of votes">0</div><span id="post-46820-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Version 1.10.6</p></blockquote><p>sounds like a known bug, which has been fixed</p><blockquote><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10016">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10016</a></p></blockquote><p>Can you please test if Wireshark crashes with the pcap file attached to the bug?</p><p>BTW: If Ubuntu 14.04 does not offer a newer Wireshark release than 1.10.6, you can either upgrade Ubuntu, or try to build Wireshark yourself:</p><blockquote><p><a href="http://linuxg.net/how-to-install-wireshark-1-12-on-ubuntu-14-04-and-derivatives-from-sources/">http://linuxg.net/how-to-install-wireshark-1-12-on-ubuntu-14-04-and-derivatives-from-sources/</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '15, 14:55</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Oct '15, 14:56</strong> </span></p></div></div><div id="comments-container-46820" class="comments-container"></div><div id="comment-tools-46820" class="comment-tools"></div><div class="clear"></div><div id="comment-46820-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46829"></span>

<div id="answer-container-46829" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46829-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46829-score" class="post-score" title="current number of votes">0</div><span id="post-46829-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There's also a separate source for an up to date stable release of Wireshark on Debian based distributions (such as Ubuntu), the <a href="https://launchpad.net/~wireshark-dev/+archive/ubuntu/stable">Wireshark Developers PPA</a>. This should be a lot easier to use than compiling your own version.</p><p>The PPA is maintained by a Wireshark Core Developer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '15, 03:47</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></br></p></div></div><div id="comments-container-46829" class="comments-container"></div><div id="comment-tools-46829" class="comment-tools"></div><div class="clear"></div><div id="comment-46829-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

