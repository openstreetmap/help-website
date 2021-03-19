+++
type = "question"
title = "How to upgrade wireshark on CentOS 5.4 in order to resolve TLS dissector and decrypt issue."
description = '''Hi , Currenty we are using 1.0.15 wireshark version on our Centos 5.4 machine. With the current installed wireshark version(1.0.15) we are not able dissect ssl packet flows. Only Client hello are getting dessected.  Alse we are not able to decrypt the TLS encrypted data. SO we thought to upgrade the...'''
date = "2016-05-24T23:59:00Z"
lastmod = "2016-05-25T06:35:00Z"
weight = 52896
keywords = [ "installation", "wireshark" ]
aliases = [ "/questions/52896" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to upgrade wireshark on CentOS 5.4 in order to resolve TLS dissector and decrypt issue.](/questions/52896/how-to-upgrade-wireshark-on-centos-54-in-order-to-resolve-tls-dissector-and-decrypt-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52896-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi ,</p><p>Currenty we are using 1.0.15 wireshark version on our Centos 5.4 machine. With the current installed wireshark version(1.0.15) we are not able dissect ssl packet flows. Only Client hello are getting dessected. Alse we are not able to decrypt the TLS encrypted data.</p><p>SO we thought to upgrade the Wireshark version to resolve the above said 2 issues. Yum install wireshark - not pulling the latest version.</p><p>Hence please help us to install Latest Version supported on CentOS 5.4. Please point us the Installation package. Tried Lates version source code but again its looking for lot of dependcies.</p><p>Please Help.</p></div><div id="question-tags" class="tags-container tags">installation wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 May '16, 23:59</strong></p><img src="https://secure.gravatar.com/avatar/df4dab12d9437bfe0ef8981b3526b069?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dhanish&#39;s gravatar image" /><p>dhanish<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dhanish has no accepted answers">0%</span></p></div></div><div id="comments-container-52896" class="comments-container"></div><div id="comment-tools-52896" class="comment-tools"></div><div class="clear"></div><div id="comment-52896-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52910"></span>

<div id="answer-container-52910" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52910-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>According to the <a href="https://wiki.wireshark.org/Development/LifeCycle">LifeCycle</a> page Wireshark 1.6 is the last version that will compile on RHEL 5. So you'll need to download and compile the <a href="https://www.wireshark.org/download/src/all-versions/">1.6.16 source code</a>. Yes, you'll need to sort out all the development dependencies (lost of <code>*-devel</code> packages) but these should all be available from RH's RPM repositories.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 May '16, 06:35</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-52910" class="comments-container"><span id="52951"></span><div id="comment-52951" class="comment"><div id="post-52951-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jeff ! Yes am able to Compile and Install. While compiling i installed libcap-devel.x86_64. One more question though, AM able open new version 1.6.16 from desktop-applications-internet-wireshark.</p><p>But at the same time when i open wireshark from terminal by typing 'wireshark' its opening the old version. Its not sourcing new one.</p><p>How can i resolve this.</p><p>Please Help !</p><p>Thanks, Dhanish</p></div><div id="comment-52951-info" class="comment-info"><span class="comment-age">(26 May '16, 02:44)</span> dhanish</div></div><span id="52955"></span><div id="comment-52955" class="comment"><div id="post-52955-score" class="comment-score"></div><div class="comment-text"><p>Uninstall the old one? Your newly build Wireshark is probably installed in /usr/local, which may not be on your path. If so you'll need to add that to your path before being able to use from the command line (without absolute path).</p></div><div id="comment-52955-info" class="comment-info"><span class="comment-age">(26 May '16, 04:48)</span> Jaap ♦</div></div></div><div id="comment-tools-52910" class="comment-tools"></div><div class="clear"></div><div id="comment-52910-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

