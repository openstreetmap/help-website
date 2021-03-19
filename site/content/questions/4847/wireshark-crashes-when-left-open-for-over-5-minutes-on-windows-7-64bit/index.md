+++
type = "question"
title = "Wireshark crashes when left open for over 5 minutes on windows 7 64bit"
description = '''Wireshark crashes after it&#x27;s been capturing for approximately 5 or more minutes. I am running the latest version of it on windows 7 64bit ultimate. Does anyone have any ideas on what I could change to stop this? I have an issue on my network that occurs randomly so I need wireshark to run a lot long...'''
date = "2011-06-30T08:17:00Z"
lastmod = "2011-06-30T08:22:00Z"
weight = 4847
keywords = [ "crash" ]
aliases = [ "/questions/4847" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark crashes when left open for over 5 minutes on windows 7 64bit](/questions/4847/wireshark-crashes-when-left-open-for-over-5-minutes-on-windows-7-64bit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4847-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark crashes after it's been capturing for approximately 5 or more minutes. I am running the latest version of it on windows 7 64bit ultimate. Does anyone have any ideas on what I could change to stop this? I have an issue on my network that occurs randomly so I need wireshark to run a lot longer than 5 minutes.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">crash</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jun '11, 08:17</strong></p><img src="https://secure.gravatar.com/avatar/fdc2ee9b009016473d408eab10580a53?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="digtial911&#39;s gravatar image" /><p>digtial911<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="digtial911 has no accepted answers">0%</span></p></div></div><div id="comments-container-4847" class="comments-container"></div><div id="comment-tools-4847" class="comment-tools"></div><div class="clear"></div><div id="comment-4847-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4848"></span>

<div id="answer-container-4848" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4848-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe you're capturing very large amounts of frames or bytes, which might crash Wireshark after a while. Have you tried saving your captured frames into multiple files? You can do that by using the capture options dialog (second button from the left on the main tool bar).</p><p>Otherwise I'd try capturing with dumpcap directly, which is installed in the same directory as Wireshark. You can use the -D parameter to get a list of all interfaces, and then use the index number of the one you want like this: <code>editcap -i &lt;interface-id&gt; -w &lt;filename&gt;</code>. You can also tell dumpcap to capture to multiple files by using the -b parameter.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jun '11, 08:22</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-4848" class="comments-container"><span id="4851"></span><div id="comment-4851" class="comment"><div id="post-4851-score" class="comment-score"></div><div class="comment-text"><p>The error message is "Microsoft visual C++ runtime library, this application has requested the runtime to terminate in an unusual way. Please contact the applications support team for more information"</p><p>Is there anyway to automate your proposed solution of saving small capture files? I need wireshark to be running around the clock to catch a random event occurring on our network. Is there something else that I could use other than wireshark???</p></div><div id="comment-4851-info" class="comment-info"><span class="comment-age">(30 Jun '11, 09:02)</span> digtial911</div></div><span id="4852"></span><div id="comment-4852" class="comment"><div id="post-4852-score" class="comment-score">1</div><div class="comment-text"><p>As Jasper has said, what you really want to do is capture the traffic first using the simplest way possible, i.e. dumpcap, this doesn't dissect the traffic, so doesn't build up memory usage over time leading to an out of memory condition. See the dumpcap man page for more info: http://www.wireshark.org/docs/man-pages/dumpcap.html</p><p>You can then user Wireshark (or tshark) to examine the capture files to find your network anomaly.</p></div><div id="comment-4852-info" class="comment-info"><span class="comment-age">(30 Jun '11, 09:29)</span> grahamb ♦</div></div><span id="4855"></span><div id="comment-4855" class="comment"><div id="post-4855-score" class="comment-score"></div><div class="comment-text"><p>Got it, I understand now. I am trying it now. Thanks</p></div><div id="comment-4855-info" class="comment-info"><span class="comment-age">(30 Jun '11, 10:25)</span> digtial911</div></div><span id="4856"></span><div id="comment-4856" class="comment"><div id="post-4856-score" class="comment-score"></div><div class="comment-text"><p>Note that you'd need to have dumpcap save to multiple files; if you save to a single file, you'd have the same Wireshark out-of-memory problem reading that file that you'd have if you'd done the capturing with Wireshark capturing to a single file.</p></div><div id="comment-4856-info" class="comment-info"><span class="comment-age">(30 Jun '11, 10:29)</span> Guy Harris ♦♦</div></div><span id="4857"></span><div id="comment-4857" class="comment not_top_scorer"><div id="post-4857-score" class="comment-score"></div><div class="comment-text"><p>Note also that if this is a 64-bit version of Wireshark, it's a lot less likely to have out-of-memory problems; there could well be a Wireshark bug that's causing the crash, in which case attempting to read a packet of the sort that caused the crash could also cause a crash.</p></div><div id="comment-4857-info" class="comment-info"><span class="comment-age">(30 Jun '11, 10:30)</span> Guy Harris ♦♦</div></div><span id="4859"></span><div id="comment-4859" class="comment not_top_scorer"><div id="post-4859-score" class="comment-score"></div><div class="comment-text"><p>Do you have the syntax for splitting the output file into multiple files? I don't see it in the dumpcap.html page.</p></div><div id="comment-4859-info" class="comment-info"><span class="comment-age">(30 Jun '11, 10:44)</span> digtial911</div></div><span id="4860"></span><div id="comment-4860" class="comment"><div id="post-4860-score" class="comment-score">1</div><div class="comment-text"><p>It's the "ring buffer" option, -b. Use "-b filesize:N" to set the maximum size of each file, and <em>don't</em> use the "-b files:N" option, as that sets the maximum number of files, so you'll only have the last N files in that case.</p></div><div id="comment-4860-info" class="comment-info"><span class="comment-age">(30 Jun '11, 10:49)</span> Guy Harris ♦♦</div></div><span id="16386"></span><div id="comment-16386" class="comment not_top_scorer"><div id="post-16386-score" class="comment-score"></div><div class="comment-text"><p>Thanks very much Jasper - I had the same issue as the OP but using dumpcap directly works just fine. :)</p></div><div id="comment-16386-info" class="comment-info"><span class="comment-age">(28 Nov '12, 06:47)</span> Jezz</div></div></div><div id="comment-tools-4848" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-4848-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

