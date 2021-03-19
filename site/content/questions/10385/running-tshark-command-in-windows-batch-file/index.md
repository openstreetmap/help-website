+++
type = "question"
title = "running tshark command in windows batch file"
description = '''I have written a batch file that runs a tshark command to filter fields from a wireshark pcap file and write them to a csv file. When i ran on the windows cmd CLI, i had to change the current working directory to the wireshark folder directory in the My Computer&amp;gt; Program Files, so i changed the c...'''
date = "2012-04-22T20:25:00Z"
lastmod = "2012-04-23T00:54:00Z"
weight = 10385
keywords = [ "batch", "tshark" ]
aliases = [ "/questions/10385" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [running tshark command in windows batch file](/questions/10385/running-tshark-command-in-windows-batch-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10385-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10385-score" class="post-score" title="current number of votes">0</div><span id="post-10385-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have written a batch file that runs a tshark command to filter fields from a wireshark pcap file and write them to a csv file. When i ran on the windows cmd CLI, i had to change the current working directory to the wireshark folder directory in the My Computer&gt; Program Files, so i changed the current working directory in the batch file so that it would run the same way as i ran in the windows cmd CLI.</p><p>However, when i ran the below batch script, the output csv file was blank. How do i correct this batch script so that i can see the contents in the output csv file generated using wireshark's tshark command?</p><p>I wrote the batch file like this.</p><pre><code>@echo off    
set curr_dir=%cd%
chdir /D cd..    
chdir /D cd..    
chdir /D cd program files    
chdir /D cd wireshark    
tshark -T fields -n -r &quot;C:\Users\L33604\Desktop\SynFlood Sample.pcap&quot; -E separator=, -e ip.src -e ip.dst &gt; &quot;C:\Users\L33604\Desktop\logcapture.txt&quot;</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-batch" rel="tag" title="see questions tagged &#39;batch&#39;">batch</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '12, 20:25</strong></p><img src="https://secure.gravatar.com/avatar/94990dfa38fcf1b33157bef842da0291?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="misteryuku&#39;s gravatar image" /><p><span>misteryuku</span><br />
<span class="score" title="20 reputation points">20</span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="misteryuku has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Apr '12, 04:41</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-10385" class="comments-container"></div><div id="comment-tools-10385" class="comment-tools"></div><div class="clear"></div><div id="comment-10385-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10390"></span>

<div id="answer-container-10390" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10390-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10390-score" class="post-score" title="current number of votes">0</div><span id="post-10390-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><pre><code>tshark -T fields -n -r &quot;C:UsersL33604DesktopSynFlood Sample.pcap&quot; -E separator=, -e ip.src -e ip.dst &gt; &quot;C:UsersL33604Desktoplogcapture.txt&quot;</code></pre><p>That will only work if the file <code>UsersL33604DesktopSynFlood Sample.pcap</code> is in the current directory, i.e. in <code>C:\Program Files\Wireshark</code>. It probably isn't there.</p><p>You would either need to do</p><pre><code>tshark -T fields -n -r &quot;C:{full path leading up to that file}\UsersL33604DesktopSynFlood Sample.pcap&quot; -E separator=, -e ip.src -e ip.dst &gt; &quot;C:UsersL33604Desktoplogcapture.txt&quot;</code></pre><p>(which will, BTW, put <code>UsersL33604Desktoplogcapture.txt</code> into the current directory; if you don't want that, you'll have to specify the full path there as well), or do</p><pre><code>&quot;C:\Program Files\Wireshark\tshark&quot; -T fields -n -r &quot;C:UsersL33604DesktopSynFlood Sample.pcap&quot; -E separator=, -e ip.src -e ip.dst &gt; &quot;C:UsersL33604Desktoplogcapture.txt&quot;</code></pre><p>in whatever directory contains the <code>UsersL33604DesktopSynFlood Sample.pcap</code>, or set your <code>Path</code> environment variable to include <code>C:\Program Files\Wireshark\tshark</code>, in which case just</p><pre><code>tshark -T fields -n -r &quot;C:UsersL33604DesktopSynFlood Sample.pcap&quot; -E separator=, -e ip.src -e ip.dst &gt; &quot;C:UsersL33604Desktoplogcapture.txt&quot;</code></pre><p>will work.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '12, 00:54</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-10390" class="comments-container"></div><div id="comment-tools-10390" class="comment-tools"></div><div class="clear"></div><div id="comment-10390-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

