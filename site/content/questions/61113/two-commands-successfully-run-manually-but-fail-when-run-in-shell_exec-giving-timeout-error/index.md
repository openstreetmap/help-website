+++
type = "question"
title = "Two commands successfully run manually but fail when run in shell_exec(), giving TimeOut error"
description = '''I am trying to execute two dmd commands simultaneously using PHP shell_exec(). One command runs Tshark for 5 seconds. The second command runs an .exe file. Tshark is a program which captures network packs transferring over a network interface. The second program (named mtu.exe) sends network packets...'''
date = "2017-04-29T02:07:00Z"
lastmod = "2017-04-29T02:07:00Z"
weight = 61113
keywords = [ "php", "shell_exec", "tshark" ]
aliases = [ "/questions/61113" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Two commands successfully run manually but fail when run in shell\_exec(), giving TimeOut error](/questions/61113/two-commands-successfully-run-manually-but-fail-when-run-in-shell_exec-giving-timeout-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61113-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to execute two dmd commands simultaneously using PHP <code>shell_exec()</code>. One command runs Tshark for 5 seconds. The second command runs an <code>.exe</code> file. Tshark is a program which captures network packs transferring over a network interface. The second program (named mtu.exe) sends network packets from my local machine to a remote machine.</p><p>Thing is that when I run these commands <em>manually</em>, I run the first command. A moment after that, I run the second one, and all goes well and within a second or so, the expected packets are transferred by <code>mtu.exe</code> and are captured by <code>tshark.exe</code>. Everything works perfectly well.</p><p>But then when I run the following script to execute these commands, I get the following output:</p><pre><code>$firstCommand = &#39;&quot;C:\Program Files\Wireshark\tshark.exe&quot;  -a duration:5  -w capture.pcapng  2&gt;&amp;1&#39;;
echo $firstCommand.&quot;&lt;br&gt;&lt;br&gt;&quot;;

$secondCommand = &quot;mtu.exe -d0 -a43020008 -g43010008 -i987654321 -s&quot;Merry Xmass&quot;  2&gt;&amp;1&quot;;
echo $secondCommand.&quot;&lt;br&gt;&lt;br&gt;&quot;;

echo shell_exec($firstCommand . &quot; &amp;&amp; &quot; . $secondCommand);</code></pre><p><strong><em>Output:</em></strong></p><pre><code>&quot;C:\Program Files\Wireshark\tshark.exe&quot;  -a duration:5  -w capture.pcapng  2&gt;&amp;1

mtu.exe -d0 -a43020008 -g43010008 -i987654321 -s&quot;Merry Xmass&quot;  2&gt;&amp;1

Fatal error: Maximum execution time of 30 seconds exceeded in C:\xampp\htdocs\Test\index.php on line 10</code></pre><p>Line 10 is the line where <code>shell_exec()</code> is. The question how to fix this issue? Why is this happening?</p></div><div id="question-tags" class="tags-container tags">php shell_exec tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Apr '17, 02:07</strong></p><img src="https://secure.gravatar.com/avatar/d2c205566b4047d6494161edbd1223c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jesss&#39;s gravatar image" /><p>Jesss<br />
<span class="score" title="51 reputation points">51</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jesss has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Apr '17, 02:08</p></div></div><div id="comments-container-61113" class="comments-container"></div><div id="comment-tools-61113" class="comment-tools"></div><div class="clear"></div><div id="comment-61113-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

