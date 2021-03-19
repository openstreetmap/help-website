+++
type = "question"
title = "how to convert k12(txt) file to pcap from the command line"
description = '''Hello, I want to convert a .pcap file to k12 file and then do the reverse (i.e. k12 -&amp;gt; pcap), and to do so from the command line. I was able to do so when I was using version 1.0.5, but I can&#x27;t do it in the newer versions.  Thanks.'''
date = "2011-03-07T07:21:00Z"
lastmod = "2011-03-10T08:54:00Z"
weight = 2697
keywords = [ "conversion" ]
aliases = [ "/questions/2697" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to convert k12(txt) file to pcap from the command line](/questions/2697/how-to-convert-k12txt-file-to-pcap-from-the-command-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2697-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I want to convert a .pcap file to k12 file and then do the reverse (i.e. k12 -&gt; pcap), and to do so from the command line. I was able to do so when I was using version 1.0.5, but I can't do it in the newer versions.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">conversion</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Mar '11, 07:21</strong></p><img src="https://secure.gravatar.com/avatar/70b4a0634aec56e904322191fad3e278?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="liron&#39;s gravatar image" /><p>liron<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="liron has no accepted answers">0%</span></p></div></div><div id="comments-container-2697" class="comments-container"><span id="2760"></span><div id="comment-2760" class="comment"><div id="post-2760-score" class="comment-score"></div><div class="comment-text"><p>anyone? please.</p></div><div id="comment-2760-info" class="comment-info"><span class="comment-age">(10 Mar '11, 08:30)</span> liron</div></div><span id="2762"></span><div id="comment-2762" class="comment"><div id="post-2762-score" class="comment-score"></div><div class="comment-text"><p>Just for my curiosity:</p><p>How does converting .pcap to .k12 &amp; back help you ?</p></div><div id="comment-2762-info" class="comment-info"><span class="comment-age">(10 Mar '11, 08:57)</span> Bill Meier ♦♦</div></div></div><div id="comment-tools-2697" class="comment-tools"></div><div class="clear"></div><div id="comment-2697-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2761"></span>

<div id="answer-container-2761" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2761-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think the following might work:</p><ol><li>To convert .pcap to .k12: editcap -F k12text abc_a.pcap abc.k12</li><li><p>To convert .k12 to .pcap: editcap -T ether abc.k12 abc_b.pcap</p><p>Note: This works properly only if <em>all</em> the frames in the .k12 file have ethernet encapsulation type (which they will if the file was originally converted from a .pcap file with ethernet encapsulation type).</p></li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Mar '11, 08:54</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Mar '11, 09:00</p></div></div><div id="comments-container-2761" class="comments-container"><span id="2764"></span><div id="comment-2764" class="comment"><div id="post-2764-score" class="comment-score"></div><div class="comment-text"><p>[After trying the above: The date on each packet is incorrect (maybe because .k12 format doesn't have a date ?) after the .pcap --&gt; .k12 --&gt; .pcap but all the rest of the info is OK].</p></div><div id="comment-2764-info" class="comment-info"><span class="comment-age">(10 Mar '11, 09:26)</span> Bill Meier ♦♦</div></div><span id="2796"></span><div id="comment-2796" class="comment"><div id="post-2796-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot!</p><p>I have an application that simulate traffic using a single pcap file, now instead of recording and generating the needed pcap each time, I use a few previously recorded pcaps as building blocks. In order to build 1 pcap from those building blocks, I'm converting the pcaps into into k12 files, edit (e.g. choosing the needed packets, changing the headers etc.) them as needed and then convert them back into a single pcap file.</p><p>Thanks again!</p></div><div id="comment-2796-info" class="comment-info"><span class="comment-age">(14 Mar '11, 02:07)</span> liron</div></div></div><div id="comment-tools-2761" class="comment-tools"></div><div class="clear"></div><div id="comment-2761-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

