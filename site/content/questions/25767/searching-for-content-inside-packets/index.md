+++
type = "question"
title = "Searching for content inside packets ?"
description = '''Hello,  I want to find packets that have a specific string inside. Is this possible ? for example : find packets which have a &quot;Content-type:audio/mpeg&quot;.'''
date = "2013-10-08T15:35:00Z"
lastmod = "2015-05-28T21:15:00Z"
weight = 25767
keywords = [ "search" ]
aliases = [ "/questions/25767" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Searching for content inside packets ?](/questions/25767/searching-for-content-inside-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25767-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I want to find packets that have a specific string inside. Is this possible ? for example : find packets which have a "Content-type:audio/mpeg".</p></div><div id="question-tags" class="tags-container tags">search</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Oct '13, 15:35</strong></p><img src="https://secure.gravatar.com/avatar/94eb051be96f49a1665b097330fd97bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ychaouche&#39;s gravatar image" /><p>ychaouche<br />
<span class="score" title="31 reputation points">31</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ychaouche has one accepted answer">100%</span></p></div></div><div id="comments-container-25767" class="comments-container"><span id="25818"></span><div id="comment-25818" class="comment"><div id="post-25818-score" class="comment-score">1</div><div class="comment-text"><p>Hi. I'd just like to add that the Find dialog box can be easily mis-understood if you don't pay attention to the radio buttons that are selected by default. By default, the Find dialog box searches the Display Filter for the string you type in (personally, I'd like to see the options reversed so that String is selected by default). Anyway given your example, you want to to search for a String so you need to select that radio button and type in the search string.</p><p>Now that you have selected the String radio button, you need to pay attention to the Search In radio buttons. By default, the Find dialog box works searches for the string in the window containing the list of packets. But this ins't where your string is going to be found - you want to search inside the actual TCP data bytes inside the packet. So to search there, you need to select the Packet Bytes radio button. Again, personally, I'd like to see this option selected as the default.</p><p>The rest of the options are pretty self-expanatory. HTH - took me a while to figure out this dialog box.</p></div><div id="comment-25818-info" class="comment-info"><span class="comment-age">(09 Oct '13, 07:32)</span> smp</div></div><span id="25820"></span><div id="comment-25820" class="comment"><div id="post-25820-score" class="comment-score">1</div><div class="comment-text"><p>EDIT - I just realized my description of the Find dialog box and it's use of the Display Filter is incorrect. It appears to be similar to typing in a display filter, the difference being that the Find dialog box will select packets individually, while the display filter will display all matching packets. Learned something...</p></div><div id="comment-25820-info" class="comment-info"><span class="comment-age">(09 Oct '13, 07:44)</span> smp</div></div></div><div id="comment-tools-25767" class="comment-tools"></div><div class="clear"></div><div id="comment-25767-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="25841"></span>

<div id="answer-container-25841" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25841-score" class="post-score" title="current number of votes">5</div></div></td><td><div class="item-right"><div class="answer-body"><p>While the other answers are correct and do provide generic methods for finding arbitrary strings within a frame, it seems that in this case, the following filter is what was desired:</p><pre><code>http.content_type == &quot;audio/mpeg&quot;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Oct '13, 10:12</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-25841" class="comments-container"><span id="26292"></span><div id="comment-26292" class="comment"><div id="post-26292-score" class="comment-score"></div><div class="comment-text"><p>I wonder why sometimes it doesn't work, see this screenshot : <a href="http://i.imgur.com/HzrloMA.png">http://i.imgur.com/HzrloMA.png</a></p></div><div id="comment-26292-info" class="comment-info"><span class="comment-age">(22 Oct '13, 13:17)</span> ychaouche</div></div><span id="26294"></span><div id="comment-26294" class="comment"><div id="post-26294-score" class="comment-score"></div><div class="comment-text"><p>@ychaouche, can you share a capture file on <a href="http://cloudshark.org/">cloudshark</a> or elsewhere?</p></div><div id="comment-26294-info" class="comment-info"><span class="comment-age">(22 Oct '13, 14:04)</span> cmaynard ♦♦</div></div><span id="26295"></span><div id="comment-26295" class="comment"><div id="post-26295-score" class="comment-score"></div><div class="comment-text"><p>maybe due to whitespaces. Did you try</p><blockquote><p>http.content_type contains "audio/mpeg"</p></blockquote><p>or the HTTP connection used a port that was not in the list of 'known HTTP ports', and thus the HTTP dissector was unable to detect it as HTTP (Edit -&gt; Preferences -&gt; Protocols -&gt; HTTP -&gt; TCP Ports)</p></div><div id="comment-26295-info" class="comment-info"><span class="comment-age">(22 Oct '13, 14:06)</span> Kurt Knochner ♦</div></div><span id="26297"></span><div id="comment-26297" class="comment"><div id="post-26297-score" class="comment-score"></div><div class="comment-text"><p>I uploaded the file here : <a href="http://cloudshark.org/captures/471105b38cc1">http://cloudshark.org/captures/471105b38cc1</a></p><p>Note that when doing live capture I couldn't display-filter on http.content_type but when stoping the capture and loadin the file it worked.</p></div><div id="comment-26297-info" class="comment-info"><span class="comment-age">(22 Oct '13, 14:59)</span> ychaouche</div></div><span id="26304"></span><div id="comment-26304" class="comment"><div id="post-26304-score" class="comment-score">1</div><div class="comment-text"><p>Well, that's strange and I don't have an answer for you, only more questions. First off, what version of Wireshark are you using, and have you tried the latest development version, 1.11.0 to see if there's any difference?</p></div><div id="comment-26304-info" class="comment-info"><span class="comment-age">(22 Oct '13, 19:17)</span> cmaynard ♦♦</div></div><span id="26323"></span><div id="comment-26323" class="comment not_top_scorer"><div id="post-26323-score" class="comment-score"></div><div class="comment-text"><p>Ok I compiled and installed wireshark 1.10.2, now the display filter works as soon as the whole file is received. I was using 1.4.15.</p></div><div id="comment-26323-info" class="comment-info"><span class="comment-age">(23 Oct '13, 08:25)</span> ychaouche</div></div><span id="28590"></span><div id="comment-28590" class="comment not_top_scorer"><div id="post-28590-score" class="comment-score"></div><div class="comment-text"><p>Please see this again @cmaynard @KurtKnochner <a href="http://www.cloudshark.org/captures/d9916e96065a.">http://www.cloudshark.org/captures/d9916e96065a.</a> If you follow the tcp stream 0 you'll find that http.content_type is audio/mpeg but if you use the display filter http.content_type contains "audio" it doesn't show any packet.</p></div><div id="comment-28590-info" class="comment-info"><span class="comment-age">(05 Jan '14, 17:08)</span> ychaouche</div></div><span id="28602"></span><div id="comment-28602" class="comment not_top_scorer"><div id="post-28602-score" class="comment-score"></div><div class="comment-text"><p>This looks to be some sort of TCP reassembly bug, one which may or may not have been reported already (would need to search the <a href="https://bugs.wireshark.org/bugzilla/">open bug list</a> to find out). If you disable the TCP preference to <em>"Allow subdissector to reassemble TCP streams"</em>, then packet #6 will match your <strong><code>http.content_type contains "audio"</code></strong> filter.</p></div><div id="comment-28602-info" class="comment-info"><span class="comment-age">(06 Jan '14, 08:15)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-25841" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-25841-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25769"></span>

