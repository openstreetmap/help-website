+++
type = "question"
title = "Named pipe on Windows 7"
description = '''At the moment I&#x27;m successfully running the following command on Windows 10 and Windows server 2012 tshark -l -n -r &quot;&#92;&#92;.&#92;pipe&#92;tsharkpipe2&quot;  but when I run it on Windows 7 and Windows server 2012, tshark gives me &quot;File does not exist error&quot;. however I can use the pipe with -i, but I need to run -Y fil...'''
date = "2016-08-22T05:54:00Z"
lastmod = "2016-08-22T05:54:00Z"
weight = 55046
keywords = [ "windows7", "tshark" ]
aliases = [ "/questions/55046" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Named pipe on Windows 7](/questions/55046/named-pipe-on-windows-7)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55046-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>At the moment I'm successfully running the following command on Windows 10 and Windows server 2012</p><pre><code>tshark -l -n -r &quot;\\.\pipe\tsharkpipe2&quot;</code></pre><p>but when I run it on Windows 7 and Windows server 2012, tshark gives me "File does not exist error". however I can use the pipe with <strong>-i</strong>, but I need to run <strong>-Y</strong> filter and <strong>-T pdml</strong> on which it seems cannot be done using <strong>-i</strong>.</p><p>am I doing something wrong here?</p></div><div id="question-tags" class="tags-container tags">windows7 tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Aug '16, 05:54</strong></p><img src="https://secure.gravatar.com/avatar/6ed60f06c812665ce60b6e6c2d8c9eb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hja&#39;s gravatar image" /><p>hja<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hja has no accepted answers">0%</span></p></div></div><div id="comments-container-55046" class="comments-container"><span id="55047"></span><div id="comment-55047" class="comment"><div id="post-55047-score" class="comment-score"></div><div class="comment-text"><p>The <a href="https://www.wireshark.org/docs/man-pages/tshark.html">tshark man page</a> says:</p><p><em>Note: the Win32 version of TShark doesn't support capturing from pipes!</em></p><p>Can you check the version (32 or 64 bit) on the Win10, Win server 2012 and Win7 machines you are using?</p><p>Normally there should be no reason why <code>-Y</code> and <code>-T pdml</code> could not be used together with either <code>-i</code> or <code>-r</code>.</p></div><div id="comment-55047-info" class="comment-info"><span class="comment-age">(22 Aug '16, 06:07)</span> sindy</div></div><span id="55051"></span><div id="comment-55051" class="comment"><div id="post-55051-score" class="comment-score"></div><div class="comment-text"><p>@sindy, All Oses were 64 bits, you are right I mixed up the -Y and -f during my tests with -i, which I can omit the -f one, thanks for the help</p></div><div id="comment-55051-info" class="comment-info"><span class="comment-age">(22 Aug '16, 08:21)</span> hja</div></div></div><div id="comment-tools-55046" class="comment-tools"></div><div class="clear"></div><div id="comment-55046-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

