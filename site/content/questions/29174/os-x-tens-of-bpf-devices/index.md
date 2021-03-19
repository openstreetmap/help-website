+++
type = "question"
title = "OS X tens of BPF devices"
description = '''My network pref started to be really slow, so I started poking around. I found over hundred /dev/pty and /dev/tty files, each. There is also 30 /dev/bpf* files, most of them don&#x27;t have rw permission for the group. Seems like chmodBPF is not working anymore, although it&#x27;s still in the startup items f...'''
date = "2014-01-27T01:56:00Z"
lastmod = "2014-01-27T15:01:00Z"
weight = 29174
keywords = [ "mavericks", "bpf" ]
aliases = [ "/questions/29174" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [OS X tens of BPF devices](/questions/29174/os-x-tens-of-bpf-devices)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29174-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My network pref started to be really slow, so I started poking around.</p><p>I found over hundred /dev/pty <em>and /dev/tty</em> files, each. There is also 30 /dev/bpf* files, most of them don't have rw permission for the group. Seems like chmodBPF is not working anymore, although it's still in the startup items folder (/Library/StartupItems).</p><p>Questions:</p><ul><li>does anyone has the network pref freeezing for up to 20s every time you change location (or anything, for that matter, not necessarily the location)?</li><li>do you also have hundreds of network interfaces under /dev/ ?</li></ul><p>I am grateful for any suggestions!</p><p>I use Mavericks 10.9.1 and Wireshark 1.10.2</p></div><div id="question-tags" class="tags-container tags">mavericks bpf</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jan '14, 01:56</strong></p><img src="https://secure.gravatar.com/avatar/afdb381fbf92702d37836f93830b39f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KaZ219&#39;s gravatar image" /><p>KaZ219<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KaZ219 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Jan '14, 14:52</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-29174" class="comments-container"></div><div id="comment-tools-29174" class="comment-tools"></div><div class="clear"></div><div id="comment-29174-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29207"></span>

<div id="answer-container-29207" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29207-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Pseudo-ttys are not network devices, they're <a href="https://en.wikipedia.org/wiki/Pseudo-TTY">pseudo-ttys</a>. Every Terminal window uses one, so they're not <em>only</em> used by people ssh'ing (or, in ancient times, Telnetting or rsh'ing) into your computer.</p><p>BPF devices aren't directly network devices, either; they're <a href="https://developer.apple.com/library/mac/documentation/darwin/reference/manpages/man4/bpf.4.html">devices that can be attached <em>to</em> network devices in order to capture traffic to or from those network devices</a>, and there can be multiple BPF devices attached to the same network device.</p><p>ChmodBPF runs when your system starts, and can only change the permissions on the devices that exist when it's run. BPF devices are "create on demand" devices, so that when you open the last of the existing BPF devices, the system creates more of them (four more, to be specific); ChmodBPF doesn't know when that happens and can't fix them. (Unfortunately, a program can't watch to see when <code>/dev</code> changes, so, for example, launchd can't monitor it and run something like ChmodBPF when new BPF devices are created.)</p><p>If you want to know how many <em>network interfaces</em> you have, try doing <code>ifconfig -l</code>. (Not all of them correspond to physical network adapters.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jan '14, 15:01</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Jan '14, 15:13</p></div></div><div id="comments-container-29207" class="comments-container"><span id="29219"></span><div id="comment-29219" class="comment"><div id="post-29219-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the explanation. It might have nothing to do with Wireshark indeed. in ifconfig everything looks ok. I thought it might ring a bell with someone and they can point me in the right direction. It's just really annoying to have to wait 20s each time I change network location.</p></div><div id="comment-29219-info" class="comment-info"><span class="comment-age">(28 Jan '14, 01:04)</span> KaZ219</div></div><span id="29221"></span><div id="comment-29221" class="comment"><div id="post-29221-score" class="comment-score"></div><div class="comment-text"><p>Just for laughs, try opening up System Preferences (but not changing your network location yet), opening up a Terminal window, running <code>sudo sample 'System Preferences' 30</code>, and then immediately going to System Preferences and changing your network location. When it finishes, see whether the <code>sample</code> command has written out the sample yet and, if it hasn't, wait for it to do so.</p><p>The results might not be useful to you, but they are likely to be useful to Apple; <a href="https://developer.apple.com/register/index.action">register as an Apple developer</a>, and then <a href="http://bugreport.apple.com">file a bug on this</a>, with the output of <code>sample</code> as an attachment.</p></div><div id="comment-29221-info" class="comment-info"><span class="comment-age">(28 Jan '14, 01:45)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-29207" class="comment-tools"></div><div class="clear"></div><div id="comment-29207-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

