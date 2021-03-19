+++
type = "question"
title = "Question about building wireshark and runtime options"
description = '''Hi, Have two questions require your advise Question1: Trying to build wireshark in SLES11 Linux (SP3). Having issues where my old build directory (wireshark1) is used for plugins and selected in the &quot;Global Configuration Folder&quot;. I am using the &quot;--prefix&quot; option to select a desired destination direc...'''
date = "2016-08-03T06:25:00Z"
lastmod = "2016-08-03T06:25:00Z"
weight = 54554
keywords = [ "capture", "build", "wireshark" ]
aliases = [ "/questions/54554" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Question about building wireshark and runtime options](/questions/54554/question-about-building-wireshark-and-runtime-options)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54554-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Have two questions require your advise</p><p><strong>Question1:</strong> Trying to build wireshark in SLES11 Linux (SP3). Having issues where my old build directory (wireshark1) is used for plugins and selected in the "Global Configuration Folder". I am using the "--prefix" option to select a desired destination directory, but no luck. Below is the commands I used</p><p>./configure --prefix=/opt/wireshark2 --with-ssl=/usr/local/ssl --with-lua --enable-setuid-install --with-gtk=2 --without-qt --with-extcap=no --enable-warnings-as-errors=no</p><p>make -j 8</p><p>make install</p><p><strong>Question2:</strong> I am running the wireshark application on a HP DL380 G8 server with capture interface 10Gig fiber. Would like to know the best possible settings/switches so that I get optimum real time capture performance. I use wireshark GTK to open and run traces in realtime</p></div><div id="question-tags" class="tags-container tags">capture build wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Aug '16, 06:25</strong></p><img src="https://secure.gravatar.com/avatar/4a2a1ab8f8fa05aa1d21e5b43f767aae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sshark&#39;s gravatar image" /><p>sshark<br />
<span class="score" title="6 reputation points">6</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sshark has no accepted answers">0%</span></p></div></div><div id="comments-container-54554" class="comments-container"><span id="54780"></span><div id="comment-54780" class="comment"><div id="post-54780-score" class="comment-score"></div><div class="comment-text"><p>Any recommendations</p></div><div id="comment-54780-info" class="comment-info"><span class="comment-age">(13 Aug '16, 07:02)</span> sshark</div></div></div><div id="comment-tools-54554" class="comment-tools"></div><div class="clear"></div><div id="comment-54554-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

