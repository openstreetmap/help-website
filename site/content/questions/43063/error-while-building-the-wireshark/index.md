+++
type = "question"
title = "Error while building the wireshark"
description = '''I was trying to bulid the wireshark version(1.12). when i run the command (nmake -f Makefile.nmake all) I got this error. why ? if exist tshark.exe xcopy tshark.exe wireshark-gtk2 /d C:tshark.exe 1 File(s) copied if exist tshark.pdb xcopy tshark.pdb wireshark-gtk2 /d C:tshark.pdb  1 File(s) copied  ...'''
date = "2015-06-11T02:28:00Z"
lastmod = "2015-06-11T02:48:00Z"
weight = 43063
keywords = [ "development", "problem", "dissector", "wireshark" ]
aliases = [ "/questions/43063" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Error while building the wireshark](/questions/43063/error-while-building-the-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43063-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was trying to bulid the wireshark version(1.12). when i run the command (nmake -f Makefile.nmake all) I got this error. why ?</p><pre><code>if exist tshark.exe xcopy tshark.exe wireshark-gtk2 /d
C:tshark.exe
1 File(s) copied
if exist tshark.pdb xcopy tshark.pdb wireshark-gtk2 /d
C:tshark.pdb
 1 File(s) copied
    xcopy &quot;doc\AUTHORS-SHORT&quot; wireshark-gtk2 /d
 0 File(s) copied
    xcopy &quot;.\manuf&quot; wireshark-gtk2 /d
 0 File(s) copied
    xcopy &quot;.\services&quot; wireshark-gtk2 /d
 0 File(s) copied
    xcopy &quot;.\pdml2html.xsl&quot; wireshark-gtk2 /d
 0 File(s) copied
    bash  tools/textify.sh &quot;./COPYING&quot; wireshark-gtk2
  tools/textify.sh: line 68: u2d: command not found
  NMAKE : fatal error U1077: &#39;C:\cygwin64\bin\bash.EXE&#39; : return code &#39;0x7f&#39;
  Stop.</code></pre><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">development problem dissector wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jun '15, 02:28</strong></p><img src="https://secure.gravatar.com/avatar/ea74f093a0efe137c7c114da864fa5cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sammee%20Sharma&#39;s gravatar image" /><p>Sammee Sharma<br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sammee Sharma has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Jun '15, 02:39</p></div></div><div id="comments-container-43063" class="comments-container"></div><div id="comment-tools-43063" class="comment-tools"></div><div class="clear"></div><div id="comment-43063-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43064"></span>

<div id="answer-container-43064" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43064-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Got it. I needed to download one package (unix2dos ) from cygwin . it worked. :)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '15, 02:48</strong></p><img src="https://secure.gravatar.com/avatar/ea74f093a0efe137c7c114da864fa5cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sammee%20Sharma&#39;s gravatar image" /><p>Sammee Sharma<br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sammee Sharma has one accepted answer">100%</span></p></div></div><div id="comments-container-43064" class="comments-container"><span id="43066"></span><div id="comment-43066" class="comment"><div id="post-43066-score" class="comment-score"></div><div class="comment-text"><p>I don't see this mentioned in the Developers Guide. Can you please raise an item at the <a href="https://bugs.wireshark.org/bugzilla/">Wireshark Bugzilla</a> so it get's fixed?</p></div><div id="comment-43066-info" class="comment-info"><span class="comment-age">(11 Jun '15, 03:12)</span> grahamb ♦</div></div><span id="43067"></span><div id="comment-43067" class="comment"><div id="post-43067-score" class="comment-score"></div><div class="comment-text"><p>@grahamb sir,okk.. but when i tried to build wireshark version(1.99) this error did not come but now i'm trying to build version (1.12 ), then this error came .</p></div><div id="comment-43067-info" class="comment-info"><span class="comment-age">(11 Jun '15, 04:05)</span> Sammee Sharma</div></div><span id="43068"></span><div id="comment-43068" class="comment"><div id="post-43068-score" class="comment-score"></div><div class="comment-text"><p>Where should i file the bug either on websites or wireshark ?</p></div><div id="comment-43068-info" class="comment-info"><span class="comment-age">(11 Jun '15, 04:10)</span> Sammee Sharma</div></div><span id="43070"></span><div id="comment-43070" class="comment"><div id="post-43070-score" class="comment-score"></div><div class="comment-text"><p>I've raised it on web sites. is it ok ?</p></div><div id="comment-43070-info" class="comment-info"><span class="comment-age">(11 Jun '15, 04:19)</span> Sammee Sharma</div></div><span id="43091"></span><div id="comment-43091" class="comment not_top_scorer"><div id="post-43091-score" class="comment-score"></div><div class="comment-text"><p>@grahamb , Why do we need to install QT in order to build the wireshark as per the developer's guide ?</p></div><div id="comment-43091-info" class="comment-info"><span class="comment-age">(12 Jun '15, 02:03)</span> Sammee Sharma</div></div><span id="43092"></span><div id="comment-43092" class="comment"><div id="post-43092-score" class="comment-score">1</div><div class="comment-text"><p>Wireshark is moving from being a GTK based application to a QT based application. See Gerald's blog <a href="https://blog.wireshark.org/2013/10/switching-to-qt/">post</a> for more info.</p><p>During the transition the build environment is set to build both GTK and QT versions. Once the QT version is feature compatible with the GTK version then it's likely we'll start to deprecate the GTK version.</p></div><div id="comment-43092-info" class="comment-info"><span class="comment-age">(12 Jun '15, 03:11)</span> grahamb ♦</div></div></div><div id="comment-tools-43064" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-43064-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

