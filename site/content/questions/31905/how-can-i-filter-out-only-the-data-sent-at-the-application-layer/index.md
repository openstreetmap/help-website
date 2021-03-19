+++
type = "question"
title = "How can I filter out only the data sent at the Application layer?"
description = '''Network has Application-Presentation-Session-Transport-Net-data-Physical layers. Assume a GDB Client and Server talk and exchange 10 packets. I want to set the filter so that I see the 10 packets exchanged as seen by the App layer only in a chronological order. I dont want to see any of the other pa...'''
date = "2014-04-16T13:59:00Z"
lastmod = "2014-04-17T00:46:00Z"
weight = 31905
keywords = [ "network" ]
aliases = [ "/questions/31905" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How can I filter out only the data sent at the Application layer?](/questions/31905/how-can-i-filter-out-only-the-data-sent-at-the-application-layer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31905-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Network has Application-Presentation-Session-Transport-Net-data-Physical layers. Assume a GDB Client and Server talk and exchange 10 packets. I want to set the filter so that I see the 10 packets exchanged as seen by the App layer only in a chronological order. I dont want to see any of the other packets. Meaning let us assume following is the packets exchanged Client(First column is Client) The second column is Server</p><p>"Hello how are you" is sent --&gt;<br />
</p><pre><code>                         &lt;--         &quot;I am fine&quot;</code></pre><p>"What time is it?" --&gt;<br />
</p><pre><code>                         &lt;--         &quot;Around noon&quot;</code></pre><p>So on and so forth. The filter should just show the strings being exchanged.</p><p>One more question. Yesterday Quadratic helped me. Here is a followup question. In the below commandline feature if my IP's are 10.x.x.x and 10.y.y.y and the names are "Client" and "Server" what do I type for the -i option. -i {what do I type here?}" C:\Program Files\Wireshark\dumpcap.exe -c 50 -i {interface name or number} -w {wherever you want to save the packet capture file}</p></div><div id="question-tags" class="tags-container tags">network</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '14, 13:59</strong></p><img src="https://secure.gravatar.com/avatar/5e0009f71c27b493081e07b2dc32a672?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="agvardha&#39;s gravatar image" /><p>agvardha<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="agvardha has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Apr '14, 14:04</p></div></div><div id="comments-container-31905" class="comments-container"></div><div id="comment-tools-31905" class="comment-tools"></div><div class="clear"></div><div id="comment-31905-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31910"></span>

<div id="answer-container-31910" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31910-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>"I want to set the filter so that I see the 10 packets exchanged as seen by the App layer only in a chronological order. I dont want to see any of the other packets."</p><p>Try <code>data.data</code> to get only packets that contain data.</p><p>"The filter should just show the strings being exchanged"</p><p>To see the strings that are exchanged in the packet list pane you need</p><ul><li>Edit -&gt; Preferences -&gt; Protocol -&gt; Data: Show data as text: check this item</li><li>Add a New Column to show a 'custom' column "data.text" in the packet list<br />
</li></ul><p><img src="https://osqa-ask.wireshark.org/upfiles/Selection_044.png" alt="alt text" /></p><p>Hope this answers <em>this</em> question.</p><p>For "One more question" open "one more thread" to keep the Q&amp;A site (vs. forum) tidy ;-)<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '14, 00:46</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 17 Apr '14, 02:56</p></div></div><div id="comments-container-31910" class="comments-container"><span id="31915"></span><div id="comment-31915" class="comment"><div id="post-31915-score" class="comment-score">2</div><div class="comment-text"><p>Grrr. It's <strong>not</strong> a forum :-)</p></div><div id="comment-31915-info" class="comment-info"><span class="comment-age">(17 Apr '14, 02:21)</span> grahamb ♦</div></div><span id="32005"></span><div id="comment-32005" class="comment"><div id="post-32005-score" class="comment-score"></div><div class="comment-text"><p>well, it's a 'forum' for questions and answers ;-))</p></div><div id="comment-32005-info" class="comment-info"><span class="comment-age">(19 Apr '14, 16:43)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-31910" class="comment-tools"></div><div class="clear"></div><div id="comment-31910-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

