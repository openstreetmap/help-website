+++
type = "question"
title = "Manually enter remote capture line"
description = '''In old versions of Wireshark (running on Win32 and Win64), I could open the capture options and type (or paste) rpcap://ip.address/br0 to capture from a remote linux device, which was fast and convenient. In new versions, there&#x27;s a remote capture tab which tries to query the remote endpoint for the ...'''
date = "2013-07-26T16:34:00Z"
lastmod = "2013-07-27T00:23:00Z"
weight = 23393
keywords = [ "interfaces", "rpcap" ]
aliases = [ "/questions/23393" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Manually enter remote capture line](/questions/23393/manually-enter-remote-capture-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23393-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In old versions of Wireshark (running on Win32 and Win64), I could open the capture options and type (or paste) <code>rpcap://ip.address/br0</code> to capture from a remote linux device, which was fast and convenient.</p><p>In new versions, there's a remote capture tab which tries to query the remote endpoint for the list of addresses, and takes forever. The <code>rpcapd</code> installed on my Linux system may be too old to support this query at all. Is there any way to go back to the old entry method? A configuration file where I can enter the interface? A command line option to use when spawning Wireshark?</p><p>(I still want to use the GUI for browsing through captures and setting filters, but I suppose doing a capture from the command-line and opening the capture dump with the GUI version would be an acceptable workaround)</p><p>And seriously, is any user who's unable to deal with the URL-style connection going to be able to make any sense out of a packet decode? Combined with the loss of the history, the new UI for remote interface selection is a net negative in usability.</p></div><div id="question-tags" class="tags-container tags">interfaces rpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jul '13, 16:34</strong></p><img src="https://secure.gravatar.com/avatar/dde3a5048e456c451b7c518857e1818c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ben%20Voigt&#39;s gravatar image" /><p>Ben Voigt<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ben Voigt has no accepted answers">0%</span></p></div></div><div id="comments-container-23393" class="comments-container"><span id="23396"></span><div id="comment-23396" class="comment"><div id="post-23396-score" class="comment-score"></div><div class="comment-text"><p>In fact there is a command-line option for pre-entering an interface, and it handles remote interfaces just fine.</p><pre><code>wireshark -i rpcap://ip.address/br0</code></pre><p>You can even make a shortcut. How much quicker is that than using the add remote interface dialog?</p></div><div id="comment-23396-info" class="comment-info"><span class="comment-age">(26 Jul '13, 17:22)</span> Ben Voigt</div></div></div><div id="comment-tools-23393" class="comment-tools"></div><div class="clear"></div><div id="comment-23393-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23400"></span>

<div id="answer-container-23400" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23400-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Both browsing and adding a remote interface have their justification.</p><ul><li>Browsing: It's necessary for remote capturing on Windows, as you will have to give the UUID of the interface, which is not that easy to remember as br0 ;-)</li><li>Adding the Interface: Fast and easy for Linux. However, the remote capturing feature is mainly for Windows, as that's a WinPcap feature. WinPcap also provides a rpcapd for Linux. However, there was almost no work on the code for some time, hence there are some bugs regarding authentication, browsing, etc. see the following discussions (and the long list of comments):</li></ul><blockquote><p><a href="http://ask.wireshark.org/questions/13217/remote-packet-capture-on-remote-linux-machine">http://ask.wireshark.org/questions/13217/remote-packet-capture-on-remote-linux-machine</a><br />
<a href="http://ask.wireshark.org/questions/16521/linux-remote-interface">http://ask.wireshark.org/questions/16521/linux-remote-interface</a><br />
</p></blockquote><p>If you want the old behavior back (adding a remote interface manually), please file an enhancement request at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a>.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '13, 00:23</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-23400" class="comments-container"><span id="23403"></span><div id="comment-23403" class="comment"><div id="post-23403-score" class="comment-score"></div><div class="comment-text"><p>Well, the command-line options is a perfectly good way of providing it, since it still works with the entire graphical interface and can even be saved in a shortcut.</p><p>The only remaining problem is that the capture options dialog gets really confused when an interface has been passed on the command line, and throws up error dialogs (however, starting the capture works fine). I'll file a bug for this.</p></div><div id="comment-23403-info" class="comment-info"><span class="comment-age">(27 Jul '13, 07:30)</span> Ben Voigt</div></div></div><div id="comment-tools-23400" class="comment-tools"></div><div class="clear"></div><div id="comment-23400-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

