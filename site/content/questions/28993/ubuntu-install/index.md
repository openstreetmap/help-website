+++
type = "question"
title = "Ubuntu Install"
description = '''Installed as recommended and when Wireshark starts up get: Couldn&#x27;t run /usr/bin/dumpcap in child process: Permission denied ~$ lsb_release -a No LSB modules are available. Distributor ID: Ubuntu Description: Ubuntu 12.04.4 LTS Release: 12.04 Codename: precise '''
date = "2014-01-17T08:43:00Z"
lastmod = "2014-01-17T09:22:00Z"
weight = 28993
keywords = [ "ubuntu" ]
aliases = [ "/questions/28993" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Ubuntu Install](/questions/28993/ubuntu-install)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28993-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Installed as recommended and when Wireshark starts up get:</p><p>Couldn't run /usr/bin/dumpcap in child process: Permission denied</p><pre><code>~$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 12.04.4 LTS
Release:    12.04
Codename:   precise</code></pre></div><div id="question-tags" class="tags-container tags">ubuntu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jan '14, 08:43</strong></p><img src="https://secure.gravatar.com/avatar/f0861df562eaf3998e456b09b6502b2a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChiefDnd&#39;s gravatar image" /><p>ChiefDnd<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChiefDnd has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Nov '15, 16:42</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-28993" class="comments-container"><span id="47593"></span><div id="comment-47593" class="comment"><div id="post-47593-score" class="comment-score"></div><div class="comment-text"><p>What does <code>ls -l /usr/bin/dumpcap</code> print?</p></div><div id="comment-47593-info" class="comment-info"><span class="comment-age">(13 Nov '15, 16:42)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-28993" class="comment-tools"></div><div class="clear"></div><div id="comment-28993-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28996"></span>

<div id="answer-container-28996" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28996-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Did you issue those commands?</p><ul><li>sudo addgroup -system wireshark</li><li>sudo chown root:wireshark /usr/bin/dumpcap</li><li>sudo setcap cap_net_raw,cap_net_admin=eip /usr/bin/dumpcap</li><li>sudo usermod -a -G wireshark YOUR_USER_NAME</li></ul><p>worekd for me ... See <a href="http://cmc.site11.com/2011/08/ubuntu-10-10-wireshark-no-interfaces-available-solved/">http://cmc.site11.com/2011/08/ubuntu-10-10-wireshark-no-interfaces-available-solved/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jan '14, 09:22</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-28996" class="comments-container"><span id="28999"></span><div id="comment-28999" class="comment"><div id="post-28999-score" class="comment-score"></div><div class="comment-text"><p>Hello</p><p>Used:</p><pre><code>sudo apt-get install wireshark
sudo groupadd wireshark
sudo usermod -a -G wireshark YOUR_USER_NAME
sudo chgrp wireshark /usr/bin/dumpcap
sudo chmod 750 /usr/bin/dumpcap
sudo setcap cap_net_raw,cap_net_admin=eip /usr/bin/dumpcap
sudo getcap /usr/bin/dumpcap</code></pre></div><div id="comment-28999-info" class="comment-info"><span class="comment-age">(17 Jan '14, 11:12)</span> ChiefDnd</div></div></div><div id="comment-tools-28996" class="comment-tools"></div><div class="clear"></div><div id="comment-28996-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

