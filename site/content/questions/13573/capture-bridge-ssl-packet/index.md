+++
type = "question"
title = "capture bridge SSL packet"
description = '''I use linux SSL server with non priviledged port in virtualbox. Virtualbox use bridge network. SSL client use a hub to connect to SSL server. I use wireshark to capture packet. But I didn&#x27;t find any packet from linux or SSL client. Why? setting problem?'''
date = "2012-08-13T02:54:00Z"
lastmod = "2012-08-13T02:54:00Z"
weight = 13573
keywords = [ "ssl", "openssl", "bridge" ]
aliases = [ "/questions/13573" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [capture bridge SSL packet](/questions/13573/capture-bridge-ssl-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13573-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I use linux SSL server with non priviledged port in virtualbox. Virtualbox use bridge network. SSL client use a hub to connect to SSL server. I use wireshark to capture packet. But I didn't find any packet from linux or SSL client. Why? setting problem?</p></div><div id="question-tags" class="tags-container tags">ssl openssl bridge</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Aug '12, 02:54</strong></p><img src="https://secure.gravatar.com/avatar/c43facb76182ec08055fa1d21ac4ddc7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eugene&#39;s gravatar image" /><p>eugene<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eugene has no accepted answers">0%</span></p></div></div><div id="comments-container-13573" class="comments-container"><span id="13574"></span><div id="comment-13574" class="comment"><div id="post-13574-score" class="comment-score"></div><div class="comment-text"><p>On which machine and on which interface where you making the capture? Did you have any capture filters?</p><p>A simple diagram of your setup would help.</p></div><div id="comment-13574-info" class="comment-info"><span class="comment-age">(13 Aug '12, 03:05)</span> grahamb ♦</div></div><span id="13575"></span><div id="comment-13575" class="comment"><div id="post-13575-score" class="comment-score"></div><div class="comment-text"><p>I did capture on a windows 192.168.1.4,and installed virtualbox with linux 192.168.1.2. SSL client use 192.168.1.70. I didn't set any filter and capture all interfaces</p></div><div id="comment-13575-info" class="comment-info"><span class="comment-age">(13 Aug '12, 03:17)</span> eugene</div></div><span id="13576"></span><div id="comment-13576" class="comment"><div id="post-13576-score" class="comment-score"></div><div class="comment-text"><p>So you have an SSL client on an unknown OS on .70 connected via a hub to a windows host pc on .4 and a linux ssh server on .2 in a VB VM.</p><p>On which machine did you make the capture, the SSL client, the Windows host or the Linux SSH server?</p></div><div id="comment-13576-info" class="comment-info"><span class="comment-age">(13 Aug '12, 03:25)</span> grahamb ♦</div></div><span id="13601"></span><div id="comment-13601" class="comment"><div id="post-13601-score" class="comment-score"></div><div class="comment-text"><p>windows host capture packet. SSL client is a linux host.</p></div><div id="comment-13601-info" class="comment-info"><span class="comment-age">(13 Aug '12, 17:47)</span> eugene</div></div></div><div id="comment-tools-13573" class="comment-tools"></div><div class="clear"></div><div id="comment-13573-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

