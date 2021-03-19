+++
type = "question"
title = "How do I display absolute time and delta at the same time with tshark?"
description = '''Hi, When you use tshark without -V option, it would extract the frames to the format like below. $ tshark -tad -r &amp;lt;packet capture=&quot;&quot; file=&quot;&quot;&amp;gt; &amp;lt;frame number=&quot;&quot;&amp;gt; &amp;lt;absolute time=&quot;&quot;&amp;gt; &amp;lt;source ip=&quot;&quot;&amp;gt; &amp;lt;destination ip=&quot;&quot;&amp;gt; &amp;lt;description of=&quot;&quot; packet=&quot;&quot; such=&quot;&quot; as=&quot;&quot; nfs=&quot;&quot; v3=...'''
date = "2014-03-14T04:36:00Z"
lastmod = "2014-03-14T06:55:00Z"
weight = 30799
keywords = [ "tshark", "timestampe" ]
aliases = [ "/questions/30799" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I display absolute time and delta at the same time with tshark?](/questions/30799/how-do-i-display-absolute-time-and-delta-at-the-same-time-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30799-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>When you use tshark without -V option, it would extract the frames to the format like below.</p><p>$ tshark -tad -r &lt;packet capture="" file=""&gt; &lt;frame number=""&gt; &lt;absolute time=""&gt; &lt;source ip=""&gt; &lt;destination ip=""&gt; &lt;description of="" packet="" such="" as="" nfs="" v3="" getattr=""&gt;.</p><p>I would like to make it something like below.</p><p>&lt;frame number=""&gt; &lt;absolute time=""&gt; &lt;difference with="" previous="" packet=""&gt; &lt;source ip=""&gt; &lt;destination ip=""&gt; &lt;description of="" packet="" such="" as="" nfs="" v3="" getattr=""&gt;.</p><p>Is there an option to do such with shark or I need to have two different text and join the fields together?</p><p>Thank you in advance,</p><p>-hisao</p></div><div id="question-tags" class="tags-container tags">tshark timestampe</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '14, 04:36</strong></p><img src="https://secure.gravatar.com/avatar/98fd7d759e70809e826fd3a35e9fe2cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CarpeDiem&#39;s gravatar image" /><p>CarpeDiem<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CarpeDiem has no accepted answers">0%</span></p></div></div><div id="comments-container-30799" class="comments-container"></div><div id="comment-tools-30799" class="comment-tools"></div><div class="clear"></div><div id="comment-30799-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30801"></span>

<div id="answer-container-30801" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30801-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is very similar to what was asked in the "<a href="http://ask.wireshark.org/questions/30393/tshark-how-to-output-date-in-iso-format">tshark - How to output date in ISO format?</a>" question, so you can refer to my answer there, but in a nutshell for your particular case:</p><ul><li>Start <strong>Wireshark</strong> and add 2 columns, using <code>Edit -&gt; Preferences -&gt; Columns -&gt; Add</code>. These 2 columns are the "Absolute date and time" and "Delta time displayed" columns. Give them appropriate names, e.g., "<code>AbsTime</code>" and "<code>DeltaTime</code>", respectively. If you don't want these columns displayed in <strong>Wireshark</strong> itself, then they can be marked as hidden by clearing the checkmark in the <em>"Displayed"</em> box.</li><li>Save the column preferences and exit <strong>Wireshark</strong>.</li><li><p>From the command-line, you can now run <code>tshark</code> as follows:</p><p>tshark.exe -r file.pcap -T fields -E header=y -e frame.number -e col.AbsTime -e col.DeltaTime -e col.Source -e col.Destination -e col.Protocol -e col.Length -e col.Info</p></li></ul><p>You can use <code>-e frame.time</code> instead of <code>-e col.AbsTime</code> if you prefer that format, in which case you don't have to add the "<code>AbsTime</code>" column in <strong>Wireshark</strong>. You can also use <code>-e frame.len</code> instead of <code>-e col.Length</code> as they're essentially the same.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Mar '14, 06:55</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-30801" class="comments-container"><span id="30809"></span><div id="comment-30809" class="comment"><div id="post-30809-score" class="comment-score"></div><div class="comment-text"><p>Thank you. This seems what I needed.</p></div><div id="comment-30809-info" class="comment-info"><span class="comment-age">(15 Mar '14, 05:20)</span> CarpeDiem</div></div><span id="30813"></span><div id="comment-30813" class="comment"><div id="post-30813-score" class="comment-score"></div><div class="comment-text"><p><code> $ tshark -r ./snoop-e1000g0-20140315-123743.out -T fields -E header=y -e frame.number -e frame.time -e frame.time_delta -e ip.src -e ip.dst -e tcp.srcport | head frame.number    frame.time  frame.time_delta    ip.src  ip.dst  tcp.srcport 1   Mar 15, 2014 21:37:43.470376000 0.000000000 192.168.150.1   192.168.150.18  49906 2   Mar 15, 2014 21:37:43.470787000 0.000411000 192.168.150.1   192.168.150.18  49906 3   Mar 15, 2014 21:37:43.470805000 0.000018000 192.168.150.18  192.168.150.1   215 4   Mar 15, 2014 21:37:43.471398000 0.000593000 192.168.150.1   192.168.150.18  49906 5   Mar 15, 2014 21:37:43.471800000 0.000402000 192.168.150.1   192.168.150.18  49906 6   Mar 15, 2014 21:37:43.471813000 0.000013000 192.168.150.18  192.168.150.1   215 7   Mar 15, 2014 21:37:43.472568000 0.000755000 192.168.150.18  192.168.150.1   215 8   Mar 15, 2014 21:37:43.472859000 0.000291000 192.168.150.1   192.168.150.18  49906 9   Mar 15, 2014 21:37:43.811069000 0.338210000 192.168.150.1   192.168.150.255</code></p><p>This however does not show me the payload. It seems that I need to look into the reference a bit more. "Display Filter Reference": <a href="http://www.wireshark.org/docs/dfref/#section_m">http://www.wireshark.org/docs/dfref/#section_m</a></p></div><div id="comment-30813-info" class="comment-info"><span class="comment-age">(15 Mar '14, 06:36)</span> CarpeDiem</div></div><span id="30815"></span><div id="comment-30815" class="comment"><div id="post-30815-score" class="comment-score"></div><div class="comment-text"><p>You seem to be asking a different question, <em>"How to show the payload?"</em> Please post a new question instead of continuing to comment on this one, which already has an answer.</p></div><div id="comment-30815-info" class="comment-info"><span class="comment-age">(15 Mar '14, 07:40)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-30801" class="comment-tools"></div><div class="clear"></div><div id="comment-30801-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

