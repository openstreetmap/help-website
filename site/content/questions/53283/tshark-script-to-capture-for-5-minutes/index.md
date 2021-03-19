+++
type = "question"
title = "tshark script to capture for 5 minutes?"
description = '''Hi All, are there any sample scripts to initiate tshark, run it for 5 minutes, initiate a few commands like ping 8.8.8.8, http://www.google.com, tracert www.msn.com, etc. and then close tshark and save the file to a local directory so it can be analyzed later? Thanks!  '''
date = "2016-06-07T08:26:00Z"
lastmod = "2016-06-07T09:41:00Z"
weight = 53283
keywords = [ "tshark", "scripting", "script" ]
aliases = [ "/questions/53283" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [tshark script to capture for 5 minutes?](/questions/53283/tshark-script-to-capture-for-5-minutes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53283-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All, are there any sample scripts to initiate tshark, run it for 5 minutes, initiate a few commands like ping 8.8.8.8, <a href="http://www.google.com">http://www.google.com</a>, tracert www.msn.com, etc. and then close tshark and save the file to a local directory so it can be analyzed later?</p><p>Thanks!<br />
</p></div><div id="question-tags" class="tags-container tags">tshark scripting script</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jun '16, 08:26</strong></p><img src="https://secure.gravatar.com/avatar/87c843fe21c32141b98302751bd94a89?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gipper2016&#39;s gravatar image" /><p>Gipper2016<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gipper2016 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-53283" class="comments-container"></div><div id="comment-tools-53283" class="comment-tools"></div><div class="clear"></div><div id="comment-53283-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53286"></span>

<div id="answer-container-53286" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53286-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sure there are but as you haven't given the operating system, we have to guess by the name of <code>tracert</code> that you have in mind Windows.</p><p>And what you ask is rather a question on scripting than on Wireshark. So by looking at <a href="https://www.wireshark.org/docs/man-pages/tshark.html">tshark man page</a>, you'd find that</p><p><code>tshark -a duration:300 ...</code> will limit tshark's run to 300 seconds = 5 minutes.</p><p>The magic command you need to spawn a parallel process in Windows is "start" and it requires a window title as the first parameter. So you'd use <code>start "my tshark window" "your\full\path\to\tshark\tshark.exe" -a duration:300 -w your\destination\file.pcap ...</code> (put your capture options instead of the dots) as the first line of your .bat file, and on the next lines, you'd run the ping, tracert etc. To see the http, use <code>start</code> as well: <code>start "meaningless" "your\full\path\to\the\browser\browser.exe" http://www.google.com</code>.</p><p>`</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jun '16, 09:41</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-53286" class="comments-container"><span id="53288"></span><div id="comment-53288" class="comment"><div id="post-53288-score" class="comment-score"></div><div class="comment-text"><p>Thank you sindy, excellent info! Another hurdle I see is how to select an active interface? Is it best to just select all interfaces? or is there a trick to pick only active interfaces? Thanks!</p></div><div id="comment-53288-info" class="comment-info"><span class="comment-age">(07 Jun '16, 11:43)</span> Gipper2016</div></div><span id="53301"></span><div id="comment-53301" class="comment"><div id="post-53301-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure I understand what you mean. You seem to be going to ping, traceroute and browse known addresses, so the routing table should give you enough information to know in advance which interface the OS will use to send those packets. But capturing on all interfaces won't do any harm, as the capture file contains the ID of the interface on which each particular frame has been captured, so you can work with that information later.</p></div><div id="comment-53301-info" class="comment-info"><span class="comment-age">(07 Jun '16, 22:20)</span> sindy</div></div><span id="53324"></span><div id="comment-53324" class="comment"><div id="post-53324-score" class="comment-score"></div><div class="comment-text"><p>Sorry, wasn't clear. Since laptops will have multiple interfaces and by default tshark will pick the first non loopback, is there a way to prompt the user to select an interface or is it possible to silently select all interfaces programmatically? I'm trying to automate the process as much as possible for someone that does not know how to use wireshark so they can run it remotely and send me the output file.</p></div><div id="comment-53324-info" class="comment-info"><span class="comment-age">(08 Jun '16, 13:18)</span> Gipper2016</div></div><span id="53326"></span><div id="comment-53326" class="comment"><div id="post-53326-score" class="comment-score"></div><div class="comment-text"><p>See <a href="https://www.wireshark.org/docs/man-pages/tshark.html">the manual</a>, use -i &lt;interface&gt; to define the interface. Prompting can be done via your script, if needed.</p></div><div id="comment-53326-info" class="comment-info"><span class="comment-age">(08 Jun '16, 22:26)</span> Jaap ♦</div></div></div><div id="comment-tools-53286" class="comment-tools"></div><div class="clear"></div><div id="comment-53286-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

