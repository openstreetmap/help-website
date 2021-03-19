+++
type = "question"
title = "problem in opening large size wireshark file"
description = '''Hi, I have a file captured as tcpdump which is the network traffic for about 1 Hour and the file size is about 1G. When I want to open the file using wireshark it takes long time and at the end via error message wireshark will be closed. Do you have any solution to open the whole file? Can I open it...'''
date = "2013-02-19T03:50:00Z"
lastmod = "2013-02-19T04:25:00Z"
weight = 18730
keywords = [ "large", "size", "data", "wireshark" ]
aliases = [ "/questions/18730" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [problem in opening large size wireshark file](/questions/18730/problem-in-opening-large-size-wireshark-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18730-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18730-score" class="post-score" title="current number of votes">0</div><span id="post-18730-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a file captured as tcpdump which is the network traffic for about 1 Hour and the file size is about 1G. When I want to open the file using wireshark it takes long time and at the end via error message wireshark will be closed.</p><p>Do you have any solution to open the whole file? Can I open it if I have a PC with higher RAM?</p><p>Best regards</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-large" rel="tag" title="see questions tagged &#39;large&#39;">large</span> <span class="post-tag tag-link-size" rel="tag" title="see questions tagged &#39;size&#39;">size</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Feb '13, 03:50</strong></p><img src="https://secure.gravatar.com/avatar/5088f143b43418c81199759c491b24c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MGBRU&#39;s gravatar image" /><p><span>MGBRU</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MGBRU has no accepted answers">0%</span></p></div></div><div id="comments-container-18730" class="comments-container"></div><div id="comment-tools-18730" class="comment-tools"></div><div class="clear"></div><div id="comment-18730-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18731"></span>

<div id="answer-container-18731" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18731-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18731-score" class="post-score" title="current number of votes">3</div><span id="post-18731-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A trace file on 1G is big, wireshark keeps track of several things while dissecting, so you will need a multiple of 1G of memory to be able to read the file. All filtering actions will also become very slow. I usually keep 100MB as a maximum for trace files, but it all depends on the HW of the system on which you do your analysis.</p><p>What options do you have?</p><ol><li>Split the file in a number of files, this can be done with <a href="http://www.wireshark.org/docs/man-pages/editcap.html">editcap</a> (which is included with wireshark) and then analyze the smaller files one-by-one</li><li>Pre-filter the file on a time range, this can also be done by editcap</li><li>Pre-filter the file on a specific host:</li><li>this can be done with <code>tshark -r &lt;file&gt; -w &lt;newfile&gt; -R "ip.addr==x.x.x.x"</code>, although <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark</a> might also run out-of-memory here</li><li>this can be done by tcpdump (on linux, osx etc) or windump (on windows) with: <code>tcpdump -r &lt;file&gt; -w &lt;newfile&gt; "host x.x.x.x"</code></li><li>Use a program like "<a href="http://www.riverbed.com/us/products/cascade/cascade_pilot.php">Riverbed Pilot</a>" (commercial software) to index the file and do some of the analysis on the indices and then zoom in the packets you really need to see in detail with wireshark.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '13, 04:25</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-18731" class="comments-container"></div><div id="comment-tools-18731" class="comment-tools"></div><div class="clear"></div><div id="comment-18731-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

