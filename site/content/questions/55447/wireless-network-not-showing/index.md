+++
type = "question"
title = "Wireless Network NOT SHOWING!"
description = '''Hello, I installed wireshark through ubuntu using a set of terminal commands.  When I open the interface list, I cannot find the option to sniff through my wireless network. I heard that I need to install winPCAP or something? But that is for windows only. Please help, I need this for an assignment ...'''
date = "2016-09-09T14:24:00Z"
lastmod = "2016-09-09T14:24:00Z"
weight = 55447
keywords = [ "linux", "networking", "wireshark", "ubuntu" ]
aliases = [ "/questions/55447" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireless Network NOT SHOWING!](/questions/55447/wireless-network-not-showing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55447-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I installed wireshark through ubuntu using a set of terminal commands.</p><p>When I open the interface list, I cannot find the option to sniff through my wireless network. I heard that I need to install winPCAP or something? But that is for windows only.</p><p>Please help, I need this for an assignment and currently I cannot find a solution.</p></div><div id="question-tags" class="tags-container tags">linux networking wireshark ubuntu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Sep '16, 14:24</strong></p><img src="https://secure.gravatar.com/avatar/27e181ea31a62600c2c08d1e5c1c0033?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alex067&#39;s gravatar image" /><p>alex067<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alex067 has no accepted answers">0%</span></p></div></div><div id="comments-container-55447" class="comments-container"><span id="55449"></span><div id="comment-55449" class="comment"><div id="post-55449-score" class="comment-score"></div><div class="comment-text"><p>Can you see any network interfaces at all in the interface list? And are there any active network interfaces other than the wireless one in your system?</p><p>Can you post here the output of <code>tshark -D</code> command issued in a terminal window?</p></div><div id="comment-55449-info" class="comment-info"><span class="comment-age">(09 Sep '16, 14:51)</span> sindy</div></div><span id="55451"></span><div id="comment-55451" class="comment"><div id="post-55451-score" class="comment-score"></div><div class="comment-text"><p>I can see some interfaces but nothing pertaining to like wireless network.</p><p>When I did tshark -D it says I don't have tshark installed, is it something I need?</p></div><div id="comment-55451-info" class="comment-info"><span class="comment-age">(09 Sep '16, 17:55)</span> alex067</div></div><span id="55452"></span><div id="comment-55452" class="comment"><div id="post-55452-score" class="comment-score"></div><div class="comment-text"><p>I installed tshark and this is what came up when I did the comand: 1. eth0 2. any 3. lo (Loopback) 4. bluetooth-monitor 5. nflog 6. nfqueue 7. usbmon1</p><p>None of them have any packets going through</p></div><div id="comment-55452-info" class="comment-info"><span class="comment-age">(09 Sep '16, 18:07)</span> alex067</div></div><span id="55455"></span><div id="comment-55455" class="comment"><div id="post-55455-score" class="comment-score"></div><div class="comment-text"><p>The reason why I've asked you for the list of interfaces was to find out whether it is an issue of user privileges (which would mean that none of the interfaces otherwise existing in the system would be shown in Wireshark or tshark) or something specific to the wireless interface.</p><p>There are several reasons why I've asked for tshark output:</p><ul><li><p>it is easier for you to copy-paste a text output</p></li><li><p>this site doesn't handle pictures in Comments well</p></li><li><p>it is easier for me to give you the command line options than to tell you where to click...</p></li></ul><p>What version of Wireshark have you installed?</p><p>Are you specifically interested in the wireless interface because you have no wired Ethernet device to connect to your eth0 or because the assignment relates to monitoring 3rd party traffic, i.e. one not originating or terminating in your machine?</p></div><div id="comment-55455-info" class="comment-info"><span class="comment-age">(09 Sep '16, 22:50)</span> sindy</div></div></div><div id="comment-tools-55447" class="comment-tools"></div><div class="clear"></div><div id="comment-55447-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

