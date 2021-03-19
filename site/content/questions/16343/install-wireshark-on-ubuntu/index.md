+++
type = "question"
title = "Install wireshark on Ubuntu"
description = '''Hi, Can we install wireshark on Ubuntu machine. Please share the download link if that is possible.'''
date = "2012-11-26T20:50:00Z"
lastmod = "2013-12-05T20:43:00Z"
weight = 16343
keywords = [ "ubuntu" ]
aliases = [ "/questions/16343" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Install wireshark on Ubuntu](/questions/16343/install-wireshark-on-ubuntu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16343-score" class="post-score" title="current number of votes">3</div><div id="favorite-count" class="favorite-count">2</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Can we install wireshark on Ubuntu machine. Please share the download link if that is possible.</p></div><div id="question-tags" class="tags-container tags">ubuntu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '12, 20:50</strong></p><img src="https://secure.gravatar.com/avatar/fe19ad71819c3b159a685c213cb9696d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gagandeep&#39;s gravatar image" /><p>Gagandeep<br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gagandeep has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Nov '12, 22:44</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-16343" class="comments-container"></div><div id="comment-tools-16343" class="comment-tools"></div><div class="clear"></div><div id="comment-16343-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27840"></span>

<div id="answer-container-27840" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27840-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>I was successful with the set of commands below:</p><pre><code>sudo apt-get install wireshark
sudo groupadd wireshark
sudo usermod -a -G wireshark YOUR_USER_NAME
sudo chgrp wireshark /usr/bin/dumpcap
sudo chmod 750 /usr/bin/dumpcap
sudo setcap cap_net_raw,cap_net_admin=eip /usr/bin/dumpcap
sudo getcap /usr/bin/dumpcap</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '13, 20:43</strong></p><img src="https://secure.gravatar.com/avatar/e6497f67a248956d28c81a2f3c263de5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Kroizman&#39;s gravatar image" /><p>Guy Kroizman<br />
<span class="score" title="81 reputation points">81</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Kroizman has no accepted answers">0%</span></p></div></div><div id="comments-container-27840" class="comments-container"><span id="27841"></span><div id="comment-27841" class="comment"><div id="post-27841-score" class="comment-score"></div><div class="comment-text"><p>Actually there is a better way: <code>sudo dpkg-reconfigure wireshark-common</code><br />
And then choose <code>Yes</code> for allowing non-superusers to be able to capture packages. Taken from here: <a href="http://askubuntu.com/a/74064/24409">http://askubuntu.com/a/74064/24409</a></p></div><div id="comment-27841-info" class="comment-info"><span class="comment-age">(05 Dec '13, 20:54)</span> Guy Kroizman</div></div><span id="28994"></span><div id="comment-28994" class="comment"><div id="post-28994-score" class="comment-score"></div><div class="comment-text"><p>Installed as recommended and when Wireshark starts up get:</p><p>Couldn't run /usr/bin/dumpcap in child process: Permission denied</p><p>~$ lsb_release -a No LSB modules are available. Distributor ID: Ubuntu Description: Ubuntu 12.04.4 LTS Release: 12.04 Codename: precise</p></div><div id="comment-28994-info" class="comment-info"><span class="comment-age">(17 Jan '14, 08:50)</span> ChiefDnd</div></div><span id="31117"></span><div id="comment-31117" class="comment"><div id="post-31117-score" class="comment-score"></div><div class="comment-text"><p>On Ubuntu 13.10, you need to log out and log back in for your new group memberships (i.e. joining the wireshark group) to take effect. I needed to do this in order to be able to execute /usr/bin/dumpcap (and this may have been your problem @ChiefDnd)</p></div><div id="comment-31117-info" class="comment-info"><span class="comment-age">(24 Mar '14, 08:51)</span> wgeorge</div></div><span id="35177"></span><div id="comment-35177" class="comment"><div id="post-35177-score" class="comment-score"></div><div class="comment-text"><p>Just went through this on Ubuntu 14.04 and found that even after doing the "sudo dpkg-reconfigure wireshark-common" and logging out and back in, I still wasn't in the wireshark group. I manually added myself by editing /etc/group and adding my username to the end of the wireshark line, then logged out and back in and then I was able to use wireshark OK.</p></div><div id="comment-35177-info" class="comment-info"><span class="comment-age">(04 Aug '14, 16:30)</span> Marnix</div></div><span id="35180"></span><div id="comment-35180" class="comment"><div id="post-35180-score" class="comment-score">1</div><div class="comment-text"><p>Please report this problem to the Ubuntu developers!</p></div><div id="comment-35180-info" class="comment-info"><span class="comment-age">(04 Aug '14, 23:02)</span> Kurt Knochner ♦</div></div><span id="53136"></span><div id="comment-53136" class="comment not_top_scorer"><div id="post-53136-score" class="comment-score"></div><div class="comment-text"><p>02/06/2016 and this bug still persist</p></div><div id="comment-53136-info" class="comment-info"><span class="comment-age">(02 Jun '16, 04:18)</span> razorborn</div></div><span id="53153"></span><div id="comment-53153" class="comment not_top_scorer"><div id="post-53153-score" class="comment-score"></div><div class="comment-text"><blockquote><p>02/06/2016 and this bug still persist</p></blockquote><p>As Kurt Knochner said, "Please report this problem to the Ubuntu developers!"</p></div><div id="comment-53153-info" class="comment-info"><span class="comment-age">(02 Jun '16, 11:35)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-27840" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-27840-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16344"></span>

<div id="answer-container-16344" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16344-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sure. You can install it from the Ubuntu Software center, or the Synaptic Package Manager or from the terminal by running the command: sudo apt-get install wireshark.</p><p>You can also install it from the source, you can download it from <a href="http://www.wireshark.org/download.html">this</a> link.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '12, 21:10</strong></p><img src="https://secure.gravatar.com/avatar/46196bc495ce51058590c4e4ae334d22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SidR&#39;s gravatar image" /><p>SidR<br />
<span class="score" title="245 reputation points">245</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SidR has 3 accepted answers">30%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Nov '12, 21:11</p></div></div><div id="comments-container-16344" class="comments-container"></div><div id="comment-tools-16344" class="comment-tools"></div><div class="clear"></div><div id="comment-16344-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

