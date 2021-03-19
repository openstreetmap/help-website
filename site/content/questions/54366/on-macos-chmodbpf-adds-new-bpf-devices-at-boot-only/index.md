+++
type = "question"
title = "On macOS, ChmodBPF adds new BPF devices at boot only"
description = '''The script ChmodBPF creates new /dev/bpf interfaces and set specific permissions thanks to the code: while [ &quot;$CUR_DEV&quot; -lt &quot;$FORCE_CREATE_BPF_MAX&quot; ] ; do  # Try to do the minimum necessary to trigger the next device.  read -n 0 &amp;lt; /dev/bpf$CUR_DEV &amp;gt; /dev/null 2&amp;gt;&amp;amp;1  CUR_DEV=$(( $CUR_DEV ...'''
date = "2016-07-27T05:14:00Z"
lastmod = "2016-07-27T17:35:00Z"
weight = 54366
keywords = [ "mac", "chmodbpf", "script" ]
aliases = [ "/questions/54366" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [On macOS, ChmodBPF adds new BPF devices at boot only](/questions/54366/on-macos-chmodbpf-adds-new-bpf-devices-at-boot-only)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54366-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The script ChmodBPF creates new /dev/bpf interfaces and set specific permissions thanks to the code:</p><pre><code>while [ &quot;$CUR_DEV&quot; -lt &quot;$FORCE_CREATE_BPF_MAX&quot; ] ; do
    # Try to do the minimum necessary to trigger the next device.
    read -n 0 &lt; /dev/bpf$CUR_DEV &gt; /dev/null 2&gt;&amp;1
    CUR_DEV=$(( $CUR_DEV + 1 ))
done</code></pre><p>I've deleted /dev/bpf250, and launched ChmodBPF as root, but "read -n 0 &lt; /dev/bpf249" doesn't create /dev/bpf250.</p><p>I rebooted macOS, and this time the script created /dev/bpf250.</p><p>What prevents the manual execution of ChmodBPF as root to create new BPF devices?</p></div><div id="question-tags" class="tags-container tags">mac chmodbpf script</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '16, 05:14</strong></p><img src="https://secure.gravatar.com/avatar/822be38630e1b9b5a1505f259322c63b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomLaBaude&#39;s gravatar image" /><p>TomLaBaude<br />
<span class="score" title="66 reputation points">66</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomLaBaude has 2 accepted answers">66%</span></p></div></div><div id="comments-container-54366" class="comments-container"></div><div id="comment-tools-54366" class="comment-tools"></div><div class="clear"></div><div id="comment-54366-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54388"></span>

<div id="answer-container-54388" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54388-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I've deleted /dev/bpf250, and launched ChmodBPF as root, "read -n 0 &lt; /dev/bpf249" doesn't create /dev/bpf250</p></blockquote><p><a href="http://opensource.apple.com/source/xnu/xnu-3248.50.21/bsd/net/bpf.c">The relevant code</a> only creates a BPF device if the device number is greater than the maximum device number ever created; it doesn't fill in artificially-created holes in the BPF device number space.</p><p>(What Apple <em>should</em> do is implement a cloning BPF device, so that you can just open <code>/dev/bpf</code> and get a new BPF device; they'd still have to leave the old numbered devices, complete with the existing creation operation, for backwards compatibility, but they could and should then enable libpcap's support for the cloning device. Darwin <em>does</em> support cloning devices.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '16, 17:35</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-54388" class="comments-container"><span id="54396"></span><div id="comment-54396" class="comment"><div id="post-54396-score" class="comment-score"></div><div class="comment-text"><p>Interesting, so why a reboot creates /dev/bpf250? Is it another part of the code at boot? My goal was to be able to manually create a new bpf device like it does at boot...</p></div><div id="comment-54396-info" class="comment-info"><span class="comment-age">(28 Jul '16, 03:01)</span> TomLaBaude</div></div><span id="54411"></span><div id="comment-54411" class="comment"><div id="post-54411-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Interesting, so why a reboot creates /dev/bpf250? Is it another part of the code at boot?</p></blockquote><p>No, it's because <code>/dev/bpf250</code> doesn't exist at boot time - the maximum device number ever created, at that point, is, as I remember, 4 (4 BPF devices are created by the BPF code at boot time). Therefore, attempts to open devices past <code>/dev/bpf3</code> create new devices.</p><blockquote><p>My goal was to be able to manually create a new bpf device like it does at boot...</p></blockquote><p>If you want to create a device to replace one that you removed, you would have to do so manually with the <code>mknod</code> command. If you want to create additional devices beyond the ones that <code>ChmodBPF</code> created, you'd have to modify <code>ChmodBPF</code> to raise the value of <code>FORCE_CREATE_BPF_MAX</code> to the maximum device number you want.</p></div><div id="comment-54411-info" class="comment-info"><span class="comment-age">(28 Jul '16, 10:58)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-54388" class="comment-tools"></div><div class="clear"></div><div id="comment-54388-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

