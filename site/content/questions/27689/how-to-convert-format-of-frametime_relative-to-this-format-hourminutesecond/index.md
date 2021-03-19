+++
type = "question"
title = "How to convert format of frame.time_relative to this format &quot;hour:minute:second&quot;?"
description = '''Here is what I tried: tshark -r test.pcap -T fields -e frame.time_relative &amp;gt; file.csv And here is the csv file I got:  frame.time_relative  0 0.000128 0.000315 0.000407 0.010027  I want this format to be a real time format. for example: 16:20:35 (hour:minute:second) Any idea please...'''
date = "2013-12-02T23:28:00Z"
lastmod = "2013-12-03T08:19:00Z"
weight = 27689
keywords = [ "timestamp", "tshark", "wireshark" ]
aliases = [ "/questions/27689" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to convert format of frame.time\_relative to this format "hour:minute:second"?](/questions/27689/how-to-convert-format-of-frametime_relative-to-this-format-hourminutesecond)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27689-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Here is what I tried:</p><p>tshark -r test.pcap -T fields -e frame.time_relative &gt; file.csv</p><h1 id="and-here-is-the-csv-file-i-got">And here is the csv file I got:</h1><ul><li>frame.time_relative</li><li>0</li><li>0.000128</li><li>0.000315</li><li>0.000407</li><li>0.010027</li></ul><p>I want this format to be a real time format. for example: 16:20:35 (hour:minute:second)</p><p>Any idea please...</p></div><div id="question-tags" class="tags-container tags">timestamp tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '13, 23:28</strong></p><img src="https://secure.gravatar.com/avatar/f6794f3ef18ab7a1ad2e4f56711db6f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Eliza%20Rana&#39;s gravatar image" /><p>Eliza Rana<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Eliza Rana has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Dec '13, 08:12</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-27689" class="comments-container"></div><div id="comment-tools-27689" class="comment-tools"></div><div class="clear"></div><div id="comment-27689-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27716"></span>

<div id="answer-container-27716" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27716-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>My answer to <a href="http://stackoverflow.com/questions/18851483/how-do-i-format-tshark-time-to-iso-format-yyyy-dd-mm">this</a> question over at <a href="http://stackoverflow.com/">http://stackoverflow.com/</a> should help you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '13, 08:19</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-27716" class="comments-container"><span id="27718"></span><div id="comment-27718" class="comment"><div id="post-27718-score" class="comment-score"></div><div class="comment-text"><p>Thanks cmaynard.</p></div><div id="comment-27718-info" class="comment-info"><span class="comment-age">(03 Dec '13, 08:32)</span> Eliza Rana</div></div><span id="27720"></span><div id="comment-27720" class="comment"><div id="post-27720-score" class="comment-score"></div><div class="comment-text"><p>You're welcome. Now please go delete your duplicate questions.</p></div><div id="comment-27720-info" class="comment-info"><span class="comment-age">(03 Dec '13, 08:33)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-27716" class="comment-tools"></div><div class="clear"></div><div id="comment-27716-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27694"></span>

