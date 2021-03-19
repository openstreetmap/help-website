+++
type = "question"
title = "linux remote capture GUI"
description = '''Hi all,  Has anyone successfully compiled wireshark 1.12.9 / 2.0.1 on linux with winpcap 4.1.3 and got a fully functional GUI working against rpcapd ? I manage to compile and get the remote interface Tab, I see the remote interfaces and manage to &quot;start&quot; a remote capture, but no packets arrive. From...'''
date = "2016-02-14T04:05:00Z"
lastmod = "2016-02-14T04:05:00Z"
weight = 50181
keywords = [ "capture", "remote", "winpcap", "linux" ]
aliases = [ "/questions/50181" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [linux remote capture GUI](/questions/50181/linux-remote-capture-gui)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50181-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, Has anyone successfully compiled wireshark 1.12.9 / 2.0.1 on linux with winpcap 4.1.3 and got a fully functional GUI working against rpcapd ?</p><p>I manage to compile and get the remote interface Tab, I see the remote interfaces and manage to "start" a remote capture, but no packets arrive. From looking at the generated TCP control packets, no "start" command is sent to the capture server. Thanks,</p></div><div id="question-tags" class="tags-container tags">capture remote winpcap linux</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Feb '16, 04:05</strong></p><img src="https://secure.gravatar.com/avatar/6e2c5f84ce49ffecda70f389fc5f5b50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yaniv_rad&#39;s gravatar image" /><p>yaniv_rad<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yaniv_rad has no accepted answers">0%</span></p></div></div><div id="comments-container-50181" class="comments-container"><span id="50184"></span><div id="comment-50184" class="comment"><div id="post-50184-score" class="comment-score"></div><div class="comment-text"><p>GTK or Qt interface?</p></div><div id="comment-50184-info" class="comment-info"><span class="comment-age">(14 Feb '16, 07:25)</span> Jaap ♦</div></div><span id="50194"></span><div id="comment-50194" class="comment"><div id="post-50194-score" class="comment-score"></div><div class="comment-text"><p>I used GTK2, but the problem doesn't seem with the GUI. The remote interface tab is present and the functionality of finding the remote capture device works. The problem is with the execution of the RPCAP protocol. I see the enumeration of the interfaces, the "authentication" message and the interface "open" message. The missing part is a "start" message to tell the remote capture device to start sending the captured packets.</p></div><div id="comment-50194-info" class="comment-info"><span class="comment-age">(14 Feb '16, 21:24)</span> yaniv_rad</div></div></div><div id="comment-tools-50181" class="comment-tools"></div><div class="clear"></div><div id="comment-50181-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

