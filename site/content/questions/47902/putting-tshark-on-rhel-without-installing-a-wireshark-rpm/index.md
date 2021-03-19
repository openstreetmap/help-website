+++
type = "question"
title = "Putting tshark on RHEL without installing a Wireshark RPM?"
description = '''Is it possible to use tshark without installing wireshark/tshark rpms on the linux box? I&#x27;d like to create a monitoring script to take live traces (and then decoding the trace) on a linux node, but I&#x27;m not allowed to install any patches on the node. So I&#x27;m just wondering if I can somehow just put th...'''
date = "2015-11-23T14:53:00Z"
lastmod = "2015-11-23T14:57:00Z"
weight = 47902
keywords = [ "tshark", "rhel", "linux" ]
aliases = [ "/questions/47902" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Putting tshark on RHEL without installing a Wireshark RPM?](/questions/47902/putting-tshark-on-rhel-without-installing-a-wireshark-rpm)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47902-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to use tshark without installing wireshark/tshark rpms on the linux box? I'd like to create a monitoring script to take live traces (and then decoding the trace) on a linux node, but I'm not allowed to install any patches on the node. So I'm just wondering if I can somehow just put the libraries/files required to run tshark to a directory and use tshark without installing anything?</p></div><div id="question-tags" class="tags-container tags">tshark rhel linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '15, 14:53</strong></p><img src="https://secure.gravatar.com/avatar/90c1e0f5c5b3a77dc4d24b1333c42dd6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Juha&#39;s gravatar image" /><p>Juha<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Juha has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Nov '15, 14:56</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-47902" class="comments-container"></div><div id="comment-tools-47902" class="comment-tools"></div><div class="clear"></div><div id="comment-47902-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47903"></span>

<div id="answer-container-47903" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47903-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could copy the tshark executable file compiled for your linux distribution into some directory you are allowed to write to, but without root privileges the executable won't be allowed to hook to the network interfaces anyway.</p><p>But if tcpdump is already installed and can be run with root privileges e.g. using sudo (consult your admin), then you could let the tshark executable read the capture saved by tcpdump and decode it in a more user-friendly way.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '15, 14:57</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Nov '15, 15:00</p></div></div><div id="comments-container-47903" class="comments-container"><span id="47904"></span><div id="comment-47904" class="comment"><div id="post-47904-score" class="comment-score"></div><div class="comment-text"><blockquote><p>You could copy the tshark executable file compiled for your linux distribution into some directory you are allowed to write to</p></blockquote><p>But if it's dynamically linked with the Wireshark libraries, you'll have to copy them as well, and somehow arrange that the executable find them when run.</p><blockquote><p>but without root privileges the executable won't be allowed to hook to the network interfaces anyway.</p></blockquote><p>So, yeah, you're going to need at least <em>some</em> privileges on that node, even if it's only the ability to run the monitoring script (and the program it uses, whether it's TShark or tcpdump or...) as root.</p></div><div id="comment-47904-info" class="comment-info"><span class="comment-age">(23 Nov '15, 15:45)</span> Guy Harris ♦♦</div></div><span id="47906"></span><div id="comment-47906" class="comment"><div id="post-47906-score" class="comment-score"></div><div class="comment-text"><p>Yep, I noticed I had to get the shared libraries as well and set the library path temporarily. I then ran into an issue where the tshark looks for the dumpcap from /usr/sbin/, but I'd like to have all related files in my own directry, e.g. /export/home/monitor/ and not have to have files or links populated in other system directories. I can use root privileges to run the script, but I cannot install packages or really touch any system files/directories.</p></div><div id="comment-47906-info" class="comment-info"><span class="comment-age">(23 Nov '15, 18:44)</span> Juha</div></div><span id="47915"></span><div id="comment-47915" class="comment"><div id="post-47915-score" class="comment-score"></div><div class="comment-text"><p>As you seem to be forced to use complex technical solutions to overcome simple administrative restrictions, and as you haven't reacted on my notice about tcpdump which might be already installed, the solution of your needs could be to "non-install" dumpcap the same way like you've "non-installed" tshark.</p><p>If you ask tshark to capture from a physical interface, it internally invokes dumpshark (and because I am a "non-dev", I can only <em>suppose</em> that tshark passes an invocation command to the shell, which implies that it is enough if the dumpcap is somewhere on the standard path where shell looks for executables).</p><p>So your first step would be to non-install dumpcap and check that it can capture.</p><p>Next, you would try to augment the path on which the shell is looking for executables, i.e. so that you could manually execute dumpcap by simply <code>dumpcap</code> rather than <code>./dumpcap</code>. If you succeed, tshark should then be able to run it as well.</p><p>Should this not be possible (because you cannot augment the path or because it is not enough for tshark to reach dumpcap), you can first run dumpcap and ask it to write the captured data to a file by appending <code>-w your_file_name</code> to its parameters, and after capturing what you wanted, ask tshark to use that file as capture input - instead of <code>-i ethX</code>, you'd use <code>-r your_file_name</code>.</p><p>If you need it "realtime", you can use a pipe instead of an intermediate file:</p><p><code>dumpcap -i ethX -P -w - | tshark -k -i -</code></p><p>However, this last possibility may have a drawback, which is that you may not be able to capture from several interfaces in parallel because until recent, tshark did not accept pcapng format on an input pipe and I don't know which version you are using. This is the reason why -P is used as dumpcap parameter; however, specifying more than one -i overrides the -P.</p></div><div id="comment-47915-info" class="comment-info"><span class="comment-age">(24 Nov '15, 03:17)</span> sindy</div></div></div><div id="comment-tools-47903" class="comment-tools"></div><div class="clear"></div><div id="comment-47903-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

