+++
type = "question"
title = "How to split voip to saperate pcap files in easy way"
description = '''Have to large pcap file. How can i get just the voip thereout. I already tried with time selection (-A -B)'''
date = "2011-11-23T10:35:00Z"
lastmod = "2011-11-23T13:19:00Z"
weight = 7585
keywords = [ "pcap", "split", "voip" ]
aliases = [ "/questions/7585" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to split voip to saperate pcap files in easy way](/questions/7585/how-to-split-voip-to-saperate-pcap-files-in-easy-way)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7585-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Have to large pcap file. How can i get just the voip thereout. I already tried with time selection (-A -B)</p></div><div id="question-tags" class="tags-container tags">pcap split voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '11, 10:35</strong></p><img src="https://secure.gravatar.com/avatar/e1ad487a049ec97db8bda42d6b23fb07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tkwire&#39;s gravatar image" /><p>tkwire<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tkwire has no accepted answers">0%</span></p></div></div><div id="comments-container-7585" class="comments-container"></div><div id="comment-tools-7585" class="comment-tools"></div><div class="clear"></div><div id="comment-7585-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7587"></span>

<div id="answer-container-7587" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7587-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>In general splitting up files is easily done with editcap</p><p><code>editcap -c &lt;packets per file&gt; or editcap -i &lt;seconds per file&gt;</code></p><p>gives you two ways to split your too big capture file into smaller ones.</p><p>If you just want to filter voip out of the trace you could use tshark to grab frames matching a specific display filter and save those to a new trace like e.g. for cisco based voip with skinny as signalling protocol</p><pre><code>tshark -r &lt;name of your trace.pcap&gt; -R &quot;skinny or rtp&quot; -w &lt;name of the new tracefile&gt;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '11, 13:19</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-7587" class="comments-container"><span id="7612"></span><div id="comment-7612" class="comment"><div id="post-7612-score" class="comment-score"></div><div class="comment-text"><p>i allready tried with editcap packets per file and seconds per file. the problem is, then i get just the first peace of voip and the next peaces are lost. (in the first file is the first peace of voip and in the next file is no voip. so i can get just about 30sec voip from a 30min. voip)<br />
</p><p>with tshark i get this error massage: This application has requested the Runtime to terminate it in an unusual way. Please contact the application’s support team for more information</p><p>my File: 733009451 bytes packets more than 139400 packets (preview timeout) format: modified tcpdump-libpcap</p></div><div id="comment-7612-info" class="comment-info"><span class="comment-age">(24 Nov '11, 10:05)</span> tkwire</div></div><span id="7614"></span><div id="comment-7614" class="comment"><div id="post-7614-score" class="comment-score"></div><div class="comment-text"><p>I don't really get the problem why the "next pieces [of voip] are lost" when you use editcap. Tshark might not like the filesize of your pcap, so even if more complicated, maybe you try the following:</p><ul><li>Split up the trace with editcap into smaller files (e.g. 100,000 packets per file</li><li>create a new folder like 'filtered' or s.th.</li><li>run tshark -r ... -R "rtp or skinny" -w filtered&lt;filename&gt; for every editcap-outfile</li><li>run mergecap over all your traces in the filtered directory and see if the file is small enough to open with wireshark then</li></ul></div><div id="comment-7614-info" class="comment-info"><span class="comment-age">(24 Nov '11, 10:25)</span> Landi</div></div><span id="7615"></span><div id="comment-7615" class="comment"><div id="post-7615-score" class="comment-score"></div><div class="comment-text"><p>I get this massage when i run tshark Read filters were specified both with "-R" and wit additional command-line arguments</p></div><div id="comment-7615-info" class="comment-info"><span class="comment-age">(24 Nov '11, 11:01)</span> tkwire</div></div></div><div id="comment-tools-7587" class="comment-tools"></div><div class="clear"></div><div id="comment-7587-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

