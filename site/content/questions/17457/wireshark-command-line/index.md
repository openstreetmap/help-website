+++
type = "question"
title = "Wireshark command line?"
description = '''Was wireshark meant to be used with command lines or was it meant to be used with the GUI provided? Is there a good command line guide?'''
date = "2013-01-04T12:38:00Z"
lastmod = "2013-01-04T12:44:00Z"
weight = 17457
keywords = [ "gui", "command", "line" ]
aliases = [ "/questions/17457" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark command line?](/questions/17457/wireshark-command-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17457-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Was wireshark meant to be used with command lines or was it meant to be used with the GUI provided? Is there a good command line guide?</p></div><div id="question-tags" class="tags-container tags">gui command line</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jan '13, 12:38</strong></p><img src="https://secure.gravatar.com/avatar/81c67f66311e7c60a0b1867f34570bb7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dalawh&#39;s gravatar image" /><p>dalawh<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dalawh has no accepted answers">0%</span></p></div></div><div id="comments-container-17457" class="comments-container"></div><div id="comment-tools-17457" class="comment-tools"></div><div class="clear"></div><div id="comment-17457-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17458"></span>

<div id="answer-container-17458" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17458-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is meant to be used with the GUI, although there are some command line options available (see the output of "wireshark -h" for details).</p><p>There is a CLI version of wireshark called "tshark" which is installed when installing wireshark. See "tshark -h" for more details.</p><p>If this does not answer your question, could you be a little more specific what you need help with?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '13, 12:44</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-17458" class="comments-container"><span id="17459"></span><div id="comment-17459" class="comment"><div id="post-17459-score" class="comment-score"></div><div class="comment-text"><ul><li>Is the GUI version more developed or is the command line version? It seems you can't tcp dump using the GUI or am I wrong?</li><li>Is there a tutorial on using wireshark through command line or can everything be found using "wireshark -h"?</li><li>What is the difference between using wireshark and tshark command if we are typing these commands into the command prompt?</li></ul></div><div id="comment-17459-info" class="comment-info"><span class="comment-age">(04 Jan '13, 12:52)</span> dalawh</div></div><span id="17461"></span><div id="comment-17461" class="comment"><div id="post-17461-score" class="comment-score"></div><div class="comment-text"><ul><li>Wireshark and tshark both use the same dissection engine, although some output might be different in wireshark and tshark because tshark runs through the capture file in one sequential run while wireshark will run through the file once and then a second time to display the packet details (tshark has the -2 option to do the same, but that is still experimental)</li><li>There is no tutorial, but there are the <a href="https://www.wireshark.org/docs/wsug_html_chunked/">user's guide</a> and <a href="https://www.wireshark.org/docs/man-pages/">manual pages</a></li><li>The difference between wireshark and tshark is that typing wireshark from the command line will open up a GUI window running wireshark and tshark will show text output in the terminal window.</li></ul></div><div id="comment-17461-info" class="comment-info"><span class="comment-age">(04 Jan '13, 13:06)</span> SYN-bit ♦♦</div></div><span id="17479"></span><div id="comment-17479" class="comment"><div id="post-17479-score" class="comment-score"></div><div class="comment-text"><p>I don't know what "tcp dump" means; if you mean "capture traffic the same way tcpdump does" (in which case you should have said "capture network traffic" rather than "tcp dump" or even "tcpdump"), you can capture traffic from the GUI - either select an interface from the main window and click "Start", or click "Capture Options" or select "Options" from the "Capture" menu and set up a capture.</p></div><div id="comment-17479-info" class="comment-info"><span class="comment-age">(05 Jan '13, 14:40)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-17458" class="comment-tools"></div><div class="clear"></div><div id="comment-17458-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

