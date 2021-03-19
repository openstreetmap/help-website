+++
type = "question"
title = "Working with file sets"
description = '''I am performing some problem analysis this morning at a client site. I am troubleshooting a problem on their SAN network. There is a large volume of data where I am capturing from. It is so much that it shuts down wireshark after a minute and a half of capture ( I am using a very robust laptop with ...'''
date = "2010-10-20T07:16:00Z"
lastmod = "2010-10-20T11:09:00Z"
weight = 557
keywords = [ "file", "sets" ]
aliases = [ "/questions/557" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Working with file sets](/questions/557/working-with-file-sets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-557-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am performing some problem analysis this morning at a client site. I am troubleshooting a problem on their SAN network. There is a large volume of data where I am capturing from. It is so much that it shuts down wireshark after a minute and a half of capture ( I am using a very robust laptop with an i7 6 G RAM and Tera hdd).</p><p>I started to set up WS thereafter to capture using file sets. I set the file size to 20 mg per file. it writes one of these each 3 seconds. I have 63 files in the newly created file set.</p><p>What I want to do now is open the file set as one file. I saw this done once before in a tip or trick that Laura had published somewhere. I tried to figure out how to open the file set (all files) and so far have not been successful.</p><p>Thanks for any help provided</p><p>KMNRuser</p></div><div id="question-tags" class="tags-container tags">file sets</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Oct '10, 07:16</strong></p><img src="https://secure.gravatar.com/avatar/9e96b23e3495316e470ba9b487b82a73?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kmnruser&#39;s gravatar image" /><p>kmnruser<br />
<span class="score" title="26 reputation points">26</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kmnruser has no accepted answers">0%</span></p></div></div><div id="comments-container-557" class="comments-container"><span id="596"></span><div id="comment-596" class="comment"><div id="post-596-score" class="comment-score"></div><div class="comment-text"><p>Most likely I demonstrated opening a file from a file set and quickly moving between each file using File &gt; File Sets.</p></div><div id="comment-596-info" class="comment-info"><span class="comment-age">(22 Oct '10, 15:42)</span> lchappell ♦</div></div></div><div id="comment-tools-557" class="comment-tools"></div><div class="clear"></div><div id="comment-557-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="559"></span>

<div id="answer-container-559" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-559-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can do the following:</p><ul><li>Use <em>File→Merge</em></li><li>Open the first file and drag subsequent files to Wireshark's main window</li><li>Use <a href="http://www.wireshark.org/docs/man-pages/mergecap.html">mergecap</a></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '10, 10:42</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-559" class="comments-container"><span id="563"></span><div id="comment-563" class="comment"><div id="post-563-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply Gerald. It is quite the privelege getting an answer back from you!</p></div><div id="comment-563-info" class="comment-info"><span class="comment-age">(20 Oct '10, 11:44)</span> kmnruser</div></div></div><div id="comment-tools-559" class="comment-tools"></div><div class="clear"></div><div id="comment-559-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="561"></span>

<div id="answer-container-561" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-561-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>AFAIK you cannot open them all at once, but you can jump from one file the another.<br />
Open one of the files of the file set.<br />
Go to File -&gt; File Set -&gt; List Files to open the "List Files" dialog box.<br />
Just select a file to open another file of the file set; but the current file will be closed.</p><p>When you use a display filter, this display filter will also be applied to the next file you open.</p><p>See the <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChIOFileSetSection.html">Wireshark User's Guide</a> for more information.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '10, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Oct '10, 11:15</p></div></div><div id="comments-container-561" class="comments-container"></div><div id="comment-tools-561" class="comment-tools"></div><div class="clear"></div><div id="comment-561-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

