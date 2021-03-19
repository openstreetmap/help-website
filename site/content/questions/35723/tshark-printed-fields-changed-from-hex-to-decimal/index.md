+++
type = "question"
title = "tshark: printed fields changed from hex to decimal"
description = '''I have a very simple script I use to print some fields from the handshake messages from SSL traffic (basically trying to make sure nobody is using apps that use obsolete versions of SSL). I have this running on two machines: one is Ubuntu 12.04.4, running tshark version 1.6.7, and another running is...'''
date = "2014-08-25T13:17:00Z"
lastmod = "2014-08-26T10:03:00Z"
weight = 35723
keywords = [ "ciphersuite", "ssl", "hexadecimal", "vs", "decimal" ]
aliases = [ "/questions/35723" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [tshark: printed fields changed from hex to decimal](/questions/35723/tshark-printed-fields-changed-from-hex-to-decimal)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35723-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a very simple script I use to print some fields from the handshake messages from SSL traffic (basically trying to make sure nobody is using apps that use obsolete versions of SSL). I have this running on two machines: one is Ubuntu 12.04.4, running tshark version 1.6.7, and another running is Windows 7, running tshark 1.10.9. Here's the command:</p><p>tshark -r pcap-file -E header=y -Tfields -e ip.src -e ip.dst -e ssl.handshake.ciphersuite -e ssl.handshake.version</p><p>On both hosts, this basically works, but on the Ubuntu the ciphersuite and version are printed in hex, while on Windows they're printed in decimal. This is inconvenient, to say the least.</p><p>Is there a way to convince 1.10.9 on Windows to print these values in hex?</p></div><div id="question-tags" class="tags-container tags">ciphersuite ssl hexadecimal vs decimal</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Aug '14, 13:17</strong></p><img src="https://secure.gravatar.com/avatar/86f23fef4114b61a16dc6e0676a9544e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Daniel%20Ellard&#39;s gravatar image" /><p>Daniel Ellard<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Daniel Ellard has no accepted answers">0%</span></p></div></div><div id="comments-container-35723" class="comments-container"></div><div id="comment-tools-35723" class="comment-tools"></div><div class="clear"></div><div id="comment-35723-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="35754"></span>

<div id="answer-container-35754" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35754-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's a bug, see <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10318">bug 10318</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '14, 07:58</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-35754" class="comments-container"><span id="35762"></span><div id="comment-35762" class="comment"><div id="post-35762-score" class="comment-score"></div><div class="comment-text"><p>While we probably shouldn't be changing formats between 1.10.5 and 1.10.8, hence the [unrelated] bug, there are no guarantees between 1.6.7 and 1.10.9. Formats change from time to time, usually for good reason, so this is something one simply has to deal with when using different major versions of the tool.</p></div><div id="comment-35762-info" class="comment-info"><span class="comment-age">(26 Aug '14, 10:10)</span> cmaynard ♦♦</div></div><span id="35763"></span><div id="comment-35763" class="comment"><div id="post-35763-score" class="comment-score"></div><div class="comment-text"><p>Hmm, I'm pretty sure the bug <em>is</em> related: between 1.10.0 and 1.10.8 we stopped printing any fields in hex and started printing them all in decimal. I agree with the originator of the bug (and the fix) who think that's a regression.</p><p>(I agree with you that, in general, we may change individual fields from hex to decimal or vice-versa but the bug here is that <em>everything</em> is now decimal--if you use tshark.)</p></div><div id="comment-35763-info" class="comment-info"><span class="comment-age">(26 Aug '14, 10:51)</span> JeffMorriss ♦</div></div><span id="35764"></span><div id="comment-35764" class="comment"><div id="post-35764-score" class="comment-score"></div><div class="comment-text"><p>If that's the case, then yes that's surely a bug. The bug description does not make it clear that it pertains to all fields though, but rather only to the <code>gtp.teid</code> field.</p></div><div id="comment-35764-info" class="comment-info"><span class="comment-age">(26 Aug '14, 10:58)</span> cmaynard ♦♦</div></div><span id="35766"></span><div id="comment-35766" class="comment"><div id="post-35766-score" class="comment-score"></div><div class="comment-text"><p>Ah, yeah, I guess that's so. But if you look at the Summary or the change that broke it, it becomes pretty clear. (The fact that someone independently reported the bug--but submitting a change to fix it--also suggests the problem is wide spread.)</p></div><div id="comment-35766-info" class="comment-info"><span class="comment-age">(26 Aug '14, 11:04)</span> JeffMorriss ♦</div></div><span id="35783"></span><div id="comment-35783" class="comment"><div id="post-35783-score" class="comment-score"></div><div class="comment-text"><p>Yup, that looks like the issue, and probably a lot of people using tshark are going to trip over this because it changes how many fields are printed.</p><p>In this particular case, it is very convenient to have the fields printed in hex because the relevant constants in the RFCs are given in hex, which makes it very easy to read. Having the numbers in decimal makes the output harder to interpret.</p></div><div id="comment-35783-info" class="comment-info"><span class="comment-age">(26 Aug '14, 19:15)</span> Daniel Ellard</div></div></div><div id="comment-tools-35754" class="comment-tools"></div><div class="clear"></div><div id="comment-35754-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="35761"></span>

<div id="answer-container-35761" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35761-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming you have cygwin running on Windows, one way might be to use <code>awk</code> and <code>printf</code> to do the conversion:</p><pre><code>tshark -r pcap-file -E header=y -Tfields -e ip.src -e ip.dst -e ssl.handshake.ciphersuite -e ssl.handshake.version | awk &#39;!/^($|#)/{printf &quot;%s %s %x %x\n&quot;, $1,$2,$3,$4}&#39;</code></pre><p>If you don't have cygwin and don't want to install it, then there might be a way to accomplish the same thing using Powershell.</p><p>Apart from those ideas, using the same version of Wireshark on both systems should avoid the problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '14, 10:03</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-35761" class="comments-container"><span id="35782"></span><div id="comment-35782" class="comment"><div id="post-35782-score" class="comment-score"></div><div class="comment-text"><p>Yes, with a little futzing I could get the output the same.</p><p>It's not as convenient as having a script that works everywhere, however.</p></div><div id="comment-35782-info" class="comment-info"><span class="comment-age">(26 Aug '14, 19:10)</span> Daniel Ellard</div></div></div><div id="comment-tools-35761" class="comment-tools"></div><div class="clear"></div><div id="comment-35761-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

