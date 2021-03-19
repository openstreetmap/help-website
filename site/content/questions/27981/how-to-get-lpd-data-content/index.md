+++
type = "question"
title = "How to get LPD data content"
description = '''Hello, can you help me please, how to get LPD data file from my capture file? I know hot to get data file from IPP protocol, but I have problems with LPD (data file is divided into more frames - IPP data file is in one frame so I can just export it easily). Here is my printcap file: http://speedy.sh...'''
date = "2013-12-10T15:05:00Z"
lastmod = "2013-12-11T05:54:00Z"
weight = 27981
keywords = [ "data-file", "lpd" ]
aliases = [ "/questions/27981" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to get LPD data content](/questions/27981/how-to-get-lpd-data-content)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27981-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>can you help me please, how to get LPD data file from my capture file? I know hot to get data file from IPP protocol, but I have problems with LPD (data file is divided into more frames - IPP data file is in one frame so I can just export it easily). Here is my printcap file: <a href="http://speedy.sh/9ZEV7/LPDtext.pcapng">http://speedy.sh/9ZEV7/LPDtext.pcapng</a></p><p>Thank you! :)</p></div><div id="question-tags" class="tags-container tags">data-file lpd</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Dec '13, 15:05</strong></p><img src="https://secure.gravatar.com/avatar/be20005a55b5334aa5e61e2faeee32c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andyn&#39;s gravatar image" /><p>Andyn<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andyn has no accepted answers">0%</span></p></div></div><div id="comments-container-27981" class="comments-container"></div><div id="comment-tools-27981" class="comment-tools"></div><div class="clear"></div><div id="comment-27981-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28001"></span>

<div id="answer-container-28001" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28001-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Right click on any of the LDP frames and choose "Follow TCP Stream". In the pop-up window that appears, <strong>de-select</strong> 'Entire conversation' from the drop down box and choose the data direction that shows the string "%!PS-Adobe-3.0". Then select everything between <strong>%!PS-Adobe-3.0</strong> and <strong>%%EOF</strong> (including those two). Press CTRL-C (Copy) and paste it into a Text Editor. Then save it as <strong>test.ps</strong> (PostScript file).</p><p><strong>UPDATE</strong></p><p>Unfortunately copy-paste to an editor <strong>does not work</strong>, as there are some binary characters the will get lost. So, please use the following method:</p><ul><li>Right click on any of the LDP frames and choose "Follow TCP Stream".</li><li>In the pop-up window that appears, de-select 'Entire conversation' from the drop down box and choose the data direction that shows the string "%!PS-Adobe-3.0".</li><li>Save that in RAW format to a file: test.ps (PostScript file).</li><li>open test.ps with an editor that can handle binary data (I used gvim).</li><li>remove everything <strong>before</strong> <code>%!PS-Adobe-3.0</code></li><li>remove everything <strong>after</strong> <code>%%EOF</code></li><li>save the modified version</li><li>open it with <a href="http://pages.cs.wisc.edu/~ghost/gsview/">GSview</a></li></ul><p><a href="http://pages.cs.wisc.edu/~ghost/gsview/">GSview</a> shows the following content for your document:</p><pre><code>      Test tisku s LPD protokolem. 
      Úterý, 10. prosinec 2013 </code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Dec '13, 05:54</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Dec '13, 00:09</p></div></div><div id="comments-container-28001" class="comments-container"><span id="28016"></span><div id="comment-28016" class="comment"><div id="post-28016-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your reply. I tried it but it doesn't work. I print from Mac OS X 10.9 to Ubuntu 13.04. When I save these lines to pdf on my MAC, content of the new PDF file is the same like before (%!PS-Adobe-3.0...%%EOF). When I try it on Ubuntu, the opened PDF file is loading its content infinitely. But output of my printer (CUPS PDF virtual printer) is correct.</p></div><div id="comment-28016-info" class="comment-info"><span class="comment-age">(11 Dec '13, 11:34)</span> Andyn</div></div><span id="28018"></span><div id="comment-28018" class="comment"><div id="post-28018-score" class="comment-score"></div><div class="comment-text"><p>sorry, my fault. It's a PostScript file not a PDF file. I simply chose the wrong extension and I've corrected my answer.</p><p>If you want to view that file, you'll need a PostScript viewer, like <a href="http://pages.cs.wisc.edu/~ghost/gsview/">GSview</a> or Adobe Acrobat Reader.</p></div><div id="comment-28018-info" class="comment-info"><span class="comment-age">(11 Dec '13, 12:19)</span> Kurt Knochner ♦</div></div><span id="28024"></span><div id="comment-28024" class="comment"><div id="post-28024-score" class="comment-score"></div><div class="comment-text"><p>Thank you, but it didn't help. I think there is a problem in that data file. Structure of the PDF file looks strange. Or not? Maybe there is a problem with Mac...</p></div><div id="comment-28024-info" class="comment-info"><span class="comment-age">(11 Dec '13, 15:18)</span> Andyn</div></div><span id="28025"></span><div id="comment-28025" class="comment"><div id="post-28025-score" class="comment-score"></div><div class="comment-text"><p>I sent another file with IPP from Mac -&gt; Ubuntu and I have the same problem (but I had sent it with IPP from Ubuntu -&gt; Mac without problems).</p></div><div id="comment-28025-info" class="comment-info"><span class="comment-age">(11 Dec '13, 15:22)</span> Andyn</div></div><span id="28026"></span><div id="comment-28026" class="comment"><div id="post-28026-score" class="comment-score"></div><div class="comment-text"><p>It's <strong>not</strong> a PDF file. It's Postscript!</p><p>BTW: Do you think you will get the original document (PDF, word, etc.) if you extract IPP or LPR/LPD data? <strong>You won't</strong>. It's either PCL, Postscript, GDI or any other 'printer language'. In your case it is Postscript.</p></div><div id="comment-28026-info" class="comment-info"><span class="comment-age">(11 Dec '13, 15:28)</span> Kurt Knochner ♦</div></div><span id="28036"></span><div id="comment-28036" class="comment not_top_scorer"><div id="post-28036-score" class="comment-score"></div><div class="comment-text"><p>see the <strong>UPDATE</strong> in my answer.</p></div><div id="comment-28036-info" class="comment-info"><span class="comment-age">(12 Dec '13, 00:05)</span> Kurt Knochner ♦</div></div><span id="28045"></span><div id="comment-28045" class="comment not_top_scorer"><div id="post-28045-score" class="comment-score"></div><div class="comment-text"><p>It works now. Thank you very much!!! :)</p></div><div id="comment-28045-info" class="comment-info"><span class="comment-age">(12 Dec '13, 03:38)</span> Andyn</div></div><span id="28048"></span><div id="comment-28048" class="comment not_top_scorer"><div id="post-28048-score" class="comment-score"></div><div class="comment-text"><p>Good.</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-28048-info" class="comment-info"><span class="comment-age">(12 Dec '13, 04:51)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-28001" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-28001-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

