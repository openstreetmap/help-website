+++
type = "question"
title = "WireShark in Ubuntu 16 is failed for libgcrypt.so.11"
description = '''Hi, wireshark 1.12.8 is build on centos 6.3. the steps mentioned in the wireshark dev page is followed (configure, make, make install). Now that binary is supposed to install in Ubuntu 16. It is failed due to libgcrypt.so.11 is not found. I checked in internet that Ubuntu 16 is having libgcrypt20. s...'''
date = "2017-04-03T01:03:00Z"
lastmod = "2017-04-03T07:24:00Z"
weight = 60538
keywords = [ "failed", "libgcrypt", "installation", "build", "ubuntu" ]
aliases = [ "/questions/60538" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [WireShark in Ubuntu 16 is failed for libgcrypt.so.11](/questions/60538/wireshark-in-ubuntu-16-is-failed-for-libgcryptso11)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60538-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, wireshark 1.12.8 is build on centos 6.3. the steps mentioned in the wireshark dev page is followed (configure, make, make install). Now that binary is supposed to install in Ubuntu 16. It is failed due to libgcrypt.so.11 is not found. I checked in internet that Ubuntu 16 is having libgcrypt20. so is there any feasible work around for the binary to run on Ubuntu.</p><p>Thanks, ABHISEK</p></div><div id="question-tags" class="tags-container tags">failed libgcrypt installation build ubuntu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Apr '17, 01:03</strong></p><img src="https://secure.gravatar.com/avatar/48912e037040264c21d2e543aca485e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Abhisek&#39;s gravatar image" /><p>Abhisek<br />
<span class="score" title="16 reputation points">16</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Abhisek has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Apr '17, 17:09</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-60538" class="comments-container"></div><div id="comment-tools-60538" class="comment-tools"></div><div class="clear"></div><div id="comment-60538-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60547"></span>

<div id="answer-container-60547" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60547-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>By far the best answer is going to be: compile for your target platform. That is, if you want to run Wireshark on Ubuntu you're going to need to compile it on Ubuntu.</p><p>There's some slight chance that, with a lot of painful work, you could get a program compiled on CentOS running on Ubuntu but it wouldn't be a fun road.</p><p>FWIW you'd have a much better chance of success using a more modern CentOS (i.e., CentOS 7) if your target is such a modern Ubuntu.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Apr '17, 07:24</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-60547" class="comments-container"><span id="60556"></span><div id="comment-60556" class="comment"><div id="post-60556-score" class="comment-score">1</div><div class="comment-text"><p>And, for better or worse, Linux isn't a "platform" at the binary level; there are <em>some</em> cases where a binary built for one distribution could work on some version of another distribution.</p><p>The fact that Centos 6.3 has <code>libgcrypt.so.11</code> and Ubuntu 16 has <code>libgcrypt.so.20</code> means one of two things:</p><ol><li>the two versions of libgcrypt are not binary compatible, and the binary built with<code>libgcrypt.so.11</code> might not work with <code>libgcyrpt.so.20</code>;</li><li>whoever is responsible for assigning shared library version numbers to libgcrypt on those distributions (whether it's the distributions or the upstream maintainers of libgcrypt) don't understand how shared libraries should be given version numbers and gratuitously broke binary compatibility without the libraries themselves being binary-incompatible.</li></ol></div><div id="comment-60556-info" class="comment-info"><span class="comment-age">(03 Apr '17, 17:07)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-60547" class="comment-tools"></div><div class="clear"></div><div id="comment-60547-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

