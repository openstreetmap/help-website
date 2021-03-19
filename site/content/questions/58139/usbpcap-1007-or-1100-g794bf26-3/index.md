+++
type = "question"
title = "USBPcap 1.0.0.7 or 1.1.0.0-g794bf26-3"
description = '''I&#x27;m confused. The 1.0.0.7 seems the authoritative version as per it&#x27;s originator:  http://desowin.org/usbpcap/ And the 1.1.0.0-g794bf26-3 version seems to be standalone with no details of source or changelog etc. 1.1.0.0-g794bf26-3 seems to be only associated with the Wireshark install and I can&#x27;t f...'''
date = "2016-12-15T10:01:00Z"
lastmod = "2016-12-15T11:35:00Z"
weight = 58139
keywords = [ "usbpcap" ]
aliases = [ "/questions/58139" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [USBPcap 1.0.0.7 or 1.1.0.0-g794bf26-3](/questions/58139/usbpcap-1007-or-1100-g794bf26-3)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58139-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58139-score" class="post-score" title="current number of votes">0</div><span id="post-58139-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm confused.</p><p>The 1.0.0.7 seems the authoritative version as per it's originator: <a href="http://desowin.org/usbpcap/">http://desowin.org/usbpcap/</a></p><p>And the 1.1.0.0-g794bf26-3 version seems to be standalone with no details of source or changelog etc.</p><p>1.1.0.0-g794bf26-3 seems to be only associated with the Wireshark install and I can't find any other instance of this.</p><p>Which should I use, and what is the origin of the 1.1.0.0-g794bf26-3 version?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-usbpcap" rel="tag" title="see questions tagged &#39;usbpcap&#39;">usbpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '16, 10:01</strong></p><img src="https://secure.gravatar.com/avatar/99349826ae84de9566f13cf0f0123276?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mikexx&#39;s gravatar image" /><p><span>Mikexx</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mikexx has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Dec '16, 10:02</strong> </span></p></div></div><div id="comments-container-58139" class="comments-container"></div><div id="comment-tools-58139" class="comment-tools"></div><div class="clear"></div><div id="comment-58139-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58142"></span>

<div id="answer-container-58142" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58142-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58142-score" class="post-score" title="current number of votes">0</div><span id="post-58142-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The USBPcap 1.1.0.0-g794bf26 installer (the latest release packaged with Wireshark is USBPcapSetup-1.1.0.0-g794bf26-5.exe, not 1.1.0.0-g794bf26-3) is a compilation of the top of tree of the (now defunct) USBPcap project as found <a href="https://github.com/desowin/usbpcap">here</a> with local modifications to sign the driver (to run properly on Windows 10) and enhance the NSIS installer.</p><p>Compared to the latest official release, the latest development snapshot supports extcap interface allowing to control USBPcap from Wireshark GUI. If you install version 1.0.07, you will have to launch the capture from the command line.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '16, 11:35</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-58142" class="comments-container"></div><div id="comment-tools-58142" class="comment-tools"></div><div class="clear"></div><div id="comment-58142-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

