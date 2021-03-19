+++
type = "question"
title = "Save packets from a filter into file"
description = '''Hi All,  I have captured packets over network for some time, I have a big file by now . Now I want to save all the packets to or from a IP into separate file,because I don&#x27;t need remaining . I used (ip.addr eq XX.XX.XX.XX) filter but it taking so much time in filtering and analyzing. Any help in thi...'''
date = "2011-01-19T00:34:00Z"
lastmod = "2011-01-21T12:51:00Z"
weight = 1808
keywords = [ "save", "packets" ]
aliases = [ "/questions/1808" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Save packets from a filter into file](/questions/1808/save-packets-from-a-filter-into-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1808-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All, I have captured packets over network for some time, I have a big file by now . Now I want to save all the packets to or from a IP into separate file,because I don't need remaining . I used (ip.addr eq XX.XX.XX.XX) filter but it taking so much time in filtering and analyzing. Any help in this would be appriciated. Thanks, Kris.</p></div><div id="question-tags" class="tags-container tags">save packets</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jan '11, 00:34</strong></p><img src="https://secure.gravatar.com/avatar/54cba49b0385c265283e8909ca8375cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kris&#39;s gravatar image" /><p>Kris<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kris has no accepted answers">0%</span></p></div></div><div id="comments-container-1808" class="comments-container"></div><div id="comment-tools-1808" class="comment-tools"></div><div class="clear"></div><div id="comment-1808-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="1810"></span>

<div id="answer-container-1810" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1810-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is what I would do:</p><ol><li>If your file is so large that tshark won't be able to read it completely I'd chop it into smaller pieces using <strong>editcap -c 100000 &lt;infile&gt; &lt;chunkfile&gt;</strong>, which gives you chunks of 100,000 frames each. Otherwise you do the tshark in step2 directly on your source file.</li><li>write a batch that uses tshark on each chunk. The tshark commands would look something like this: <strong>tshark -r &lt;chunkfile##&gt; -R "ip.addr eq XX.XX.XX.XX" -w &lt;filteredfile##&gt;</strong></li><li>Use mergecap to merge all filtered files into one single file again: **mergecap -a &lt;finalfile&gt; &lt;filteredfile01&gt; &lt;filteredfile02&gt; &lt;filteredfile03&gt;...</li></ol><p>You should end up with one file containing only the filtered IP. Hope it helps.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jan '11, 06:19</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-1810" class="comments-container"><span id="1822"></span><div id="comment-1822" class="comment"><div id="post-1822-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper, you solved my issue.</p></div><div id="comment-1822-info" class="comment-info"><span class="comment-age">(19 Jan '11, 20:39)</span> Kris</div></div></div><div id="comment-tools-1810" class="comment-tools"></div><div class="clear"></div><div id="comment-1810-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1859"></span>

<div id="answer-container-1859" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1859-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can also use tcpdump (or WinDump if you are using Windows). It is quicker as it does not do full dissection of each packet. This is was you would be using:</p><pre><code>tcpdump -r &lt;infile&gt; -w &lt;outfile&gt; host x.x.x.x</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '11, 12:51</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1859" class="comments-container"><span id="1901"></span><div id="comment-1901" class="comment"><div id="post-1901-score" class="comment-score"></div><div class="comment-text"><p>Thanks SYNbit for the info, this is very helpful where I can filter out the packets while capturing itself.</p></div><div id="comment-1901-info" class="comment-info"><span class="comment-age">(23 Jan '11, 20:39)</span> Kris</div></div><span id="1929"></span><div id="comment-1929" class="comment"><div id="post-1929-score" class="comment-score"></div><div class="comment-text"><p>If you run tcpdump on a network card instead of reading from file (leave out the "-r &lt;infile&gt;" part from Sake's answer) you should be doing just that. You might have to specify the network card if you've got multiple of them.</p></div><div id="comment-1929-info" class="comment-info"><span class="comment-age">(25 Jan '11, 09:29)</span> Jasper ♦♦</div></div></div><div id="comment-tools-1859" class="comment-tools"></div><div class="clear"></div><div id="comment-1859-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1809"></span>

<div id="answer-container-1809" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1809-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You have several options:</p><ul><li>Script it, using tshark</li><li>Use a faster disk</li><li>Use more / faster memory</li><li>Use a faster CPU (in clock cycles, not cores)</li><li>Recompile Wireshark / Tshark without zlib</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jan '11, 05:52</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-1809" class="comments-container"></div><div id="comment-tools-1809" class="comment-tools"></div><div class="clear"></div><div id="comment-1809-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

