+++
type = "question"
title = "tshark display filter not working while writing pakets to an outfile"
description = '''Hey everyone,  i have a little problem with capturing packets and write the raw data to an output file while using display filters. Here an short example: &quot;tshark -i eth5 -R imap -w test.pcap&quot; When watching at the contents with &quot;tshark -r test.pcap&quot; following comes out: `TIME SRC-IP -&amp;gt; DST-IP TCP...'''
date = "2010-10-05T08:04:00Z"
lastmod = "2012-06-16T00:52:00Z"
weight = 412
keywords = [ "tshark", "display-filter" ]
aliases = [ "/questions/412" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [tshark display filter not working while writing pakets to an outfile](/questions/412/tshark-display-filter-not-working-while-writing-pakets-to-an-outfile)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-412-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-412-score" class="post-score" title="current number of votes">0</div><span id="post-412-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey everyone,</p><p>i have a little problem with capturing packets and write the raw data to an output file while using display filters. Here an short example:</p><p>"tshark -i eth5 -R imap -w test.pcap" When watching at the contents with "tshark -r test.pcap" following comes out:</p><p>`TIME SRC-IP -&gt; DST-IP TCP 56776 &gt; 50143 [ACK] Seq=416 Ack=782 Win=7504 Len=0 TSV=1012820827 TSER=186804250 7504</p><p>TIME SRC-IP -&gt; DST-IP TCP 49360 &gt; 143 [ACK] Seq=101 Ack=919 Win=32762 Len=0 TSV=840349364 TSER=1012820794 32762</p><p>TIME SRC-IP -&gt; DST-IP IMAP Response: 4 OK STORE complete 6432</p><p>TIME SRC-IP -&gt; DST-IP IMAP Response: * BYE session timeout 6432`</p><p>As you can see, the display filter is not applied. When opening it with "tshark -r test.pcap R imap" output is like: `</p><p>TIME SRC-IP -&gt; DST-IP IMAP Response: 4 OK STORE complete 6432</p><p>TIME SRC-IP -&gt; DST-IP IMAP Response: * BYE session timeout 6432 `</p><p>Exectly that is, what should be written to the file, nothing more, only the parts with the decoded IMAP stack. Can anyone explain me what I did wrong and how to solve that issue?</p><p>Thank in advance Sascha</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Oct '10, 08:04</strong></p><img src="https://secure.gravatar.com/avatar/db9b0d7d89cd815ac939136eacbb1d4c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sascha&#39;s gravatar image" /><p><span>Sascha</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sascha has one accepted answer">100%</span></p></div></div><div id="comments-container-412" class="comments-container"></div><div id="comment-tools-412" class="comment-tools"></div><div class="clear"></div><div id="comment-412-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="414"></span>

<div id="answer-container-414" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-414-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-414-score" class="post-score" title="current number of votes">1</div><span id="post-414-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Sascha has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Which version are you using? There is a known bug relating to using "-R" with captures in version 1.4.0.</p><p><em>"Filtering tshark captures with display filters (-R) no longer works. (Bug 2234)"</em></p><p>To see the "Known Bugs" list, read the <strong>news.txt</strong> file in the Wireshark program files directory.</p><p><strong>Suggestion</strong>: You can capture the packets to a file first (use your -w test.pcap) and then use the <strong>-r test.pcap -R testfiltered.pcap</strong> method however. Not as graceful, but "doable."</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Oct '10, 09:33</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p><span>lchappell ♦</span><br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-414" class="comments-container"><span id="416"></span><div id="comment-416" class="comment"><div id="post-416-score" class="comment-score"></div><div class="comment-text"><p>Definitely in sync :-)</p></div><div id="comment-416-info" class="comment-info"><span class="comment-age">(05 Oct '10, 09:35)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="423"></span><div id="comment-423" class="comment"><div id="post-423-score" class="comment-score"></div><div class="comment-text"><p>Owe u an email - been loopy on drugs for a back problem - touch base with you later today!</p></div><div id="comment-423-info" class="comment-info"><span class="comment-age">(05 Oct '10, 14:12)</span> <span class="comment-user userinfo">lchappell ♦</span></div></div><span id="433"></span><div id="comment-433" class="comment"><div id="post-433-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your hints to the known bug list, dont know why i didnt look there before, maybe because its still mentioned in the man page.</p><p>As this bug seems to be still persistent in actual version, I compiled and now use the latest versions where writing to disk with display filters was known to work correctly (0.99.6), because data amount is too high to do any post-processing for all captures. For all other work (viewing, analysing, writing to disk only with capture filters) an up to date version is used.</p><p>Again, thanks for your help.</p></div><div id="comment-433-info" class="comment-info"><span class="comment-age">(06 Oct '10, 04:22)</span> <span class="comment-user userinfo">Sascha</span></div></div></div><div id="comment-tools-414" class="comment-tools"></div><div class="clear"></div><div id="comment-414-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="413"></span>

<div id="answer-container-413" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-413-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-413-score" class="post-score" title="current number of votes">1</div><span id="post-413-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From the <a href="http://www.wireshark.org/docs/relnotes/wireshark-1.4.0.html">release notes</a>:</p><p><em>Filtering tshark captures with display filters (-R) no longer works. (<a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=2234">Bug 2234</a>)</em></p><p>In short, while capturing with tshark and writing to disk, display filters will not work. This needs to be fixed, but is rather difficult to fix.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Oct '10, 09:30</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-413" class="comments-container"><span id="415"></span><div id="comment-415" class="comment"><div id="post-415-score" class="comment-score"></div><div class="comment-text"><p>We must be in sync today, Sake! &lt;g&gt;</p></div><div id="comment-415-info" class="comment-info"><span class="comment-age">(05 Oct '10, 09:34)</span> <span class="comment-user userinfo">lchappell ♦</span></div></div></div><div id="comment-tools-413" class="comment-tools"></div><div class="clear"></div><div id="comment-413-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11985"></span>

<div id="answer-container-11985" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11985-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11985-score" class="post-score" title="current number of votes">0</div><span id="post-11985-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>tshark Read filters aren't supported when capturing and saving the captured packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jun '12, 00:52</strong></p><img src="https://secure.gravatar.com/avatar/d23c5ef9003fef53ac06d0238c43ab29?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DavidMeng&#39;s gravatar image" /><p><span>DavidMeng</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DavidMeng has no accepted answers">0%</span></p></div></div><div id="comments-container-11985" class="comments-container"></div><div id="comment-tools-11985" class="comment-tools"></div><div class="clear"></div><div id="comment-11985-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

