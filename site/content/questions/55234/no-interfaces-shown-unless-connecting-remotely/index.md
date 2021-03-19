+++
type = "question"
title = "No interfaces shown unless connecting remotely"
description = '''I&#x27;ve come across a strange situation on OS X Mavericks that I don&#x27;t understand. If I log into my server running Mavericks locally using my general admin account (a local account with standard administrator privileges) and start Wireshark it finds no interfaces. This is not a surprise as I&#x27;ve done no...'''
date = "2016-08-31T06:18:00Z"
lastmod = "2016-08-31T06:18:00Z"
weight = 55234
keywords = [ "interfaces", "remote-login", "mavericks" ]
aliases = [ "/questions/55234" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [No interfaces shown unless connecting remotely](/questions/55234/no-interfaces-shown-unless-connecting-remotely)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55234-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've come across a strange situation on OS X Mavericks that I don't understand.</p><p>If I log into my server running Mavericks locally using my general admin account (a local account with standard administrator privileges) and start Wireshark it finds no interfaces. This is not a surprise as I've done nothing to give this user rights over the interface files.</p><p>If I reboot the machine and open a screen sharing session from another Mac (using the same admin account) then login to the server (again using the same account) and start Wireshark it immediately finds the active network interface and loopback.</p><p>Can anyone explain why this might happen? I've repeated this a number of times to make sure I'm not imagining it and the results are the same every time. Login via screen sharing and interfaces are found, don't use screen sharing and none are found.</p></div><div id="question-tags" class="tags-container tags">interfaces remote-login mavericks</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Aug '16, 06:18</strong></p><img src="https://secure.gravatar.com/avatar/7954ca09fd2f94a072ba890c80c14f18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kaulmain&#39;s gravatar image" /><p>kaulmain<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kaulmain has no accepted answers">0%</span></p></div></div><div id="comments-container-55234" class="comments-container"><span id="55240"></span><div id="comment-55240" class="comment"><div id="post-55240-score" class="comment-score"></div><div class="comment-text"><p>What's that with rebooting the machine? When do you do that?</p></div><div id="comment-55240-info" class="comment-info"><span class="comment-age">(31 Aug '16, 07:42)</span> Jaap ♦</div></div><span id="55254"></span><div id="comment-55254" class="comment"><div id="post-55254-score" class="comment-score"></div><div class="comment-text"><p>The rebooting is just to make sure I am starting the tests from exactly the same point. So the reboot is done before both of the tests described. I've tried with both reboot and shutting down for a cold boot.</p><p>reboot - local login - wireshark = no interfaces found</p><p>reboot - login via screen sharing - wireshark = interfaces found</p></div><div id="comment-55254-info" class="comment-info"><span class="comment-age">(31 Aug '16, 14:24)</span> kaulmain</div></div></div><div id="comment-tools-55234" class="comment-tools"></div><div class="clear"></div><div id="comment-55234-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