<div id="answer-container-27694" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27694-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Raksmey, Eliza, or whatever your name may be</p><p><strong>really not meant as an offense</strong>,</p><p>BUT, why do you open 3!! questions for the <strong>identical</strong> problem?</p><ul><li><a href="http://ask.wireshark.org/questions/27599/when-transform-pcap-to-csv-data-how-to-convert-timestamp-to-standard-format-using-tshark-command">Question #1</a></li><li><a href="http://ask.wireshark.org/questions/27666/by-using-tshark-command-i-want-to-transform-the-timestamp-dataframetime-into-csv-file-that-has-a-format-hourminutesecond-so-what-should-i-do">Question #2</a></li><li><a href="http://ask.wireshark.org/questions/27689/how-to-convert-format-of-frametime_relative-to-this-format-hourminutesecond">Question #3</a></li></ul><p>This is a Q&amp;A site, with the purpose to get answers for questions and to search for answers to similar problems. If you clutter the site with questions, you will <strong>not</strong> help others to find an answer to their problems, as all your redundant, open questions will distract/confuse them.</p><p>The reason why you don't get <strong>that many</strong> answers to your questions is pretty simple. It is obvious, that your are trying to get the work done for your homework, by other people. You are asking for complete solutions, like: 'please draw CDR of TCP frames with R'. Why do you think people would do that? It's quite some work and foremost it is <strong>your work</strong> as it is <strong>your homework</strong>.</p><p>If you promise the following things, I promise to give you some hints how to finish your homework.</p><ul><li>you promise to stop creating questions over and over again for the <strong>same</strong> homework problem</li><li>you promise to consolidate <strong>all your questions</strong> in <strong>one</strong> new question</li><li>you promise to add information to that question what you have already tried and what problems you are still facing</li><li>you promise to delete your other, <strong>redundant</strong> questions</li></ul><p>If all that happens</p><ul><li>I promise to give you some <strong>hints</strong> for your homework problems. <strong>However:</strong> don't expect to get any (R) code or a colored PDF with your letterhead and all the answers for your homework!!<br />
</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '13, 03:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Dec '13, 03:09</p></div></div><div id="comments-container-27694" class="comments-container"><span id="27698"></span><div id="comment-27698" class="comment"><div id="post-27698-score" class="comment-score"></div><div class="comment-text"><p>I'm sorry for this</p></div><div id="comment-27698-info" class="comment-info"><span class="comment-age">(03 Dec '13, 04:22)</span> Eliza Rana</div></div><span id="27711"></span><div id="comment-27711" class="comment"><div id="post-27711-score" class="comment-score"></div><div class="comment-text"><p>no need to be sorry. You can help others to help you, by asking the right questions in the right way ;-))</p><p>So, regarding your time problem, you have these options:</p><blockquote><p>tshark -nr input.pcap -T fields -e <strong>frame.time</strong></p></blockquote><p>which will print the <strong>absolute date/time</strong> in the following format</p><pre><code>Dec  3, 2013 15:04:01.154144000
Dec  3, 2013 15:04:02.678225000
Dec  3, 2013 15:04:02.778029000</code></pre><blockquote><p>tshark -nr input.pcap -T fields -e <strong>frame.time_relative</strong></p></blockquote><p>which will print the <strong>absolute date/time</strong> in 'Unix time', which is seconds passed since 1.1.1970 00:00:00.</p><blockquote><p><a href="http://en.wikipedia.org/wiki/Unix_time">http://en.wikipedia.org/wiki/Unix_time</a></p></blockquote><pre><code>1386079441.154144000
1386079442.678225000
1386079442.778029000</code></pre><blockquote><p>tshark -nr input.pcap -T fields -e <strong>frame.time_relative</strong></p></blockquote><p>which will print the <strong>relative</strong> time (in seconds) since the beginning of the capture file.</p><pre><code>0.000000000
1.524081000
1.623885000
1.624036000</code></pre><p>Those time formats are all described in the docs</p><blockquote><p><a href="http://www.wireshark.org/docs/wsug_html_chunked/ChWorkTimeFormatsSection.html">http://www.wireshark.org/docs/wsug_html_chunked/ChWorkTimeFormatsSection.html</a></p></blockquote><p>So, to solve your 'CDR graphing problem', you could use <strong>frame.time</strong> and remove the date part (with a script) or <strong>frame.time_relative</strong> and convert the seconds to hh:mm:ss (with a script).</p><p>Regards<br />
Kurt</p></div><div id="comment-27711-info" class="comment-info"><span class="comment-age">(03 Dec '13, 06:33)</span> Kurt Knochner ♦</div></div><span id="27717"></span><div id="comment-27717" class="comment"><div id="post-27717-score" class="comment-score"></div><div class="comment-text"><p>Thank you!</p></div><div id="comment-27717-info" class="comment-info"><span class="comment-age">(03 Dec '13, 08:32)</span> Eliza Rana</div></div></div><div id="comment-tools-27694" class="comment-tools"></div><div class="clear"></div><div id="comment-27694-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

