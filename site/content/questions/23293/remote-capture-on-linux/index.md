+++
type = "question"
title = "Remote capture on linux"
description = '''Hi all, i have one question regarding remote capture. I am asking it here so that anyone else can also get the relevant discussions. My question is that why the wireshark versions for linux platform don&#x27;t have the option &quot;Remote interface&quot; in Options menu like windows?  Can we enable it by changing ...'''
date = "2013-07-23T09:15:00Z"
lastmod = "2013-07-23T18:53:00Z"
weight = 23293
keywords = [ "rpcapd", "remote", "linux" ]
aliases = [ "/questions/23293" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Remote capture on linux](/questions/23293/remote-capture-on-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23293-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, i have one question regarding remote capture. I am asking it here so that anyone else can also get the relevant discussions.</p><p>My question is that why the wireshark versions for linux platform don't have the option "Remote interface" in Options menu like windows?</p><ol><li>Can we enable it by changing configure file during installation?</li><li>Will it work as similar as of wireshark versions available for windows?</li><li>Is it unavailable as we can capture packets of remote linux machine from host linux machine using ssh tunnel with pipe?</li></ol><p>Please answer me.</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags">rpcapd remote linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jul '13, 09:15</strong></p><img src="https://secure.gravatar.com/avatar/e82780891a1e938f0bf3a529adc858a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baila&#39;s gravatar image" /><p>baila<br />
<span class="score" title="21 reputation points">21</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baila has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted 23 Jul '13, 09:54</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-23293" class="comments-container"><span id="23296"></span><div id="comment-23296" class="comment"><div id="post-23296-score" class="comment-score"></div><div class="comment-text"><p>I've converted your comment on another question to its own question, each question should remain distinct.</p></div><div id="comment-23296-info" class="comment-info"><span class="comment-age">(23 Jul '13, 09:55)</span> grahamb ♦</div></div><span id="23302"></span><div id="comment-23302" class="comment"><div id="post-23302-score" class="comment-score"></div><div class="comment-text"><p>Thanks grahamb. Actually previously one of my question was closed stating as duplicate, so i felt safe to continue this discussion there. Thanks a lot for your concern.</p></div><div id="comment-23302-info" class="comment-info"><span class="comment-age">(23 Jul '13, 10:44)</span> baila</div></div></div><div id="comment-tools-23293" class="comment-tools"></div><div class="clear"></div><div id="comment-23293-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23309"></span>

<div id="answer-container-23309" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23309-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>My question is that why the wireshark versions for linux platform don't have the option "Remote interface" in Options menu like windows?</p></blockquote><p>Because the libpcap version for the Linux platform doesn't have the APIs to support remote packet capture.</p><blockquote><p>Can we enable it by changing configure file during installation?</p></blockquote><p>No.</p><p>You could enable it by hacking libpcap to support remote packet capture, installing your modified version of libpcap, and building Wireshark with the new version of libpcap, although you might have to hack Wireshark to recognize that your version of libpcap supports remote packet capture.</p><p>At some point in the future libpcap for non-Windows platforms might support remote packet capture, in which case Wireshark would be modified to support that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '13, 18:53</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-23309" class="comments-container"><span id="23313"></span><div id="comment-23313" class="comment"><div id="post-23313-score" class="comment-score"></div><div class="comment-text"><p>Thanks Guy for your answer. Let me try that thing. Hope that it would work!</p></div><div id="comment-23313-info" class="comment-info"><span class="comment-age">(23 Jul '13, 23:14)</span> baila</div></div><span id="23314"></span><div id="comment-23314" class="comment"><div id="post-23314-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-23314-info" class="comment-info"><span class="comment-age">(23 Jul '13, 23:18)</span> grahamb ♦</div></div><span id="23324"></span><div id="comment-23324" class="comment"><div id="post-23324-score" class="comment-score"></div><div class="comment-text"><p>hi Guy, i have tried the remote capture using ssh tunnel as per the instructions follows :</p><ol><li>mkfifo /tmp/packet_capture</li><li>ssh hostname_or_ip_of_remote_pc "tcpdump -s 0 -U -n -w - -i eth0 not port 22" &gt; /tmp/packet_capture</li><li>wireshark -k -i /tmp/packet_capture</li></ol><p>but during 2nd step, sometimes the password authentication is not coming and it is just paused. Am i doing anything wrong? Without that " &gt; /tmp/packet_capture", its all working fine.</p><p>Thanks in advance.</p></div><div id="comment-23324-info" class="comment-info"><span class="comment-age">(24 Jul '13, 05:42)</span> baila</div></div><span id="23355"></span><div id="comment-23355" class="comment"><div id="post-23355-score" class="comment-score"></div><div class="comment-text"><p>hi all, please share if you have any update on this issue.</p><p>Thanks.</p></div><div id="comment-23355-info" class="comment-info"><span class="comment-age">(25 Jul '13, 00:42)</span> baila</div></div><span id="24694"></span><div id="comment-24694" class="comment"><div id="post-24694-score" class="comment-score"></div><div class="comment-text"><p>Baila, the reason why it "pauses" during step two is because it's waiting for you to type in the command (on a separate terminal) for step three. At that point go back to the terminal for step two and it should prompt you for the password.</p></div><div id="comment-24694-info" class="comment-info"><span class="comment-age">(14 Sep '13, 15:06)</span> Marikawn</div></div></div><div id="comment-tools-23309" class="comment-tools"></div><div class="clear"></div><div id="comment-23309-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

