+++
type = "question"
title = "extract from pcap to csv using tshark"
description = '''I want to convert normal.pcap file to csv file but I get  C:&#92;Program Files&#92;Wireshark&amp;gt;tshark -r normal.pcap -T fields -e frame.number -e frame.time -e eth.src -e eth.dst -e ip.src -e ip.dst -e ip.proto -E header=y -E separator=, -E quote=d -E occurrence=f &amp;gt; test.csv  Accès refusé.  what is the ...'''
date = "2016-05-10T13:22:00Z"
lastmod = "2016-05-10T13:48:00Z"
weight = 52404
keywords = [ "csv", "pcap", "tshark" ]
aliases = [ "/questions/52404" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [extract from pcap to csv using tshark](/questions/52404/extract-from-pcap-to-csv-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52404-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to convert normal.pcap file to csv file but I get</p><blockquote><p>C:\Program Files\Wireshark&gt;tshark -r normal.pcap -T fields -e frame.number -e frame.time -e eth.src -e eth.dst -e ip.src -e ip.dst -e ip.proto -E header=y -E separator=, -E quote=d -E occurrence=f &gt; test.csv Accès refusé.</p></blockquote><p>what is the pb here.</p><p>thanks in advance</p></div><div id="question-tags" class="tags-container tags">csv pcap tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 May '16, 13:22</strong></p><img src="https://secure.gravatar.com/avatar/279908d3c8338ae7ec02baa9f51a3c1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Khadidja%20Khadidja&#39;s gravatar image" /><p>Khadidja Kha...<br />
<span class="score" title="41 reputation points">41</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Khadidja Khadidja has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 May '16, 14:19</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-52404" class="comments-container"><span id="52415"></span><div id="comment-52415" class="comment"><div id="post-52415-score" class="comment-score"></div><div class="comment-text"><p>thanks for all your responses it works perfectly :)</p></div><div id="comment-52415-info" class="comment-info"><span class="comment-age">(10 May '16, 14:01)</span> Khadidja Kha...</div></div><span id="52416"></span><div id="comment-52416" class="comment"><div id="post-52416-score" class="comment-score">1</div><div class="comment-text"><p>The idea of this site is that only answers to the original Question are posted as Answers; therefore, I've converted what you've posted as an Answer into a comment.</p><p>Another idea of this site is that the one who asked the Question marks the Answer which suited him best as "Accepted", which helps others who come with the same or similar question to choose from those similar Questions to which a useful Answer exists.</p><p>What this site does <em>not</em> anticipate is that you get several identical answers in parallel (nor that you ask the same thing in two distinct Questions). So please randomly choose one Answer here and mark it as Accepted (using the checkmark icon, not the thumbs up one), and also accept @Christian_R's Answer to your other Question.</p><p>Cheers.</p></div><div id="comment-52416-info" class="comment-info"><span class="comment-age">(10 May '16, 14:08)</span> sindy</div></div><span id="52419"></span><div id="comment-52419" class="comment"><div id="post-52419-score" class="comment-score"></div><div class="comment-text"><p>I am newbie on this site, so thanks a lot for your advice ^^</p></div><div id="comment-52419-info" class="comment-info"><span class="comment-age">(10 May '16, 14:31)</span> Khadidja Kha...</div></div></div><div id="comment-tools-52404" class="comment-tools"></div><div class="clear"></div><div id="comment-52404-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="52412"></span>

<div id="answer-container-52412" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52412-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you are logged in as normal user (no admin rights), Windows will not let you write anything into <code>C:\Program Files</code> or any of its sub-directories. So please modify the destination file name to <code>c:\Users\your_user_name\Documents\test.csv</code> and try again.</p><p>My qualified guess is that the reason why it worked for @Jasper was that he was (exceptionally) logged in using an account with administrator rights.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '16, 13:48</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-52412" class="comments-container"><span id="52413"></span><div id="comment-52413" class="comment"><div id="post-52413-score" class="comment-score"></div><div class="comment-text"><p>No, it worked for me because I have the Wireshark installation directory in my path variable and ran tshark in my D:\Work\Traces directory :-)</p><p>So I oversaw that I didn't use the same directory, and that it was the problem.</p></div><div id="comment-52413-info" class="comment-info"><span class="comment-age">(10 May '16, 13:51)</span> Jasper ♦♦</div></div><span id="52414"></span><div id="comment-52414" class="comment"><div id="post-52414-score" class="comment-score"></div><div class="comment-text"><p>I just love to send an answer and find out that an identical one has already been posted twice in the meantime :-)</p></div><div id="comment-52414-info" class="comment-info"><span class="comment-age">(10 May '16, 13:55)</span> sindy</div></div></div><div id="comment-tools-52412" class="comment-tools"></div><div class="clear"></div><div id="comment-52412-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52405"></span>

<div id="answer-container-52405" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52405-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I just tried your command and it works fine for me. Maybe test.csv already existed and was open/locked by another program?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '16, 13:27</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-52405" class="comments-container"><span id="52406"></span><div id="comment-52406" class="comment"><div id="post-52406-score" class="comment-score"></div><div class="comment-text"><p>thanks for your response. there is no any test.csv file in C:\Program Files\Wireshark directory. and it Still does not work</p></div><div id="comment-52406-info" class="comment-info"><span class="comment-age">(10 May '16, 13:36)</span> Khadidja Kha...</div></div><span id="52408"></span><div id="comment-52408" class="comment"><div id="post-52408-score" class="comment-score">1</div><div class="comment-text"><p>Try redirecting the output to <code>C:\some\place\you\have\permission\to\write\to\test.csv</code>.</p></div><div id="comment-52408-info" class="comment-info"><span class="comment-age">(10 May '16, 13:38)</span> cmaynard ♦♦</div></div><span id="52409"></span><div id="comment-52409" class="comment"><div id="post-52409-score" class="comment-score">1</div><div class="comment-text"><p>Oh, you're doing it in the "C:\Program Files" path? Windows does not allow you to write files there without an elevated command prompt (which you should <strong>not</strong> use)</p><p>Try writing the File to a location where you are allowed to create files, e.g. your Desktop.</p></div><div id="comment-52409-info" class="comment-info"><span class="comment-age">(10 May '16, 13:40)</span> Jasper ♦♦</div></div><span id="52410"></span><div id="comment-52410" class="comment"><div id="post-52410-score" class="comment-score">1</div><div class="comment-text"><p>Because <code>C:\Program Files\Wireshark</code> isn't writable without elevated permission.</p></div><div id="comment-52410-info" class="comment-info"><span class="comment-age">(10 May '16, 13:40)</span> grahamb ♦</div></div></div><div id="comment-tools-52405" class="comment-tools"></div><div class="clear"></div><div id="comment-52405-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

