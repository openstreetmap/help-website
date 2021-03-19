+++
type = "question"
title = "Forensic Analysis (XMPP)"
description = '''Hi Guys, Is it possible to extract the files that are transferred captured under the XMPP/XML Protocol? I am able to see the filename and size, but i have no idea how to extract/rebuild the image. Here is the PCAP if you any of you are willing to help. Forensic Analysis - PCAP File Kind Regards, Sen'''
date = "2015-10-12T01:02:00Z"
lastmod = "2015-10-12T15:03:00Z"
weight = 46463
keywords = [ "xml", "xmpp", "forensic", "pcap", "analysis" ]
aliases = [ "/questions/46463" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Forensic Analysis (XMPP)](/questions/46463/forensic-analysis-xmpp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46463-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Guys,</p><p>Is it possible to extract the files that are transferred captured under the XMPP/XML Protocol?</p><p>I am able to see the filename and size, but i have no idea how to extract/rebuild the image.</p><p>Here is the PCAP if you any of you are willing to help.</p><p>Forensic Analysis - <a href="http://s000.tinyupload.com/?file_id=96317863518412042830">PCAP File</a></p><p>Kind Regards,</p><p>Sen</p></div><div id="question-tags" class="tags-container tags">xml xmpp forensic pcap analysis</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Oct '15, 01:02</strong></p><img src="https://secure.gravatar.com/avatar/2f4eda63b995c69c7693d10d31fab14c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sentral&#39;s gravatar image" /><p>sentral<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sentral has no accepted answers">0%</span></p></div></div><div id="comments-container-46463" class="comments-container"></div><div id="comment-tools-46463" class="comment-tools"></div><div class="clear"></div><div id="comment-46463-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46481"></span>

<div id="answer-container-46481" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46481-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is it possible to extract the files that are transferred captured under the XMPP/XML Protocol?</p></blockquote><p>Yes.</p><p>Description based on Wireshark 1.12.7. As there are only JPEGs in your pcap file, the following description is related to JPEG files (see remove bytes at the beginning of the file!).</p><p><strong>Step #1</strong>: Follow the TCP stream.</p><blockquote><p>tcp.stream eq 1</p></blockquote><p><strong>Step #2</strong>: right click any frame and select "Follow TCP Stream"<br />
<strong>Step #3</strong>: In the pop-up window, click "save as" and save the file to a directory<br />
<strong>Step #4</strong>: get a HEX editor, like <a href="http://mh-nexus.de/de/hxd/">HxD</a><br />
<strong>Step #5</strong>: open the saved file in the HEX editor<br />
<strong>Step #6</strong>: remove everything <strong>up to the 6 bytes</strong> in front of "JFIF"<br />
</p><p><img src="https://osqa-ask.wireshark.org/upfiles/ask_46463_screenshot_1.png" alt="alt text" /></p><p><strong>Step #7</strong>: save the file<br />
<strong>Step #8</strong>: Open the file with an image viewer.</p><p><strong>Hint</strong>: 'save as' in the pop-up of 'Follow TCP stream' in 1.99.x somehow cripples the file, so don't use 1.99.x!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Oct '15, 15:03</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 12 Oct '15, 15:05</p></div></div><div id="comments-container-46481" class="comments-container"><span id="46491"></span><div id="comment-46491" class="comment"><div id="post-46491-score" class="comment-score"></div><div class="comment-text"><p>Hey Kurt,</p><p>Thanks for your help!</p><p>Sen</p></div><div id="comment-46491-info" class="comment-info"><span class="comment-age">(13 Oct '15, 01:40)</span> sentral</div></div><span id="46495"></span><div id="comment-46495" class="comment"><div id="post-46495-score" class="comment-score"></div><div class="comment-text"><p>You're welcome!</p></div><div id="comment-46495-info" class="comment-info"><span class="comment-age">(13 Oct '15, 04:57)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-46481" class="comment-tools"></div><div class="clear"></div><div id="comment-46481-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

