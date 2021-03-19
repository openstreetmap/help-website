+++
type = "question"
title = "Help with a tshark cmd"
description = '''Hey guys, Im not new to tshark but I&#x27;m trying to make my life quite a bit easier with command lines and Im having quite a bit of difficulty. I can convert .pcap&#x27;s to .txt&#x27;s just fine, but the summary information isn&#x27;t enough. What I was hoping to get is [SEQ/ACK Analysis] that are located in the TCP...'''
date = "2013-10-24T12:37:00Z"
lastmod = "2013-11-12T14:32:00Z"
weight = 26374
keywords = [ "txt", "conversion", "cmd", "pcap", "tshark" ]
aliases = [ "/questions/26374" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Help with a tshark cmd](/questions/26374/help-with-a-tshark-cmd)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26374-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26374-score" class="post-score" title="current number of votes">0</div><span id="post-26374-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey guys, Im not new to tshark but I'm trying to make my life quite a bit easier with command lines and Im having quite a bit of difficulty.</p><p>I can convert .pcap's to .txt's just fine, but the summary information isn't enough. What I was hoping to get is [SEQ/ACK Analysis] that are located in the TCP files and the [Domain Name System Query] information in the DNS files.</p><p>Is it possible to convert a pcap to a txt file and retain this information?</p><p>Thanks Guys, Z</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-txt" rel="tag" title="see questions tagged &#39;txt&#39;">txt</span> <span class="post-tag tag-link-conversion" rel="tag" title="see questions tagged &#39;conversion&#39;">conversion</span> <span class="post-tag tag-link-cmd" rel="tag" title="see questions tagged &#39;cmd&#39;">cmd</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Oct '13, 12:37</strong></p><img src="https://secure.gravatar.com/avatar/fbc5b3a06e0bdd9408c2356da21566c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nefarii&#39;s gravatar image" /><p><span>Nefarii</span><br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nefarii has one accepted answer">100%</span></p></div></div><div id="comments-container-26374" class="comments-container"></div><div id="comment-tools-26374" class="comment-tools"></div><div class="clear"></div><div id="comment-26374-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="26906"></span>

<div id="answer-container-26906" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26906-score" class="post-score" title="current number of votes">0</div><span id="post-26906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Nefarii has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The more I dig into tshark, the more I realize how little I know. I am providing the following examples to help people that come across this that are at the same skill level that I was when I first asked this. The man page is great for when you have a handle on things, but impossible to read until then.</p><p><strong>Basics:</strong></p><pre><code>tshark -r C:\this.pcap &gt; C:\that.txt  //writes the pcap to txt single line

tshark -r C:\this.pcap -V &gt; C:\that.txt //writes all the lines of pcap to text

tshark -r C:\this.pcap -VV &gt; C:\that.txt //single line but more information

tshark -r C:\this.pcap -VVV &gt; C:\that.txt //single line and even more information

tshark -r C:\this.pcap -t a &gt; C:\that.txt //single line but uses the Real Time instead of log time

tshark -r C:\this.pcap -t ad &gt; C:\that.txt //single line but uses the Real Time with date

tshark -r C:\this.pcap -t d &gt; C:\that.txt //single line with delta between frames</code></pre><p><strong>More Complicated:</strong></p><pre><code>tshark -r C:\this.pcap -T Fields -e frame.number -e frame.time &gt; C:\that.txt 
//converts the file but only display the frame number and the frame time

tshark -r C:\this.pcap -T Fields -e frame.number -e frame.time -e ip.src -e ip.dst &gt; C:\that.txt //Same as above but adds the ip source and destination fields

tshark -r C:\this.pcap -T Fields -e frame.number -e frame.time -E separator=\ &gt; C:\that.txt 
//Same as the first one but seperates the column with a &quot;\&quot; (any single character can be used)

tshark -r C:\this.pcap -T Fields -e frame.number -e frame.time -E separator=\ -Y DNS &gt; C:\that.txt //Same as the last one but filters out all DNS packets

tshark -r C:\this.pcap -T Fields -e frame.number -e frame.time -E separator=\ -2 -Y &quot;tcp.flags.syn &amp;&amp; tcp.flags.fin&quot; 
//Same as the last one but this time filters for .syn and .fin requests (notice the -2)</code></pre><p>For reference on syntax, please refer to the "Man Page": <a href="http://www.wireshark.org/docs/man-pages/tshark.html">http://www.wireshark.org/docs/man-pages/tshark.html</a></p><p>For reference on all possible field options "-e": <a href="http://www.wireshark.org/docs/dfref/">http://www.wireshark.org/docs/dfref/</a></p><p>For reference on possible filters -Y or -R: The easiest of I have found is too just go into wireshark and create the filter string as needed.</p><p>I hope this is as useful as it was too me once I finally figured it out. Enjoy : )</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '13, 14:32</strong></p><img src="https://secure.gravatar.com/avatar/fbc5b3a06e0bdd9408c2356da21566c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nefarii&#39;s gravatar image" /><p><span>Nefarii</span><br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nefarii has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Nov '13, 02:46</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-26906" class="comments-container"></div><div id="comment-tools-26906" class="comment-tools"></div><div class="clear"></div><div id="comment-26906-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26377"></span>

