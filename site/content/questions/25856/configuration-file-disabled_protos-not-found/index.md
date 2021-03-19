+++
type = "question"
title = "Configuration file &quot;disabled_protos&quot; NOT Found"
description = '''Hi all, I&#x27;m reading an introduction of tshark . In which, I see there is a globla and personal configuration file &quot;disabled_protos&quot; to disable some protocols. Then I find global preference on my Windows 7 at   &quot;C:&#92;Program Files&#92;Wireshark&#92;preferences&quot;  but the directory &quot;preferences&quot; not found . And ...'''
date = "2013-10-10T00:27:00Z"
lastmod = "2013-10-14T04:42:00Z"
weight = 25856
keywords = [ "configuration", "tshark", "preferences" ]
aliases = [ "/questions/25856" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Configuration file "disabled\_protos" NOT Found](/questions/25856/configuration-file-disabled_protos-not-found)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25856-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I'm reading <a href="http://www.wireshark.org/docs/man-pages/tshark.html">an introduction of tshark</a> . In which, I see there is a globla and personal configuration file "disabled_protos" to disable some protocols. Then I find <strong>global preference</strong> on my Windows 7 at</p><blockquote><p>"C:\Program Files\Wireshark\preferences"</p></blockquote><p>but the directory "preferences" not found . And i check on my server which install Linux with root user at</p><blockquote><p>/usr/local/share/wireshark/preferences</p></blockquote><p>but the directory "preferences" also not found. About the <strong>personal preference</strong>. I got the same thing when I check these locations:</p><pre><code>cd ~
ls -a</code></pre><p>or</p><pre><code>cd /home
ls -a</code></pre><p>I cannot find .wireshark as mentioned in that link. I use wireshark 1.10 for both of Windows7 and Linux. Could you please help me to find out this config file. Thanks so much.</p></div><div id="question-tags" class="tags-container tags">configuration tshark preferences</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Oct '13, 00:27</strong></p><img src="https://secure.gravatar.com/avatar/824a7342f59ff90e6040505b38626416?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hoangsonk49&#39;s gravatar image" /><p>hoangsonk49<br />
<span class="score" title="81 reputation points">81</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hoangsonk49 has 2 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Oct '13, 00:27</p></div></div><div id="comments-container-25856" class="comments-container"><span id="25857"></span><div id="comment-25857" class="comment"><div id="post-25857-score" class="comment-score">1</div><div class="comment-text"><p>On my windows 7 system the file is in C:\Users\XXXXX\AppData\Roaming\Wireshark NOTE the files may be hidden.</p></div><div id="comment-25857-info" class="comment-info"><span class="comment-age">(10 Oct '13, 01:00)</span> Anders ♦</div></div><span id="25858"></span><div id="comment-25858" class="comment"><div id="post-25858-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I also found it on my Win7.</p></div><div id="comment-25858-info" class="comment-info"><span class="comment-age">(10 Oct '13, 01:10)</span> hoangsonk49</div></div><span id="25860"></span><div id="comment-25860" class="comment"><div id="post-25860-score" class="comment-score">1</div><div class="comment-text"><p>Also look at the Help | About dialog, on the Folders tab.</p></div><div id="comment-25860-info" class="comment-info"><span class="comment-age">(10 Oct '13, 01:37)</span> grahamb ♦</div></div></div><div id="comment-tools-25856" class="comment-tools"></div><div class="clear"></div><div id="comment-25856-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25960"></span>

<div id="answer-container-25960" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25960-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The file won't actually exist until you disable a protocol in Wireshark. At that point Wireshark creates the file, so you can try disabling a protocol from within Wireshark and then try to locate the file. Once you've verified that you know the correct location, you can delete it or overwrite it to disable protocols for both tshark and Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Oct '13, 04:42</strong></p><img src="https://secure.gravatar.com/avatar/6f579677517345ebea1cfef9e9e88f0c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="beroset&#39;s gravatar image" /><p>beroset<br />
<span class="score" title="226 reputation points">226</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="beroset has 4 accepted answers">33%</span></p></div></div><div id="comments-container-25960" class="comments-container"></div><div id="comment-tools-25960" class="comment-tools"></div><div class="clear"></div><div id="comment-25960-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

