+++
type = "question"
title = "Wireshark and Fedora"
description = '''Dear Sir, I have downloaded and installed Wireshark on my netbook running Fedora 15, using the command: &quot;yum install wireshark-gnome&quot;. It has intalled with no errors. Though, when I run the program, it freezes, and I get the following message &quot;couldnt run /usr/sbin/dumpcap in child process: permissi...'''
date = "2011-08-11T19:32:00Z"
lastmod = "2014-01-17T15:10:00Z"
weight = 5660
keywords = [ "fedora" ]
aliases = [ "/questions/5660" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark and Fedora](/questions/5660/wireshark-and-fedora)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5660-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5660-score" class="post-score" title="current number of votes">0</div><span id="post-5660-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear Sir, I have downloaded and installed Wireshark on my netbook running Fedora 15, using the command: "yum install wireshark-gnome". It has intalled with no errors. Though, when I run the program, it freezes, and I get the following message "couldnt run /usr/sbin/dumpcap in child process: permission denied. Are you member of 'wireshark' group? Try running 'usermod -a -G wireshark username as root". I'm not member of Wireshark, and I didn't need it to run in Windows 7. Could you explain what does it mean? I'm a newcommer in Linux. Thanks in advance! Stilson (from Brazil, e-mail: <span class="__cf_email__" data-cfemail="017275686d726e6f2f776473607241666c60686d2f626e6c">[email protected]</span>)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fedora" rel="tag" title="see questions tagged &#39;fedora&#39;">fedora</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Aug '11, 19:32</strong></p><img src="https://secure.gravatar.com/avatar/f944fbf945979d72022a2c02a3334cd5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stilson&#39;s gravatar image" /><p><span>stilson</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stilson has no accepted answers">0%</span></p></div></div><div id="comments-container-5660" class="comments-container"></div><div id="comment-tools-5660" class="comment-tools"></div><div class="clear"></div><div id="comment-5660-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="5663"></span>

<div id="answer-container-5663" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5663-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5663-score" class="post-score" title="current number of votes">2</div><span id="post-5663-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See the <a href="http://docs.fedoraproject.org/en-US/Fedora/15/html/Release_Notes/sect-Release_Notes-Changes_for_Desktop_Users.html">Fedora15 Release Notes</a></p><p>Quote:</p><p>2.3.3. Wireshark permissions changes Wireshark in Fedora 15 uses Linux capabilities instead of console helper. As result, the Wireshark users are no longer required to enter the root password. To grant a user permission to capture network traffic using Wireshark or tshark, the system administrator should add the user to wireshark group. The Wireshark or tshark application then runs as ordinary user, only the capturing backend runs with permission to sniff on the network.</p><p>So: It sounds like you need to do the "usermod ..." command as suggested.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Aug '11, 19:51</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Aug '11, 19:53</strong> </span></p></div></div><div id="comments-container-5663" class="comments-container"><span id="5664"></span><div id="comment-5664" class="comment"><div id="post-5664-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much!</p></div><div id="comment-5664-info" class="comment-info"><span class="comment-age">(11 Aug '11, 20:24)</span> <span class="comment-user userinfo">stilson</span></div></div><span id="5666"></span><div id="comment-5666" class="comment"><div id="post-5666-score" class="comment-score"></div><div class="comment-text"><p>(I've converted your Answer to a comment as per the convention for ask.wireshark.org. See the FAQ)</p></div><div id="comment-5666-info" class="comment-info"><span class="comment-age">(11 Aug '11, 20:45)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="15197"></span><div id="comment-15197" class="comment"><div id="post-15197-score" class="comment-score"></div><div class="comment-text"><p>This did not work in my case. My user is in the wireshark group after running as root:</p><p>usermod -a -G wireshark _your_username</p><p>/etc/group shows</p><p>wireshark:x:482:_my_user_name</p><p>What gives?</p></div><div id="comment-15197-info" class="comment-info"><span class="comment-age">(23 Oct '12, 10:57)</span> <span class="comment-user userinfo">UdaMan</span></div></div><span id="15201"></span><div id="comment-15201" class="comment"><div id="post-15201-score" class="comment-score"></div><div class="comment-text"><p><span>@UdaMan</span>, did you try logging off and on again?</p></div><div id="comment-15201-info" class="comment-info"><span class="comment-age">(23 Oct '12, 14:35)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-5663" class="comment-tools"></div><div class="clear"></div><div id="comment-5663-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15214"></span>

<div id="answer-container-15214" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15214-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15214-score" class="post-score" title="current number of votes">0</div><span id="post-15214-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I had the same problem and I just changed the owner of /usr/sbin/dumpcap with "sudo chown [yourusername] /usr/sbin/dumpcap" and that helped.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Oct '12, 01:59</strong></p><img src="https://secure.gravatar.com/avatar/bd4e5a8da561e4305bc2a06569e388db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JacKal&#39;s gravatar image" /><p><span>JacKal</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JacKal has no accepted answers">0%</span></p></div></div><div id="comments-container-15214" class="comments-container"><span id="15217"></span><div id="comment-15217" class="comment"><div id="post-15217-score" class="comment-score"></div><div class="comment-text"><p>As long as there are no other users on the system hoping to use dumpcap that would work, but it's not the recommended solution.</p></div><div id="comment-15217-info" class="comment-info"><span class="comment-age">(24 Oct '12, 02:38)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="15218"></span><div id="comment-15218" class="comment"><div id="post-15218-score" class="comment-score"></div><div class="comment-text"><p>ahh.. now I understand!</p></div><div id="comment-15218-info" class="comment-info"><span class="comment-age">(24 Oct '12, 03:54)</span> <span class="comment-user userinfo">JacKal</span></div></div></div><div id="comment-tools-15214" class="comment-tools"></div><div class="clear"></div><div id="comment-15214-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="29004"></span>

<div id="answer-container-29004" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29004-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29004-score" class="post-score" title="current number of votes">0</div><span id="post-29004-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I had the same problem as UdaMan. I added myself to the wireshark:x:490: group in /etc/. Even after logging out and in I receive the same error as documented by the original poster. When I ran the command: ls -l /usr/sbin/dumpcap I received the following output:</p><p>-rwxr-x---. 1 root 489 65216 May 23 2012 /usr/sbin/dumpcap</p><p>Seeing the GID for the dumpcap command was 489, I changed the GID for the wireshark group in /etc/group from 490 to 489 (note: 489 was not used by any other group). This fixed the problem.</p><p>So there appears to be a bug in the wireshark install package.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jan '14, 15:10</strong></p><img src="https://secure.gravatar.com/avatar/b0006076f7a8b0e82ed822efafa0d2f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ted_jane&#39;s gravatar image" /><p><span>ted_jane</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ted_jane has no accepted answers">0%</span></p></div></div><div id="comments-container-29004" class="comments-container"></div><div id="comment-tools-29004" class="comment-tools"></div><div class="clear"></div><div id="comment-29004-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

