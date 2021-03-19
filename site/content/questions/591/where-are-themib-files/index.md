+++
type = "question"
title = "Where are theMIB Files"
description = '''The Wireshark book talks about MIB files in the installation Directory: Wiresharksnmpmibs However, I do not see this directory in my Windows Wireshark 4.1 installation. If I want to add more MIBs should I create this directory? Where are the MIB&#x27;s that are supposed to be in the installation.'''
date = "2010-10-22T15:26:00Z"
lastmod = "2010-10-22T15:49:00Z"
weight = 591
keywords = [ "mib", "snmp" ]
aliases = [ "/questions/591" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Where are theMIB Files](/questions/591/where-are-themib-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-591-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The Wireshark book talks about MIB files in the installation Directory: Wiresharksnmpmibs However, I do not see this directory in my Windows Wireshark 4.1 installation. If I want to add more MIBs should I create this directory? Where are the MIB's that are supposed to be in the installation.</p></div><div id="question-tags" class="tags-container tags">mib snmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Oct '10, 15:26</strong></p><img src="https://secure.gravatar.com/avatar/c3bd1443d5ce7c6fbcb0e450a31f84b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vmjr&#39;s gravatar image" /><p>vmjr<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vmjr has one accepted answer">100%</span></p></div></div><div id="comments-container-591" class="comments-container"></div><div id="comment-tools-591" class="comment-tools"></div><div class="clear"></div><div id="comment-591-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="597"></span>

<div id="answer-container-597" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-597-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I did a complete uninstall, I have been upgrading for some time, and had delete the director manually. ON the re-install the directory and the files were there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '10, 15:49</strong></p><img src="https://secure.gravatar.com/avatar/c3bd1443d5ce7c6fbcb0e450a31f84b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vmjr&#39;s gravatar image" /><p>vmjr<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vmjr has one accepted answer">100%</span></p></div></div><div id="comments-container-597" class="comments-container"><span id="598"></span><div id="comment-598" class="comment"><div id="post-598-score" class="comment-score"></div><div class="comment-text"><p>Great!!! Just noticed this forum removes the backslashes by default - so should be snmp[backslash]mibs.</p></div><div id="comment-598-info" class="comment-info"><span class="comment-age">(22 Oct '10, 16:40)</span> lchappell ♦</div></div></div><div id="comment-tools-597" class="comment-tools"></div><div class="clear"></div><div id="comment-597-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="593"></span>

<div id="answer-container-593" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-593-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The directory is snmpmibs. Select Help &gt; About Wireshark &gt; Folders to find your global configuration directory. This is the directory your snmpmibs directory should be under.</p><p>"There are over 300 MIBs in Wireshark’s snmpmibs folder as of Wireshark v1.4. Additional SNMP MIBs can be found at www.mibdepot.com or www.oidview.com/mibs/detail.html."</p><p>For details on formatting, naming and adding MIBs, refer to wiki.wireshark.org/SNMP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '10, 15:35</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p>lchappell ♦<br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-593" class="comments-container"><span id="595"></span><div id="comment-595" class="comment"><div id="post-595-score" class="comment-score"></div><div class="comment-text"><p>Laura - thanks for your quick response. Maybe I'll try a reinstall. My Global Configuration location is C;ProgramFilesWireshark and there is no snmp or snmpmibs directory.</p></div><div id="comment-595-info" class="comment-info"><span class="comment-age">(22 Oct '10, 15:40)</span> vmjr</div></div></div><div id="comment-tools-593" class="comment-tools"></div><div class="clear"></div><div id="comment-593-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

