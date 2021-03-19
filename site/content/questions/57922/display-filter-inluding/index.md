+++
type = "question"
title = "Display Filter inluding &quot;@&quot;"
description = '''Hill all,  I am not sure, if the foolowing issue is a bug or just my fault... I refer to wireshark 2.2.2 and I am almost sure, this probem didn&#x27;t exist in the 1.8.X releases. Anyway - my problem is this: I want to start wireshark inclusive open a pcap file and apply a display filter. So my syntax lo...'''
date = "2016-12-07T01:41:00Z"
lastmod = "2016-12-07T03:25:00Z"
weight = 57922
keywords = [ "filter", "display" ]
aliases = [ "/questions/57922" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Display Filter inluding "@"](/questions/57922/display-filter-inluding)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57922-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hill all, I am not sure, if the foolowing issue is a bug or just my fault... I refer to wireshark 2.2.2 and I am almost sure, this probem didn't exist in the 1.8.X releases. Anyway - my problem is this:</p><p>I want to start wireshark inclusive open a pcap file and apply a display filter. So my syntax looks like this: "path to wireshark"\wireshark.exe -r abc.pcap -Y "display filter"</p><p>This works great, as long as my display filter doesn't contain the @ character. But as I often work with SIP Call-IDs as a display filter, I need to have the @ in my filter.</p><p>Previously, it was sufficient to embrace the Call-ID with quotations, for example: wireshark.exe -r input.pcap -Y "sip.Call-ID == "[email protected]"" -w call.pcap</p><p>But after wireshark has started and opened the input.pcap, it states, that the "@" was unexpected in this context. But when you look at the actual display filter, it looks like this: sip.Call-ID == [email protected] So, obviously, wireshark trimmed the quotations, and therefore the display filter becomes invalid.</p><p>When I start wireshark with the same syntax, including a display filter without an "@" it works just fine.</p><p>And it also works, when I start wireshark without any parameter, then open the pcap-file manually and then apply also manually the filter like this: sip.Call-ID == "[email protected]"</p><p>And by the way: It's the same behavior, when I use tshark instead of wireshark.</p><p>My question is now: Is it a bug in the current release, or is there another functional way, how to let wireshark start, open a pcap-file, apply a display filter with "@" characters, and save the filtered packets in another pcap-file?</p><p>Thanks a lot in advance, Josch</p></div><div id="question-tags" class="tags-container tags">filter display</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Dec '16, 01:41</strong></p><img src="https://secure.gravatar.com/avatar/35c51318e9c9101bf17ad43f14aa3237?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Josch&#39;s gravatar image" /><p>Josch<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Josch has no accepted answers">0%</span></p></div></div><div id="comments-container-57922" class="comments-container"><span id="57924"></span><div id="comment-57924" class="comment"><div id="post-57924-score" class="comment-score"></div><div class="comment-text"><p>What OS and shell are you running the commands from?</p></div><div id="comment-57924-info" class="comment-info"><span class="comment-age">(07 Dec '16, 02:42)</span> grahamb ♦</div></div><span id="57925"></span><div id="comment-57925" class="comment"><div id="post-57925-score" class="comment-score"></div><div class="comment-text"><p>It was from a "windows 7 enterprise" out of a "cmd.exe" box...</p></div><div id="comment-57925-info" class="comment-info"><span class="comment-age">(07 Dec '16, 02:50)</span> Josch</div></div></div><div id="comment-tools-57922" class="comment-tools"></div><div class="clear"></div><div id="comment-57922-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57926"></span>

<div id="answer-container-57926" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57926-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>From the command line you have to quote it correctly, you need to quote the filter expression for the shell (cmd.exe) and the argument (for Wireshark) using either different quote characters or escapes. Using different quote characters (single quotes for the argument containing <code>@</code> gives an expression such as:</p><pre><code>wireshark.exe -r input.pcap -Y &quot;sip.Call-ID == &#39;[email protected]&#39;&quot; -w call.pcap</code></pre><p>Using escaping requires 2 additional double quotes to escape one of them giving:</p><pre><code>wireshark.exe -r input.pcap -Y &quot;sip.Call-ID == &quot;&quot;&quot;[email protected]&quot;&quot;&quot;&quot; -w call.pcap</code></pre><p>Note you now have 4 double quotes at the end of the filter expression, 2 to escape the one for the end of the argument and one to end the expression.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '16, 03:25</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-57926" class="comments-container"><span id="57929"></span><div id="comment-57929" class="comment"><div id="post-57929-score" class="comment-score"></div><div class="comment-text"><p>Graham,</p><p>first of all: Thanks a lot for you quick response!</p><p>I tested both alternatives - and one does the trick! ;-)</p><p>1) Using different quote characters didn't work (hoping I typed it in correctly...) I tested it with the followong command: <code>"C:\Program Files\Wireshark\wireshark.exe" -r input.pcap -Y "sip.Call-ID == '[email protected]'"</code></p><p>Result: <code>"sip.Call-ID == '[email protected]'" isn't a valid display filter: "120098715_115318183" was unexpected in this context.</code></p><p>2) Using the double quotes: <code>"C:\Program Files\Wireshark\wireshark.exe" -r output_1.pcap -Y "sip.Call-ID == """[email protected]""""</code></p><p>This worked fine and the resulting display filter in wireshark was: <code>sip.Call-ID == "[email protected]"</code></p><p>Thanks again, Josch</p></div><div id="comment-57929-info" class="comment-info"><span class="comment-age">(07 Dec '16, 03:53)</span> Josch</div></div><span id="57931"></span><div id="comment-57931" class="comment"><div id="post-57931-score" class="comment-score"></div><div class="comment-text"><p>Looks like the first one wasn't typed correctly as it works for me and has been my standard quoting technique for this issue for decades. The ending quotes should be a single quote then a double quote which is hard to differentiate on the screen, i.e. the inner string has single quotes, the entire expression has double quotes.</p><p>The second one requires more typing and careful typing which is why I don't bother with it.</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-57931-info" class="comment-info"><span class="comment-age">(07 Dec '16, 04:46)</span> grahamb ♦</div></div></div><div id="comment-tools-57926" class="comment-tools"></div><div class="clear"></div><div id="comment-57926-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

