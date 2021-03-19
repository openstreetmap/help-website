+++
type = "question"
title = "Filtering Using TShark to generate an Output"
description = '''I stumbled across this link and found it potentially advantageous if I can learn how to use it: How to Export Packet Summary to Text File My problem is that the filter here does not work. This is what I put into cmd: &quot;C:&#92;Program Files&#92;Wireshark&#92;tshark.exe&quot; -r &quot;C:&#92;temp&#92;filename.pcap&quot; -Y &quot;ip&quot; -o &quot;gui....'''
date = "2015-11-23T09:08:00Z"
lastmod = "2015-11-23T13:07:00Z"
weight = 47870
keywords = [ "filter", "ip", "cmd", "tshark", "wireshark1.10.0" ]
aliases = [ "/questions/47870" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Filtering Using TShark to generate an Output](/questions/47870/filtering-using-tshark-to-generate-an-output)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47870-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47870-score" class="post-score" title="current number of votes">0</div><span id="post-47870-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I stumbled across this link and found it potentially advantageous if I can learn how to use it:</p><p><a href="https://ask.wireshark.org/questions/25936/how-to-export-packet-summary-to-text-file">How to Export Packet Summary to Text File</a></p><p>My problem is that the filter here does not work.<br />
This is what I put into cmd:<br />
<code>"C:\Program Files\Wireshark\tshark.exe" -r "C:\temp\filename.pcap" -Y "ip" -o "gui.column.format:\"Info\",\"%i\"" &gt; "C:\temp\filename.txt" </code><br />
<br />
Instead of getting filtered results, I get an empty file.</p><p>I am simply trying to grab the lines that are ip only, just as I would if I were in Wireshark filtering "ip" of an existing pcap file.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-cmd" rel="tag" title="see questions tagged &#39;cmd&#39;">cmd</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-wireshark1.10.0" rel="tag" title="see questions tagged &#39;wireshark1.10.0&#39;">wireshark1.10.0</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '15, 09:08</strong></p><img src="https://secure.gravatar.com/avatar/3a4bc2ba5c09d24f214dc472eb5b7993?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Midimistro&#39;s gravatar image" /><p><span>Midimistro</span><br />
<span class="score" title="11 reputation points">11</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Midimistro has one accepted answer">50%</span> </br></br></p></div></div><div id="comments-container-47870" class="comments-container"></div><div id="comment-tools-47870" class="comment-tools"></div><div class="clear"></div><div id="comment-47870-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="47887"></span>

<div id="answer-container-47887" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47887-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47887-score" class="post-score" title="current number of votes">0</div><span id="post-47887-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Midimistro has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I finally figured it out. There was nothing wrong with my file except a missing preference setting. It was apparently the preferences for Wireshark that needed to be set in order for it to properly filter the <em>type</em> of .pcap files I am using.<br />
<br />
What I had to add was this (separate from the other -o):<br />
<br />
<code>-o "uat:user_dlts:\"User 8 (DLT=155)\",\"pxt\",\"0\",\"\",\"0\",\"\""</code><br />
<br />
This is because I was bringing the .pcaps from a different application (Agilent) that used different analysis tools. Thus the examples above wouldn't find anything anyway since tshark wouldn't know how to parse anything except the time and packet number under those conditions (aka if it didn't have the above preference).<br />
<br />
Thanks for the help anyway!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '15, 13:07</strong></p><img src="https://secure.gravatar.com/avatar/3a4bc2ba5c09d24f214dc472eb5b7993?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Midimistro&#39;s gravatar image" /><p><span>Midimistro</span><br />
<span class="score" title="11 reputation points">11</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Midimistro has one accepted answer">50%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Nov '15, 13:08</strong> </span></p></div></div><div id="comments-container-47887" class="comments-container"></div><div id="comment-tools-47887" class="comment-tools"></div><div class="clear"></div><div id="comment-47887-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47872"></span>

<div id="answer-container-47872" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47872-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47872-score" class="post-score" title="current number of votes">0</div><span id="post-47872-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I am simply trying to grab the lines that are ip only, just as I would if I were in Wireshark filtering "ip" of an existing pcap file.</p></blockquote><p>Then please try this:</p><blockquote><p>tshark -nr input.pcap -Y "ip" &gt; c:\temp\output.txt</p></blockquote><p>There is no need to redefine the column formar, unless you are looking for something very special.</p><p>If you want to write a new pcap file, please try this</p><blockquote><p>tshark -nr input.pcap -Y "IP" -w output.pcap</p></blockquote><p>BTW: the correct format for gui.column.format would be:</p><blockquote><p>tshark -nr input.pcap -Y "ip" -o "gui.column.format:\"Info\", \"%i\""</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '15, 09:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Nov '15, 10:30</strong> </span></p></div></div><div id="comments-container-47872" class="comments-container"><span id="47874"></span><div id="comment-47874" class="comment"><div id="post-47874-score" class="comment-score"></div><div class="comment-text"><p>First, I am trying to grab only the info column of each line that is ip only. Second, the pcap file is a file that already exists (captured by a different program and converted to pcap), not as a live capture, like you showed here. Third, the output file desired is a .txt file.</p><p>"C:\Program Files\Wireshark\tshark.exe" -r "C:\temp\filename.pcap" -o "gui.column.format:\"Info\",\"%i\"" &gt; "C:\temp\filename.txt" works, BUT it prints out every line, which is not what I want.</p><p>Lastly, I would think {-Y "ip"} or {-2 -r &lt;filename.pcap&gt; -R "ip"} would work, but as I said before, both of them turn out blanks. If I try -O on the other hand, it generates a file even bigger than the pcap and that is not open-able.</p><p>Any ideas?</p></div><div id="comment-47874-info" class="comment-info"><span class="comment-age">(23 Nov '15, 10:19)</span> <span class="comment-user userinfo">Midimistro</span></div></div><span id="47875"></span><div id="comment-47875" class="comment"><div id="post-47875-score" class="comment-score"></div><div class="comment-text"><blockquote><p>not as a live capture, like you showed here.</p></blockquote><p><code>-ni</code> was just a typo. I corrected it to <code>-nr</code></p><blockquote><p>BUT it prints out every line, which is not what I want.</p></blockquote><p>O.K. can you please post an example of <strong>what</strong> you want?</p><blockquote><p>Lastly, I would think {-Y "ip"} or {-2 -r &lt;filename.pcap&gt; -R "ip"} would work, but as I said before, both of them turn out blanks.</p></blockquote><p>It works on my system, so I assume it will work on yours as well.</p><p>Please run the following command. It should show at least some output if there is IP traffic in the pcap file.</p><blockquote><p>tshark -nr input.pcap -Y "ip"</p></blockquote><p>Regards Kurt</p></div><div id="comment-47875-info" class="comment-info"><span class="comment-age">(23 Nov '15, 10:32)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-47872" class="comment-tools"></div><div class="clear"></div><div id="comment-47872-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

