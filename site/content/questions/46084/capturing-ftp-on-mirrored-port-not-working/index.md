+++
type = "question"
title = "Capturing FTP on mirrored port not working"
description = '''Hi, We have Extreme switches in our environment and I&#x27;m trying to capture FTP traffic between a copier on my network and a file server.  I mirrored the copier port Plugged a laptop into the mirrored port Started Wireshark capture in promiscuous mode Scanned a document on the copier which opens and F...'''
date = "2015-09-23T11:29:00Z"
lastmod = "2015-09-23T13:05:00Z"
weight = 46084
keywords = [ "ftp", "mirroring", "extreme" ]
aliases = [ "/questions/46084" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing FTP on mirrored port not working](/questions/46084/capturing-ftp-on-mirrored-port-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46084-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>We have Extreme switches in our environment and I'm trying to capture FTP traffic between a copier on my network and a file server.</p><ul><li>I mirrored the copier port</li><li>Plugged a laptop into the mirrored port</li><li>Started Wireshark capture in promiscuous mode</li><li>Scanned a document on the copier which opens and FTP connection to our file server</li><li>No FTP traffic appears in the capture</li></ul><p>OK. Let's see if I Wireshark can pick up the FTP traffic natively from my laptop, with no port mirroring</p><ul><li>Opened Wireshark on my laptop ... capturing in promiscuous mode</li><li>established and FTP connection with the file server via CLI</li><li>Observed FTP protocol in Wireshark capture (Success!)</li></ul><p>OK. So it's not my config of Wireshark. It is picking up FTP traffic natively from my laptop. So let's mirror the port my laptop is in and try again</p><ul><li>I mirrored my laptop port on the swtich</li><li>Plugged a new laptop into the mirrored port</li><li>Opened Wireshark on the new laptop... capturing again in promiscuous mode</li><li>established an FTP connection from my laptop to the file server via CLI</li><li>No FTP traffic captured</li></ul><p>This leads me to believe that there is something about the mirroring process on my switches that is not sending FTP traffic to a mirrored port. I know not everyone has Extreme switches, but has anyone heard of such behavior in their own environments?</p><p>Thanks for listening and I appreciate any help.</p><p>Regards, Joe</p></div><div id="question-tags" class="tags-container tags">ftp mirroring extreme</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Sep '15, 11:29</strong></p><img src="https://secure.gravatar.com/avatar/b2cdf181f709cd05d5fa9afb725a7355?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JoeyJoeJoe1970&#39;s gravatar image" /><p>JoeyJoeJoe1970<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JoeyJoeJoe1970 has no accepted answers">0%</span></p></div></div><div id="comments-container-46084" class="comments-container"><span id="46086"></span><div id="comment-46086" class="comment"><div id="post-46086-score" class="comment-score"></div><div class="comment-text"><p>Do you see <strong>any</strong> traffic on that mirrored port?</p></div><div id="comment-46086-info" class="comment-info"><span class="comment-age">(23 Sep '15, 12:58)</span> Kurt Knochner ♦</div></div><span id="46087"></span><div id="comment-46087" class="comment"><div id="post-46087-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt.</p><p>Yes I see plenty of traffic coming through. Just no FTP protocol.</p></div><div id="comment-46087-info" class="comment-info"><span class="comment-age">(23 Sep '15, 13:01)</span> JoeyJoeJoe1970</div></div></div><div id="comment-tools-46084" class="comment-tools"></div><div class="clear"></div><div id="comment-46084-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46088"></span>

<div id="answer-container-46088" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46088-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Yes I see plenty of traffic coming through. Just no FTP protocol.</p></blockquote><p>well, then it's neither a problem with Wireshark nor a general problem with your port mirroring, so you should ask this question in a <a href="https://community.extremenetworks.com/extreme">Extreme Networks forum</a>, because your chances to get a usefull answer will be much higher.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '15, 13:05</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-46088" class="comments-container"></div><div id="comment-tools-46088" class="comment-tools"></div><div class="clear"></div><div id="comment-46088-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

