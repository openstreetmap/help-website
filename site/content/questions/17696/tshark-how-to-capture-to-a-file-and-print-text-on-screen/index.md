+++
type = "question"
title = "Tshark how to capture to a file and print text on screen"
description = '''Hello  I have problem with saving Tshark output to a pcap and in paralel print text on the screen. I know that there is -P option but it seems it is not working. I&#x27;m trying to run following command using LINUX (ubuntu 12.10 and tshark 1.7.0): tshark -P -i eth0 -f tcp -w /tmp/eth0.pcap  Thank you in ...'''
date = "2013-01-15T06:45:00Z"
lastmod = "2016-06-28T05:08:00Z"
weight = 17696
keywords = [ "screen", "printing", "pcap", "tshark", "file" ]
aliases = [ "/questions/17696" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark how to capture to a file and print text on screen](/questions/17696/tshark-how-to-capture-to-a-file-and-print-text-on-screen)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17696-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello I have problem with saving Tshark output to a pcap and in paralel print text on the screen. I know that there is -P option but it seems it is not working. I'm trying to run following command using LINUX (ubuntu 12.10 and tshark 1.7.0):</p><pre><code>tshark -P -i eth0 -f tcp -w /tmp/eth0.pcap</code></pre><p>Thank you in advance</p><p>Krzysztof</p></div><div id="question-tags" class="tags-container tags">screen printing pcap tshark file</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '13, 06:45</strong></p><img src="https://secure.gravatar.com/avatar/47478158a4065488a4db9ee10dced213?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krzysztof&#39;s gravatar image" /><p>krzysztof<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krzysztof has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jan '13, 04:59</p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-17696" class="comments-container"></div><div id="comment-tools-17696" class="comment-tools"></div><div class="clear"></div><div id="comment-17696-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17716"></span>

<div id="answer-container-17716" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17716-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not sure in which version the option to print packets on screen while writing them to disk has changed, but it used to be '-S' and now it is '-P'. Could you check the output of 'tshark -h' to see if it is '-P' in your version of tshark?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jan '13, 05:01</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-17716" class="comments-container"></div><div id="comment-tools-17716" class="comment-tools"></div><div class="clear"></div><div id="comment-17716-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53698"></span>

<div id="answer-container-53698" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53698-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>tshark -P -i eth0</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jun '16, 05:08</strong></p><img src="https://secure.gravatar.com/avatar/da92abc8722e5f1c85a0055e4f904215?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mninawe%20Matrose&#39;s gravatar image" /><p>Mninawe Matrose<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mninawe Matrose has no accepted answers">0%</span></p></div></div><div id="comments-container-53698" class="comments-container"></div><div id="comment-tools-53698" class="comment-tools"></div><div class="clear"></div><div id="comment-53698-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