<div id="answer-container-26377" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26377-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26377-score" class="post-score" title="current number of votes">0</div><span id="post-26377-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Does <code>tshark -O tcp,dns</code> give you what you're looking for?</p><p>If not, feel free to experiment with the various <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark</a> options, such as <code>-T fields -e field1 -e field2</code>, etc., as maybe that would be more useful to you?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Oct '13, 14:56</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-26377" class="comments-container"><span id="26379"></span><div id="comment-26379" class="comment"><div id="post-26379-score" class="comment-score"></div><div class="comment-text"><p>Can you give me a couple commands of each one? Im still trying to get a hang of the snytax. Say my pcap file is C:\this.pcap, what would a few commands be to start playing with the fields? This website <a href="http://www.wireshark.org/docs/man-pages/tshark.html">http://www.wireshark.org/docs/man-pages/tshark.html</a> seems only useful to someone that has the basics of the cmd line down already.</p></div><div id="comment-26379-info" class="comment-info"><span class="comment-age">(24 Oct '13, 15:16)</span> <span class="comment-user userinfo">Nefarii</span></div></div><span id="26381"></span><div id="comment-26381" class="comment"><div id="post-26381-score" class="comment-score"></div><div class="comment-text"><p>The man page provides an example:</p><pre><code>tshark -T fields -e frame.number -e ip.addr -e udp -e col.info</code></pre><p>Here's another one for some TCP-related stuff you might be interested in:</p><pre><code>tshark -r file -Y tcp.analysis.flags -T fields -e frame.number -e tcp.analysis.duplicate_ack -e tcp.analysis.lost_segment -e tcp.analysis.bytes_in_flight</code></pre></div><div id="comment-26381-info" class="comment-info"><span class="comment-age">(24 Oct '13, 15:37)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="26403"></span><div id="comment-26403" class="comment"><div id="post-26403-score" class="comment-score"></div><div class="comment-text"><p>How do you use the -V option?</p></div><div id="comment-26403-info" class="comment-info"><span class="comment-age">(25 Oct '13, 09:18)</span> <span class="comment-user userinfo">Nefarii</span></div></div><span id="26404"></span><div id="comment-26404" class="comment"><div id="post-26404-score" class="comment-score"></div><div class="comment-text"><blockquote><p>How do you use the -V option?</p></blockquote><pre><code>tshark -V</code></pre><p>It's that simple. But I doubt it's what you're after.</p></div><div id="comment-26404-info" class="comment-info"><span class="comment-age">(25 Oct '13, 09:27)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="26405"></span><div id="comment-26405" class="comment"><div id="post-26405-score" class="comment-score"></div><div class="comment-text"><p>lol sorry I should of been more specific, how do you use the -v option while outputting a file? right now the best I can gather is tshark -i - &lt; C:\this.pcap &gt; -V C:\this.txt or tshark -r C:\this.pcap -V -w C:\this.txt neither of which seems to work</p></div><div id="comment-26405-info" class="comment-info"><span class="comment-age">(25 Oct '13, 09:59)</span> <span class="comment-user userinfo">Nefarii</span></div></div><span id="26406"></span><div id="comment-26406" class="comment not_top_scorer"><div id="post-26406-score" class="comment-score"></div><div class="comment-text"><p><code>tshark -r C:\this.pcap -V -w C:\thiscopy.pcap</code></p><p>The file specified with the <code>-w</code> option is a pcap file, not a text file. If you want a text file as output, but you also want to see the packets on the screen at the same time, then you should look into using something like <a href="http://unixhelp.ed.ac.uk/CGI/man-cgi?tee">tee</a>, as in:</p><pre><code>tshark -r C:\this.pcap -V | tee C:\this.txt</code></pre><p>If you're on Windows, then <code>tee</code> is available with <a href="http://www.cygwin.com/"><code>cygwin</code></a>.</p></div><div id="comment-26406-info" class="comment-info"><span class="comment-age">(25 Oct '13, 10:15)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-26377" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-26377-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

