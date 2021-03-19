+++
type = "question"
title = "wireshark command not found"
description = '''Hi ,I am trying to install wireshark on CentOS 6 and get the following error - bash:wireshark command not found , i tried to uninstall rpm , run as sudo , but have had no luck . any suggestions ? '''
date = "2012-08-01T07:02:00Z"
lastmod = "2012-08-01T07:16:00Z"
weight = 13243
keywords = [ "rpm", "wireshark" ]
aliases = [ "/questions/13243" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [wireshark command not found](/questions/13243/wireshark-command-not-found)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13243-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi ,I am trying to install wireshark on CentOS 6 and get the following error - bash:wireshark command not found , i tried to uninstall rpm , run as sudo , but have had no luck . any suggestions ?</p></div><div id="question-tags" class="tags-container tags">rpm wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Aug '12, 07:02</strong></p><img src="https://secure.gravatar.com/avatar/9b296b0c1a89a6d15e65215e5e6c69b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld0722&#39;s gravatar image" /><p>helloworld0722<br />
<span class="score" title="10 reputation points">10</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld0722 has no accepted answers">0%</span></p></div></div><div id="comments-container-13243" class="comments-container"></div><div id="comment-tools-13243" class="comment-tools"></div><div class="clear"></div><div id="comment-13243-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13249"></span>

<div id="answer-container-13249" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13249-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I guess you installed just the package 'wireshark'. That's only the CLI tools (tshark, etc.), so bash cannot find 'wireshark'. If you need the GUI version, you should install 'wireshark-gnome'</p><blockquote><p><code>yum install wireshark-gnome</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '12, 07:16</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Aug '12, 07:31</p></div></div><div id="comments-container-13249" class="comments-container"><span id="35341"></span><div id="comment-35341" class="comment"><div id="post-35341-score" class="comment-score"></div><div class="comment-text"><p>Thanks it worked..</p></div><div id="comment-35341-info" class="comment-info"><span class="comment-age">(09 Aug '14, 03:38)</span> Divesh</div></div><span id="42880"></span><div id="comment-42880" class="comment"><div id="post-42880-score" class="comment-score"></div><div class="comment-text"><p>This command is not working. It will help only for install. But not able to use the wireshark.</p></div><div id="comment-42880-info" class="comment-info"><span class="comment-age">(04 Jun '15, 04:52)</span> Suresh Babu</div></div><span id="42881"></span><div id="comment-42881" class="comment"><div id="post-42881-score" class="comment-score"></div><div class="comment-text"><p>I got the following error: (wireshark:20297): Gtk-WARNING **: cannot open display:</p><p>Pls if you can guide me.</p></div><div id="comment-42881-info" class="comment-info"><span class="comment-age">(04 Jun '15, 04:53)</span> Suresh Babu</div></div></div><div id="comment-tools-13249" class="comment-tools"></div><div class="clear"></div><div id="comment-13249-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