<div id="answer-container-25769" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25769-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use the following display filter:</p><blockquote><p>frame contains "Content-Type:audio/mpeg"</p></blockquote><p>or</p><blockquote><p>frame matches &lt;regexp&gt;</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '13, 15:45</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Oct '13, 13:32</p></div></div><div id="comments-container-25769" class="comments-container"><span id="25831"></span><div id="comment-25831" class="comment"><div id="post-25831-score" class="comment-score">1</div><div class="comment-text"><p>Or assuming this is http traffic:</p><pre><code>http.content_type == &quot;audio/mpeg&quot;</code></pre></div><div id="comment-25831-info" class="comment-info"><span class="comment-age">(09 Oct '13, 08:28)</span> cmaynard ♦♦</div></div><span id="25839"></span><div id="comment-25839" class="comment"><div id="post-25839-score" class="comment-score"></div><div class="comment-text"><p>If you put that as an answer I'd probably validate it.</p></div><div id="comment-25839-info" class="comment-info"><span class="comment-age">(09 Oct '13, 09:59)</span> ychaouche</div></div></div><div id="comment-tools-25769" class="comment-tools"></div><div class="clear"></div><div id="comment-25769-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42737"></span>

<div id="answer-container-42737" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42737-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is late reply to an interesting question. I think the problem is because the HTTP transaction didn't complete. According to the HTTP response header, the content length should be 7257219, but the body is only 7180879, so it's not complete.<br />
</p><p>I carved out the data as a mpeg file and it sounds pretty good :-)<br />
Here is the link to this beautiful song: <a href="https://www.dropbox.com/s/j3vts8zshjp99wk/tmp.mpeg?dl=0">https://www.dropbox.com/s/j3vts8zshjp99wk/tmp.mpeg?dl=0</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 May '15, 21:15</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p>pktUser1001<br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span> </br></br></p></div></div><div id="comments-container-42737" class="comments-container"><span id="58336"></span><div id="comment-58336" class="comment"><div id="post-58336-score" class="comment-score"></div><div class="comment-text"><p>Natalie Walker -- No One Else</p></div><div id="comment-58336-info" class="comment-info"><span class="comment-age">(26 Dec '16, 04:54)</span> ychaouche</div></div></div><div id="comment-tools-42737" class="comment-tools"></div><div class="clear"></div><div id="comment-42737-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

